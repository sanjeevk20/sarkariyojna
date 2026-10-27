"""Build the Sathi guides website (one page, hash-routed) from docs/workflows.

Reads the index (docs/workflows/README.md) for titles and categories, each guide's
generated EN / MR HTML for the citizen steps, and each guide's .md for the
Official links table, the Mermaid system workflow and the sources.

    python3 docs/site/build_site.py   ->   docs/site/index.html
"""
import json, pathlib, re
from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parent
WF = ROOT.parent / "workflows"

# Index section -> site category. Mixed index sections are split per guide.
CATEGORY = {
    "pm-kisan": "farm", "namo-shetkari": "farm", "pik-vima": "farm", "krushi-swavalamban": "farm",
    "birsa-munda": "farm", "magel-tyala-shettale": "farm", "saur-krushi-pump": "farm",
    "income-certificate": "docs", "domicile-certificate": "docs", "caste-certificate": "docs",
    "ncl-certificate": "docs", "caste-validity": "docs", "ferfar": "docs",
    "mahadbt-scholarship": "edu", "mjprf": "edu",
    "ladki-bahin": "women", "ujjwala": "women",
    "pmay-gramin": "home", "pmay-urban": "home",
    "sanjay-gandhi": "pension", "shravanbal": "pension", "shiv-bhojan": "pension",
    "ayushman-card": "health", "mjpjay": "health",
    "annasaheb-patil": "loan", "mahatma-phule-mahamandal": "loan",
}
CATS = [
    ("farm", "Farming", "शेती"), ("docs", "Certificates & land", "दाखले व जमीन"),
    ("edu", "Education", "शिक्षण"), ("women", "Women & family", "महिला व कुटुंब"),
    ("home", "Housing", "घरकुल"), ("pension", "Pensions & food", "निवृत्तीवेतन व अन्न"),
    ("health", "Health", "आरोग्य"), ("loan", "Business loans", "व्यवसाय कर्ज"),
]
TIP_LABELS = ("Tip:", "सूचना:")


def index_rows():
    rows = []
    for line in (WF / "README.md").read_text().splitlines():
        m = re.match(r"\| \[([^\]]+)\]\(([a-z0-9-]+)\.md\) \| ([^|]+) \| ([^|]+) \|", line)
        if m:
            rows.append(dict(slug=m[2], title=m[1].strip(), mr_name=m[3].strip(), audience=m[4].strip()))
    return rows


def routers():
    text = (WF / "README.md").read_text().split("## Quick routers", 1)[1].split("\n## ", 1)[0]
    out = []
    for line in text.strip().splitlines():
        line = re.sub(r"\[([^\]]+)\]\(([a-z0-9-]+)\.md\)", r'<a href="#\2">\1</a>', line.lstrip("- "))
        out.append(re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", line))
    return out


def inner(tag):
    return tag.decode_contents().strip() if tag else ""


def parse_guide(path):
    soup = BeautifulSoup(path.read_text(), "html.parser")
    page = soup.select_one("#page")
    items, phase = [], None
    for el in page.find_all("div", recursive=False):
        cls = el.get("class", [])
        if "phase" in cls:
            phase = el.get_text(strip=True)
        elif "step" in cls:
            kind = next(c for c in cls if c in ("you", "gov", "done"))
            title = el.select_one(".title")
            for s in title.select(".mr"):
                s.decompose()
            note = None
            nd = el.select_one(".stuck")
            if nd:
                b = nd.find("b")
                label = b.get_text(strip=True) if b else ""
                if b:
                    b.decompose()
                note = dict(kind="tip" if label in TIP_LABELS else "stuck", label=label, html=inner(nd))
            items.append(dict(phase=phase, kind=kind, who=el.select_one(".who").get_text(strip=True),
                              title=title.get_text(" ", strip=True), body=inner(el.select_one(".body")), note=note))
            phase = None
    rights = page.select_one(".rights")
    rights_t = ""
    if rights:
        t = rights.select_one(".t")
        rights_t = t.get_text(strip=True)
        t.decompose()
    return dict(h1=page.find("h1").get_text(strip=True), benefit=inner(page.select_one(".benefit")),
                steps=items, rights_t=rights_t, rights=inner(rights), help=inner(page.select_one(".help")))


def parse_md(path):
    md = path.read_text()
    guide = re.search(r"\[`([a-z0-9-]+-guide)\.html`\]", md)[1]
    links = []
    sect = md.split("## Official links", 1)[1].split("\n## ", 1)[0]
    for m in re.finditer(r"^\| (?!What|:---)(.+?) \| (<(\S+)>|-) \| (.+?) \|$", sect, re.M):
        links.append(dict(label=m[1], url=m[3], gov=m[4].startswith("Government")))
    mermaid = re.search(r"```mermaid\n(.*?)```", md, re.S)[1].strip()
    ver = md.split("## Verification", 1)[1] if "## Verification" in md else ""
    sources, seen = [], set()
    for m in re.finditer(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", ver):
        if m[2] not in seen:
            seen.add(m[2])
            sources.append(dict(label=m[1], url=m[2]))
    return guide, links, mermaid, sources


def build():
    posts = []
    for row in index_rows():
        slug = row["slug"]
        guide, links, mermaid, sources = parse_md(WF / f"{slug}.md")
        posts.append(dict(row, cat=CATEGORY[slug], links=links, mermaid=mermaid, sources=sources,
                          en=parse_guide(WF / f"{guide}.html"), mr=parse_guide(WF / f"{guide}-mr.html")))
    order = [c[0] for c in CATS]
    posts.sort(key=lambda p: order.index(p["cat"]))
    data = dict(cats=[dict(id=i, en=e, mr=m) for i, e, m in CATS], posts=posts, routers=routers())
    js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    tpl = (ROOT / "template.html").read_text()
    (ROOT / "index.html").write_text(tpl.replace("/*__DATA__*/null", js))
    print(f"{len(posts)} guides -> {ROOT / 'index.html'}")


if __name__ == "__main__":
    build()
