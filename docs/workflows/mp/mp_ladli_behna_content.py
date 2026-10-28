"""Ladli Behna Yojana (MP) guide content (EN + HI)."""

OUT = "mp-ladli-behna-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Ladli Behna Yojana: ₹1,500 a month for women in MP',
        'sub': 'मुख्यमंत्री लाड़ली बहना योजना: महिलाओं को हर महीने ₹1,500',
        'benefit': "₹1,500 a month by DBT into the woman's own bank account (most 2026 reports)",
        'legend': ['You do this', 'Government does this (you wait)', 'Money received'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you can get it',
                   'पात्रता जांचें',
                   '<ul><li>Woman aged <b>21 to 60</b>, living in Madhya Pradesh</li><li>Married, widowed, divorced or '
                   'abandoned</li><li>Family income up to about <b>₹2.5 lakh a year</b>; no income-tax payer or '
                   'government employee in the family</li></ul>',
                   None),
                  ('you',
                   'Know if registration is open',
                   'जानें पंजीकरण खुला है या नहीं',
                   'New registrations have been <b>closed most of the time since 2023</b>, with occasional windows '
                   '(for example for women newly turning 21). Ask your <b>Gram Panchayat / ward office</b> or '
                   'Anganwadi before going anywhere.',
                   ('stuck',
                    "Anyone offering to 'add your name' for money while registration is closed is cheating you.")),
                  ('you',
                   'Keep these ready',
                   'ये तैयार रखें',
                   '<ul><li><b>Samagra member ID with eKYC</b></li><li>Aadhaar</li><li>Your own bank account, '
                   '<b>Aadhaar-linked with DBT on</b></li><li>Mobile number</li></ul>',
                   ('tip',
                    'Almost every MP service needs a <b>Samagra member ID with eKYC done</b>. No Samagra yet? See the '
                    '<b>Samagra ID (MP)</b> guide first.')),
                  ('gov',
                   'Verification and approval',
                   'सत्यापन और स्वीकृति',
                   'Applications taken at camps are checked against Samagra, income and tax data, then approved.',
                   ('stuck',
                    'Shown as rejected? Ask the Gram Panchayat / ward office for the reason; if it is wrong, raise it '
                    'with the CM Helpline 181.')),
                  ('you',
                   'Keep eKYC and bank link current',
                   'ई-केवाईसी और बैंक लिंक चालू रखें',
                   'Complete the <b>yearly eKYC</b> when the window opens (it ran 1 June – 15 July in 2026, as '
                   'reported) and keep your bank account active.',
                   ('stuck',
                    'Missed eKYC is the most common reason payments stop. Do it at an MP Online kiosk or CSC; it is '
                    'reported to be free.')),
                  ('done',
                   '₹1,500 every month',
                   'हर महीने ₹1,500',
                   'Money comes by DBT, usually around the 10th of the month. Check your instalment history on '
                   '<b>cmladlibahna.mp.gov.in</b>.',
                   ('stuck',
                    'Not received? Check the portal status, then the bank for Aadhaar seeding and DBT. Still stuck: CM '
                    'Helpline 181.'))],
        'rights_t': 'Payment missing? Complain.',
        'rights': 'Use the <b>CM Helpline 181</b> or the Ladli Behna helpline listed on the portal, with your '
                  'registration number. You can also write to the district <b>Women and Child Development</b> office.',
        'help': '<b>Status:</b> cmladlibahna.mp.gov.in · <b>Complaints:</b> CM Helpline 181 · Amount and windows as '
                'reported; check the portal<br><b>Registration is free</b> · <b>Never share your OTP</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'लाड़ली बहना योजना: मध्य प्रदेश की महिलाओं को हर महीने ₹1,500',
        'sub': None,
        'benefit': 'हर महीने ₹1,500 डीबीटी से महिला के अपने बैंक खाते में (2026 की अधिकतर ख़बरों के अनुसार)',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'राशि मिली'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   '<ul><li><b>21 से 60 वर्ष</b> की महिला, मध्य प्रदेश की निवासी</li><li>विवाहित, विधवा, तलाकशुदा या '
                   'परित्यक्ता</li><li>पारिवारिक आय लगभग <b>₹2.5 लाख प्रति वर्ष</b> तक; परिवार में कोई आयकरदाता या '
                   'सरकारी कर्मचारी न हो</li></ul>',
                   None),
                  ('you',
                   'जानें पंजीकरण खुला है या नहीं',
                   None,
                   'नए पंजीकरण <b>2023 से ज़्यादातर बंद</b> रहे हैं, बीच-बीच में कुछ अवसर खुलते हैं (जैसे 21 वर्ष पूरी '
                   'करने वाली महिलाओं के लिए)। कहीं जाने से पहले <b>ग्राम पंचायत / वार्ड कार्यालय</b> या आंगनवाड़ी से '
                   'पूछें।',
                   ('stuck', "पंजीकरण बंद होने पर पैसे लेकर 'नाम जुड़वाने' की बात करने वाला आपको ठग रहा है।")),
                  ('you',
                   'ये तैयार रखें',
                   None,
                   '<ul><li><b>ई-केवाईसी वाली समग्र सदस्य आईडी</b></li><li>आधार</li><li>आपका अपना बैंक खाता, <b>आधार '
                   'से जुड़ा और डीबीटी चालू</b></li><li>मोबाइल नंबर</li></ul>',
                   ('tip',
                    'मध्य प्रदेश की लगभग हर सेवा के लिए <b>ई-केवाईसी वाली समग्र सदस्य आईडी</b> चाहिए। समग्र नहीं है? '
                    'पहले <b>समग्र आईडी (मप्र)</b> मार्गदर्शिका देखें।')),
                  ('gov',
                   'सत्यापन और स्वीकृति',
                   None,
                   'शिविरों में लिए गए आवेदन समग्र, आय और कर रिकॉर्ड से जांचकर स्वीकृत होते हैं।',
                   ('stuck',
                    'अस्वीकृत दिख रहा है? ग्राम पंचायत / वार्ड कार्यालय से कारण पूछें; गलत लगे तो सीएम हेल्पलाइन 181 '
                    'पर उठाएं।')),
                  ('you',
                   'ई-केवाईसी और बैंक लिंक चालू रखें',
                   None,
                   'खिड़की खुलने पर <b>सालाना ई-केवाईसी</b> पूरा करें (2026 में बताए अनुसार 1 जून – 15 जुलाई) और बैंक '
                   'खाता चालू रखें।',
                   ('stuck',
                    'ई-केवाईसी छूटना भुगतान रुकने का सबसे आम कारण है। एमपी ऑनलाइन कियोस्क या सीएससी पर करें; बताए '
                    'अनुसार यह मुफ़्त है।')),
                  ('done',
                   'हर महीने ₹1,500',
                   None,
                   'राशि डीबीटी से आती है, आमतौर पर महीने की 10 तारीख के आसपास। किस्तों का इतिहास '
                   '<b>cmladlibahna.mp.gov.in</b> पर देखें।',
                   ('stuck',
                    'राशि नहीं आई? पोर्टल पर स्थिति देखें, फिर बैंक में आधार सीडिंग और डीबीटी जांचें। फिर भी अटके: '
                    'सीएम हेल्पलाइन 181।'))],
        'rights_t': 'भुगतान नहीं आया? शिकायत करें।',
        'rights': 'पंजीकरण संख्या के साथ <b>सीएम हेल्पलाइन 181</b> या पोर्टल पर दी गई लाड़ली बहना हेल्पलाइन का उपयोग '
                  'करें। ज़िला <b>महिला एवं बाल विकास</b> कार्यालय को भी लिख सकती हैं।',
        'help': '<b>स्थिति:</b> cmladlibahna.mp.gov.in · <b>शिकायत:</b> सीएम हेल्पलाइन 181 · राशि और अवसर बताए अनुसार; '
                'पोर्टल देखें<br><b>पंजीकरण मुफ़्त है</b> · <b>ओटीपी किसी को न बताएं</b>'}}
