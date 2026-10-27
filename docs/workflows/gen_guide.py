"""Render EN + MR step-by-step citizen guides from a content file.

Usage: python3 gen_guide.py <content.py>
"""
import os
import runpy
import sys

here = os.path.dirname(os.path.abspath(__file__))
c = runpy.run_path(sys.argv[1])
T, OUT, PHASE_BREAK = c["T"], c["OUT"], c["PHASE_BREAK"]
base = open(f"{here}/pm-kisan-farmer-guide.html").read()
style = base[base.index("<style>"):base.index("</style>")]
style += """  .rights { margin-top:20px; background:#fff7ed; border:2px solid #ea580c; border-radius:14px; padding:14px 18px; font-size:17px; line-height:1.6; }
  .rights .t { font-size:21px; font-weight:700; color:#c2410c; }
</style>"""

COLORS = {"you": "#2563eb", "gov": "#7c3aed", "done": "#059669"}

for key, t in T.items():
    st = style.replace("font-family:'Noto Sans','FreeSans',sans-serif;", f"font-family:{t['font']};")
    out = [f'<!doctype html>\n<html lang="{t["lang"]}"><head><meta charset="utf-8">',
           '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;600;700&family=Noto+Sans+Devanagari:wght@400;500;600;700&display=swap" rel="stylesheet">',
           st, "</head>", '<body><div id="page">', f"  <h1>{t['h1']}</h1>"]
    if t["sub"]:
        out.append(f'  <div class="sub mr">{t["sub"]}</div>')
    out.append(f'  <div class="benefit">{t["benefit"]}</div>')
    out.append('  <div class="legend">' + "".join(
        f'<span><span class="dot" style="background:{c}"></span>{l}</span>'
        for c, l in zip(COLORS.values(), t["legend"])) + "</div>")
    n = len(t["steps"])
    for i, (kind, title, mr, body, note) in enumerate(t["steps"], 1):
        if i == 1:
            out.append(f'  <div class="phase">{t["phases"][0]}</div>')
        if i == PHASE_BREAK:
            out.append(f'  <div class="phase">{t["phases"][1]}</div>')
        line = '<div class="line"></div>' if i < n else ""
        mr_html = f' <span class="mr">{mr}</span>' if mr else ""
        note_html = ""
        if note:
            note_html = f'<div class="stuck"><b>{t[note[0]]}</b> {note[1]}</div>'
        out.append(
            f'  <div class="step {kind}"><div class="rail"><div class="num">{i}</div>{line}</div><div class="card">'
            f'<div class="who">{t["who"][kind]}</div><div class="title">{title}{mr_html}</div>'
            f'<div class="body">{body}</div>{note_html}</div></div>')
    out.append(f'  <div class="rights"><div class="t">{t["rights_t"]}</div>{t["rights"]}</div>')
    out.append(f'  <div class="help">{t["help"]}</div>')
    out.append("</div></body></html>\n")
    suffix = "" if key == "en" else "-mr"
    open(f"{here}/{OUT}{suffix}.html", "w").write("\n".join(out))
