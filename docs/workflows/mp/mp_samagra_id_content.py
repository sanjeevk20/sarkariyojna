"""Samagra ID (MP) guide content (EN + HI)."""

OUT = "mp-samagra-id-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Samagra ID: The family ID behind almost every MP scheme',
        'sub': 'समग्र आईडी: मध्य प्रदेश की लगभग हर योजना की पारिवारिक पहचान',
        'benefit': 'One family ID and member IDs, used for pensions, ration, Ladli Behna, certificates and '
                   'scholarships',
        'legend': ['You do this', 'Government does this (you wait)', 'Samagra ready'],
        'phases': ['Find or create', 'Keep it correct'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you already have one',
                   'पता करें कि पहले से है या नहीं',
                   'Most families were registered in surveys. Search on <b>samagra.gov.in</b> by name, mobile or '
                   'Aadhaar. The <b>family ID</b> is 8 digits and each <b>member ID</b> is 9 digits (as reported).',
                   ('tip', 'Schemes usually ask for the <b>member</b> ID, not the family ID.')),
                  ('you',
                   'New family or moved to MP?',
                   'नया परिवार या मप्र में आए हैं?',
                   'Apply for a new family ID at your <b>Gram Panchayat</b>, <b>Janpad</b> or <b>urban ward '
                   'office</b>, or through the new-family option on the portal. Take Aadhaar of all members and '
                   'address proof.',
                   None),
                  ('you',
                   'Do eKYC for every member',
                   'हर सदस्य का ई-केवाईसी करें',
                   'Samagra eKYC links each member to Aadhaar. Do it on the portal with an OTP, or at an <b>MP Online '
                   'kiosk / CSC</b>, where it is reported to be free.',
                   ('stuck',
                    'Name or date of birth differs between Samagra and Aadhaar? Correct it first, or eKYC will fail.')),
                  ('gov',
                   'Changes are verified',
                   'बदलाव सत्यापित होते हैं',
                   'Adding a member, splitting a family or correcting details is verified by the Panchayat or ward '
                   'office.',
                   ('stuck',
                    'Request pending for weeks? Ask the Panchayat secretary or ward office with the request number.')),
                  ('done',
                   'Samagra ready for schemes',
                   'योजनाओं के लिए समग्र तैयार',
                   'With eKYC done, your member ID works for certificates, ration, pensions, Ladli Behna and '
                   'scholarships.',
                   None)],
        'rights_t': 'Stuck on Samagra? Complain.',
        'rights': 'Write to the <b>Janpad / ward office</b>, or complain on the <b>CM Helpline 181</b> with your '
                  'Samagra and request numbers.',
        'help': '<b>Portal:</b> samagra.gov.in · eKYC at MP Online kiosks and CSCs (reported free)<br><b>Never pay for '
                'Samagra registration</b> · <b>Use only official websites</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'समग्र आईडी: मध्य प्रदेश की लगभग हर योजना की पारिवारिक पहचान',
        'sub': None,
        'benefit': 'एक परिवार आईडी और सदस्य आईडी, पेंशन, राशन, लाड़ली बहना, प्रमाण पत्र और छात्रवृत्ति के लिए',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'समग्र तैयार'],
        'phases': ['खोजें या बनवाएं', 'सही रखें'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पता करें कि पहले से है या नहीं',
                   None,
                   'ज़्यादातर परिवार सर्वे में पंजीकृत हो चुके हैं। <b>samagra.gov.in</b> पर नाम, मोबाइल या आधार से '
                   'खोजें। <b>परिवार आईडी</b> 8 अंकों की और हर <b>सदस्य आईडी</b> 9 अंकों की होती है (बताए अनुसार)।',
                   ('tip', 'योजनाएं आमतौर पर परिवार आईडी नहीं, <b>सदस्य</b> आईडी मांगती हैं।')),
                  ('you',
                   'नया परिवार या मप्र में आए हैं?',
                   None,
                   'नई परिवार आईडी के लिए अपनी <b>ग्राम पंचायत</b>, <b>जनपद</b> या <b>नगरीय वार्ड कार्यालय</b> में, या '
                   'पोर्टल के नए परिवार विकल्प से आवेदन करें। सभी सदस्यों का आधार और पते का प्रमाण साथ रखें।',
                   None),
                  ('you',
                   'हर सदस्य का ई-केवाईसी करें',
                   None,
                   'समग्र ई-केवाईसी हर सदस्य को आधार से जोड़ता है। पोर्टल पर ओटीपी से, या <b>एमपी ऑनलाइन कियोस्क / '
                   'सीएससी</b> पर करें, जहां बताए अनुसार यह मुफ़्त है।',
                   ('stuck', 'समग्र और आधार में नाम या जन्मतिथि अलग है? पहले सुधार कराएं, वरना ई-केवाईसी नहीं होगा।')),
                  ('gov',
                   'बदलाव सत्यापित होते हैं',
                   None,
                   'सदस्य जोड़ना, परिवार अलग करना या विवरण सुधारना पंचायत या वार्ड कार्यालय सत्यापित करता है।',
                   ('stuck', 'हफ़्तों से अनुरोध लंबित? अनुरोध संख्या के साथ पंचायत सचिव या वार्ड कार्यालय से पूछें।')),
                  ('done',
                   'योजनाओं के लिए समग्र तैयार',
                   None,
                   'ई-केवाईसी होने पर आपकी सदस्य आईडी प्रमाण पत्र, राशन, पेंशन, लाड़ली बहना और छात्रवृत्ति के लिए काम '
                   'करती है।',
                   None)],
        'rights_t': 'समग्र में अटके? शिकायत करें।',
        'rights': 'समग्र और अनुरोध संख्या के साथ <b>जनपद / वार्ड कार्यालय</b> को लिखें, या <b>सीएम हेल्पलाइन 181</b> '
                  'पर शिकायत करें।',
        'help': '<b>पोर्टल:</b> samagra.gov.in · ई-केवाईसी एमपी ऑनलाइन कियोस्क और सीएससी पर (बताए अनुसार '
                'मुफ़्त)<br><b>समग्र पंजीकरण के लिए कभी पैसे न दें</b> · <b>केवल आधिकारिक वेबसाइट का उपयोग करें</b>'}}
