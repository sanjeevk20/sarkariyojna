"""Caste certificate (UP) guide content (EN + HI)."""

OUT = "up-caste-certificate-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Caste Certificate (UP): How to get your jati praman patra',
        'sub': 'जाति प्रमाण पत्र (उत्तर प्रदेश): कैसे बनवाएं',
        'benefit': 'Needed for reserved seats, government jobs, scholarships and fee concessions',
        'legend': ['You do this', 'Government does this (you wait)', 'Certificate ready'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check who can get it',
                   'पात्रता जांचें',
                   "For <b>SC, ST and OBC</b> families of UP. Your caste is taken from your <b>father's side</b>.",
                   ('tip',
                    'If your father or a sibling already has a UP caste certificate, attach a copy. It speeds up '
                    'verification.')),
                  ('you',
                   'Keep these papers ready',
                   'कागज़ तैयार रखें',
                   "<ul><li>Aadhaar</li><li>Address proof: ration card, voter ID or electricity bill</li><li>Father's "
                   "or a family member's caste certificate, if any</li><li>Signed self-declaration and a "
                   'photo</li></ul>',
                   None),
                  ('you',
                   'Apply online or at a Jan Seva Kendra',
                   'ऑनलाइन या जन सेवा केंद्र से आवेदन करें',
                   'Apply on <b>edistrict.up.gov.in</b> or at a <b>Jan Seva Kendra</b>. Keep the <b>application '
                   'number</b>.',
                   ('tip',
                    'Reported fee: about <b>₹15</b> if you apply online yourself, <b>₹30</b> at a Jan Seva Kendra. Do '
                    'not pay more.')),
                  ('gov',
                   'Lekhpal verifies',
                   'लेखपाल जांच करते हैं',
                   'The Lekhpal confirms your caste and residence locally and sends a report.',
                   ('stuck',
                    "Lekhpal says records do not show your caste? Give the family member's certificate or old school "
                    'records showing caste, and ask for a fresh report.')),
                  ('gov',
                   'Tehsildar approves',
                   'तहसीलदार स्वीकृति देते हैं',
                   'The Tehsildar approves and the certificate is digitally signed.',
                   None),
                  ('done',
                   'Download your certificate',
                   'प्रमाण पत्र डाउनलोड करें',
                   'Download it from e-District. Check that the <b>caste name and category</b> are exactly right.',
                   ('tip',
                    'For central government jobs or admissions, check whether they need the <b>central format</b> '
                    'certificate; ask when you apply.'))],
        'rights_t': 'Taking too long? Complain.',
        'rights': 'UP services have fixed time limits. If yours is crossed, complain on <b>IGRS Jansunwai</b> '
                  '(jansunwai.up.nic.in) or the <b>CM Helpline 1076</b> with your application number.',
        'help': '<b>Apply / status:</b> edistrict.up.gov.in or any Jan Seva Kendra · <b>Complaints:</b> '
                'jansunwai.up.nic.in, CM Helpline 1076<br><b>Use only official websites</b> · <b>Never pay a tout</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'जाति प्रमाण पत्र (उत्तर प्रदेश): कैसे बनवाएं',
        'sub': None,
        'benefit': 'आरक्षित सीटों, सरकारी नौकरी, छात्रवृत्ति और फीस छूट के लिए ज़रूरी',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'प्रमाण पत्र तैयार'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   'उत्तर प्रदेश के <b>अनुसूचित जाति, अनुसूचित जनजाति और पिछड़ा वर्ग</b> परिवारों के लिए। जाति <b>पिता '
                   'की ओर से</b> मानी जाती है।',
                   ('tip',
                    'पिता या भाई-बहन के पास पहले से यूपी का जाति प्रमाण पत्र है तो उसकी कॉपी लगाएं। जांच जल्दी होती '
                    'है।')),
                  ('you',
                   'कागज़ तैयार रखें',
                   None,
                   '<ul><li>आधार</li><li>पते का प्रमाण: राशन कार्ड, वोटर आईडी या बिजली बिल</li><li>पिता या परिवार के '
                   'किसी सदस्य का जाति प्रमाण पत्र, अगर हो</li><li>हस्ताक्षरित स्व-घोषणा पत्र और फोटो</li></ul>',
                   None),
                  ('you',
                   'ऑनलाइन या जन सेवा केंद्र से आवेदन करें',
                   None,
                   '<b>edistrict.up.gov.in</b> पर या <b>जन सेवा केंद्र</b> से आवेदन करें। <b>आवेदन संख्या</b> संभाल कर '
                   'रखें।',
                   ('tip',
                    'बताया गया शुल्क: खुद ऑनलाइन आवेदन पर लगभग <b>₹15</b>, जन सेवा केंद्र पर <b>₹30</b>। इससे ज़्यादा '
                    'न दें।')),
                  ('gov',
                   'लेखपाल जांच करते हैं',
                   None,
                   'लेखपाल स्थानीय स्तर पर आपकी जाति और निवास की पुष्टि कर रिपोर्ट भेजते हैं।',
                   ('stuck',
                    'लेखपाल कहें कि रिकॉर्ड में जाति नहीं है? परिवार के सदस्य का प्रमाण पत्र या जाति दर्शाने वाले '
                    'पुराने स्कूल रिकॉर्ड दें और नई रिपोर्ट मांगें।')),
                  ('gov',
                   'तहसीलदार स्वीकृति देते हैं',
                   None,
                   'तहसीलदार स्वीकृति देते हैं और प्रमाण पत्र पर डिजिटल हस्ताक्षर होते हैं।',
                   None),
                  ('done',
                   'प्रमाण पत्र डाउनलोड करें',
                   None,
                   'ई-डिस्ट्रिक्ट से डाउनलोड करें। जांचें कि <b>जाति का नाम और वर्ग</b> बिल्कुल सही है।',
                   ('tip',
                    'केंद्र सरकार की नौकरी या प्रवेश के लिए पूछ लें कि <b>केंद्रीय प्रारूप</b> का प्रमाण पत्र चाहिए या '
                    'नहीं।'))],
        'rights_t': 'बहुत देर हो रही है? शिकायत करें।',
        'rights': 'उत्तर प्रदेश में हर सेवा की तय समय-सीमा है। समय-सीमा पार हो जाए तो आवेदन संख्या के साथ <b>आईजीआरएस '
                  'जनसुनवाई</b> (jansunwai.up.nic.in) या <b>मुख्यमंत्री हेल्पलाइन 1076</b> पर शिकायत करें।',
        'help': '<b>आवेदन / स्थिति:</b> edistrict.up.gov.in या कोई भी जन सेवा केंद्र · <b>शिकायत:</b> '
                'jansunwai.up.nic.in, मुख्यमंत्री हेल्पलाइन 1076<br><b>केवल आधिकारिक वेबसाइट का उपयोग करें</b> · '
                '<b>दलाल को पैसे न दें</b>'}}
