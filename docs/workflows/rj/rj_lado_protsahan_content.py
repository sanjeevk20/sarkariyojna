"""Lado Protsahan Yojana (Rajasthan) guide content (EN + HI)."""

OUT = "rj-lado-protsahan-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Lado Protsahan: ₹1.5 lakh for a daughter in Rajasthan',
        'sub': 'लाडो प्रोत्साहन योजना: बेटी के लिए ₹1.5 लाख',
        'benefit': '₹1.5 lakh savings bond paid in 7 instalments by DBT, from birth to graduation (raised from ₹1 lakh '
                   'in 2025)',
        'legend': ['You do this', 'Government does this (you wait)', 'All instalments received'],
        'phases': ['At birth', 'As she grows'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you can get it',
                   'पात्रता जांचें',
                   '<ul><li>Mother is a <b>native of Rajasthan</b></li><li>Girl born in a <b>government or approved '
                   'hospital</b></li><li>Family from an economically weaker group (as reported)</li></ul>',
                   ('tip',
                    'Reported: the older Rajshree Yojana was merged into Lado Protsahan in March 2026. Check with the '
                    'Anganwadi.')),
                  ('you',
                   'Keep these ready',
                   'ये तैयार रखें',
                   "<ul><li>Mother's <b>Jan Aadhaar</b> with the girl added</li><li>Birth certificate and hospital "
                   "discharge papers</li><li>Mother's bank account, Aadhaar-linked</li></ul>",
                   ('tip',
                    "Almost every Rajasthan service now starts from your family's <b>Jan Aadhaar</b>. Names must match "
                    'Aadhaar. No Jan Aadhaar yet? See the <b>Jan Aadhaar</b> guide first.')),
                  ('gov',
                   'Registered at the hospital',
                   'अस्पताल में पंजीकरण',
                   'The bond is registered from the hospital delivery record; ask the hospital or ASHA to confirm.',
                   ('stuck',
                    'No registration at discharge? Ask the Anganwadi worker or the block Women and Child Development '
                    'office.')),
                  ('gov',
                   'First instalments',
                   'पहली किस्तें',
                   '<ul><li>₹2,500 at birth</li><li>₹2,500 on completing vaccinations (about 1 year)</li></ul>',
                   None),
                  ('gov',
                   'School-stage instalments',
                   'पढ़ाई के दौरान किस्तें',
                   '<ul><li>₹4,000 at Class 1 admission</li><li>₹5,000 at Class 6</li><li>₹11,000 at Class '
                   '10</li><li>₹25,000 at Class 12</li></ul>',
                   ('tip',
                    'Since November 2025, girls in recognised private schools also qualify (reported). The school '
                    'updates enrolment.')),
                  ('done',
                   '₹1 lakh after graduation at 21',
                   '21 वर्ष पर स्नातक के बाद ₹1 लाख',
                   'The final ₹1 lakh is paid after graduation at age 21.',
                   ('stuck',
                    'An instalment missing? Ask the school or Anganwadi to check the enrolment record, then complain '
                    'on Sampark 181.'))],
        'rights_t': 'Instalment missing? Complain.',
        'rights': "Complain on <b>Rajasthan Sampark 181</b> with the mother's Jan Aadhaar number, or to the district "
                  '<b>Women and Child Development</b> office.',
        'help': '<b>Help:</b> Anganwadi, ASHA, school · <b>Complaints:</b> Sampark 181<br><b>Registration is free</b> '
                '· Instalments as reported; check with WCD'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'लाडो प्रोत्साहन: राजस्थान में बेटी के लिए ₹1.5 लाख',
        'sub': None,
        'benefit': '₹1.5 लाख का सेविंग बॉन्ड, जन्म से स्नातक तक 7 किस्तों में डीबीटी से (2025 में ₹1 लाख से बढ़ा)',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'सभी किस्तें मिलीं'],
        'phases': ['जन्म के समय', 'बड़ी होने पर'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   '<ul><li>माता <b>राजस्थान की मूल निवासी</b></li><li>बालिका का जन्म <b>सरकारी या मान्यता प्राप्त '
                   'अस्पताल</b> में</li><li>आर्थिक रूप से कमज़ोर परिवार (बताए अनुसार)</li></ul>',
                   ('tip',
                    'बताए अनुसार: पुरानी राजश्री योजना मार्च 2026 में लाडो प्रोत्साहन में मिला दी गई। आंगनवाड़ी से '
                    'पुष्टि करें।')),
                  ('you',
                   'ये तैयार रखें',
                   None,
                   '<ul><li>माता का <b>जन आधार</b>, जिसमें बालिका का नाम जुड़ा हो</li><li>जन्म प्रमाण पत्र और अस्पताल '
                   'के डिस्चार्ज कागज़</li><li>माता का आधार से जुड़ा बैंक खाता</li></ul>',
                   ('tip',
                    'राजस्थान की लगभग हर सेवा अब परिवार के <b>जन आधार</b> से शुरू होती है। नाम आधार से मेल खाने चाहिए। '
                    'जन आधार नहीं है? पहले <b>जन आधार</b> मार्गदर्शिका देखें।')),
                  ('gov',
                   'अस्पताल में पंजीकरण',
                   None,
                   'बॉन्ड अस्पताल के प्रसव रिकॉर्ड से पंजीकृत होता है; अस्पताल या आशा से पुष्टि कराएं।',
                   ('stuck',
                    'डिस्चार्ज पर पंजीकरण नहीं हुआ? आंगनवाड़ी कार्यकर्ता या ब्लॉक महिला एवं बाल विकास कार्यालय से '
                    'पूछें।')),
                  ('gov',
                   'पहली किस्तें',
                   None,
                   '<ul><li>जन्म पर ₹2,500</li><li>टीकाकरण पूरा होने पर (लगभग 1 वर्ष) ₹2,500</li></ul>',
                   None),
                  ('gov',
                   'पढ़ाई के दौरान किस्तें',
                   None,
                   '<ul><li>कक्षा 1 में प्रवेश पर ₹4,000</li><li>कक्षा 6 में ₹5,000</li><li>कक्षा 10 में '
                   '₹11,000</li><li>कक्षा 12 में ₹25,000</li></ul>',
                   ('tip',
                    'नवंबर 2025 से मान्यता प्राप्त निजी स्कूलों की बालिकाएं भी पात्र हैं (बताए अनुसार)। स्कूल नामांकन '
                    'अपडेट करता है।')),
                  ('done',
                   '21 वर्ष पर स्नातक के बाद ₹1 लाख',
                   None,
                   'अंतिम ₹1 लाख 21 वर्ष की आयु में स्नातक के बाद मिलता है।',
                   ('stuck',
                    'कोई किस्त नहीं आई? स्कूल या आंगनवाड़ी से नामांकन रिकॉर्ड जांचने को कहें, फिर संपर्क 181 पर शिकायत '
                    'करें।'))],
        'rights_t': 'किस्त नहीं आई? शिकायत करें।',
        'rights': 'माता की जन आधार संख्या के साथ <b>राजस्थान संपर्क 181</b> पर, या ज़िला <b>महिला एवं बाल विकास</b> '
                  'कार्यालय में शिकायत करें।',
        'help': '<b>सहायता:</b> आंगनवाड़ी, आशा, स्कूल · <b>शिकायत:</b> संपर्क 181<br><b>पंजीकरण मुफ़्त है</b> · '
                'किस्तें बताए अनुसार; WCD से पुष्टि करें'}}
