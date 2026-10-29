"""Tests for the pilot scorecard and the weekly scheme watch. Run: python3 -m unittest discover tests"""
import csv, functools, http.server, json, pathlib, sys, tempfile, threading, unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "docs" / "pilot"), str(ROOT / "docs" / "watch")]
import scorecard  # noqa: E402
import scheme_watch  # noqa: E402

COLS = ["operator_code", "district", "row", "date", "scheme", "stage_shown", "action_today",
        "follow_up_date", "outcome_30_days", "minutes"]


def row(**kw):
    return {c: str(kw.get(c, "")) for c in COLS}


class Scorecard(unittest.TestCase):
    def test_pass_marks(self):
        rows = [row(operator_code="MH-01", district="A", date="2026-09-01", scheme="pm-kisan", stage_shown="ekyc",
                    action_today="complaint", outcome_30_days="solved", minutes=4),
                row(operator_code="MH-01", district="A", date="02/09/2026", scheme="pm-kisan", stage_shown="",
                    action_today="शिकायत", outcome_30_days="not solved", minutes=6),
                row(operator_code="UP-01", district="B", date="2026-09-03", scheme="up-pm-kisan", stage_shown="failed",
                    action_today="wait", outcome_30_days="", minutes=20),
                row(operator_code="UP-01", district="B", date="2026-09-03", scheme="up-pm-kisan", stage_shown="ekyc",
                    action_today="तक्रार", outcome_30_days="हल", minutes=5)]
        report = scorecard.score(rows, cont=(7, 10), errors=(1, 1))
        self.assertIn("| Cases logged | 4 (target 300", report)
        self.assertIn("| Stage shown by Sathi | 75% (target 80%) | **ON TRACK** |", report)
        self.assertIn("| Action written | 100% (target 90%) | **PASS** |", report)
        # Three fix/complaint cases; "not solved" counts as stuck, so 2 of 3 solved.
        self.assertIn("| Stuck files solved at 30 days | 67% of 3 followed up", report)
        self.assertIn("| Median minutes per case | 5.5 (target 10 or less) | **PASS** |", report)
        self.assertIn("| Operators who want to continue | 70% (target 70%), 7/10 | **PASS** |", report)

    def test_flags_unreadable_rows(self):
        report = scorecard.score([row(operator_code="X", date="yesterday", action_today="maybe", outcome_30_days="?")])
        self.assertIn("date 'yesterday' not recognised", report)
        self.assertIn("action 'maybe' not recognised", report)

    def test_empty_log(self):
        self.assertIn("**NO DATA**", scorecard.score([]))

    def test_week_prorates_target(self):
        self.assertIn("target 150", scorecard.score([row(operator_code="A")], week=2))


class SchemeWatch(unittest.TestCase):
    """Three weekly runs against a local web server: baseline, then changes, then recovery."""

    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        (self.tmp / "www").mkdir()
        class Quiet(http.server.SimpleHTTPRequestHandler):
            def log_message(self, *a):
                pass
        handler = functools.partial(Quiet, directory=str(self.tmp / "www"))
        self.srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        threading.Thread(target=self.srv.serve_forever, daemon=True).start()
        base = f"http://127.0.0.1:{self.srv.server_address[1]}/"
        self.urls = {"a": base + "a.html", "b": base + "b.html"}
        self._orig = scheme_watch.guide_links
        scheme_watch.guide_links = lambda: {self.urls["a"]: [("mp/mp-ladli-behna.md", "Portal")],
                                            self.urls["b"]: [("rj/rj-x.md", "X")]}

    def tearDown(self):
        scheme_watch.guide_links = self._orig
        self.srv.shutdown()
        self.srv.server_close()

    def page(self, name, body):
        (self.tmp / "www" / name).write_text(f"<html><body>{body}</body></html>", encoding="utf-8")

    def run_watch(self, n):
        out = self.tmp / f"r{n}.md"
        scheme_watch.main(["--state", str(self.tmp / "state.json"), "--report", str(out), "--workers", "2"])
        return out.read_text(encoding="utf-8")

    def test_detects_changes_notices_breaks_and_recovery(self):
        static = "<p>" + "Static scheme text. " * 20 + "</p>"
        self.page("a.html", "<h1>Ladli Behna</h1><p>Monthly amount ₹1,250 per woman.</p><p>Visitor count: 100</p>"
                            '<a href="/o1.pdf">Order dated 10/01/2026</a><script>var x = 1</script>')
        self.page("b.html", static)
        r1 = self.run_watch(1)
        self.assertIn("First run: baseline recorded", r1)

        # Week 2: amount changes, a new order appears, the visitor counter changes, page b disappears.
        self.page("a.html", "<h1>Ladli Behna</h1><p>Monthly amount ₹1,500 per woman.</p><p>Visitor count: 999</p>"
                            '<a href="/o1.pdf">Order dated 10/01/2026</a> <a href="/o2.pdf">Order dated 15/10/2026</a>')
        (self.tmp / "www" / "b.html").unlink()
        r2 = self.run_watch(2)
        self.assertIn("⚠ " + self.urls["a"], r2)
        self.assertIn("+Monthly amount ₹1,500 per woman.", r2)
        self.assertNotIn("Visitor count", r2)
        self.assertIn("o2.pdf", r2)
        self.assertIn("## Links that stopped working", r2)

        # Week 3: page b is back with the same text: listed as working again, not as changed.
        self.page("b.html", static)
        r3 = self.run_watch(3)
        self.assertIn("## Working again", r3)
        self.assertNotIn("## Pages whose text changed", r3)
        state = json.loads((self.tmp / "state.json").read_text())
        self.assertTrue(state["pages"][self.urls["b"]]["ok"])

    def test_real_guides_have_official_links(self):
        links = self._orig()
        self.assertGreater(len(links), 50)
        self.assertTrue(all(u.startswith(("http://", "https://")) for u in links))


if __name__ == "__main__":
    unittest.main()
