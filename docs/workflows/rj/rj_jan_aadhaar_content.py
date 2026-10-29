"""Jan Aadhaar card (Rajasthan) guide content (EN + HI)."""

OUT = "rj-jan-aadhaar-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': "Jan Aadhaar: your family's key to Rajasthan schemes",
        'sub': 'जन आधार: राजस्थान की योजनाओं की परिवार चाबी',
        'benefit': 'One family ID (10 digits) and member IDs (11 digits) used for pensions, ration, health cover, '
                   'scholarships and certificates',
        'legend': ['You do this', 'Government does this (you wait)', 'Jan Aadhaar ready'],
        'phases': ['Before you enrol', 'After you enrol'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Know why it matters',
                   'जानें क्यों ज़रूरी है',
                   'Jan Aadhaar replaced the old Bhamashah card. Pensions, ration, MAA health cover and most '
                   'certificates check your details <b>against Jan Aadhaar</b>, so a wrong name or missing member '
                   'blocks them.',
                   None),
                  ('you',
                   'Keep these ready',
                   'ये तैयार रखें',
                   '<ul><li><b>Aadhaar</b> of every family member</li><li>Photo of the woman head of '
                   'family</li><li>Bank passbook or cancelled cheque</li><li>A mobile number that <b>matches '
                   'Aadhaar</b> (for OTP)</li></ul>',
                   ('tip',
                    'If your mobile differs between Aadhaar and Jan Aadhaar, fix one first, or verify by fingerprint '
                    'at e-Mitra.')),
                  ('you',
                   'Enrol online or at e-Mitra',
                   'ऑनलाइन या ई-मित्र से नामांकन',
                   'Enrol with your <b>SSO ID</b> on the Jan Aadhaar portal, or at any <b>e-Mitra kiosk</b>. Keep the '
                   '<b>enrolment number</b>.',
                   ('tip', 'Kiosk charges reported are about ₹30–50. Ask for a receipt.')),
                  ('gov',
                   'Verification',
                   'सत्यापन',
                   'Your details are checked and the family ID is generated, reported as <b>7–15 working days</b>.',
                   ('stuck',
                    'Still pending after 15 working days? Check status on the portal with your enrolment number, then '
                    'complain on Sampark 181.')),
                  ('you',
                   'Keep it up to date',
                   'इसे अपडेट रखें',
                   'Add a newborn or a bride, remove a member who died or left, and correct names to match Aadhaar, '
                   'through SSO or e-Mitra. Do <b>member eKYC</b> when asked.',
                   ('stuck',
                    'Name mismatch between Aadhaar and Jan Aadhaar is a common reason pensions and ration stop. Fix it '
                    'here first.')),
                  ('done',
                   'Download and use your Jan Aadhaar',
                   'जन आधार डाउनलोड करें और उपयोग करें',
                   'Download the e-card from the portal and quote the family ID in every scheme form.',
                   None)],
        'rights_t': 'Stuck? Complain.',
        'rights': 'Complain on <b>Rajasthan Sampark 181</b> (toll-free) or sampark.rajasthan.gov.in with your '
                  'enrolment number. Keep the complaint number.',
        'help': '<b>Enrol / update:</b> janaadhaar.rajasthan.gov.in via SSO, or any e-Mitra · <b>Complaints:</b> '
                'Sampark 181<br><b>Never share your OTP</b> · Fees and times as reported; check the portal'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'जन आधार: राजस्थान की योजनाओं की परिवार चाबी',
        'sub': None,
        'benefit': 'एक पारिवारिक आईडी (10 अंक) और सदस्य आईडी (11 अंक), जो पेंशन, राशन, स्वास्थ्य बीमा, छात्रवृत्ति और '
                   'प्रमाण पत्रों में काम आती है',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'जन आधार तैयार'],
        'phases': ['नामांकन से पहले', 'नामांकन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'जानें क्यों ज़रूरी है',
                   None,
                   'जन आधार ने पुराने भामाशाह कार्ड की जगह ली है। पेंशन, राशन, मा योजना और ज़्यादातर प्रमाण पत्र आपकी '
                   'जानकारी <b>जन आधार से मिलाते</b> हैं, इसलिए गलत नाम या छूटा सदस्य इन्हें रोक देता है।',
                   None),
                  ('you',
                   'ये तैयार रखें',
                   None,
                   '<ul><li>परिवार के हर सदस्य का <b>आधार</b></li><li>परिवार की महिला मुखिया का फ़ोटो</li><li>बैंक '
                   'पासबुक या रद्द चेक</li><li><b>आधार से मेल खाता</b> मोबाइल नंबर (ओटीपी के लिए)</li></ul>',
                   ('tip',
                    'आधार और जन आधार में मोबाइल अलग है तो पहले एक ठीक कराएं, या ई-मित्र पर अंगूठे से सत्यापन कराएं।')),
                  ('you',
                   'ऑनलाइन या ई-मित्र से नामांकन',
                   None,
                   'जन आधार पोर्टल पर अपनी <b>SSO आईडी</b> से, या किसी भी <b>ई-मित्र कियोस्क</b> पर नामांकन कराएं। '
                   '<b>नामांकन संख्या</b> संभाल कर रखें।',
                   ('tip', 'कियोस्क शुल्क लगभग ₹30–50 बताया गया है। रसीद ज़रूर लें।')),
                  ('gov',
                   'सत्यापन',
                   None,
                   'आपकी जानकारी जांचकर पारिवारिक आईडी बनती है, बताए अनुसार <b>7–15 कार्यदिवस</b> में।',
                   ('stuck',
                    '15 कार्यदिवस बाद भी लंबित? नामांकन संख्या से पोर्टल पर स्थिति देखें, फिर संपर्क 181 पर शिकायत '
                    'करें।')),
                  ('you',
                   'इसे अपडेट रखें',
                   None,
                   'नवजात या बहू का नाम जोड़ें, गुज़र गए या अलग हुए सदस्य को हटाएं, और नाम आधार के अनुसार सुधारें, SSO '
                   'या ई-मित्र से। मांगे जाने पर <b>सदस्य ई-केवाईसी</b> कराएं।',
                   ('stuck', 'आधार और जन आधार में नाम अलग होना पेंशन और राशन रुकने का आम कारण है। पहले यहीं सुधारें।')),
                  ('done',
                   'जन आधार डाउनलोड करें और उपयोग करें',
                   None,
                   'पोर्टल से ई-कार्ड डाउनलोड करें और हर योजना फ़ॉर्म में पारिवारिक आईडी लिखें।',
                   None)],
        'rights_t': 'अटक गए? शिकायत करें।',
        'rights': 'नामांकन संख्या के साथ <b>राजस्थान संपर्क 181</b> (टोल-फ़्री) या sampark.rajasthan.gov.in पर शिकायत '
                  'करें। शिकायत संख्या संभाल कर रखें।',
        'help': '<b>नामांकन / अपडेट:</b> janaadhaar.rajasthan.gov.in (SSO से) या कोई भी ई-मित्र · <b>शिकायत:</b> '
                'संपर्क 181<br><b>ओटीपी किसी को न बताएं</b> · शुल्क और समय बताए अनुसार; पोर्टल देखें'}}
