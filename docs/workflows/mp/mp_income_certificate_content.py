"""Income certificate (MP) guide content (EN + HI)."""

OUT = "mp-income-certificate-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Income Certificate (MP): Apply on e-District',
        'sub': 'आय प्रमाण पत्र (मध्य प्रदेश): ई-डिस्ट्रिक्ट से आवेदन',
        'benefit': 'Needed for scholarships, fee waivers and income-based schemes',
        'legend': ['You do this', 'Government does this (you wait)', 'Certificate ready'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check who can get it',
                   'पात्रता जांचें',
                   'Any MP resident who needs proof of family income.',
                   ('tip',
                    'Almost every MP service needs a <b>Samagra member ID with eKYC done</b>. No Samagra yet? See the '
                    '<b>Samagra ID (MP)</b> guide first.')),
                  ('you',
                   'Keep these papers ready',
                   'कागज़ तैयार रखें',
                   '<ul><li>Samagra member ID</li><li>Aadhaar</li><li>Income proof: salary slip, or a '
                   '<b>self-declaration</b> for farmers and daily-wage earners</li><li>Address proof, photo</li></ul>',
                   None),
                  ('you',
                   'Apply online or at a Lok Seva Kendra',
                   'ऑनलाइन या लोक सेवा केंद्र से आवेदन करें',
                   'Apply yourself on <b>mpedistrict.gov.in</b>, or at a <b>Lok Seva Kendra</b> / MP Online kiosk. '
                   'Keep the <b>application number</b>.',
                   ('tip',
                    'Applying online yourself is reported to be free or nearly free; kiosks charge a small service '
                    'fee. Do not pay more.')),
                  ('gov',
                   'Checked by the revenue office',
                   'राजस्व कार्यालय द्वारा जांच',
                   'The revenue office checks your declaration; the Patwari may be asked to report.',
                   ('stuck',
                    'Asked for more documents? Upload them against the same application number instead of applying '
                    'again.')),
                  ('gov',
                   'Tehsildar approves',
                   'तहसीलदार स्वीकृति देते हैं',
                   'The <b>Tehsildar</b> approves and the certificate is <b>digitally signed</b>.',
                   None),
                  ('done',
                   'Download your certificate',
                   'प्रमाण पत्र डाउनलोड करें',
                   'Download it from e-District with your application number and check every detail.',
                   ('tip', 'Schemes often want a recent income certificate. Check the date your scheme accepts.'))],
        'rights_t': 'Taking too long? Use your rights.',
        'rights': 'Certificates are covered by the <b>MP Lok Seva Guarantee Act</b>, with a fixed time limit for each '
                  'service. If it is crossed, file a <b>first appeal</b>, or complain to the <b>CM Helpline 181</b>, '
                  'with your application number.',
        'help': '<b>Apply / status:</b> mpedistrict.gov.in or any Lok Seva Kendra / MP Online kiosk · '
                '<b>Complaints:</b> CM Helpline 181<br><b>Applying online yourself is cheapest</b> · <b>Never pay a '
                'tout</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'आय प्रमाण पत्र (मध्य प्रदेश): ई-डिस्ट्रिक्ट से आवेदन',
        'sub': None,
        'benefit': 'छात्रवृत्ति, फीस माफी और आय-आधारित योजनाओं के लिए ज़रूरी',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'प्रमाण पत्र तैयार'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   'आय का प्रमाण चाहने वाला मध्य प्रदेश का कोई भी निवासी।',
                   ('tip',
                    'मध्य प्रदेश की लगभग हर सेवा के लिए <b>ई-केवाईसी वाली समग्र सदस्य आईडी</b> चाहिए। समग्र नहीं है? '
                    'पहले <b>समग्र आईडी (मप्र)</b> मार्गदर्शिका देखें।')),
                  ('you',
                   'कागज़ तैयार रखें',
                   None,
                   '<ul><li>समग्र सदस्य आईडी</li><li>आधार</li><li>आय प्रमाण: वेतन पर्ची, या किसानों और दिहाड़ी '
                   'मज़दूरों के लिए <b>स्व-घोषणा पत्र</b></li><li>पते का प्रमाण, फोटो</li></ul>',
                   None),
                  ('you',
                   'ऑनलाइन या लोक सेवा केंद्र से आवेदन करें',
                   None,
                   '<b>mpedistrict.gov.in</b> पर खुद, या <b>लोक सेवा केंद्र</b> / एमपी ऑनलाइन कियोस्क से आवेदन करें। '
                   '<b>आवेदन संख्या</b> संभाल कर रखें।',
                   ('tip',
                    'खुद ऑनलाइन आवेदन बताए अनुसार मुफ़्त या लगभग मुफ़्त है; कियोस्क थोड़ा सेवा शुल्क लेते हैं। इससे '
                    'ज़्यादा न दें।')),
                  ('gov',
                   'राजस्व कार्यालय द्वारा जांच',
                   None,
                   'राजस्व कार्यालय आपकी घोषणा जांचता है; पटवारी से रिपोर्ट मांगी जा सकती है।',
                   ('stuck', 'और दस्तावेज़ मांगे गए? नया आवेदन करने के बजाय उसी आवेदन संख्या पर अपलोड करें।')),
                  ('gov',
                   'तहसीलदार स्वीकृति देते हैं',
                   None,
                   '<b>तहसीलदार</b> स्वीकृति देते हैं और प्रमाण पत्र पर <b>डिजिटल हस्ताक्षर</b> होते हैं।',
                   None),
                  ('done',
                   'प्रमाण पत्र डाउनलोड करें',
                   None,
                   'आवेदन संख्या से ई-डिस्ट्रिक्ट से डाउनलोड करें और हर विवरण जांच लें।',
                   ('tip', 'योजनाएं अक्सर हाल का आय प्रमाण पत्र मांगती हैं। अपनी योजना की शर्त देखें।'))],
        'rights_t': 'बहुत देर हो रही है? अपने अधिकार का उपयोग करें।',
        'rights': 'प्रमाण पत्र <b>मप्र लोक सेवा गारंटी अधिनियम</b> के तहत आते हैं और हर सेवा की तय समय-सीमा है। '
                  'समय-सीमा निकल जाए तो आवेदन संख्या के साथ <b>प्रथम अपील</b> करें या <b>सीएम हेल्पलाइन 181</b> पर '
                  'शिकायत करें।',
        'help': '<b>आवेदन / स्थिति:</b> mpedistrict.gov.in या कोई भी लोक सेवा केंद्र / एमपी ऑनलाइन कियोस्क · '
                '<b>शिकायत:</b> सीएम हेल्पलाइन 181<br><b>खुद ऑनलाइन आवेदन सबसे सस्ता है</b> · <b>दलाल को पैसे न '
                'दें</b>'}}
