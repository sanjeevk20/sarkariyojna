"""Income certificate (Rajasthan) guide content (EN + HI)."""

OUT = "rj-income-certificate-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Income certificate in Rajasthan',
        'sub': 'आय प्रमाण पत्र, राजस्थान',
        'benefit': 'Proof of yearly family income for scholarships, fee concessions, EWS, pensions and schemes',
        'legend': ['You do this', 'Government does this (you wait)', 'Certificate ready'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check who can get it',
                   'पात्रता जांचें',
                   "Any resident of Rajasthan. The certificate states the family's income from all sources for the "
                   'year.',
                   ('tip',
                    "Almost every Rajasthan service now starts from your family's <b>Jan Aadhaar</b>. Names must match "
                    'Aadhaar. No Jan Aadhaar yet? See the <b>Jan Aadhaar</b> guide first.')),
                  ('you',
                   'Keep these papers ready',
                   'कागज़ तैयार रखें',
                   '<ul><li><b>Jan Aadhaar</b> and Aadhaar</li><li>Self-declaration of income (form on '
                   'e-Mitra)</li><li>Salary slip, or land / farming income papers if relevant</li><li>Ration card if '
                   'you have one</li></ul>',
                   None),
                  ('you',
                   'Apply online or at e-Mitra',
                   'ऑनलाइन या ई-मित्र से आवेदन करें',
                   'Log in to <b>sso.rajasthan.gov.in</b>, open <b>e-Mitra</b> (citizen login) and apply, or go to any '
                   '<b>e-Mitra kiosk</b>. Keep the <b>application number</b>.',
                   ('tip',
                    'From your own citizen login you pay only the government fee; kiosks add a small service charge. '
                    'Ask for the printed rate list and do not pay more.')),
                  ('gov',
                   'Checked by the revenue office',
                   'राजस्व कार्यालय द्वारा जांच',
                   'The Patwari / revenue office may check your income declaration. Guides report about <b>5–30 '
                   'days</b>; the time limit is shown when you apply.',
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
                   'Download it from SSO / e-Mitra with your application number and check every detail.',
                   ('tip', 'Most schemes want a certificate from the current year. Note its validity date.'))],
        'rights_t': 'Taking too long? Use your rights.',
        'rights': 'Certificates are notified services under the <b>Rajasthan Guaranteed Delivery of Public Services '
                  'Act, 2011</b>. If the time limit shown when you applied is crossed, or you are refused without a '
                  'written reason, file a <b>first appeal within 30 days</b>, or complain on <b>Rajasthan Sampark '
                  '181</b> with your application number.',
        'help': '<b>Apply / status:</b> sso.rajasthan.gov.in (citizen login) or any e-Mitra kiosk · <b>Complaints:</b> '
                'Rajasthan Sampark 181<br><b>Applying yourself costs only the government fee</b> · <b>Never pay a '
                'tout</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'राजस्थान में आय प्रमाण पत्र',
        'sub': None,
        'benefit': 'छात्रवृत्ति, फ़ीस छूट, EWS, पेंशन और योजनाओं के लिए सालाना पारिवारिक आय का प्रमाण',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'प्रमाण पत्र तैयार'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   'राजस्थान का कोई भी निवासी। प्रमाण पत्र में साल भर की सभी स्रोतों से पारिवारिक आय लिखी होती है।',
                   ('tip',
                    'राजस्थान की लगभग हर सेवा अब परिवार के <b>जन आधार</b> से शुरू होती है। नाम आधार से मेल खाने चाहिए। '
                    'जन आधार नहीं है? पहले <b>जन आधार</b> मार्गदर्शिका देखें।')),
                  ('you',
                   'कागज़ तैयार रखें',
                   None,
                   '<ul><li><b>जन आधार</b> और आधार</li><li>आय का स्व-घोषणा पत्र (फ़ॉर्म ई-मित्र पर)</li><li>वेतन '
                   'पर्ची, या खेती की आय के कागज़ (यदि लागू)</li><li>राशन कार्ड (यदि हो)</li></ul>',
                   None),
                  ('you',
                   'ऑनलाइन या ई-मित्र से आवेदन करें',
                   None,
                   '<b>sso.rajasthan.gov.in</b> पर लॉगिन करके <b>ई-मित्र</b> (सिटिज़न लॉगिन) से आवेदन करें, या किसी भी '
                   '<b>ई-मित्र कियोस्क</b> पर जाएं। <b>आवेदन संख्या</b> संभाल कर रखें।',
                   ('tip',
                    'अपने सिटिज़न लॉगिन से सिर्फ़ सरकारी शुल्क लगता है; कियोस्क थोड़ा सेवा शुल्क जोड़ते हैं। छपी हुई '
                    'दर सूची मांगें और उससे ज़्यादा न दें।')),
                  ('gov',
                   'राजस्व कार्यालय द्वारा जांच',
                   None,
                   'पटवारी / राजस्व कार्यालय आपकी आय घोषणा जांच सकता है। मार्गदर्शिकाओं के अनुसार लगभग <b>5–30 '
                   'दिन</b>; समय-सीमा आवेदन के समय दिखती है।',
                   ('stuck', 'और दस्तावेज़ मांगे गए? नया आवेदन करने के बजाय उसी आवेदन संख्या पर अपलोड करें।')),
                  ('gov',
                   'तहसीलदार स्वीकृति देते हैं',
                   None,
                   '<b>तहसीलदार</b> स्वीकृति देते हैं और प्रमाण पत्र पर <b>डिजिटल हस्ताक्षर</b> होते हैं।',
                   None),
                  ('done',
                   'प्रमाण पत्र डाउनलोड करें',
                   None,
                   'आवेदन संख्या से SSO / ई-मित्र से डाउनलोड करें और हर विवरण जांच लें।',
                   ('tip', 'ज़्यादातर योजनाएं इसी साल का प्रमाण पत्र मांगती हैं। उसकी वैधता तिथि नोट करें।'))],
        'rights_t': 'बहुत देर हो रही है? अपने अधिकार का उपयोग करें।',
        'rights': 'प्रमाण पत्र <b>राजस्थान लोक सेवाओं के प्रदान की गारंटी अधिनियम, 2011</b> के तहत अधिसूचित सेवाएं '
                  'हैं। आवेदन के समय दिखाई गई समय-सीमा निकल जाए, या बिना लिखित कारण मना किया जाए, तो <b>30 दिन के भीतर '
                  'प्रथम अपील</b> करें, या आवेदन संख्या के साथ <b>राजस्थान संपर्क 181</b> पर शिकायत करें।',
        'help': '<b>आवेदन / स्थिति:</b> sso.rajasthan.gov.in (सिटिज़न लॉगिन) या कोई भी ई-मित्र कियोस्क · '
                '<b>शिकायत:</b> राजस्थान संपर्क 181<br><b>खुद आवेदन करने पर सिर्फ़ सरकारी शुल्क लगता है</b> · <b>दलाल '
                'को पैसे न दें</b>'}}
