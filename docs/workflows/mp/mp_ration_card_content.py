"""Ration eligibility slip (MP) guide content (EN + HI)."""

OUT = "mp-ration-card-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Ration in MP: Get your eligibility slip (patrata parchi)',
        'sub': 'मध्य प्रदेश में राशन: पात्रता पर्ची कैसे मिले',
        'benefit': 'Monthly food grain: 35 kg per Antyodaya family, 5 kg per person for priority households',
        'legend': ['You do this', 'Government does this (you wait)', 'Ration received'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Know how MP ration works',
                   'मप्र में राशन कैसे मिलता है',
                   'In MP, ration is linked to your <b>Samagra family ID</b>. Eligible families get an <b>eligibility '
                   'slip (patrata parchi)</b>; the fair price shop serves you against it.',
                   ('tip',
                    'Almost every MP service needs a <b>Samagra member ID with eKYC done</b>. No Samagra yet? See the '
                    '<b>Samagra ID (MP)</b> guide first.')),
                  ('you',
                   'Check if you are already eligible',
                   'जांचें कि आप पहले से पात्र हैं या नहीं',
                   "On the state food (Ration Mitra) portal, download the <b>current month's eligibility slip</b> with "
                   'your family ID, member ID or Aadhaar.',
                   ('tip', 'Already listed? You only need the slip, not a new card.')),
                  ('you',
                   'Apply if not listed',
                   'सूची में नहीं हैं तो आवेदन करें',
                   'Apply through the <b>Gram Panchayat / Janpad</b> or urban body office, with Samagra eKYC done for '
                   'all members and proof of your eligible category.',
                   None),
                  ('gov',
                   'Verification',
                   'सत्यापन',
                   'The local body and food department verify the family and category, and add you to the eligible '
                   'list.',
                   ('stuck', 'Rejected? Ask for the reason in writing and approach the district food office.')),
                  ('done',
                   'Collect ration monthly',
                   'हर महीने राशन लें',
                   'At the fair price shop, a member gives an <b>Aadhaar fingerprint</b> on the POS machine and '
                   'collects grain for all members.',
                   ('stuck',
                    'Shop gives less or asks for money? Ask for a receipt and complain on the CM Helpline 181.'))],
        'rights_t': 'Short supply or slip pending? Complain.',
        'rights': 'Complain to the <b>district food office</b> or the <b>CM Helpline 181</b> with your Samagra family '
                  'ID.',
        'help': '<b>Eligibility slip:</b> state Ration Mitra portal · Entitlements as per NFSA<br><b>Ration is your '
                'right; never pay extra</b> · <b>Use only official websites</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'मध्य प्रदेश में राशन: पात्रता पर्ची कैसे मिले',
        'sub': None,
        'benefit': 'हर महीने अनाज: अंत्योदय परिवार को 35 किलो, प्राथमिकता परिवार में प्रति व्यक्ति 5 किलो',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'राशन मिला'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'मप्र में राशन कैसे मिलता है',
                   None,
                   'मध्य प्रदेश में राशन आपकी <b>समग्र परिवार आईडी</b> से जुड़ा है। पात्र परिवारों को <b>पात्रता '
                   'पर्ची</b> मिलती है; उचित मूल्य दुकान उसी पर राशन देती है।',
                   ('tip',
                    'मध्य प्रदेश की लगभग हर सेवा के लिए <b>ई-केवाईसी वाली समग्र सदस्य आईडी</b> चाहिए। समग्र नहीं है? '
                    'पहले <b>समग्र आईडी (मप्र)</b> मार्गदर्शिका देखें।')),
                  ('you',
                   'जांचें कि आप पहले से पात्र हैं या नहीं',
                   None,
                   'राज्य खाद्य (राशन मित्र) पोर्टल पर परिवार आईडी, सदस्य आईडी या आधार से <b>इस महीने की पात्रता '
                   'पर्ची</b> डाउनलोड करें।',
                   ('tip', 'पहले से सूची में हैं? आपको सिर्फ़ पर्ची चाहिए, नया कार्ड नहीं।')),
                  ('you',
                   'सूची में नहीं हैं तो आवेदन करें',
                   None,
                   'सभी सदस्यों के समग्र ई-केवाईसी और पात्र श्रेणी के प्रमाण के साथ <b>ग्राम पंचायत / जनपद</b> या '
                   'नगरीय निकाय कार्यालय से आवेदन करें।',
                   None),
                  ('gov',
                   'सत्यापन',
                   None,
                   'स्थानीय निकाय और खाद्य विभाग परिवार और श्रेणी सत्यापित कर पात्र सूची में जोड़ते हैं।',
                   ('stuck', 'अस्वीकृत? कारण लिखित में मांगें और ज़िला खाद्य कार्यालय जाएं।')),
                  ('done',
                   'हर महीने राशन लें',
                   None,
                   'उचित मूल्य दुकान पर एक सदस्य पीओएस मशीन पर <b>आधार अंगूठा</b> लगाकर सभी सदस्यों का अनाज लेता है।',
                   ('stuck',
                    'दुकानदार कम देता है या पैसे मांगता है? रसीद मांगें और सीएम हेल्पलाइन 181 पर शिकायत करें।'))],
        'rights_t': 'कम राशन या पर्ची लंबित? शिकायत करें।',
        'rights': 'समग्र परिवार आईडी के साथ <b>ज़िला खाद्य कार्यालय</b> या <b>सीएम हेल्पलाइन 181</b> पर शिकायत करें।',
        'help': '<b>पात्रता पर्ची:</b> राज्य राशन मित्र पोर्टल · एनएफएसए के अनुसार हक<br><b>राशन आपका अधिकार है; '
                'अतिरिक्त पैसे न दें</b> · <b>केवल आधिकारिक वेबसाइट का उपयोग करें</b>'}}
