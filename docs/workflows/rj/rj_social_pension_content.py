"""Social security pension (Rajasthan) guide content (EN + HI)."""

OUT = "rj-social-pension-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Social security pension in Rajasthan',
        'sub': 'राजस्थान सामाजिक सुरक्षा पेंशन',
        'benefit': 'Monthly pension: ₹1,300 from January 2026 by order; a rise to ₹1,450 was announced in the 2026-27 '
                   'budget (reported)',
        'legend': ['You do this', 'Government does this (you wait)', 'Pension received'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you can get it',
                   'पात्रता जांचें',
                   '<ul><li>Old age: women 55+, men 58+</li><li>Widowed, divorced or abandoned women</li><li>People '
                   'with 40% or more disability</li><li>Family income from all sources up to about <b>₹48,000 a '
                   'year</b>, or an eligible category such as BPL (as reported)</li></ul>',
                   None),
                  ('you',
                   'Keep these ready',
                   'ये तैयार रखें',
                   "<ul><li><b>Jan Aadhaar</b> with your name matching Aadhaar</li><li>Age proof; husband's death "
                   'certificate for widows; disability certificate</li><li>Bank account linked to Jan '
                   'Aadhaar</li></ul>',
                   ('tip',
                    "Almost every Rajasthan service now starts from your family's <b>Jan Aadhaar</b>. Names must match "
                    'Aadhaar. No Jan Aadhaar yet? See the <b>Jan Aadhaar</b> guide first.')),
                  ('you',
                   'Apply at e-Mitra',
                   'ई-मित्र से आवेदन करें',
                   'Apply through <b>e-Mitra</b> or your SSO login. The application goes to the <b>BDO</b> (rural) or '
                   '<b>SDM / municipal office</b> (urban). Keep the <b>PPO / application number</b>.',
                   None),
                  ('gov',
                   'Sanction',
                   'स्वीकृति',
                   'The office checks your details against Jan Aadhaar and sanctions the pension.',
                   ('stuck',
                    'Rejected? Ask for the reason on ssp.rajasthan.gov.in. A name or age mismatch with Jan Aadhaar is '
                    'the usual cause; fix Jan Aadhaar and apply again.')),
                  ('you',
                   'Do the yearly verification',
                   'सालाना सत्यापन कराएं',
                   'Every pensioner must do <b>annual physical verification</b>: at an <b>e-Mitra</b> by fingerprint, '
                   'or by face on the <b>Rajasthan Social Pension and Aadhaar Face</b> app. The 2026 deadline was '
                   '<b>31 March</b>.',
                   ('stuck',
                    'Missed verification is the most common reason pensions stop. Do it as soon as possible; the '
                    'stopped amount is usually restored once verified.')),
                  ('done',
                   'Pension every month',
                   'हर महीने पेंशन',
                   'The pension comes by DBT. Check payments on <b>ssp.rajasthan.gov.in</b> (Reports) with your Jan '
                   'Aadhaar or PPO number.',
                   ('stuck',
                    "Shown as 'dead' or 'out of state' by mistake? Go to the BDO / SDM office with Aadhaar and Jan "
                    'Aadhaar to be re-verified.'))],
        'rights_t': 'Pension stopped? Complain.',
        'rights': 'Complain on <b>Rajasthan Sampark 181</b> with your PPO or Jan Aadhaar number, or write to the BDO / '
                  'SDM who sanctioned it.',
        'help': '<b>Status:</b> ssp.rajasthan.gov.in · <b>Verification:</b> e-Mitra or the face app · '
                '<b>Complaints:</b> Sampark 181<br><b>Applying is free</b> · Amounts as reported; check the portal'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'राजस्थान सामाजिक सुरक्षा पेंशन',
        'sub': None,
        'benefit': 'मासिक पेंशन: आदेश के अनुसार जनवरी 2026 से ₹1,300; 2026-27 बजट में ₹1,450 करने की घोषणा (बताए '
                   'अनुसार)',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'पेंशन मिली'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   '<ul><li>वृद्धावस्था: महिला 55+, पुरुष 58+</li><li>विधवा, तलाकशुदा या परित्यक्ता महिला</li><li>40% '
                   'या अधिक दिव्यांगता वाले व्यक्ति</li><li>सभी स्रोतों से पारिवारिक आय लगभग <b>₹48,000 प्रति वर्ष</b> '
                   'तक, या BPL जैसी पात्र श्रेणी (बताए अनुसार)</li></ul>',
                   None),
                  ('you',
                   'ये तैयार रखें',
                   None,
                   '<ul><li><b>जन आधार</b>, जिसमें नाम आधार से मेल खाता हो</li><li>आयु प्रमाण; विधवा के लिए पति का '
                   'मृत्यु प्रमाण पत्र; दिव्यांगता प्रमाण पत्र</li><li>जन आधार से जुड़ा बैंक खाता</li></ul>',
                   ('tip',
                    'राजस्थान की लगभग हर सेवा अब परिवार के <b>जन आधार</b> से शुरू होती है। नाम आधार से मेल खाने चाहिए। '
                    'जन आधार नहीं है? पहले <b>जन आधार</b> मार्गदर्शिका देखें।')),
                  ('you',
                   'ई-मित्र से आवेदन करें',
                   None,
                   '<b>ई-मित्र</b> या अपने SSO लॉगिन से आवेदन करें। आवेदन <b>बीडीओ</b> (ग्रामीण) या <b>एसडीएम / नगर '
                   'निकाय</b> (शहरी) के पास जाता है। <b>पीपीओ / आवेदन संख्या</b> संभाल कर रखें।',
                   None),
                  ('gov',
                   'स्वीकृति',
                   None,
                   'कार्यालय जन आधार से आपकी जानकारी मिलाकर पेंशन स्वीकृत करता है।',
                   ('stuck',
                    'अस्वीकृत? ssp.rajasthan.gov.in पर कारण देखें। आमतौर पर जन आधार से नाम या आयु का अंतर कारण होता '
                    'है; जन आधार सुधारकर फिर आवेदन करें।')),
                  ('you',
                   'सालाना सत्यापन कराएं',
                   None,
                   'हर पेंशनर को <b>सालाना भौतिक सत्यापन</b> कराना होता है: <b>ई-मित्र</b> पर अंगूठे से, या '
                   '<b>राजस्थान सोशल पेंशन एंड आधार फ़ेस</b> ऐप पर चेहरे से। 2026 की अंतिम तिथि <b>31 मार्च</b> थी।',
                   ('stuck',
                    'सत्यापन छूटना पेंशन रुकने का सबसे आम कारण है। जल्द से जल्द कराएं; सत्यापन के बाद रुकी राशि आमतौर '
                    'पर फिर मिल जाती है।')),
                  ('done',
                   'हर महीने पेंशन',
                   None,
                   'पेंशन डीबीटी से आती है। जन आधार या पीपीओ संख्या से <b>ssp.rajasthan.gov.in</b> (रिपोर्ट्स) पर '
                   'भुगतान देखें।',
                   ('stuck',
                    "गलती से 'मृत' या 'राज्य से बाहर' दिखा रहे हैं? आधार और जन आधार लेकर बीडीओ / एसडीएम कार्यालय में "
                    'दोबारा सत्यापन कराएं।'))],
        'rights_t': 'पेंशन रुक गई? शिकायत करें।',
        'rights': 'पीपीओ या जन आधार संख्या के साथ <b>राजस्थान संपर्क 181</b> पर शिकायत करें, या स्वीकृति देने वाले '
                  'बीडीओ / एसडीएम को लिखें।',
        'help': '<b>स्थिति:</b> ssp.rajasthan.gov.in · <b>सत्यापन:</b> ई-मित्र या फ़ेस ऐप · <b>शिकायत:</b> संपर्क '
                '181<br><b>आवेदन मुफ़्त है</b> · राशि बताए अनुसार; पोर्टल देखें'}}
