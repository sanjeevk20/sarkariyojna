"""Make the printable CSC / e-Mitra operator handout for the Sathi pilot.

Writes operator-handout-<lang>.html (A4, two pages: how to use Sathi, then a case log to fill by hand)
for English, Marathi (Maharashtra pilot) and Hindi (Uttar Pradesh pilot). Print from a browser, or
render PDFs with Playwright (see README.md). The QR code (qr-check.svg) opens the "Am I stuck?" checker.

    python3 docs/pilot/build_handout.py
"""
import html, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
URL = "sanjeevk20.github.io/sarkariyojna/#check"
QR = re.sub(r"<\?xml[^>]*\?>", "", (HERE / "qr-check.svg").read_text())
QR = re.sub(r'width="[^"]*" height="[^"]*"', 'width="100%" height="100%"', QR, count=1)

T = {
 "en": dict(
  font="'Noto Sans',sans-serif", title="Sathi pilot: operator guide",
  h1="Customer's government work stuck? Find the next step in 2 minutes",
  lead="Sathi is a free website that reads a scheme's status and tells the customer what it means, what to do next, and drafts a complaint if the office is late.",
  when_h="Use it when a customer says", when=["“My money / instalment has not come”", "“My application has been pending for a long time”", "“It shows rejected and I don't know why”"],
  steps_h="Six steps",
  steps=[f"Scan the QR code or open <b>{URL}</b>. Choose the language.",
         "Choose the scheme.",
         "<b>Paste the status text</b> from the portal or SMS, or tick the status that matches. Enter the date of application.",
         "Read out <b>What it means</b> and <b>What to do next</b> to the customer.",
         "If it is overdue or stuck: type only the customer's name and mobile, then print, copy or WhatsApp the <b>complaint letter</b>, and tell them where to submit it.",
         "Write <b>one line in the case log</b> (page 2). Set a follow-up date 30 days ahead."],
  cover_h="Status checker covers", cover="{cover}. Step-by-step guides cover {n} schemes; open any guide from the home page.",
  rules_h="Rules", rules=["Sathi is <b>free</b>. Do not charge for using it. Your normal fee for portal work is fine.",
         "<b>Never type</b> Aadhaar number, bank account, OTP or passwords into Sathi. It does not need them.",
         "What you type stays in this browser. Nothing is sent unless the customer chooses <b>Help others: share this anonymously</b>.",
         "Do not write customer names, Aadhaar or mobile numbers in the case log."],
  say_h="What to tell the customer", say="“This is what your status means. Do this next. If nothing changes by <i>[follow-up date]</i>, come back and we will send this complaint.”",
  help_h="Pilot help", help="Pilot coordinator: ____________________ · WhatsApp: ____________________ · Wrong information on a guide? Tap <b>Report an error</b> on that guide.",
  op="Operator code", dist="District", log_h="Case log: one line per customer. No names, Aadhaar or mobile numbers.",
  cols=["#", "Date", "Scheme", "Stage Sathi showed", "Action today: wait / fix / complaint", "Follow-up date", "After 30 days: solved / still stuck / not known", "Minutes"],
  foot="Sathi is not a government website. Always use the official links shown on each guide."),
 "mr": dict(
  font="'Noto Sans Devanagari','Noto Sans',sans-serif", title="साथी पायलट: ऑपरेटर मार्गदर्शक",
  h1="ग्राहकाचे सरकारी काम अडकले आहे? 2 मिनिटांत पुढचे पाऊल शोधा",
  lead="साथी ही मोफत वेबसाइट आहे. ती योजनेची स्थिती वाचून ग्राहकाला सांगते की त्याचा अर्थ काय, पुढे काय करायचे, आणि कार्यालयाने उशीर केला असल्यास तक्रारीचा मसुदा तयार करते.",
  when_h="ग्राहक असे म्हणाला तर वापरा", when=["“माझे पैसे / हप्ता आलेला नाही”", "“माझा अर्ज खूप दिवसांपासून प्रलंबित आहे”", "“नाकारला असे दाखवते, कारण कळत नाही”"],
  steps_h="सहा पायऱ्या",
  steps=[f"QR कोड स्कॅन करा किंवा <b>{URL}</b> उघडा. भाषा निवडा.",
         "योजना निवडा.",
         "पोर्टल किंवा SMS मधील <b>स्थितीचा मजकूर पेस्ट करा</b>, किंवा जुळणारी स्थिती निवडा. अर्जाची तारीख भरा.",
         "<b>याचा अर्थ</b> आणि <b>पुढे काय करायचे</b> ग्राहकाला वाचून सांगा.",
         "मुदत संपली असेल किंवा काम अडकले असेल: फक्त ग्राहकाचे नाव आणि मोबाईल भरा, मग <b>तक्रार पत्र</b> प्रिंट, कॉपी किंवा WhatsApp करा आणि ते कुठे द्यायचे ते सांगा.",
         "<b>केस नोंदवहीत एक ओळ</b> लिहा (पान 2). 30 दिवसांनंतरची पाठपुरावा तारीख ठरवा."],
  cover_h="स्थिती तपासणी उपलब्ध", cover="{cover}. {n} योजनांसाठी टप्प्याटप्प्याने मार्गदर्शक आहेत; मुख्य पानावरून कोणताही मार्गदर्शक उघडा.",
  rules_h="नियम", rules=["साथी <b>मोफत</b> आहे. ते वापरण्यासाठी पैसे घेऊ नका. पोर्टलच्या कामाचे तुमचे नेहमीचे शुल्क चालेल.",
         "साथीमध्ये आधार क्रमांक, बँक खाते, OTP किंवा पासवर्ड <b>कधीही टाइप करू नका</b>. त्याची गरज नाही.",
         "तुम्ही टाइप केलेले याच ब्राउझरमध्ये राहते. ग्राहकाने <b>अनामिकपणे शेअर करा</b> निवडले तरच काही पाठवले जाते.",
         "केस नोंदवहीत ग्राहकाचे नाव, आधार किंवा मोबाईल क्रमांक लिहू नका."],
  say_h="ग्राहकाला काय सांगायचे", say="“तुमच्या स्थितीचा अर्थ हा आहे. पुढे हे करा. <i>[पाठपुरावा तारीख]</i> पर्यंत काही बदलले नाही तर परत या, आपण ही तक्रार पाठवू.”",
  help_h="पायलट मदत", help="पायलट समन्वयक: ____________________ · WhatsApp: ____________________ · मार्गदर्शकात चुकीची माहिती? त्या मार्गदर्शकावर <b>चूक कळवा</b> दाबा.",
  op="ऑपरेटर कोड", dist="जिल्हा", log_h="केस नोंदवही: प्रत्येक ग्राहकासाठी एक ओळ. नाव, आधार किंवा मोबाईल क्रमांक नको.",
  cols=["#", "तारीख", "योजना", "साथीने दाखवलेली स्थिती", "आज काय केले: थांबा / दुरुस्ती / तक्रार", "पाठपुरावा तारीख", "30 दिवसांनी: सुटले / अजून अडकले / माहीत नाही", "मिनिटे"],
  foot="साथी ही सरकारी वेबसाइट नाही. नेहमी प्रत्येक मार्गदर्शकावर दिलेल्या अधिकृत लिंक वापरा."),
 "hi": dict(
  font="'Noto Sans Devanagari','Noto Sans',sans-serif", title="साथी पायलट: ऑपरेटर मार्गदर्शिका",
  h1="ग्राहक का सरकारी काम अटका है? 2 मिनट में अगला कदम जानें",
  lead="साथी एक मुफ़्त वेबसाइट है। यह योजना की स्थिति पढ़कर ग्राहक को बताती है कि इसका मतलब क्या है, आगे क्या करना है, और दफ़्तर देर करे तो शिकायत का मसौदा बनाती है।",
  when_h="ग्राहक यह कहे तो इस्तेमाल करें", when=["“मेरा पैसा / किस्त नहीं आई”", "“मेरा आवेदन बहुत दिनों से लंबित है”", "“अस्वीकृत दिखा रहा है, कारण नहीं पता”"],
  steps_h="छह कदम",
  steps=[f"QR कोड स्कैन करें या <b>{URL}</b> खोलें। भाषा चुनें।",
         "योजना चुनें।",
         "पोर्टल या SMS से <b>स्थिति का टेक्स्ट पेस्ट करें</b>, या मिलती-जुलती स्थिति चुनें। आवेदन की तारीख भरें।",
         "<b>इसका मतलब</b> और <b>आगे क्या करें</b> ग्राहक को पढ़कर बताएं।",
         "समय-सीमा निकल गई हो या काम अटका हो: सिर्फ़ ग्राहक का नाम और मोबाइल भरें, फिर <b>शिकायत पत्र</b> प्रिंट, कॉपी या WhatsApp करें और बताएं कि कहां जमा करना है।",
         "<b>केस रजिस्टर में एक लाइन</b> लिखें (पेज 2)। 30 दिन बाद की फ़ॉलो-अप तारीख तय करें।"],
  cover_h="स्थिति जांच उपलब्ध", cover="{cover}। {n} योजनाओं के लिए कदम-दर-कदम मार्गदर्शिकाएं हैं; मुख्य पेज से कोई भी मार्गदर्शिका खोलें।",
  rules_h="नियम", rules=["साथी <b>मुफ़्त</b> है। इसके इस्तेमाल के पैसे न लें। पोर्टल के काम का आपका सामान्य शुल्क ठीक है।",
         "साथी में आधार नंबर, बैंक खाता, ओटीपी या पासवर्ड <b>कभी न टाइप करें</b>। इसकी ज़रूरत नहीं है।",
         "आप जो टाइप करते हैं वह इसी ब्राउज़र में रहता है। ग्राहक <b>गुमनाम रूप से साझा करें</b> चुने तभी कुछ भेजा जाता है।",
         "केस रजिस्टर में ग्राहक का नाम, आधार या मोबाइल नंबर न लिखें।"],
  say_h="ग्राहक को क्या बताएं", say="“आपकी स्थिति का मतलब यह है। आगे यह करें। <i>[फ़ॉलो-अप तारीख]</i> तक कुछ न बदले तो वापस आइए, हम यह शिकायत भेजेंगे।”",
  help_h="पायलट सहायता", help="पायलट समन्वयक: ____________________ · WhatsApp: ____________________ · मार्गदर्शिका में गलत जानकारी? उस मार्गदर्शिका पर <b>गलती बताएं</b> दबाएं।",
  op="ऑपरेटर कोड", dist="ज़िला", log_h="केस रजिस्टर: हर ग्राहक के लिए एक लाइन। नाम, आधार या मोबाइल नंबर नहीं।",
  cols=["#", "तारीख", "योजना", "साथी ने जो स्थिति दिखाई", "आज क्या किया: प्रतीक्षा / सुधार / शिकायत", "फ़ॉलो-अप तारीख", "30 दिन बाद: हल / अब भी अटका / पता नहीं", "मिनट"],
  foot="साथी सरकारी वेबसाइट नहीं है। हमेशा हर मार्गदर्शिका पर दिए गए आधिकारिक लिंक का उपयोग करें।"),
}

# Which checkers each pilot handout lists (the pilot states' own schemes first).
COVER = {
 "en": ("PM-KISAN, Ladki Bahin, income certificate (UP), old-age pension (UP), Ladli Behna (MP), "
        "Gruha Lakshmi (Karnataka), social security pension (Rajasthan)", 68),
 "mr": ("पीएम-किसान, माझी लाडकी बहीण योजना (तसेच UP, MP, कर्नाटक व राजस्थानच्या काही योजना)", 68),
 "hi": ("पीएम-किसान, वृद्धावस्था पेंशन, आय प्रमाण पत्र (उत्तर प्रदेश), लाड़ली बहना (मप्र), सामाजिक सुरक्षा पेंशन (राजस्थान)", 68),
}

CSS = """
@page { size: A4; margin: 12mm; }
* { box-sizing: border-box; }
body { margin: 0; font-family: %(font)s; color: #1b1f24; background: #fff; font-size: 10.5pt; line-height: 1.45; }
.page { width: 186mm; min-height: 270mm; margin: 0 auto; padding: 0; page-break-after: always; }
.page:last-child { page-break-after: auto; }
header { display: flex; gap: 6mm; align-items: flex-start; border-bottom: 2px solid #1f6f43; padding-bottom: 4mm; margin-bottom: 4mm; }
.brand { font-size: 9pt; color: #1f6f43; font-weight: 700; letter-spacing: .04em; text-transform: uppercase; }
h1 { font-size: 17pt; line-height: 1.25; margin: 1mm 0 2mm; }
.lead { margin: 0; color: #3a4048; }
.qr { flex: 0 0 34mm; text-align: center; font-size: 7.5pt; color: #3a4048; }
.qr .box { width: 32mm; height: 32mm; margin: 0 auto 1mm; }
h2 { font-size: 11.5pt; margin: 4mm 0 1.5mm; color: #1f6f43; }
ol.steps { margin: 0; padding: 0; list-style: none; counter-reset: s; }
ol.steps li { counter-increment: s; position: relative; padding: 1.6mm 0 1.6mm 10mm; border-bottom: 1px solid #e3e6ea; }
ol.steps li::before { content: counter(s); position: absolute; left: 0; top: 1.4mm; width: 7mm; height: 7mm; border-radius: 50%%;
  background: #1f6f43; color: #fff; font-weight: 700; text-align: center; line-height: 7mm; font-size: 10pt; }
ul { margin: 0; padding-left: 5mm; }
li { margin: .6mm 0; }
.cols { display: grid; grid-template-columns: 1fr 1fr; gap: 5mm; }
.box2 { border: 1px solid #d5d9de; border-radius: 3mm; padding: 2.5mm 3.5mm; }
.rules { border-color: #c0392b; background: #fdf3f2; }
.say { background: #eef6f1; border-color: #9cc9ae; }
.foot { margin-top: 4mm; font-size: 8.5pt; color: #5b626b; border-top: 1px solid #e3e6ea; padding-top: 2mm; }
.meta { display: flex; gap: 8mm; margin: 2mm 0 3mm; font-size: 10pt; }
.meta span { flex: 1; border-bottom: 1px solid #1b1f24; padding-bottom: 1mm; }
table { width: 100%%; border-collapse: collapse; font-size: 8.5pt; table-layout: fixed; }
th, td { border: 1px solid #8a9199; padding: 1.2mm; vertical-align: top; }
th { background: #eef1f4; text-align: left; font-weight: 700; }
td { height: 11.5mm; }
col.n { width: 6mm; } col.d { width: 17mm; } col.s { width: 26mm; } col.m { width: 13mm; } col.f { width: 18mm; }
"""


def page(lang):
    t = T[lang]
    cover, n = COVER[lang]
    e = lambda s: s  # strings are trusted, hand-written HTML
    steps = "".join(f"<li>{s}</li>" for s in t["steps"])
    when = "".join(f"<li>{html.escape(w)}</li>" for w in t["when"])
    rules = "".join(f"<li>{r}</li>" for r in t["rules"])
    head = "".join(f"<th>{html.escape(c)}</th>" for c in t["cols"])
    rows = "".join("<tr>" + f"<td>{i}</td>" + "<td></td>" * (len(t["cols"]) - 1) + "</tr>" for i in range(1, 19))
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(t['title'])}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&family=Noto+Sans+Devanagari:wght@400;700&display=swap">
<style>{CSS % {'font': t['font']}}</style></head>
<body>
<section class="page">
  <header>
    <div style="flex:1">
      <div class="brand">Sathi · {html.escape(t['title'])}</div>
      <h1>{e(t['h1'])}</h1>
      <p class="lead">{e(t['lead'])}</p>
    </div>
    <div class="qr"><div class="box">{QR}</div>{URL}</div>
  </header>
  <div class="cols">
    <div><h2>{e(t['when_h'])}</h2><ul>{when}</ul></div>
    <div><h2>{e(t['cover_h'])}</h2><p style="margin:0">{t['cover'].format(cover=cover, n=n)}</p></div>
  </div>
  <h2>{e(t['steps_h'])}</h2>
  <ol class="steps">{steps}</ol>
  <div class="cols" style="margin-top:4mm">
    <div class="box2 rules"><h2 style="margin-top:0;color:#c0392b">{e(t['rules_h'])}</h2><ul>{rules}</ul></div>
    <div class="box2 say"><h2 style="margin-top:0">{e(t['say_h'])}</h2><p style="margin:0">{t['say']}</p></div>
  </div>
  <h2>{e(t['help_h'])}</h2>
  <p style="margin:0">{t['help']}</p>
  <p class="foot">{e(t['foot'])}</p>
</section>
<section class="page">
  <div class="brand">Sathi · {html.escape(t['title'])}</div>
  <h1 style="font-size:14pt">{e(t['log_h'])}</h1>
  <div class="meta"><span>{e(t['op'])}:</span><span>{e(t['dist'])}:</span></div>
  <table><colgroup><col class="n"><col class="d"><col class="s"><col><col><col class="f"><col><col class="m"></colgroup>
  <thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>
</section>
</body></html>
"""


if __name__ == "__main__":
    for lang in T:
        out = HERE / f"operator-handout-{lang}.html"
        out.write_text(page(lang))
        print("wrote", out.name)
