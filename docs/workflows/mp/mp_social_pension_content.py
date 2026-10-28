"""Old-age and widow pension (MP) guide content (EN + HI)."""

OUT = "mp-social-pension-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Social Security Pension (MP): Old-age, widow and disability pension',
        'sub': 'सामाजिक सुरक्षा पेंशन (मध्य प्रदेश): वृद्धावस्था, कल्याणी और दिव्यांग पेंशन',
        'benefit': 'About ₹600 a month by DBT (higher for some 80+ beneficiaries, as reported)',
        'legend': ['You do this', 'Government does this (you wait)', 'Pension received'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you can get it',
                   'पात्रता जांचें',
                   '<ul><li><b>Old-age:</b> 60 or older</li><li><b>Kalyani (widow) pension:</b> widowed '
                   'women</li><li><b>Disability pension:</b> with a disability certificate</li><li>Low-income family, '
                   'as per the scheme rules</li></ul>',
                   None),
                  ('you',
                   'Keep these ready',
                   'ये तैयार रखें',
                   "<ul><li><b>Samagra member ID with eKYC</b></li><li>Aadhaar, age proof</li><li>Widows: husband's "
                   'death certificate</li><li>Bank account <b>linked to Samagra and Aadhaar</b></li></ul>',
                   ('tip',
                    'Almost every MP service needs a <b>Samagra member ID with eKYC done</b>. No Samagra yet? See the '
                    '<b>Samagra ID (MP)</b> guide first.')),
                  ('you',
                   'Apply',
                   'आवेदन करें',
                   'Apply on <b>socialsecurity.mp.gov.in</b>, at the <b>Gram Panchayat / Janpad</b>, or at the urban '
                   'body office. Keep the application number.',
                   ('tip',
                    'Applying is <b>free</b>. Under the Lok Seva Guarantee Act a decision is due within a fixed time '
                    '(15 working days reported).')),
                  ('gov',
                   'Verification and sanction',
                   'सत्यापन और स्वीकृति',
                   'The Janpad / urban body verifies and sanctions the pension.',
                   ('stuck', 'No decision in time? File a first appeal or complain on the CM Helpline 181.')),
                  ('done',
                   'Pension every month',
                   'हर महीने पेंशन',
                   'Paid by DBT into the Samagra-linked account.',
                   ('stuck',
                    'Payment stopped? Samagra eKYC is now mandatory for payment; redo it, and check the bank account '
                    'is active.'))],
        'rights_t': 'Stopped or not sanctioned? Complain.',
        'rights': 'Complain on the <b>CM Helpline 181</b> or to the <b>Janpad CEO / urban body</b> with your '
                  'application or Samagra number.',
        'help': '<b>Apply / status:</b> socialsecurity.mp.gov.in · Amounts as reported; check the '
                'portal<br><b>Applying is free</b> · <b>Use only official websites</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'सामाजिक सुरक्षा पेंशन (मध्य प्रदेश): वृद्धावस्था, कल्याणी और दिव्यांग पेंशन',
        'sub': None,
        'benefit': 'हर महीने लगभग ₹600 डीबीटी से (बताए अनुसार कुछ 80+ लाभार्थियों को अधिक)',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'पेंशन मिली'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   '<ul><li><b>वृद्धावस्था:</b> 60 वर्ष या अधिक</li><li><b>कल्याणी (विधवा) पेंशन:</b> विधवा '
                   'महिलाएं</li><li><b>दिव्यांग पेंशन:</b> दिव्यांग प्रमाण पत्र के साथ</li><li>योजना के नियमों के '
                   'अनुसार कम आय वाला परिवार</li></ul>',
                   None),
                  ('you',
                   'ये तैयार रखें',
                   None,
                   '<ul><li><b>ई-केवाईसी वाली समग्र सदस्य आईडी</b></li><li>आधार, उम्र का प्रमाण</li><li>विधवा: पति का '
                   'मृत्यु प्रमाण पत्र</li><li>बैंक खाता <b>समग्र और आधार से जुड़ा</b></li></ul>',
                   ('tip',
                    'मध्य प्रदेश की लगभग हर सेवा के लिए <b>ई-केवाईसी वाली समग्र सदस्य आईडी</b> चाहिए। समग्र नहीं है? '
                    'पहले <b>समग्र आईडी (मप्र)</b> मार्गदर्शिका देखें।')),
                  ('you',
                   'आवेदन करें',
                   None,
                   '<b>socialsecurity.mp.gov.in</b> पर, <b>ग्राम पंचायत / जनपद</b> में, या नगरीय निकाय कार्यालय में '
                   'आवेदन करें। आवेदन संख्या रखें।',
                   ('tip',
                    'आवेदन <b>मुफ़्त</b> है। लोक सेवा गारंटी अधिनियम के तहत तय समय में निर्णय होना चाहिए (बताए अनुसार '
                    '15 कार्य दिवस)।')),
                  ('gov',
                   'सत्यापन और स्वीकृति',
                   None,
                   'जनपद / नगरीय निकाय सत्यापन कर पेंशन स्वीकृत करता है।',
                   ('stuck', 'समय पर निर्णय नहीं? प्रथम अपील करें या सीएम हेल्पलाइन 181 पर शिकायत करें।')),
                  ('done',
                   'हर महीने पेंशन',
                   None,
                   'डीबीटी से समग्र से जुड़े खाते में भुगतान।',
                   ('stuck',
                    'भुगतान रुका? भुगतान के लिए अब समग्र ई-केवाईसी अनिवार्य है; दोबारा करें और बैंक खाता चालू है यह '
                    'जांचें।'))],
        'rights_t': 'पेंशन रुकी या स्वीकृत नहीं? शिकायत करें।',
        'rights': 'आवेदन या समग्र संख्या के साथ <b>सीएम हेल्पलाइन 181</b> पर या <b>जनपद सीईओ / नगरीय निकाय</b> से '
                  'शिकायत करें।',
        'help': '<b>आवेदन / स्थिति:</b> socialsecurity.mp.gov.in · राशि बताए अनुसार; पोर्टल देखें<br><b>आवेदन मुफ़्त '
                'है</b> · <b>केवल आधिकारिक वेबसाइट का उपयोग करें</b>'}}
