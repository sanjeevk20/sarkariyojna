"""Checks on the site's source data: checkers, map signals and guides. Run: python3 -m unittest discover tests"""
import json, pathlib, re, runpy, string, unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SITE, WF = ROOT / "docs" / "site", ROOT / "docs" / "workflows"
TR = runpy.run_path(str(SITE / "tracker.py"))
SIG = runpy.run_path(str(SITE / "signals.py"))
GEO = json.loads((SITE / "geo" / "districts.json").read_text())["districts"]
LANGS = {"mr", "hi", "kn"}
BODY_KEYS = {"to", "subject", "scheme", "app", "date", "days", "status", "ask", "name", "mobile", "today"}


def norm(x):
    """Same clean-up the page applies before matching (template.html, const norm)."""
    x = re.sub(r"[:|_\-–—/,.()\[\]\"']+", " ", str(x).lower())
    return re.sub(r"\s+", " ", x).strip()


def guide_slugs():
    return {md.stem for md in WF.rglob("*.md") if md.name != "README.md"}


class Trackers(unittest.TestCase):
    def test_every_tracker_points_at_a_guide(self):
        slugs = guide_slugs()
        for t in TR["TRACKERS"]:
            self.assertIn(t["guide"], slugs, f"tracker for unknown guide {t['guide']}")

    def test_one_tracker_per_guide(self):
        guides = [t["guide"] for t in TR["TRACKERS"]]
        self.assertEqual(len(guides), len(set(guides)), "a guide has two trackers")

    def test_stages(self):
        for t in TR["TRACKERS"]:
            g = t["guide"]
            self.assertIn(t["local"], LANGS, g)
            ids = [s["id"] for s in t["stages"]]
            self.assertEqual(len(ids), len(set(ids)), f"{g}: duplicate stage ids")
            self.assertTrue(any(s["kind"] == "done" for s in t["stages"]), f"{g}: no done stage")
            for s in t["stages"]:
                where = f"{g}/{s['id']}"
                self.assertIn(s["kind"], ("wait", "act", "stuck", "done"), where)
                if s["kind"] in ("wait",):
                    self.assertTrue(s["follow_up"], f"{where}: a wait stage needs follow_up days")
                for field in ("status", "meaning", "next"):
                    for lang in ("en", "loc"):
                        self.assertTrue(s[field][lang].strip(), f"{where}: empty {field}.{lang}")
                self.assertTrue(s["match"], f"{where}: no match phrases")
                for ph in s["match"]:
                    # A phrase that is only punctuation would become empty and match every pasted text.
                    self.assertTrue(norm(ph), f"{where}: match phrase {ph!r} is empty after clean-up")

    def test_complaint_letters(self):
        for t in TR["TRACKERS"]:
            c = t["complaint"]
            for key in ("to", "subject", "ask", "where"):
                for lang in ("en", "loc"):
                    self.assertTrue(c[key][lang].strip(), f"{t['guide']}: complaint {key}.{lang} empty")

    def test_letter_templates_fill(self):
        for lang, body in TR["BODY"].items():
            keys = {f for _, f, _, _ in string.Formatter().parse(body) if f}
            self.assertEqual(keys - BODY_KEYS, set(), f"{lang}: unknown placeholder")
            body.format(**{k: "x" for k in BODY_KEYS})

    def test_every_tracker_has_paste_cases(self):
        cases = json.loads((ROOT / "tests" / "paste_cases.json").read_text())["cases"]
        stages = {t["guide"]: {s["id"] for s in t["stages"]} for t in TR["TRACKERS"]}
        for g in stages:
            self.assertTrue(any(c["guide"] == g for c in cases), f"no paste cases for {g}")
        for c in cases:
            self.assertIn(c["guide"], stages, f"paste case for unknown checker {c['guide']}")
            if c["stage"] is not None:
                self.assertIn(c["stage"], stages[c["guide"]], f"paste case expects unknown stage {c['stage']}")


class Signals(unittest.TestCase):
    def test_mapped_signals_use_real_districts(self):
        names = {(d["state"], d["name"]) for d in GEO}
        for s in SIG["SIGNALS"]:
            if s["district"]:
                self.assertIn((s["state"], s["district"]), names,
                              f"signal district {s['district']} ({s['state']}) is not a Census 2011 name in geo/districts.json")

    def test_signal_fields(self):
        for s in SIG["SIGNALS"]:
            self.assertIn(s["kind"], ("bribe-arrest", "delay"))
            self.assertRegex(s["month"], r"^20\d\d-(0[1-9]|1[0-2])$")
            self.assertTrue(s["url"].startswith("https://"), s["url"])

    def test_every_state_has_districts(self):
        states = {d["state"] for d in GEO}
        for st in ("mh", "up", "ka", "mp", "rj"):
            self.assertIn(st, states)


class Guides(unittest.TestCase):
    def test_every_guide_has_its_files(self):
        for md in WF.rglob("*.md"):
            if md.name == "README.md":
                continue
            text = md.read_text(encoding="utf-8")
            self.assertIn("## Official links", text, md.name)
            self.assertRegex(text, r"## Verification", md.name)
            for out in re.findall(r"\]\(([\w.-]+-guide(?:-\w\w)?\.(?:png|html))\)", text):
                self.assertTrue((md.parent / out).exists(), f"{md.name} links missing file {out}")

    def test_content_files_have_both_languages(self):
        for f in WF.rglob("*_content.py"):
            t = runpy.run_path(str(f))["T"]
            self.assertIn("en", t, f.name)
            self.assertTrue(set(t) & LANGS, f"{f.name}: no local-language text")
            for lang, d in t.items():
                self.assertTrue(d["h1"].strip() and d["steps"], f"{f.name} [{lang}]: empty title or steps")


if __name__ == "__main__":
    unittest.main()
