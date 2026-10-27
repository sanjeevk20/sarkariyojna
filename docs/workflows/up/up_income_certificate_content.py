"""Income certificate (UP) guide content (EN + HI)."""

OUT = "up-income-certificate-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Income Certificate (UP): How to get your aay praman patra',
        'sub': 'आय प्रमाण पत्र (उत्तर प्रदेश): कैसे बनवाएं',
        'benefit': 'Needed for scholarships, pensions, fee waivers and most welfare schemes',
        'legend': ['You do this', 'Government does this (you wait)', 'Certificate ready'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Know who issues it',
                   'जानें कौन बनाता है',
                   'The <b>Tehsildar</b> issues it after the <b>Lekhpal</b> checks your family income. Apply through '
                   '<b>e-District UP</b>.',
                   ('tip',
                    "Apply in the name the scheme asks for. For a student, this is usually the parent's income.")),
                  ('you',
                   'Keep these papers ready',
                   'कागज़ तैयार रखें',
                   '<ul><li>Aadhaar</li><li>Ration card or other address proof</li><li>Income proof: salary or pension '
                   'slip; farmers and daily-wage earners give a <b>self-declaration</b></li><li>Passport-size '
                   'photo</li></ul>',
                   None),
                  ('you',
                   'Apply online or at a Jan Seva Kendra',
                   'ऑनलाइन या जन सेवा केंद्र से आवेदन करें',
                   'Apply yourself on <b>edistrict.up.gov.in</b> or at a <b>Jan Seva Kendra (CSC)</b>. Pay the fee and '
                   'keep the <b>application number</b>.',
                   ('tip',
                    'Reported fee: about <b>₹15</b> if you apply online yourself, <b>₹30</b> at a Jan Seva Kendra. Do '
                    'not pay more.')),
                  ('gov',
                   'Lekhpal verifies',
                   'लेखपाल जांच करते हैं',
                   'The Lekhpal checks your income, sometimes by visiting the village, and sends a report.',
                   ('stuck',
                    'Report delayed? Meet the Lekhpal with your application number. Wrong income written? Ask for '
                    're-verification before the Tehsildar signs.')),
                  ('gov',
                   'Tehsildar approves',
                   'तहसीलदार स्वीकृति देते हैं',
                   'The Tehsildar approves the report and the certificate is <b>digitally signed</b>.',
                   None),
                  ('done',
                   'Download your certificate',
                   'प्रमाण पत्र डाउनलोड करें',
                   'Download it from e-District with your application number, or collect it at the CSC. Check your '
                   "name, father's name and income.",
                   ('tip',
                    'Schemes often want a recent certificate (commonly within a year). Check what your scheme asks '
                    'for.'))],
        'rights_t': 'Taking too long? Complain.',
        'rights': 'UP services have fixed time limits. If yours is crossed, complain on <b>IGRS Jansunwai</b> '
                  '(jansunwai.up.nic.in) or the <b>CM Helpline 1076</b> with your application number.',
        'help': '<b>Apply / status:</b> edistrict.up.gov.in or any Jan Seva Kendra · <b>Complaints:</b> '
                'jansunwai.up.nic.in, CM Helpline 1076<br><b>Use only official websites</b> · <b>Never pay a tout</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'आय प्रमाण पत्र (उत्तर प्रदेश): कैसे बनवाएं',
        'sub': None,
        'benefit': 'छात्रवृत्ति, पेंशन, फीस माफी और ज़्यादातर कल्याण योजनाओं के लिए ज़रूरी',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'प्रमाण पत्र तैयार'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'जानें कौन बनाता है',
                   None,
                   '<b>लेखपाल</b> द्वारा परिवार की आय की जांच के बाद <b>तहसीलदार</b> यह प्रमाण पत्र जारी करते हैं। '
                   'आवेदन <b>ई-डिस्ट्रिक्ट यूपी</b> से होता है।',
                   ('tip',
                    'योजना जिसके नाम से मांगे, उसी के नाम से आवेदन करें। छात्र के लिए अक्सर माता-पिता की आय मानी जाती '
                    'है।')),
                  ('you',
                   'कागज़ तैयार रखें',
                   None,
                   '<ul><li>आधार</li><li>राशन कार्ड या अन्य पते का प्रमाण</li><li>आय का प्रमाण: वेतन या पेंशन पर्ची; '
                   'किसान और दिहाड़ी मज़दूर <b>स्व-घोषणा पत्र</b> दें</li><li>पासपोर्ट साइज़ फोटो</li></ul>',
                   None),
                  ('you',
                   'ऑनलाइन या जन सेवा केंद्र से आवेदन करें',
                   None,
                   '<b>edistrict.up.gov.in</b> पर खुद या किसी <b>जन सेवा केंद्र (CSC)</b> से आवेदन करें। शुल्क भरें और '
                   '<b>आवेदन संख्या</b> संभाल कर रखें।',
                   ('tip',
                    'बताया गया शुल्क: खुद ऑनलाइन आवेदन पर लगभग <b>₹15</b>, जन सेवा केंद्र पर <b>₹30</b>। इससे ज़्यादा '
                    'न दें।')),
                  ('gov',
                   'लेखपाल जांच करते हैं',
                   None,
                   'लेखपाल आपकी आय की जांच करते हैं, कभी-कभी गांव जाकर, और रिपोर्ट भेजते हैं।',
                   ('stuck',
                    'रिपोर्ट में देरी? आवेदन संख्या लेकर लेखपाल से मिलें। आय गलत लिखी? तहसीलदार के हस्ताक्षर से पहले '
                    'दोबारा जांच मांगें।')),
                  ('gov',
                   'तहसीलदार स्वीकृति देते हैं',
                   None,
                   'तहसीलदार रिपोर्ट स्वीकार करते हैं और प्रमाण पत्र पर <b>डिजिटल हस्ताक्षर</b> होते हैं।',
                   None),
                  ('done',
                   'प्रमाण पत्र डाउनलोड करें',
                   None,
                   'आवेदन संख्या से ई-डिस्ट्रिक्ट पर डाउनलोड करें या CSC से लें। अपना नाम, पिता का नाम और आय जांच लें।',
                   ('tip',
                    'योजनाएं अक्सर हाल का प्रमाण पत्र मांगती हैं (आमतौर पर एक साल के भीतर का)। अपनी योजना की शर्त '
                    'देखें।'))],
        'rights_t': 'बहुत देर हो रही है? शिकायत करें।',
        'rights': 'उत्तर प्रदेश में हर सेवा की तय समय-सीमा है। समय-सीमा पार हो जाए तो आवेदन संख्या के साथ <b>आईजीआरएस '
                  'जनसुनवाई</b> (jansunwai.up.nic.in) या <b>मुख्यमंत्री हेल्पलाइन 1076</b> पर शिकायत करें।',
        'help': '<b>आवेदन / स्थिति:</b> edistrict.up.gov.in या कोई भी जन सेवा केंद्र · <b>शिकायत:</b> '
                'jansunwai.up.nic.in, मुख्यमंत्री हेल्पलाइन 1076<br><b>केवल आधिकारिक वेबसाइट का उपयोग करें</b> · '
                '<b>दलाल को पैसे न दें</b>'}}
