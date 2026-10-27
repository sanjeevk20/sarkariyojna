"""Ration card (UP, NFSA) guide content (EN + HI)."""

OUT = "up-ration-card-guide"
PHASE_BREAK = 5

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Ration Card (UP): Get free grain under the food security law',
        'sub': 'राशन कार्ड (उत्तर प्रदेश): खाद्य सुरक्षा कानून के तहत मुफ़्त अनाज',
        'benefit': 'Free grain every month from the fair price shop',
        'legend': ['You do this', 'Government does this (you wait)', 'Ration received'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Know the two card types',
                   'कार्ड के दो प्रकार जानें',
                   '<ul><li><b>Antyodaya (AAY):</b> poorest families, <b>35 kg</b> grain per family a '
                   'month</li><li><b>Patra Grihasthi:</b> eligible households, <b>5 kg</b> per person a '
                   'month</li></ul>Grain under these cards is <b>free</b>.',
                   None),
                  ('you',
                   'Check if you can get it',
                   'पात्रता जांचें',
                   'Low-income families usually qualify. Families with an <b>income-tax payer</b>, a <b>government '
                   'job</b> or large land or vehicles are usually <b>excluded</b>.',
                   ('tip',
                    'Search your name in the eligibility list on <b>fcs.up.gov.in</b> first; you may already be '
                    'listed.')),
                  ('you',
                   'Keep these papers ready',
                   'कागज़ तैयार रखें',
                   '<ul><li>Aadhaar of <b>every family member</b></li><li>Photo of the head of family (the <b>eldest '
                   'woman</b> is usually made head)</li><li>Bank account details</li><li>Income certificate and '
                   'address proof</li></ul>',
                   None),
                  ('you',
                   'Apply',
                   'आवेदन करें',
                   'Apply on <b>fcs.up.gov.in</b>, at a <b>Jan Seva Kendra</b>, or at the tehsil / town supply office. '
                   'Keep the <b>application number</b>.',
                   ('tip', 'The form is <b>free</b>.')),
                  ('gov',
                   'Verification',
                   'सत्यापन',
                   'The <b>Supply Inspector</b> (town) or <b>ADO / block official</b> (village) checks your family and '
                   'income.',
                   ('stuck',
                    'Rejected? Ask for the reason in writing; you can apply again or appeal to the District Supply '
                    'Officer.')),
                  ('gov',
                   'Card issued',
                   'कार्ड जारी',
                   'Your card number is generated and the family is attached to a <b>fair price shop (kotedar)</b>.',
                   None),
                  ('done',
                   'Collect ration every month',
                   'हर महीने राशन लें',
                   'At the shop, a family member gives an <b>Aadhaar fingerprint</b> on the ePoS machine and collects '
                   'the grain.',
                   ('stuck',
                    'Fingerprint fails or shopkeeper gives less? Ask for a receipt and complain to the supply office '
                    'or <b>CM Helpline 1076</b>.'))],
        'rights_t': 'Shopkeeper cheating or card pending? Complain.',
        'rights': 'Complain to the <b>District Supply Officer</b>, on the helpline shown on <b>fcs.up.gov.in</b>, or '
                  'the <b>CM Helpline 1076</b>.',
        'help': '<b>Apply / lists:</b> fcs.up.gov.in · Free grain under NFSA / PM Garib Kalyan Anna Yojana<br><b>The '
                'form is free</b> · <b>Use only official websites</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'राशन कार्ड (उत्तर प्रदेश): खाद्य सुरक्षा कानून के तहत मुफ़्त अनाज',
        'sub': None,
        'benefit': 'हर महीने उचित दर की दुकान से मुफ़्त अनाज',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'राशन मिला'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'कार्ड के दो प्रकार जानें',
                   None,
                   '<ul><li><b>अंत्योदय (AAY):</b> सबसे गरीब परिवार, प्रति परिवार हर महीने <b>35 किलो</b> '
                   'अनाज</li><li><b>पात्र गृहस्थी:</b> पात्र परिवार, प्रति व्यक्ति हर महीने <b>5 किलो</b></li></ul>इन '
                   'कार्डों पर अनाज <b>मुफ़्त</b> है।',
                   None),
                  ('you',
                   'पात्रता जांचें',
                   None,
                   'कम आय वाले परिवार आमतौर पर पात्र होते हैं। जिन परिवारों में <b>आयकर दाता</b>, <b>सरकारी नौकरी</b> '
                   'या बड़ी ज़मीन / वाहन हों, वे आमतौर पर <b>बाहर</b> रहते हैं।',
                   ('tip',
                    'पहले <b>fcs.up.gov.in</b> पर पात्रता सूची में अपना नाम खोजें; हो सकता है आप पहले से सूची में '
                    'हों।')),
                  ('you',
                   'कागज़ तैयार रखें',
                   None,
                   '<ul><li><b>परिवार के हर सदस्य</b> का आधार</li><li>परिवार के मुखिया की फोटो (आमतौर पर <b>सबसे बड़ी '
                   'महिला</b> मुखिया बनती हैं)</li><li>बैंक खाते का विवरण</li><li>आय प्रमाण पत्र और पते का '
                   'प्रमाण</li></ul>',
                   None),
                  ('you',
                   'आवेदन करें',
                   None,
                   '<b>fcs.up.gov.in</b> पर, <b>जन सेवा केंद्र</b> से, या तहसील / नगर आपूर्ति कार्यालय में आवेदन करें। '
                   '<b>आवेदन संख्या</b> रखें।',
                   ('tip', 'फॉर्म <b>मुफ़्त</b> है।')),
                  ('gov',
                   'सत्यापन',
                   None,
                   '<b>पूर्ति निरीक्षक</b> (शहर) या <b>एडीओ / ब्लॉक अधिकारी</b> (गांव) परिवार और आय की जांच करते हैं।',
                   ('stuck',
                    'अस्वीकार हुआ? कारण लिखित में मांगें; दोबारा आवेदन या ज़िला पूर्ति अधिकारी के यहां अपील कर सकते '
                    'हैं।')),
                  ('gov',
                   'कार्ड जारी',
                   None,
                   'आपका कार्ड नंबर बनता है और परिवार को एक <b>उचित दर दुकान (कोटेदार)</b> से जोड़ा जाता है।',
                   None),
                  ('done',
                   'हर महीने राशन लें',
                   None,
                   'दुकान पर परिवार का कोई सदस्य ई-पॉस मशीन पर <b>आधार अंगूठा</b> लगाकर अनाज लेता है।',
                   ('stuck',
                    'अंगूठा नहीं लगता या दुकानदार कम देता है? पर्ची मांगें और आपूर्ति कार्यालय या <b>मुख्यमंत्री '
                    'हेल्पलाइन 1076</b> पर शिकायत करें।'))],
        'rights_t': 'दुकानदार धोखा दे या कार्ड अटका हो? शिकायत करें।',
        'rights': '<b>ज़िला पूर्ति अधिकारी</b>, <b>fcs.up.gov.in</b> पर दी गई हेल्पलाइन, या <b>मुख्यमंत्री हेल्पलाइन '
                  '1076</b> पर शिकायत करें।',
        'help': '<b>आवेदन / सूची:</b> fcs.up.gov.in · एनएफएसए / प्रधानमंत्री गरीब कल्याण अन्न योजना के तहत मुफ़्त '
                'अनाज<br><b>फॉर्म मुफ़्त है</b> · <b>केवल आधिकारिक वेबसाइट का उपयोग करें</b>'}}
