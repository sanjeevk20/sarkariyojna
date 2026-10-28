"""Caste certificate (MP) guide content (EN + HI)."""

OUT = "mp-caste-certificate-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Caste Certificate (MP): Apply on e-District',
        'sub': 'जाति प्रमाण पत्र (मध्य प्रदेश): ई-डिस्ट्रिक्ट से आवेदन',
        'benefit': 'Needed for reserved seats, government jobs, scholarships and fee concessions',
        'legend': ['You do this', 'Government does this (you wait)', 'Certificate ready'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check who can get it',
                   'पात्रता जांचें',
                   'Members of recognised <b>SC, ST and OBC</b> communities who live permanently in MP.',
                   ('tip',
                    'Almost every MP service needs a <b>Samagra member ID with eKYC done</b>. No Samagra yet? See the '
                    '<b>Samagra ID (MP)</b> guide first.')),
                  ('you',
                   'Keep these papers ready',
                   'कागज़ तैयार रखें',
                   "<ul><li>Samagra member ID</li><li>Aadhaar</li><li>A family member's caste certificate or old "
                   'records showing caste</li><li>Residence proof, photo</li></ul>',
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
                   'The revenue office verifies caste and residence; the Patwari may report locally.',
                   ('stuck',
                    'Asked for more documents? Upload them against the same application number instead of applying '
                    'again.')),
                  ('gov',
                   'SDM approves',
                   'एसडीएम स्वीकृति देते हैं',
                   'The <b>SDM</b> approves and the certificate is <b>digitally signed</b>.',
                   None),
                  ('done',
                   'Download your certificate',
                   'प्रमाण पत्र डाउनलोड करें',
                   'Download it from e-District with your application number and check every detail.',
                   ('tip',
                    'Some services (for example OBC) are available only online or at a Lok Seva Kendra. Check the '
                    'exact caste name and category.'))],
        'rights_t': 'Taking too long? Use your rights.',
        'rights': 'Certificates are covered by the <b>MP Lok Seva Guarantee Act</b>, with a fixed time limit for each '
                  'service. If it is crossed, file a <b>first appeal</b>, or complain to the <b>CM Helpline 181</b>, '
                  'with your application number.',
        'help': '<b>Apply / status:</b> mpedistrict.gov.in or any Lok Seva Kendra / MP Online kiosk · '
                '<b>Complaints:</b> CM Helpline 181<br><b>Applying online yourself is cheapest</b> · <b>Never pay a '
                'tout</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'जाति प्रमाण पत्र (मध्य प्रदेश): ई-डिस्ट्रिक्ट से आवेदन',
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
                   'मध्य प्रदेश में स्थायी रूप से रहने वाले मान्यता प्राप्त <b>अनुसूचित जाति, जनजाति और पिछड़ा '
                   'वर्ग</b> समुदायों के सदस्य।',
                   ('tip',
                    'मध्य प्रदेश की लगभग हर सेवा के लिए <b>ई-केवाईसी वाली समग्र सदस्य आईडी</b> चाहिए। समग्र नहीं है? '
                    'पहले <b>समग्र आईडी (मप्र)</b> मार्गदर्शिका देखें।')),
                  ('you',
                   'कागज़ तैयार रखें',
                   None,
                   '<ul><li>समग्र सदस्य आईडी</li><li>आधार</li><li>परिवार के सदस्य का जाति प्रमाण पत्र या जाति दर्शाने '
                   'वाले पुराने रिकॉर्ड</li><li>निवास प्रमाण, फोटो</li></ul>',
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
                   'राजस्व कार्यालय जाति और निवास सत्यापित करता है; पटवारी स्थानीय रिपोर्ट दे सकते हैं।',
                   ('stuck', 'और दस्तावेज़ मांगे गए? नया आवेदन करने के बजाय उसी आवेदन संख्या पर अपलोड करें।')),
                  ('gov',
                   'एसडीएम स्वीकृति देते हैं',
                   None,
                   '<b>एसडीएम</b> स्वीकृति देते हैं और प्रमाण पत्र पर <b>डिजिटल हस्ताक्षर</b> होते हैं।',
                   None),
                  ('done',
                   'प्रमाण पत्र डाउनलोड करें',
                   None,
                   'आवेदन संख्या से ई-डिस्ट्रिक्ट से डाउनलोड करें और हर विवरण जांच लें।',
                   ('tip',
                    'कुछ सेवाएं (जैसे ओबीसी) केवल ऑनलाइन या लोक सेवा केंद्र पर उपलब्ध हैं। जाति का नाम और वर्ग ठीक से '
                    'जांचें।'))],
        'rights_t': 'बहुत देर हो रही है? अपने अधिकार का उपयोग करें।',
        'rights': 'प्रमाण पत्र <b>मप्र लोक सेवा गारंटी अधिनियम</b> के तहत आते हैं और हर सेवा की तय समय-सीमा है। '
                  'समय-सीमा निकल जाए तो आवेदन संख्या के साथ <b>प्रथम अपील</b> करें या <b>सीएम हेल्पलाइन 181</b> पर '
                  'शिकायत करें।',
        'help': '<b>आवेदन / स्थिति:</b> mpedistrict.gov.in या कोई भी लोक सेवा केंद्र / एमपी ऑनलाइन कियोस्क · '
                '<b>शिकायत:</b> सीएम हेल्पलाइन 181<br><b>खुद ऑनलाइन आवेदन सबसे सस्ता है</b> · <b>दलाल को पैसे न '
                'दें</b>'}}
