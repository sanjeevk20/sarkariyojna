"""PM-KISAN + CM Kisan Kalyan (MP) guide content (EN + HI)."""

OUT = "mp-kisan-kalyan-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'PM-KISAN + CM Kisan Kalyan: ₹10,000 a year for MP farmers',
        'sub': 'पीएम-किसान + मुख्यमंत्री किसान कल्याण: मप्र के किसानों को वर्ष में ₹10,000',
        'benefit': '₹6,000 a year from PM-KISAN plus ₹4,000 a year from the state (as reported)',
        'legend': ['You do this', 'Government does this (you wait)', 'Money received'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you can get it',
                   'पात्रता जांचें',
                   'Your name must be in the <b>khasra / B-1</b> as a landholder. You <b>cannot</b> get it if someone '
                   'in the family pays income tax, holds a government job, or is a practising doctor, lawyer, CA or '
                   'engineer.',
                   ('stuck',
                    "Land still in a parent's name? Get <b>naamantaran</b> done first. See the <b>Land mutation "
                    '(MP)</b> guide.')),
                  ('you',
                   'Register for PM-KISAN',
                   'पीएम-किसान में पंजीकरण करें',
                   'Register on <b>pmkisan.gov.in</b> or at a CSC with khasra, Aadhaar, bank passbook and mobile. '
                   '<b>No separate form</b> is needed for CM Kisan Kalyan: approved PM-KISAN farmers are included '
                   'automatically.',
                   None),
                  ('gov',
                   'Land verification',
                   'भूमि सत्यापन',
                   'The Patwari / tehsil checks your name against the land record and the state approves you.',
                   ('stuck',
                    'Name spelling differs between Aadhaar, khasra and bank? Correct it, then ask the Patwari to '
                    're-verify.')),
                  ('you',
                   'Do eKYC',
                   'ई-केवाईसी करें',
                   'Complete eKYC by OTP on pmkisan.gov.in, face authentication in the PM-KISAN app, or fingerprint at '
                   'a CSC.',
                   ('stuck', 'Without eKYC, <b>both</b> the central and state payments stop.')),
                  ('gov',
                   'Payments released',
                   'भुगतान जारी',
                   'PM-KISAN pays ₹2,000 three times a year; the state pays its ₹4,000 a year in instalments into the '
                   'same account.',
                   None),
                  ('done',
                   'Money in your account',
                   'खाते में राशि',
                   'Check PM-KISAN on pmkisan.gov.in and the state instalments on <b>saara.mp.gov.in</b>.',
                   ('stuck',
                    'PM-KISAN received but not the state amount? Check saara.mp.gov.in, then contact the tehsil / '
                    'agriculture office.'))],
        'rights_t': 'Instalment missing? Complain.',
        'rights': 'Use the PM-KISAN helpline <b>155261 / 011-24300606</b>, the district <b>agriculture office</b>, or '
                  'the <b>CM Helpline 181</b>.',
        'help': '<b>PM-KISAN:</b> pmkisan.gov.in · <b>State instalments:</b> saara.mp.gov.in · <b>Helpline:</b> 155261 '
                '/ 011-24300606<br><b>Use only official websites</b> · <b>Never pay an agent</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'पीएम-किसान + मुख्यमंत्री किसान कल्याण: मप्र के किसानों को वर्ष में ₹10,000',
        'sub': None,
        'benefit': 'पीएम-किसान से वर्ष में ₹6,000 और राज्य से वर्ष में ₹4,000 (बताए अनुसार)',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'राशि मिली'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   '<b>खसरा / बी-1</b> में भूमिस्वामी के रूप में आपका नाम होना चाहिए। परिवार में कोई आयकर देता हो, '
                   'सरकारी नौकरी में हो, या प्रैक्टिस करने वाला डॉक्टर, वकील, सीए या इंजीनियर हो तो लाभ <b>नहीं</b> '
                   'मिलेगा।',
                   ('stuck',
                    'ज़मीन अभी माता-पिता के नाम? पहले <b>नामांतरण</b> कराएं। <b>नामांतरण (मप्र)</b> मार्गदर्शिका '
                    'देखें।')),
                  ('you',
                   'पीएम-किसान में पंजीकरण करें',
                   None,
                   'खसरा, आधार, बैंक पासबुक और मोबाइल के साथ <b>pmkisan.gov.in</b> पर या सीएससी पर पंजीकरण करें। '
                   'मुख्यमंत्री किसान कल्याण के लिए <b>अलग फॉर्म नहीं</b> लगता: स्वीकृत पीएम-किसान किसान अपने आप शामिल '
                   'होते हैं।',
                   None),
                  ('gov',
                   'भूमि सत्यापन',
                   None,
                   'पटवारी / तहसील भू-अभिलेख से आपका नाम मिलाते हैं और राज्य स्वीकृति देता है।',
                   ('stuck',
                    'आधार, खसरा और बैंक में नाम की वर्तनी अलग है? सुधार कराएं, फिर पटवारी से दोबारा सत्यापन कराएं।')),
                  ('you',
                   'ई-केवाईसी करें',
                   None,
                   'pmkisan.gov.in पर ओटीपी से, पीएम-किसान ऐप में चेहरा प्रमाणीकरण से, या सीएससी पर अंगूठे से '
                   'ई-केवाईसी करें।',
                   ('stuck', 'ई-केवाईसी के बिना केंद्र और राज्य <b>दोनों</b> के भुगतान रुक जाते हैं।')),
                  ('gov',
                   'भुगतान जारी',
                   None,
                   'पीएम-किसान वर्ष में तीन बार ₹2,000 देता है; राज्य अपने ₹4,000 वार्षिक किस्तों में उसी खाते में '
                   'देता है।',
                   None),
                  ('done',
                   'खाते में राशि',
                   None,
                   'पीएम-किसान की स्थिति pmkisan.gov.in पर और राज्य की किस्तें <b>saara.mp.gov.in</b> पर देखें।',
                   ('stuck',
                    'पीएम-किसान आया पर राज्य की राशि नहीं? saara.mp.gov.in देखें, फिर तहसील / कृषि कार्यालय से संपर्क '
                    'करें।'))],
        'rights_t': 'किस्त नहीं आई? शिकायत करें।',
        'rights': 'पीएम-किसान हेल्पलाइन <b>155261 / 011-24300606</b>, ज़िला <b>कृषि कार्यालय</b>, या <b>सीएम हेल्पलाइन '
                  '181</b> का उपयोग करें।',
        'help': '<b>पीएम-किसान:</b> pmkisan.gov.in · <b>राज्य की किस्तें:</b> saara.mp.gov.in · <b>हेल्पलाइन:</b> '
                '155261 / 011-24300606<br><b>केवल आधिकारिक वेबसाइट का उपयोग करें</b> · <b>एजेंट को पैसे न दें</b>'}}
