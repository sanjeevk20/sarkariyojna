"""Vridhavastha Pension (UP old-age pension) guide content (EN + HI)."""

OUT = "up-old-age-pension-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Old-Age Pension (UP): Monthly pension for seniors',
        'sub': 'वृद्धावस्था पेंशन (उत्तर प्रदेश): बुज़ुर्गों के लिए मासिक पेंशन',
        'benefit': 'About ₹1,000 a month, paid every three months into the bank account',
        'legend': ['You do this', 'Government does this (you wait)', 'Pension received'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you can get it',
                   'पात्रता जांचें',
                   '<ul><li>Age <b>60 or more</b>, living in UP</li><li>Yearly income below about <b>₹46,080 '
                   '(village)</b> or <b>₹56,460 (city)</b></li><li>Not getting any other government pension</li></ul>',
                   None),
                  ('you',
                   'Keep these papers ready',
                   'कागज़ तैयार रखें',
                   '<ul><li>Aadhaar</li><li>Age proof</li><li><b>Income certificate</b></li><li>Bank passbook (account '
                   '<b>linked to Aadhaar</b>)</li><li>Photo</li></ul>',
                   ('tip', 'No income certificate yet? See the <b>Income certificate (UP)</b> guide first.')),
                  ('you',
                   'Apply on the pension portal',
                   'पेंशन पोर्टल पर आवेदन करें',
                   'Apply on <b>sspy-up.gov.in</b> (old-age pension) yourself or through a Jan Seva Kendra. Note the '
                   '<b>registration number</b>.',
                   ('tip', "Applying is <b>free</b>. Do not pay anyone to 'get the pension passed'.")),
                  ('gov',
                   'Verification',
                   'सत्यापन',
                   'In villages the <b>BDO</b> office checks, in towns the <b>SDM</b> office. They may visit your '
                   'home.',
                   ('stuck',
                    'Verification pending for months? Visit the block or tehsil office with your registration '
                    'number.')),
                  ('gov',
                   'District approval',
                   'ज़िले से स्वीकृति',
                   'The <b>District Social Welfare Officer</b> sanctions the pension.',
                   None),
                  ('done',
                   'Pension in your account',
                   'खाते में पेंशन',
                   'Money comes by <b>DBT</b>, usually in instalments every three months. Check status on '
                   'sspy-up.gov.in.',
                   ('stuck',
                    'Payment stopped? Usually the bank account is not Aadhaar-linked, or yearly verification is '
                    'pending. Fix it at the bank, then ask the social welfare office.'))],
        'rights_t': 'Not paid for long? Complain.',
        'rights': 'Complain to the <b>District Social Welfare Officer</b>, on <b>IGRS Jansunwai</b> or the <b>CM '
                  'Helpline 1076</b> with your registration number.',
        'help': '<b>Apply / status:</b> sspy-up.gov.in · Amount and income limits as reported; check the current '
                'notice<br><b>Applying is free</b> · <b>Use only official websites</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'वृद्धावस्था पेंशन (उत्तर प्रदेश): बुज़ुर्गों के लिए मासिक पेंशन',
        'sub': None,
        'benefit': 'लगभग ₹1,000 प्रति माह, हर तीन महीने पर बैंक खाते में',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'पेंशन मिली'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   '<ul><li>उम्र <b>60 वर्ष या अधिक</b>, उत्तर प्रदेश के निवासी</li><li>वार्षिक आय लगभग <b>₹46,080 '
                   '(गांव)</b> या <b>₹56,460 (शहर)</b> से कम</li><li>कोई अन्य सरकारी पेंशन न मिल रही हो</li></ul>',
                   None),
                  ('you',
                   'कागज़ तैयार रखें',
                   None,
                   '<ul><li>आधार</li><li>उम्र का प्रमाण</li><li><b>आय प्रमाण पत्र</b></li><li>बैंक पासबुक (खाता '
                   '<b>आधार से जुड़ा</b>)</li><li>फोटो</li></ul>',
                   ('tip', 'आय प्रमाण पत्र नहीं है? पहले <b>आय प्रमाण पत्र (यूपी)</b> मार्गदर्शिका देखें।')),
                  ('you',
                   'पेंशन पोर्टल पर आवेदन करें',
                   None,
                   '<b>sspy-up.gov.in</b> पर (वृद्धावस्था पेंशन) खुद या जन सेवा केंद्र से आवेदन करें। <b>पंजीकरण '
                   'संख्या</b> लिख लें।',
                   ('tip', "आवेदन <b>मुफ़्त</b> है। 'पेंशन पास कराने' के लिए किसी को पैसे न दें।")),
                  ('gov',
                   'सत्यापन',
                   None,
                   'गांव में <b>बीडीओ</b> कार्यालय, शहर में <b>एसडीएम</b> कार्यालय जांच करता है। घर आकर भी जांच हो '
                   'सकती है।',
                   ('stuck', 'महीनों से सत्यापन बाकी? पंजीकरण संख्या लेकर ब्लॉक या तहसील कार्यालय जाएं।')),
                  ('gov', 'ज़िले से स्वीकृति', None, '<b>ज़िला समाज कल्याण अधिकारी</b> पेंशन स्वीकृत करते हैं।', None),
                  ('done',
                   'खाते में पेंशन',
                   None,
                   'पैसा <b>डीबीटी</b> से आता है, आमतौर पर हर तीन महीने की किस्त में। स्थिति sspy-up.gov.in पर देखें।',
                   ('stuck',
                    'भुगतान रुक गया? अक्सर खाता आधार से नहीं जुड़ा होता या सालाना सत्यापन बाकी होता है। बैंक में ठीक '
                    'कराएं, फिर समाज कल्याण कार्यालय से पूछें।'))],
        'rights_t': 'लंबे समय से भुगतान नहीं? शिकायत करें।',
        'rights': 'पंजीकरण संख्या के साथ <b>ज़िला समाज कल्याण अधिकारी</b>, <b>आईजीआरएस जनसुनवाई</b> या <b>मुख्यमंत्री '
                  'हेल्पलाइन 1076</b> पर शिकायत करें।',
        'help': '<b>आवेदन / स्थिति:</b> sspy-up.gov.in · राशि और आय सीमा बताए गए अनुसार; वर्तमान सूचना '
                'देखें<br><b>आवेदन मुफ़्त है</b> · <b>केवल आधिकारिक वेबसाइट का उपयोग करें</b>'}}
