"""Generate EN + MR customer guides for Aaple Sarkar income certificate."""
import sys

repo = sys.argv[1]
base = open(f"{repo}/docs/workflows/pm-kisan-farmer-guide.html").read()
style = base[base.index("<style>"):base.index("</style>")]
style += """  .rights { margin-top:20px; background:#fff7ed; border:2px solid #ea580c; border-radius:14px; padding:14px 18px; font-size:17px; line-height:1.6; }
  .rights .t { font-size:21px; font-weight:700; color:#c2410c; }
</style>"""

T = {
 "en": dict(
  lang="en", font="'Noto Sans','FreeSans',sans-serif",
  h1="Income Certificate: How to get it on Aaple Sarkar",
  sub="उत्पन्नाचा दाखला: आपले सरकार वरून कसा मिळवायचा",
  benefit="Needed for scholarships, fee concession, EWS and many schemes",
  legend=["You do this", "Government does this (you wait)", "Certificate ready"],
  phases=["Before you apply", "After you apply"],
  who={"you": "You", "gov": "Government", "done": "Done"},
  stuck="Stuck?", tip="Tip:",
  steps=[
   ("you", "Check which certificate you need", "कोणता दाखला हवा ते तपासा",
    "Ask the scheme or office: <b>which year's income</b> (1 year or 3 years) and <b>in whose name</b> (yours or your parent's). Most schemes want a certificate from the <b>current financial year</b>.",
    ("stuck", "Have last year's certificate? Most schemes reject it. Apply fresh, early.")),
   ("you", "Keep these papers ready", "कागदपत्रे तयार ठेवा",
    "<ul><li><b>Identity:</b> Aadhaar / PAN / Voter ID</li><li><b>Address:</b> Ration card / Electricity bill</li><li><b>Income:</b> Job → Form 16 or salary slip · Farmer → 7/12 and 8A · Others → self-declaration</li><li>Passport-size photo</li></ul>",
    ("tip", "No stamp-paper affidavit needed. A signed <b>self-declaration</b> is enough.")),
   ("you", "Apply", "अर्ज करा",
    "Choose any one:<ul><li>Website <b>aaplesarkar.mahaonline.gov.in</b> → Revenue Department → Income Certificate</li><li>Nearest <b>Aaple Sarkar Seva Kendra</b> / Maha e-Seva Kendra</li></ul>Pay the small fee. Note down your <b>Application ID</b> and the <b>time limit (days)</b> shown.",
    ("tip", "At a Seva Kendra pay only the fixed fee and take a receipt. Never pay an agent extra.")),
   ("gov", "Your papers are checked", "कागदपत्रांची तपासणी",
    "The Tahsil office checks your form and documents.",
    ("stuck", "Status says <b>sent back</b>? Read the remark, upload the missing paper and resubmit online. <b>No visit needed.</b>")),
   ("gov", "Income is verified (if needed)", "उत्पन्नाची पडताळणी",
    "For farm or business income, the Talathi may be asked for a report.",
    ("stuck", "Pending at Talathi for long? Visit the Talathi office with your Application ID.")),
   ("gov", "Tahsildar approves", "तहसीलदारांची मंजुरी",
    "Tahsildar / Naib Tahsildar approves and <b>signs digitally</b>.", None),
   ("done", "Download your certificate", "दाखला डाउनलोड करा",
    "Log in to Aaple Sarkar and download it. It is <b>digitally signed</b>, so it is valid <b>without any stamp</b>.", None),
  ],
  rights_t="Late? It's your right.",
  rights="If the time limit has passed, you can file a <b>First Appeal</b> on Aaple Sarkar with your Application ID, under the <b>Maharashtra Right to Public Services Act, 2015</b>.",
  help="<b>Check status anytime:</b> Aaple Sarkar → Track your application (Application ID)<br><b>Renew every year</b> · <b>Use only .gov.in websites</b>",
 ),
 "mr": dict(
  lang="mr", font="'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
  h1="उत्पन्नाचा दाखला: आपले सरकार वरून कसा मिळवायचा",
  sub=None,
  benefit="शिष्यवृत्ती, फी सवलत, EWS आणि अनेक योजनांसाठी आवश्यक",
  legend=["हे तुम्ही करायचे", "हे सरकार करते (तुम्ही वाट पाहा)", "दाखला तयार"],
  phases=["अर्ज करण्यापूर्वी", "अर्ज केल्यानंतर"],
  who={"you": "तुम्ही", "gov": "सरकार", "done": "पूर्ण"},
  stuck="अडचण?", tip="सूचना:",
  steps=[
   ("you", "कोणता दाखला हवा ते तपासा", None,
    "ज्या योजनेसाठी किंवा कार्यालयासाठी दाखला हवा आहे तिथे विचारा: <b>किती वर्षांचे उत्पन्न</b> (1 वर्ष की 3 वर्षे) आणि <b>कोणाच्या नावाने</b> (तुमच्या की पालकांच्या). बहुतेक योजनांना <b>चालू आर्थिक वर्षाचा</b> दाखला लागतो.",
    ("stuck", "मागील वर्षाचा दाखला आहे? बहुतेक योजना तो स्वीकारत नाहीत. लवकर नवीन अर्ज करा.")),
   ("you", "कागदपत्रे तयार ठेवा", None,
    "<ul><li><b>ओळखीचा पुरावा:</b> आधार / पॅन / मतदार ओळखपत्र</li><li><b>पत्त्याचा पुरावा:</b> रेशन कार्ड / वीज बिल</li><li><b>उत्पन्नाचा पुरावा:</b> नोकरी → फॉर्म 16 किंवा पगार पत्रक · शेतकरी → 7/12 व 8-अ उतारा · इतर → स्वयंघोषणापत्र</li><li>पासपोर्ट आकाराचा फोटो</li></ul>",
    ("tip", "स्टॅम्प पेपरवरील प्रतिज्ञापत्राची गरज नाही. सही केलेले <b>स्वयंघोषणापत्र</b> पुरेसे आहे.")),
   ("you", "अर्ज करा", None,
    "यापैकी कोणताही एक मार्ग:<ul><li>वेबसाइट <b>aaplesarkar.mahaonline.gov.in</b> → महसूल विभाग → उत्पन्नाचा दाखला</li><li>जवळचे <b>आपले सरकार सेवा केंद्र</b> / महा ई-सेवा केंद्र</li></ul>थोडी फी भरा. तुमचा <b>अर्ज क्रमांक</b> (Application ID) आणि दाखवलेली <b>कालमर्यादा (दिवस)</b> लिहून ठेवा.",
    ("tip", "सेवा केंद्रात फक्त ठरलेली फी भरा आणि पावती घ्या. एजंटला जास्त पैसे देऊ नका.")),
   ("gov", "कागदपत्रांची तपासणी", None,
    "तहसील कार्यालय तुमचा अर्ज आणि कागदपत्रे तपासते.",
    ("stuck", "अर्ज <b>परत पाठवला</b> (Sent back) असे दिसले? शेरा वाचा, राहिलेले कागदपत्र अपलोड करून ऑनलाइन पुन्हा सादर करा. <b>कार्यालयात जाण्याची गरज नाही.</b>")),
   ("gov", "उत्पन्नाची पडताळणी (गरज असल्यास)", None,
    "शेती किंवा व्यवसायाच्या उत्पन्नासाठी तलाठ्यांकडून अहवाल मागवला जाऊ शकतो.",
    ("stuck", "तलाठ्यांकडे बराच काळ प्रलंबित? अर्ज क्रमांक घेऊन तलाठी कार्यालयात भेटा.")),
   ("gov", "तहसीलदारांची मंजुरी", None,
    "तहसीलदार / नायब तहसीलदार मंजुरी देऊन <b>डिजिटल सही</b> करतात.", None),
   ("done", "दाखला डाउनलोड करा", None,
    "आपले सरकार वर लॉगिन करून दाखला डाउनलोड करा. त्यावर <b>डिजिटल सही</b> असल्याने तो <b>कोणत्याही शिक्क्याशिवाय वैध</b> आहे.", None),
  ],
  rights_t="उशीर झाला? हा तुमचा हक्क आहे.",
  rights="कालमर्यादा संपली असेल तर <b>महाराष्ट्र लोकसेवा हक्क अधिनियम, 2015</b> नुसार अर्ज क्रमांक वापरून आपले सरकार वर <b>प्रथम अपील</b> करता येते.",
  help="<b>स्थिती कधीही तपासा:</b> आपले सरकार → Track your application (अर्ज क्रमांक)<br><b>दरवर्षी नवीन दाखला काढा</b> · <b>फक्त .gov.in वेबसाइट वापरा</b>",
 ),
}

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
        if i == 4:
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
    open(f"{repo}/docs/workflows/income-certificate-guide{suffix}.html", "w").write("\n".join(out))
