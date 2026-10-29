"""Ration card and food security (Rajasthan) guide content (EN + HI)."""

OUT = "rj-ration-card-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Food security (NFSA) ration in Rajasthan',
        'sub': 'राजस्थान में खाद्य सुरक्षा (NFSA) राशन',
        'benefit': '5 kg wheat per person per month under food security, and entry to other state schemes (reported)',
        'legend': ['You do this', 'Government does this (you wait)', 'Ration received'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you can get it',
                   'पात्रता जांचें',
                   'Families are <b>left out</b> if any member pays income tax or works in government, a '
                   'semi-government or autonomous body, among other conditions. Coverage has a fixed quota.',
                   None),
                  ('you',
                   'Know if new names are being added',
                   'जानें नए नाम जुड़ रहे हैं या नहीं',
                   'The food security portal reopened on <b>26 January 2025</b> after the <b>Give Up</b> campaign '
                   'freed places; over 1 crore new people were added. Ask your ration dealer or e-Mitra whether '
                   'applications are open now.',
                   ('stuck',
                    "Nobody can 'add your name' for money when the portal is closed. Report such offers on Sampark "
                    '181.')),
                  ('you',
                   'Apply through e-Mitra',
                   'ई-मित्र से आवेदन करें',
                   'Apply with your <b>Jan Aadhaar</b> at e-Mitra when applications are open. All members you want '
                   'included must be in Jan Aadhaar.',
                   ('tip',
                    "Almost every Rajasthan service now starts from your family's <b>Jan Aadhaar</b>. Names must match "
                    'Aadhaar. No Jan Aadhaar yet? See the <b>Jan Aadhaar</b> guide first.')),
                  ('gov',
                   'Verification and approval',
                   'सत्यापन और स्वीकृति',
                   'The application is verified by the rural or urban local office and approved within the quota.',
                   ('stuck',
                    'Not approved? Ask the office for the written reason. If you are eligible and others have been '
                    'added, complain on Sampark 181.')),
                  ('you',
                   'Do eKYC at the ration shop',
                   'राशन दुकान पर ई-केवाईसी कराएं',
                   "Each member may need <b>eKYC</b> by fingerprint on the shop's POS machine. Members without eKYC "
                   'can be removed.',
                   None),
                  ('done',
                   'Collect ration every month',
                   'हर महीने राशन लें',
                   'Take ration from any fair price shop with your fingerprint. Ask for a printed receipt and check '
                   'the weight.',
                   ('stuck',
                    'Short weight or refusal? Complain on Sampark 181 or the food department helpline with the shop '
                    'name.'))],
        'rights_t': 'Denied ration? Complain.',
        'rights': 'Complain on <b>Rajasthan Sampark 181</b>, or to the district supply officer (DSO), with your Jan '
                  'Aadhaar number and shop name.',
        'help': '<b>Apply / status:</b> e-Mitra with Jan Aadhaar · food.rajasthan.gov.in · <b>Complaints:</b> Sampark '
                '181<br><b>Applying is free</b> · Quantities as reported'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'राजस्थान में खाद्य सुरक्षा (NFSA) राशन',
        'sub': None,
        'benefit': 'खाद्य सुरक्षा में प्रति व्यक्ति हर महीने 5 किलो गेहूं, और राज्य की अन्य योजनाओं में प्रवेश (बताए '
                   'अनुसार)',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'राशन मिला'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   'अगर परिवार का कोई सदस्य आयकर देता है या सरकारी, अर्ध-सरकारी या स्वायत्त संस्था में काम करता है, तो '
                   'परिवार <b>बाहर</b> रहता है, और भी शर्तें हैं। कोटा तय है।',
                   None),
                  ('you',
                   'जानें नए नाम जुड़ रहे हैं या नहीं',
                   None,
                   '<b>गिव अप</b> अभियान से जगह खाली होने के बाद खाद्य सुरक्षा पोर्टल <b>26 जनवरी 2025</b> को फिर '
                   'खुला; 1 करोड़ से अधिक नए लोग जुड़े। राशन डीलर या ई-मित्र से पूछें कि अभी आवेदन खुले हैं या नहीं।',
                   ('stuck',
                    "पोर्टल बंद हो तो कोई पैसे लेकर 'नाम नहीं जुड़वा' सकता। ऐसे प्रस्ताव की शिकायत संपर्क 181 पर "
                    'करें।')),
                  ('you',
                   'ई-मित्र से आवेदन करें',
                   None,
                   'आवेदन खुले होने पर <b>जन आधार</b> के साथ ई-मित्र पर आवेदन करें। जिन सदस्यों को जोड़ना है वे जन '
                   'आधार में होने चाहिए।',
                   ('tip',
                    'राजस्थान की लगभग हर सेवा अब परिवार के <b>जन आधार</b> से शुरू होती है। नाम आधार से मेल खाने चाहिए। '
                    'जन आधार नहीं है? पहले <b>जन आधार</b> मार्गदर्शिका देखें।')),
                  ('gov',
                   'सत्यापन और स्वीकृति',
                   None,
                   'ग्रामीण या शहरी स्थानीय कार्यालय आवेदन जांचता है और कोटे के भीतर स्वीकृति देता है।',
                   ('stuck',
                    'स्वीकृत नहीं हुआ? कार्यालय से लिखित कारण मांगें। आप पात्र हैं और दूसरों के नाम जुड़ गए, तो संपर्क '
                    '181 पर शिकायत करें।')),
                  ('you',
                   'राशन दुकान पर ई-केवाईसी कराएं',
                   None,
                   'हर सदस्य को दुकान की POS मशीन पर अंगूठे से <b>ई-केवाईसी</b> करानी पड़ सकती है। बिना ई-केवाईसी वाले '
                   'सदस्य हटाए जा सकते हैं।',
                   None),
                  ('done',
                   'हर महीने राशन लें',
                   None,
                   'किसी भी उचित मूल्य दुकान से अंगूठा लगाकर राशन लें। छपी रसीद मांगें और तौल जांचें।',
                   ('stuck',
                    'कम तौल या मना किया? दुकान के नाम के साथ संपर्क 181 या खाद्य विभाग हेल्पलाइन पर शिकायत करें।'))],
        'rights_t': 'राशन नहीं मिला? शिकायत करें।',
        'rights': 'जन आधार संख्या और दुकान के नाम के साथ <b>राजस्थान संपर्क 181</b> पर, या ज़िला रसद अधिकारी (DSO) को '
                  'शिकायत करें।',
        'help': '<b>आवेदन / स्थिति:</b> जन आधार के साथ ई-मित्र · food.rajasthan.gov.in · <b>शिकायत:</b> संपर्क '
                '181<br><b>आवेदन मुफ़्त है</b> · मात्रा बताए अनुसार'}}
