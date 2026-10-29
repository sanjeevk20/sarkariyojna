"""Caste certificate (Rajasthan) guide content (EN + HI)."""

OUT = "rj-caste-certificate-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Caste certificate in Rajasthan (SC / ST / OBC / MBC)',
        'sub': 'जाति प्रमाण पत्र, राजस्थान',
        'benefit': 'Needed for reservation in jobs and education, scholarships and many schemes',
        'legend': ['You do this', 'Government does this (you wait)', 'Certificate ready'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check who can get it',
                   'पात्रता जांचें',
                   'Members of a caste on the Rajasthan SC, ST, OBC or MBC list. OBC / MBC non-creamy-layer '
                   'certificates also need an income check.',
                   ('tip',
                    "Almost every Rajasthan service now starts from your family's <b>Jan Aadhaar</b>. Names must match "
                    'Aadhaar. No Jan Aadhaar yet? See the <b>Jan Aadhaar</b> guide first.')),
                  ('you',
                   'Keep these papers ready',
                   'कागज़ तैयार रखें',
                   "<ul><li><b>Jan Aadhaar</b> and Aadhaar</li><li>Proof of the family's caste: father's or a "
                   "relative's caste certificate, or old land / school records showing caste</li><li>Mool Niwas "
                   'proof</li><li>Self-declaration</li></ul>',
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
                   "The Patwari / revenue office checks the family's caste records. Guides report about <b>7–10 "
                   'working days</b> when papers are complete.',
                   ('stuck',
                    'Asked for more documents? Upload them against the same application number instead of applying '
                    'again.')),
                  ('gov',
                   'Tehsildar / SDM approves',
                   'तहसीलदार / एसडीएम स्वीकृति देते हैं',
                   'The <b>Tehsildar / SDM</b> approves and the certificate is <b>digitally signed</b>.',
                   None),
                  ('done',
                   'Download your certificate',
                   'प्रमाण पत्र डाउनलोड करें',
                   'Download it from SSO / e-Mitra with your application number and check every detail.',
                   ('tip',
                    "A father's caste certificate makes later certificates for the children much faster. Keep a copy "
                    'safe.'))],
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
        'h1': 'राजस्थान में जाति प्रमाण पत्र (SC / ST / OBC / MBC)',
        'sub': None,
        'benefit': 'नौकरी और शिक्षा में आरक्षण, छात्रवृत्ति और कई योजनाओं के लिए ज़रूरी',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'प्रमाण पत्र तैयार'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   'राजस्थान की SC, ST, OBC या MBC सूची की जाति के सदस्य। OBC / MBC नॉन-क्रीमी लेयर प्रमाण पत्र के लिए '
                   'आय जांच भी होती है।',
                   ('tip',
                    'राजस्थान की लगभग हर सेवा अब परिवार के <b>जन आधार</b> से शुरू होती है। नाम आधार से मेल खाने चाहिए। '
                    'जन आधार नहीं है? पहले <b>जन आधार</b> मार्गदर्शिका देखें।')),
                  ('you',
                   'कागज़ तैयार रखें',
                   None,
                   '<ul><li><b>जन आधार</b> और आधार</li><li>परिवार की जाति का प्रमाण: पिता या रिश्तेदार का जाति प्रमाण '
                   'पत्र, या जाति दिखाने वाले पुराने ज़मीन / स्कूल रिकॉर्ड</li><li>मूल निवास का '
                   'प्रमाण</li><li>स्व-घोषणा पत्र</li></ul>',
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
                   'पटवारी / राजस्व कार्यालय परिवार के जाति रिकॉर्ड जांचता है। कागज़ पूरे हों तो लगभग <b>7–10 '
                   'कार्यदिवस</b> बताए गए हैं।',
                   ('stuck', 'और दस्तावेज़ मांगे गए? नया आवेदन करने के बजाय उसी आवेदन संख्या पर अपलोड करें।')),
                  ('gov',
                   'तहसीलदार / एसडीएम स्वीकृति देते हैं',
                   None,
                   '<b>तहसीलदार / एसडीएम</b> स्वीकृति देते हैं और प्रमाण पत्र पर <b>डिजिटल हस्ताक्षर</b> होते हैं।',
                   None),
                  ('done',
                   'प्रमाण पत्र डाउनलोड करें',
                   None,
                   'आवेदन संख्या से SSO / ई-मित्र से डाउनलोड करें और हर विवरण जांच लें।',
                   ('tip',
                    'पिता का जाति प्रमाण पत्र बच्चों के प्रमाण पत्र आसान बना देता है। उसकी प्रति संभाल कर रखें।'))],
        'rights_t': 'बहुत देर हो रही है? अपने अधिकार का उपयोग करें।',
        'rights': 'प्रमाण पत्र <b>राजस्थान लोक सेवाओं के प्रदान की गारंटी अधिनियम, 2011</b> के तहत अधिसूचित सेवाएं '
                  'हैं। आवेदन के समय दिखाई गई समय-सीमा निकल जाए, या बिना लिखित कारण मना किया जाए, तो <b>30 दिन के भीतर '
                  'प्रथम अपील</b> करें, या आवेदन संख्या के साथ <b>राजस्थान संपर्क 181</b> पर शिकायत करें।',
        'help': '<b>आवेदन / स्थिति:</b> sso.rajasthan.gov.in (सिटिज़न लॉगिन) या कोई भी ई-मित्र कियोस्क · '
                '<b>शिकायत:</b> राजस्थान संपर्क 181<br><b>खुद आवेदन करने पर सिर्फ़ सरकारी शुल्क लगता है</b> · <b>दलाल '
                'को पैसे न दें</b>'}}
