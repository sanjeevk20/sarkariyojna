"""Build the Sathi guides website (one page, hash-routed) from docs/workflows.

For each state it reads the index (docs/workflows/README.md for Maharashtra,
docs/workflows/up/README.md for Uttar Pradesh) for titles and quick routes, each
guide's generated English and local-language HTML (Marathi / Hindi) for the citizen
steps, and each guide's .md for the Official links table, the Mermaid system
workflow and the sources.

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
    "up-income-certificate": "docs", "up-caste-certificate": "docs", "up-domicile-certificate": "docs",
    "up-dakhil-kharij": "docs", "up-old-age-pension": "pension", "up-widow-pension": "pension",
    "up-ration-card": "pension", "up-kanya-sumangala": "women", "up-samuhik-vivah": "women",
    "up-scholarship": "edu", "up-cm-yuva": "loan", "up-pm-kisan": "farm",
}
# (id, English, Marathi, Hindi, folder, local language of its guides)
STATES = [
    ("mh", "Maharashtra", "महाराष्ट्र", "महाराष्ट्र", WF, "mr"),
    ("up", "Uttar Pradesh", "उत्तर प्रदेश", "उत्तर प्रदेश", WF / "up", "hi"),
]
CATS = [
    ("farm", "Farming", "शेती", "खेती"), ("docs", "Certificates & land", "दाखले व जमीन", "प्रमाण पत्र व भूमि"),
    ("edu", "Education", "शिक्षण", "शिक्षा"), ("women", "Women & family", "महिला व कुटुंब", "महिला व परिवार"),
    ("home", "Housing", "घरकुल", "आवास"), ("pension", "Pensions & food", "निवृत्तीवेतन व अन्न", "पेंशन व खाद्य"),
    ("health", "Health", "आरोग्य", "स्वास्थ्य"), ("loan", "Business loans", "व्यवसाय कर्ज", "व्यवसाय ऋण"),
]
TIP_LABELS = ("Tip:", "सूचना:", "सुझाव:")


def index_rows(folder):
    rows = []
    for line in (folder / "README.md").read_text().splitlines():
        m = re.match(r"\| \[([^\]]+)\]\(([a-z0-9-]+)\.md\) \| ([^|]+) \| ([^|]+) \|", line)
        if m:
            rows.append(dict(slug=m[2], title=m[1].strip(), local_name=m[3].strip(), audience=m[4].strip()))
    return rows


def routers(folder):
    text = (folder / "README.md").read_text().split("## Quick routers", 1)[1].split("\n## ", 1)[0]
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
    posts, state_routers = [], {}
    for sid, _, _, _, folder, local in STATES:
        for row in index_rows(folder):
            slug = row["slug"]
            guide, links, mermaid, sources = parse_md(folder / f"{slug}.md")
            posts.append(dict(row, state=sid, local=local, cat=CATEGORY[slug], links=links, mermaid=mermaid,
                              sources=sources, en=parse_guide(folder / f"{guide}.html"),
                              loc=parse_guide(folder / f"{guide}-{local}.html")))
        state_routers[sid] = routers(folder)
    order = [c[0] for c in CATS]
    posts.sort(key=lambda p: ([s[0] for s in STATES].index(p["state"]), order.index(p["cat"])))
    data = dict(cats=[dict(id=i, en=e, mr=m, hi=h) for i, e, m, h in CATS],
                states=[dict(id=i, en=e, mr=m, hi=h) for i, e, m, h, _, _ in STATES],
                posts=posts, routers=state_routers)
    js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    page = (ROOT / "template.html").read_text().replace("/*__DATA__*/null", js)
    # index.html: page fragment for the claude.ai artifact host, which adds the document skeleton.
    (ROOT / "index.html").write_text(page)
    # dist/index.html: complete document for static hosting (GitHub Pages).
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "dist" / "index.html").write_text(standalone(page))
    print(f"{len(posts)} guides -> {ROOT / 'index.html'}, {ROOT / 'dist' / 'index.html'}")


SITE_URL = "https://sanjeevk20.github.io/sarkariyojna/"
DESC = "Step-by-step guides to Maharashtra, Uttar Pradesh and central government schemes, in English, Marathi and Hindi, with official links."
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Ccircle cx='16' cy='16' r='16' fill='%232d6a39'/%3E%3Cpath d='M9 21c0-7 5-11 14-12-1 9-5 14-12 14' "
           "fill='none' stroke='%23fff' stroke-width='2.5' stroke-linecap='round'/%3E%3C/svg%3E")


def standalone(page):
    head, body = page.split("</style>", 1)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<meta property="og:type" content="website">
<meta property="og:title" content="Sathi Yojana Guides">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{SITE_URL}">
<link rel="canonical" href="{SITE_URL}">
<link rel="icon" href="{FAVICON}">
{head}
/* Reset normally supplied by the artifact host. */
:root {{ padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }}
body {{ margin: 0; -webkit-text-size-adjust: 100%; }}
img {{ max-width: 100%; }}
[hidden] {{ display: none !important; }}
</style>
</head>
<body>
{body.strip()}
</body>
</html>
"""


if __name__ == "__main__":
    build()
