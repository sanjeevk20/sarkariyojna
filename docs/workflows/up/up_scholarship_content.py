"""UP Scholarship (pre and post-matric) guide content (EN + HI)."""

OUT = "up-scholarship-guide"
PHASE_BREAK = 5

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'UP Scholarship: Fee reimbursement and scholarship for students',
        'sub': 'उत्तर प्रदेश छात्रवृत्ति एवं शुल्क प्रतिपूर्ति',
        'benefit': "Scholarship and fee reimbursement paid into the student's bank account",
        'legend': ['You do this', 'Government does this (you wait)', 'Money received'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you can get it',
                   'पात्रता जांचें',
                   '<ul><li>Student domiciled in UP, in <b>Class 9–10</b> (pre-matric) or <b>Class 11 to college</b> '
                   '(post-matric)</li><li>Institute and course registered on the portal</li><li>Family income within '
                   'the limit: about <b>₹2 to 2.5 lakh</b> depending on category; the limit shown on the portal is '
                   'final</li></ul>',
                   None),
                  ('you',
                   'Keep these papers ready',
                   'कागज़ तैयार रखें',
                   "<ul><li>Aadhaar and an <b>Aadhaar-seeded bank account</b> in the student's name</li><li><b>Income "
                   "certificate</b> from the tehsil, in the parent's name</li><li>Caste certificate, if applying in a "
                   'reserved category</li><li>Last marksheet, fee receipt, photo</li></ul>',
                   ('stuck',
                    'Private-employer salary letters or plain-paper declarations are not accepted as income proof. Get '
                    'a tehsil income certificate.')),
                  ('you',
                   'Register and apply on the portal',
                   'पोर्टल पर पंजीकरण और आवेदन',
                   'Do the <b>One Time Registration (OTR)</b> on <b>scholarship.up.gov.in</b>, then fill the fresh or '
                   'renewal form before the deadline (usually <b>September–October</b>).',
                   ('tip', "Deadlines are strict. Check the current dates on the portal's notice board.")),
                  ('you',
                   'Submit the printout to your institute',
                   'संस्थान में प्रिंट जमा करें',
                   'Print the final form and give it with documents to your school or college if asked, and get a '
                   'receipt.',
                   None),
                  ('gov',
                   'Institute verifies',
                   'संस्थान सत्यापन करता है',
                   'Your institute checks and forwards the application online, usually within a few days.',
                   ('stuck',
                    'Institute has not verified? Remind the scholarship clerk before the institute deadline.')),
                  ('gov',
                   'Department and bank checks',
                   'विभाग और बैंक की जांच',
                   'The district office checks eligibility and the bank account is validated through PFMS.',
                   ('stuck',
                    'Error shown in status? Use the <b>correction window</b> on the portal; bank errors are fixed at '
                    'your bank.')),
                  ('done',
                   'Money in your account',
                   'खाते में राशि',
                   'The scholarship and fee reimbursement are paid by <b>DBT</b>. Check status on the portal.',
                   None)],
        'rights_t': 'Not paid? Follow up.',
        'rights': 'Check the status page first, then contact the <b>District Social Welfare / Backward Class / '
                  'Minority Welfare Officer</b> (by your category), or complain on <b>IGRS Jansunwai</b>.',
        'help': '<b>Apply / status:</b> scholarship.up.gov.in · Income limits and dates change each year; the portal '
                'is final<br><b>Applying is free</b> · <b>Use only official websites</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'यूपी छात्रवृत्ति: छात्रों के लिए छात्रवृत्ति और शुल्क प्रतिपूर्ति',
        'sub': None,
        'benefit': 'छात्रवृत्ति और शुल्क प्रतिपूर्ति छात्र के बैंक खाते में',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'राशि मिली'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   '<ul><li>उत्तर प्रदेश के निवासी छात्र, <b>कक्षा 9–10</b> (पूर्वदशम) या <b>कक्षा 11 से कॉलेज</b> '
                   '(दशमोत्तर)</li><li>संस्थान और कोर्स पोर्टल पर पंजीकृत हों</li><li>पारिवारिक आय सीमा के भीतर: वर्ग '
                   'के अनुसार लगभग <b>₹2 से 2.5 लाख</b>; पोर्टल पर दिखी सीमा अंतिम है</li></ul>',
                   None),
                  ('you',
                   'कागज़ तैयार रखें',
                   None,
                   '<ul><li>आधार और छात्र के नाम <b>आधार से जुड़ा बैंक खाता</b></li><li>तहसील से माता/पिता के नाम '
                   '<b>आय प्रमाण पत्र</b></li><li>आरक्षित वर्ग में आवेदन पर जाति प्रमाण पत्र</li><li>पिछली मार्कशीट, '
                   'फीस रसीद, फोटो</li></ul>',
                   ('stuck',
                    'निजी नियोक्ता का वेतन पत्र या सादे कागज़ का घोषणा पत्र आय प्रमाण नहीं माना जाता। तहसील से आय '
                    'प्रमाण पत्र बनवाएं।')),
                  ('you',
                   'पोर्टल पर पंजीकरण और आवेदन',
                   None,
                   '<b>scholarship.up.gov.in</b> पर <b>वन टाइम रजिस्ट्रेशन (OTR)</b> करें, फिर अंतिम तिथि से पहले नया '
                   'या नवीनीकरण फॉर्म भरें (आमतौर पर <b>सितंबर–अक्टूबर</b>)।',
                   ('tip', 'अंतिम तिथियां सख्त हैं। पोर्टल की सूचना पर वर्तमान तिथियां देखें।')),
                  ('you',
                   'संस्थान में प्रिंट जमा करें',
                   None,
                   'अंतिम फॉर्म का प्रिंट दस्तावेज़ों के साथ मांगे जाने पर अपने स्कूल या कॉलेज में जमा करें और रसीद '
                   'लें।',
                   None),
                  ('gov',
                   'संस्थान सत्यापन करता है',
                   None,
                   'आपका संस्थान आवेदन जांच कर ऑनलाइन आगे भेजता है, आमतौर पर कुछ दिनों में।',
                   ('stuck',
                    'संस्थान ने सत्यापन नहीं किया? संस्थान की अंतिम तिथि से पहले छात्रवृत्ति लिपिक को याद दिलाएं।')),
                  ('gov',
                   'विभाग और बैंक की जांच',
                   None,
                   'ज़िला कार्यालय पात्रता जांचता है और PFMS से बैंक खाते का सत्यापन होता है।',
                   ('stuck',
                    'स्थिति में त्रुटि दिख रही है? पोर्टल की <b>संशोधन खिड़की</b> का उपयोग करें; बैंक की त्रुटि बैंक '
                    'में ठीक होती है।')),
                  ('done',
                   'खाते में राशि',
                   None,
                   'छात्रवृत्ति और शुल्क प्रतिपूर्ति <b>डीबीटी</b> से मिलती है। स्थिति पोर्टल पर देखें।',
                   None)],
        'rights_t': 'भुगतान नहीं हुआ? पाठपुरावा करें।',
        'rights': 'पहले स्थिति पेज देखें, फिर अपने वर्ग के अनुसार <b>ज़िला समाज कल्याण / पिछड़ा वर्ग / अल्पसंख्यक '
                  'कल्याण अधिकारी</b> से संपर्क करें, या <b>आईजीआरएस जनसुनवाई</b> पर शिकायत करें।',
        'help': '<b>आवेदन / स्थिति:</b> scholarship.up.gov.in · आय सीमा और तिथियां हर साल बदलती हैं; पोर्टल अंतिम '
                'है<br><b>आवेदन मुफ़्त है</b> · <b>केवल आधिकारिक वेबसाइट का उपयोग करें</b>'}}
