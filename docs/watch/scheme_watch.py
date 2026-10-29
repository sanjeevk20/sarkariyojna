"""Weekly scheme watch: checks every official link in the guides and reports what changed since last week.

For each URL in the guides' "Official links" tables it records whether the page opens, a fingerprint of
its visible text, and the notice / order / circular links on it. Compared with the previous run's state
it reports pages whose text changed (with the changed lines, and a flag when amounts or dates moved),
new notices, links that stopped working, and links that recovered. Standard library only.

    python3 docs/watch/scheme_watch.py --state /path/state.json --report report.md

Run weekly by .github/workflows/scheme-watch.yml, which keeps state.json on the scheme-watch-data branch
and opens a "Scheme watch" issue when something changed. The first run only records a baseline.
"""
import argparse, concurrent.futures as cf, datetime as dt, difflib, hashlib, html, json, os, pathlib, re, ssl, sys
import urllib.error, urllib.parse, urllib.request
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parents[2]
WF = ROOT / "docs" / "workflows"
UA = "Mozilla/5.0 (compatible; SathiSchemeWatch/1.0; +https://github.com/sanjeevk20/sarkariyojna)"
MAX_BYTES = 3_000_000
KEEP_LINES = 600
NOTICE_RE = re.compile(r"\.pdf($|\?)|notification|circular|notice|order|\bgr\b|guideline|आदेश|परिपत्र|अधिसूचना|"
                       r"शासन निर्णय|सूचना|ಆದೇಶ|ಸುತ್ತೋಲೆ|ಅಧಿಸೂಚನೆ", re.I)
VOLATILE_RE = re.compile(r"visitor|hit counter|page views|last updated|updated on|last modified|copyright|©|"
                         r"\b\d{1,2}:\d{2}(:\d{2})?\s*(am|pm)?\b|server time|current date", re.I)
MONEY_DATE_RE = re.compile(r"₹|\brs\.?\s?\d|rupees|lakh|crore|deadline|last date|due date|instal+ment|kist|किस्त|हप्ता|"
                           r"अंतिम तिथि|अंतिम दिनांक|मुदत|\b\d{1,2}[./-]\d{1,2}[./-]\d{2,4}\b|"
                           r"\b\d{1,2}\s+(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\b", re.I)


# ------------------------------------------------------------------ links from the guides
def guide_links():
    """{url: [(guide, label)]} from every 'Official links' table under docs/workflows."""
    links = {}
    for md in sorted(WF.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        m = re.search(r"^## Official links\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
        if not m:
            continue
        for line in m.group(1).splitlines():
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            for url in re.findall(r"<(https?://[^>\s]+)>|\((https?://[^)\s]+)\)", line):
                url = (url[0] or url[1]).rstrip(".,")
                links.setdefault(url, []).append((md.relative_to(WF).as_posix(), cells[0] if cells else ""))
    return links


# ------------------------------------------------------------------ fetching and text extraction
class Extract(HTMLParser):
    SKIP = {"script", "style", "noscript", "svg", "template", "head"}

    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base, self.skip, self.lines, self.cur, self.links, self.a = base, 0, [], [], [], None

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        if tag in ("p", "div", "li", "tr", "br", "h1", "h2", "h3", "h4", "td", "section", "table"):
            self.flush()
        if tag == "a":
            href = dict(attrs).get("href")
            self.a = [urllib.parse.urljoin(self.base, href), ""] if href and not href.startswith(("javascript:", "#", "mailto:")) else None

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip:
            self.skip -= 1
        if tag == "a" and self.a:
            self.links.append(tuple(self.a))
            self.a = None
        if tag in ("p", "div", "li", "tr", "h1", "h2", "h3", "h4", "td", "section", "table"):
            self.flush()

    def handle_data(self, data):
        if self.skip:
            return
        self.cur.append(data)
        if self.a is not None:
            self.a[1] += data

    def flush(self):
        line = re.sub(r"\s+", " ", "".join(self.cur)).strip()
        if line:
            self.lines.append(line)
        self.cur = []


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-IN,en;q=0.9,hi;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=30, context=ssl.create_default_context()) as r:
            body = r.read(MAX_BYTES)
            return dict(status=r.status, final=r.geturl(), ctype=r.headers.get("Content-Type", ""), body=body,
                        charset=r.headers.get_content_charset() or "utf-8")
    except urllib.error.HTTPError as e:
        return dict(status=e.code, error=f"HTTP {e.code}")
    except (ssl.SSLError, ssl.CertificateError) as e:
        return dict(status=None, error=f"certificate error: {str(e)[:80]}")
    except urllib.error.URLError as e:
        reason = e.reason
        if isinstance(reason, ssl.SSLError):
            return dict(status=None, error=f"certificate error: {str(reason)[:80]}")
        return dict(status=None, error=f"unreachable: {str(reason)[:80]}")
    except Exception as e:  # timeouts, resets
        return dict(status=None, error=f"{type(e).__name__}: {str(e)[:80]}")


def snapshot(url):
    r = fetch(url)
    snap = dict(url=url, checked=dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), status=r.get("status"),
                error=r.get("error"), final=r.get("final"))
    if r.get("error") or not (200 <= (r.get("status") or 0) < 400):
        snap["ok"] = False
        return snap
    snap["ok"] = True
    body, ctype = r["body"], r["ctype"].lower()
    if "html" not in ctype and not body.lstrip()[:15].lower().startswith((b"<!doctype", b"<html")):
        snap.update(kind="file", hash=hashlib.sha256(body).hexdigest(), size=len(body))
        return snap
    p = Extract(r["final"] or url)
    try:
        p.feed(body.decode(r["charset"], errors="replace"))
        p.flush()
    except Exception:
        pass
    lines = [l for l in p.lines if not VOLATILE_RE.search(l)]
    # Drop exact repeats (menus repeated in header and footer) but keep order.
    seen, uniq = set(), []
    for l in lines:
        if l not in seen:
            seen.add(l)
            uniq.append(l)
    text_len = sum(len(l) for l in uniq)
    notices = sorted({h for h, t in p.links if NOTICE_RE.search(h) or NOTICE_RE.search(t or "")})
    snap.update(kind="page", hash=hashlib.sha256("\n".join(uniq).encode()).hexdigest(), lines=uniq[:KEEP_LINES],
                notices=notices[:300], notice_text={h: re.sub(r"\s+", " ", t).strip()[:120] for h, t in p.links if h in notices[:300]},
                thin=text_len < 80)
    return snap


# ------------------------------------------------------------------ comparison and report
def compare(prev, cur, links):
    out = dict(changed=[], notices=[], failing=[], recovered=[], still=[], thin=[], new=[])
    for url, s in cur.items():
        p = prev.get(url)
        if s.get("ok") and s.get("thin"):
            out["thin"].append(url)
        if not p:
            out["new"].append(url)
            if not s["ok"]:
                out["failing"].append(url)
            continue
        if p.get("ok") and not s["ok"]:
            out["failing"].append(url)
        elif not p.get("ok") and not s["ok"]:
            out["still"].append(url)
        elif not p.get("ok") and s["ok"]:
            out["recovered"].append(url)
        if s["ok"] and p.get("ok") and p.get("hash") and s.get("hash") != p.get("hash") and not s.get("thin"):
            out["changed"].append(url)
        if s["ok"] and p.get("ok") and s.get("kind") == "page":
            fresh = [h for h in s.get("notices", []) if h not in set(p.get("notices", []))]
            if fresh and p.get("notices") is not None:
                out["notices"].append((url, fresh))
    return out


def diff_lines(old, new, limit=24):
    d = [l for l in difflib.unified_diff(old or [], new or [], lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---")]
    return d[:limit], len(d)


def cites(links, url):
    gs = sorted({g for g, _ in links.get(url, [])})
    return ", ".join(f"`{g}`" for g in gs[:6]) + (f" and {len(gs) - 6} more" if len(gs) > 6 else "")


def report(cmp, prev_state, cur, links, baseline):
    today = dt.date.today().isoformat()
    ok = sum(1 for s in cur.values() if s["ok"])
    lines = [f"# Scheme watch: {today}", "",
             f"Checked **{len(cur)}** official links from the guides: {ok} opened, {len(cur) - ok} did not.", ""]
    if baseline:
        lines += ["**First run: baseline recorded.** From next week this report lists what changed.", ""]
    lines += ["| What | Count |", "| :--- | ---: |",
              f"| Pages whose text changed | {len(cmp['changed'])} |",
              f"| Pages with new notices / orders / PDFs | {len(cmp['notices'])} |",
              f"| Links that stopped working | {len(cmp['failing'])} |",
              f"| Links working again | {len(cmp['recovered'])} |",
              f"| Still not working | {len(cmp['still'])} |", ""]
    prev = prev_state.get("pages", {})
    if cmp["changed"]:
        lines += ["## Pages whose text changed", ""]
        for url in cmp["changed"]:
            s, p = cur[url], prev[url]
            d, total = diff_lines(p.get("lines"), s.get("lines"))
            money = any(MONEY_DATE_RE.search(l) for l in d)
            lines += [f"### {'⚠ ' if money else ''}{url}", "",
                      f"Cited in {cites(links, url)}." + (" **Amounts or dates appear in the changed lines.**" if money else ""), ""]
            if s.get("kind") == "file":
                lines += ["The file itself changed (not an HTML page).", ""]
            elif d:
                lines += ["<details><summary>Changed lines" + (f" (first {len(d)} of {total})" if total > len(d) else "") + "</summary>", "",
                          "```diff"] + [l[:300] for l in d] + ["```", "", "</details>", ""]
    if cmp["notices"]:
        lines += ["## New notices, orders or PDFs", ""]
        for url, fresh in cmp["notices"]:
            nt = cur[url].get("notice_text", {})
            lines += [f"**{url}** (cited in {cites(links, url)})", ""]
            lines += [f"- [{html.escape(nt.get(h) or h.rsplit('/', 1)[-1])[:100]}]({h})" for h in fresh[:15]]
            if len(fresh) > 15:
                lines.append(f"- … and {len(fresh) - 15} more")
            lines.append("")
    if cmp["failing"]:
        lines += ["## Links that stopped working", "", "| Link | Problem | Cited in |", "| :--- | :--- | :--- |"]
        lines += [f"| {u} | {cur[u].get('error') or cur[u].get('status')} | {cites(links, u)} |" for u in cmp["failing"]]
        lines.append("")
    if cmp["recovered"]:
        lines += ["## Working again", ""] + [f"- {u}" for u in cmp["recovered"]] + [""]
    if cmp["still"]:
        lines += ["<details><summary>Still not working (" + str(len(cmp["still"])) + ")</summary>", "",
                  "| Link | Problem | Cited in |", "| :--- | :--- | :--- |"]
        lines += [f"| {u} | {cur[u].get('error') or cur[u].get('status')} | {cites(links, u)} |" for u in cmp["still"]]
        lines += ["", "</details>", ""]
    if cmp["thin"]:
        lines += ["<details><summary>Pages with too little text to watch (" + str(len(cmp["thin"])) + ")</summary>", "",
                  "These load their content with JavaScript, so only whether they open is checked.", ""]
        lines += [f"- {u}" for u in cmp["thin"]] + ["", "</details>", ""]
    lines += ["---", "A page changing does not always mean the scheme changed (menus and banners change too). "
              "Check flagged pages, then update the guide's content file, its Official links and Verification sections."]
    return "\n".join(lines) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--state", required=True, help="state.json from the previous run (created if missing)")
    ap.add_argument("--report", required=True, help="where to write the Markdown report")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--only", help="check only URLs containing this text (for testing)")
    a = ap.parse_args(argv)

    links = guide_links()
    urls = sorted(u for u in links if not a.only or a.only in u)
    state_path = pathlib.Path(a.state)
    prev_state = json.loads(state_path.read_text()) if state_path.exists() else {}
    baseline = not prev_state.get("pages")
    with cf.ThreadPoolExecutor(a.workers) as ex:
        cur = dict(zip(urls, ex.map(snapshot, urls)))
    cmp = compare(prev_state.get("pages", {}), cur, links)
    text = report(cmp, prev_state, cur, links, baseline)
    pathlib.Path(a.report).write_text(text, encoding="utf-8")

    # Keep the previous good snapshot for a page that failed this week, so a temporary outage
    # does not reset its baseline and show every line as changed when it comes back.
    merged = dict(prev_state.get("pages", {}))
    for u, s in cur.items():
        merged[u] = s if s["ok"] or u not in merged else {**merged[u], "ok": False, "status": s.get("status"),
                                                           "error": s.get("error"), "checked": s["checked"]}
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps({"updated": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), "pages": merged},
                                     ensure_ascii=False, indent=0, sort_keys=True), encoding="utf-8")

    notable = bool(cmp["changed"] or cmp["notices"] or cmp["failing"] or cmp["recovered"]) or baseline
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"notable={'true' if notable else 'false'}\n")
    print(f"{len(urls)} links: {sum(1 for s in cur.values() if s['ok'])} ok, changed {len(cmp['changed'])}, "
          f"new notices on {len(cmp['notices'])} pages, failing {len(cmp['failing'])}, recovered {len(cmp['recovered'])}"
          + (" (baseline)" if baseline else ""))


if __name__ == "__main__":
    main()
