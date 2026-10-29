"""PM-KISAN + CM Kisan Samman Nidhi (Rajasthan) guide content (EN + HI)."""

OUT = "rj-kisan-samman-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': '₹9,000 a year for Rajasthan farmers: PM-KISAN + CM Kisan Samman Nidhi',
        'sub': 'पीएम-किसान + मुख्यमंत्री किसान सम्मान निधि',
        'benefit': '₹6,000 a year from PM-KISAN plus ₹3,000 a year from the state, by DBT (state says it will rise '
                   'step by step to ₹12,000 total)',
        'legend': ['You do this', 'Government does this (you wait)', 'Money received'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you can get it',
                   'पात्रता जांचें',
                   'Farmer family with cultivable land <b>in your name in the jamabandi</b>. Income-tax payers, '
                   'government employees and some professionals are excluded under PM-KISAN.',
                   ('stuck',
                    "Land still in a parent's name? Do <b>namantaran</b> first; see the Land mutation guide.")),
                  ('you',
                   'Register for PM-KISAN',
                   'पीएम-किसान में पंजीकरण',
                   'Register on <b>pmkisan.gov.in</b> (New Farmer Registration) or at e-Mitra / CSC with Aadhaar, '
                   'jamabandi details and bank account.',
                   ('tip',
                    "Almost every Rajasthan service now starts from your family's <b>Jan Aadhaar</b>. Names must match "
                    'Aadhaar. No Jan Aadhaar yet? See the <b>Jan Aadhaar</b> guide first.')),
                  ('you',
                   'Finish eKYC and land seeding',
                   'ई-केवाईसी और भूमि सीडिंग पूरी करें',
                   'Do <b>PM-KISAN eKYC</b> (OTP, fingerprint or face) and make sure <b>land seeding</b> shows Yes and '
                   'the bank is Aadhaar-seeded.',
                   ('stuck',
                    'Instalment stopped? Check eKYC, land seeding and Aadhaar-bank seeding on the PM-KISAN status '
                    'page.')),
                  ('gov',
                   'State and centre approve',
                   'राज्य और केंद्र स्वीकृति',
                   "The state verifies your land record and approves; the centre releases PM-KISAN. The state's ₹3,000 "
                   'goes to the <b>same PM-KISAN farmers</b>.',
                   None),
                  ('gov',
                   'State instalments',
                   'राज्य की किस्तें',
                   'The state pays its share in separate DBT instalments (for example about ₹718 crore to 72 lakh '
                   'farmers in October 2025).',
                   None),
                  ('done',
                   '₹9,000 a year',
                   'सालाना ₹9,000',
                   'Check both on the PM-KISAN status page and your bank passbook.',
                   ('stuck',
                    'Getting PM-KISAN but not the state share? Complain on Sampark 181 with your PM-KISAN registration '
                    'number.'))],
        'rights_t': 'Instalment missing? Complain.',
        'rights': 'PM-KISAN helpline <b>155261</b> / 011-24300606 or the grievance tab on pmkisan.gov.in; state share: '
                  '<b>Rajasthan Sampark 181</b> or the agriculture supervisor / tehsil.',
        'help': '<b>Status:</b> pmkisan.gov.in · <b>Helpline:</b> 155261 · <b>State complaints:</b> Sampark '
                '181<br><b>Registration is free</b> · State amounts as reported'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'राजस्थान के किसानों को सालाना ₹9,000: पीएम-किसान + मुख्यमंत्री किसान सम्मान निधि',
        'sub': None,
        'benefit': 'पीएम-किसान से सालाना ₹6,000 और राज्य से सालाना ₹3,000, डीबीटी से (राज्य के अनुसार कुल राशि '
                   'धीरे-धीरे ₹12,000 तक होगी)',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'राशि मिली'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   'जिस किसान परिवार की खेती योग्य ज़मीन <b>जमाबंदी में उनके नाम</b> हो। पीएम-किसान में आयकरदाता, '
                   'सरकारी कर्मचारी और कुछ पेशेवर बाहर हैं।',
                   ('stuck',
                    'ज़मीन अभी माता-पिता के नाम है? पहले <b>नामांतरण</b> कराएं; नामांतरण मार्गदर्शिका देखें।')),
                  ('you',
                   'पीएम-किसान में पंजीकरण',
                   None,
                   '<b>pmkisan.gov.in</b> (न्यू फ़ार्मर रजिस्ट्रेशन) पर, या ई-मित्र / सीएससी पर आधार, जमाबंदी विवरण और '
                   'बैंक खाते के साथ पंजीकरण करें।',
                   ('tip',
                    'राजस्थान की लगभग हर सेवा अब परिवार के <b>जन आधार</b> से शुरू होती है। नाम आधार से मेल खाने चाहिए। '
                    'जन आधार नहीं है? पहले <b>जन आधार</b> मार्गदर्शिका देखें।')),
                  ('you',
                   'ई-केवाईसी और भूमि सीडिंग पूरी करें',
                   None,
                   '<b>पीएम-किसान ई-केवाईसी</b> (ओटीपी, अंगूठा या चेहरा) करें और देखें कि <b>लैंड सीडिंग</b> Yes हो और '
                   'बैंक खाता आधार से जुड़ा हो।',
                   ('stuck',
                    'किस्त रुक गई? पीएम-किसान स्थिति पेज पर ई-केवाईसी, लैंड सीडिंग और आधार-बैंक सीडिंग जांचें।')),
                  ('gov',
                   'राज्य और केंद्र स्वीकृति',
                   None,
                   'राज्य आपका भूमि रिकॉर्ड जांचकर स्वीकृति देता है; केंद्र पीएम-किसान जारी करता है। राज्य के ₹3,000 '
                   '<b>उन्हीं पीएम-किसान किसानों</b> को मिलते हैं।',
                   None),
                  ('gov',
                   'राज्य की किस्तें',
                   None,
                   'राज्य अपना हिस्सा अलग डीबीटी किस्तों में देता है (जैसे अक्टूबर 2025 में लगभग 72 लाख किसानों को '
                   '₹718 करोड़)।',
                   None),
                  ('done',
                   'सालाना ₹9,000',
                   None,
                   'दोनों को पीएम-किसान स्थिति पेज और बैंक पासबुक में जांचें।',
                   ('stuck',
                    'पीएम-किसान मिल रहा है पर राज्य का हिस्सा नहीं? पीएम-किसान पंजीकरण संख्या के साथ संपर्क 181 पर '
                    'शिकायत करें।'))],
        'rights_t': 'किस्त नहीं आई? शिकायत करें।',
        'rights': 'पीएम-किसान हेल्पलाइन <b>155261</b> / 011-24300606 या pmkisan.gov.in का शिकायत टैब; राज्य का हिस्सा: '
                  '<b>राजस्थान संपर्क 181</b> या कृषि पर्यवेक्षक / तहसील।',
        'help': '<b>स्थिति:</b> pmkisan.gov.in · <b>हेल्पलाइन:</b> 155261 · <b>राज्य शिकायत:</b> संपर्क '
                '181<br><b>पंजीकरण मुफ़्त है</b> · राज्य की राशि बताए अनुसार'}}
