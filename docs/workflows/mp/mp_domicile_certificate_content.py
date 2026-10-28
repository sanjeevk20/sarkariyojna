"""Domicile certificate (MP) guide content (EN + HI)."""

OUT = "mp-domicile-certificate-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Domicile Certificate (MP): Mool Niwasi Praman Patra',
        'sub': 'मूल निवासी प्रमाण पत्र (मध्य प्रदेश)',
        'benefit': 'Needed for state-quota admissions, MP government jobs and state scholarships',
        'legend': ['You do this', 'Government does this (you wait)', 'Certificate ready'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check who can get it',
                   'पात्रता जांचें',
                   'People who live permanently in Madhya Pradesh. Read the admission or job notice for any '
                   'residence-period rule.',
                   ('tip',
                    'Almost every MP service needs a <b>Samagra member ID with eKYC done</b>. No Samagra yet? See the '
                    '<b>Samagra ID (MP)</b> guide first.')),
                  ('you',
                   'Keep these papers ready',
                   'कागज़ तैयार रखें',
                   '<ul><li>Samagra member ID</li><li>Aadhaar</li><li>Residence proof: ration card, voter ID, '
                   'electricity bill, school leaving certificate</li><li>Photo</li></ul>',
                   None),
                  ('you',
                   'Apply online or at a Lok Seva Kendra',
                   'ऑनलाइन या लोक सेवा केंद्र से आवेदन करें',
                   'Apply yourself on <b>mpedistrict.gov.in</b>, or at a <b>Lok Seva Kendra</b> / MP Online kiosk. '
                   'Keep the <b>application number</b>.',
                   ('tip',
                    'Applying online yourself is reported to be free or nearly free; kiosks charge a small service '
                    'fee. Do not pay more.')),
                  ('gov',
                   'Checked by the revenue office',
                   'राजस्व कार्यालय द्वारा जांच',
                   'The revenue office checks your residence documents; a local inquiry may be made.',
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
                   'Download it from e-District with your application number and check every detail.',
                   ('tip',
                    'The domicile certificate is reported to be valid for life. Keep printed copies for admissions.'))],
        'rights_t': 'Taking too long? Use your rights.',
        'rights': 'Certificates are covered by the <b>MP Lok Seva Guarantee Act</b>, with a fixed time limit for each '
                  'service. If it is crossed, file a <b>first appeal</b>, or complain to the <b>CM Helpline 181</b>, '
                  'with your application number.',
        'help': '<b>Apply / status:</b> mpedistrict.gov.in or any Lok Seva Kendra / MP Online kiosk · '
                '<b>Complaints:</b> CM Helpline 181<br><b>Applying online yourself is cheapest</b> · <b>Never pay a '
                'tout</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'मूल निवासी प्रमाण पत्र (मध्य प्रदेश)',
        'sub': None,
        'benefit': 'राज्य कोटे के प्रवेश, मप्र सरकारी नौकरी और राज्य छात्रवृत्ति के लिए ज़रूरी',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'प्रमाण पत्र तैयार'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   'मध्य प्रदेश के स्थायी निवासी। निवास अवधि के नियम के लिए प्रवेश या नौकरी की सूचना पढ़ें।',
                   ('tip',
                    'मध्य प्रदेश की लगभग हर सेवा के लिए <b>ई-केवाईसी वाली समग्र सदस्य आईडी</b> चाहिए। समग्र नहीं है? '
                    'पहले <b>समग्र आईडी (मप्र)</b> मार्गदर्शिका देखें।')),
                  ('you',
                   'कागज़ तैयार रखें',
                   None,
                   '<ul><li>समग्र सदस्य आईडी</li><li>आधार</li><li>निवास प्रमाण: राशन कार्ड, वोटर आईडी, बिजली बिल, '
                   'स्कूल छोड़ने का प्रमाण पत्र</li><li>फोटो</li></ul>',
                   None),
                  ('you',
                   'ऑनलाइन या लोक सेवा केंद्र से आवेदन करें',
                   None,
                   '<b>mpedistrict.gov.in</b> पर खुद, या <b>लोक सेवा केंद्र</b> / एमपी ऑनलाइन कियोस्क से आवेदन करें। '
                   '<b>आवेदन संख्या</b> संभाल कर रखें।',
                   ('tip',
                    'खुद ऑनलाइन आवेदन बताए अनुसार मुफ़्त या लगभग मुफ़्त है; कियोस्क थोड़ा सेवा शुल्क लेते हैं। इससे '
                    'ज़्यादा न दें।')),
                  ('gov',
                   'राजस्व कार्यालय द्वारा जांच',
                   None,
                   'राजस्व कार्यालय निवास दस्तावेज़ जांचता है; स्थानीय जांच हो सकती है।',
                   ('stuck', 'और दस्तावेज़ मांगे गए? नया आवेदन करने के बजाय उसी आवेदन संख्या पर अपलोड करें।')),
                  ('gov',
                   'तहसीलदार / एसडीएम स्वीकृति देते हैं',
                   None,
                   '<b>तहसीलदार / एसडीएम</b> स्वीकृति देते हैं और प्रमाण पत्र पर <b>डिजिटल हस्ताक्षर</b> होते हैं।',
                   None),
                  ('done',
                   'प्रमाण पत्र डाउनलोड करें',
                   None,
                   'आवेदन संख्या से ई-डिस्ट्रिक्ट से डाउनलोड करें और हर विवरण जांच लें।',
                   ('tip', 'मूल निवासी प्रमाण पत्र बताए अनुसार आजीवन मान्य है। प्रवेश के लिए प्रिंट कॉपी रखें।'))],
        'rights_t': 'बहुत देर हो रही है? अपने अधिकार का उपयोग करें।',
        'rights': 'प्रमाण पत्र <b>मप्र लोक सेवा गारंटी अधिनियम</b> के तहत आते हैं और हर सेवा की तय समय-सीमा है। '
                  'समय-सीमा निकल जाए तो आवेदन संख्या के साथ <b>प्रथम अपील</b> करें या <b>सीएम हेल्पलाइन 181</b> पर '
                  'शिकायत करें।',
        'help': '<b>आवेदन / स्थिति:</b> mpedistrict.gov.in या कोई भी लोक सेवा केंद्र / एमपी ऑनलाइन कियोस्क · '
                '<b>शिकायत:</b> सीएम हेल्पलाइन 181<br><b>खुद ऑनलाइन आवेदन सबसे सस्ता है</b> · <b>दलाल को पैसे न '
                'दें</b>'}}
