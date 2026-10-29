"""Land mutation / Namantaran (Rajasthan) guide content (EN + HI)."""

OUT = "rj-land-mutation-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Namantaran: get land into your name in Rajasthan',
        'sub': 'नामांतरण: ज़मीन अपने नाम कराएं',
        'benefit': 'Your name in the jamabandi (record of rights), needed for PM-KISAN, crop loans, insurance and '
                   'selling the land',
        'legend': ['You do this', 'Government does this (you wait)', 'Name in jamabandi'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Know when you need it',
                   'जानें कब ज़रूरी है',
                   'After a <b>sale, gift, inheritance (death of the holder)</b> or partition, the land is not yours '
                   'on paper until namantaran is done.',
                   None),
                  ('you',
                   'Keep these ready',
                   'ये तैयार रखें',
                   '<ul><li>Registered sale / gift deed, or death certificate and list of heirs</li><li>Current '
                   '<b>jamabandi copy</b> (from Apna Khata)</li><li>Jan Aadhaar and Aadhaar of applicants</li></ul>',
                   ('tip',
                    "Almost every Rajasthan service now starts from your family's <b>Jan Aadhaar</b>. Names must match "
                    'Aadhaar. No Jan Aadhaar yet? See the <b>Jan Aadhaar</b> guide first.')),
                  ('you',
                   'Apply online or at the tehsil',
                   'ऑनलाइन या तहसील में आवेदन करें',
                   'Apply on <b>Apna Khata / e-Dharti</b> (apnakhata.rajasthan.gov.in) through e-Mitra, or give an '
                   'application to the Patwari / tehsil. Keep the <b>application or mutation number</b>.',
                   ('tip',
                    'After a registered sale the registration office often starts the mutation itself. Ask for the '
                    'mutation number at the sub-registrar.')),
                  ('gov',
                   'Patwari report and public notice',
                   'पटवारी रिपोर्ट और सार्वजनिक सूचना',
                   'The Patwari checks on the ground and a <b>notice</b> lets co-holders object. The Tehsildar / '
                   'revenue officer then decides.',
                   ('stuck',
                    "Patwari asking for money to 'start' or 'pass' the file? That is a bribe. Report it to the ACB "
                    'helpline 1064 before paying anything.')),
                  ('gov',
                   'Order and jamabandi update',
                   'आदेश और जमाबंदी अपडेट',
                   'The officer approves the mutation and the jamabandi is updated online.',
                   ('stuck', 'Rejected or objected? Ask for the written order; you can appeal to the SDM.')),
                  ('done',
                   'Check your name online',
                   'ऑनलाइन नाम जांचें',
                   'Search your khasra / khata on <b>Apna Khata</b> and download the new jamabandi copy.',
                   ('tip', "Now update PM-KISAN land details and your bank's crop-loan record."))],
        'rights_t': 'Taking too long? Use your rights.',
        'rights': 'Ask the tehsil for the mutation status in writing, then complain on <b>Rajasthan Sampark 181</b> '
                  'with the mutation number. Bribe demand: <b>ACB helpline 1064</b>.',
        'help': '<b>Records / status:</b> apnakhata.rajasthan.gov.in · <b>Complaints:</b> Sampark 181 · <b>Bribe '
                'demand:</b> ACB 1064<br>Fees and timelines vary by case; check the portal'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'नामांतरण: राजस्थान में ज़मीन अपने नाम कराएं',
        'sub': None,
        'benefit': 'जमाबंदी में आपका नाम, जो पीएम-किसान, फ़सल ऋण, बीमा और ज़मीन बेचने के लिए ज़रूरी है',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'जमाबंदी में नाम'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'जानें कब ज़रूरी है',
                   None,
                   '<b>खरीद, दान (गिफ़्ट), विरासत (खातेदार की मृत्यु)</b> या बंटवारे के बाद, नामांतरण होने तक ज़मीन '
                   'कागज़ पर आपकी नहीं होती।',
                   None),
                  ('you',
                   'ये तैयार रखें',
                   None,
                   '<ul><li>पंजीकृत बैनामा / दानपत्र, या मृत्यु प्रमाण पत्र और वारिसों की सूची</li><li>ताज़ा '
                   '<b>जमाबंदी नकल</b> (अपना खाता से)</li><li>आवेदकों का जन आधार और आधार</li></ul>',
                   ('tip',
                    'राजस्थान की लगभग हर सेवा अब परिवार के <b>जन आधार</b> से शुरू होती है। नाम आधार से मेल खाने चाहिए। '
                    'जन आधार नहीं है? पहले <b>जन आधार</b> मार्गदर्शिका देखें।')),
                  ('you',
                   'ऑनलाइन या तहसील में आवेदन करें',
                   None,
                   'ई-मित्र के ज़रिए <b>अपना खाता / ई-धरती</b> (apnakhata.rajasthan.gov.in) पर आवेदन करें, या पटवारी / '
                   'तहसील में आवेदन दें। <b>आवेदन या नामांतरण संख्या</b> संभाल कर रखें।',
                   ('tip',
                    'पंजीकृत खरीद के बाद उप-पंजीयक कार्यालय अक्सर नामांतरण खुद शुरू कर देता है। वहीं नामांतरण संख्या '
                    'पूछें।')),
                  ('gov',
                   'पटवारी रिपोर्ट और सार्वजनिक सूचना',
                   None,
                   'पटवारी मौके पर जांच करते हैं और <b>सूचना</b> जारी होती है ताकि सह-खातेदार आपत्ति कर सकें। फिर '
                   'तहसीलदार / राजस्व अधिकारी निर्णय लेते हैं।',
                   ('stuck',
                    "पटवारी फ़ाइल 'शुरू' या 'पास' करने के लिए पैसे मांगें? यह रिश्वत है। कुछ भी देने से पहले एसीबी "
                    'हेल्पलाइन 1064 पर बताएं।')),
                  ('gov',
                   'आदेश और जमाबंदी अपडेट',
                   None,
                   'अधिकारी नामांतरण स्वीकृत करते हैं और जमाबंदी ऑनलाइन अपडेट होती है।',
                   ('stuck', 'अस्वीकृत या आपत्ति? लिखित आदेश मांगें; एसडीएम के पास अपील कर सकते हैं।')),
                  ('done',
                   'ऑनलाइन नाम जांचें',
                   None,
                   '<b>अपना खाता</b> पर अपना खसरा / खाता खोजें और नई जमाबंदी नकल डाउनलोड करें।',
                   ('tip', 'अब पीएम-किसान में ज़मीन का विवरण और बैंक का फ़सल ऋण रिकॉर्ड अपडेट कराएं।'))],
        'rights_t': 'बहुत देर हो रही है? अपने अधिकार का उपयोग करें।',
        'rights': 'तहसील से नामांतरण की स्थिति लिखित में मांगें, फिर नामांतरण संख्या के साथ <b>राजस्थान संपर्क 181</b> '
                  'पर शिकायत करें। रिश्वत की मांग: <b>एसीबी हेल्पलाइन 1064</b>।',
        'help': '<b>रिकॉर्ड / स्थिति:</b> apnakhata.rajasthan.gov.in · <b>शिकायत:</b> संपर्क 181 · <b>रिश्वत की '
                'मांग:</b> एसीबी 1064<br>शुल्क और समय मामले के अनुसार; पोर्टल देखें'}}
