"""Kanya Sumangala Yojana guide content (EN + HI)."""

OUT = "up-kanya-sumangala-guide"
PHASE_BREAK = 5

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Kanya Sumangala Yojana: ₹25,000 for your daughter in six stages',
        'sub': 'मुख्यमंत्री कन्या सुमंगला योजना: बेटी के लिए छह चरणों में ₹25,000',
        'benefit': '₹25,000 per girl, paid in six instalments from birth to college',
        'legend': ['You do this', 'Government does this (you wait)', 'Instalment received'],
        'phases': ['Before you apply', 'After you apply (repeat at each stage)'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you can get it',
                   'पात्रता जांचें',
                   '<ul><li>Family living permanently in UP</li><li>Family income up to <b>₹3 lakh a '
                   'year</b></li><li>Usually up to <b>two daughters</b> per family (twins counted '
                   'specially)</li><li>Adopted daughters can also be covered</li></ul>',
                   None),
                  ('you',
                   'Know the six stages',
                   'छह चरण जानें',
                   '<ul><li>Birth: <b>₹5,000</b></li><li>Full vaccination by age 1: <b>₹2,000</b></li><li>Class 1 '
                   'admission: <b>₹3,000</b></li><li>Class 6 admission: <b>₹3,000</b></li><li>Class 9 admission: '
                   '<b>₹5,000</b></li><li>Degree or diploma admission after Class 12: <b>₹7,000</b></li></ul>',
                   ('tip',
                    'Amounts as reported after the increase to ₹25,000. Check the portal for the current split.')),
                  ('you',
                   'Keep these papers ready',
                   'कागज़ तैयार रखें',
                   "<ul><li>Girl's <b>birth certificate</b></li><li>Parent's Aadhaar and photo</li><li>Income "
                   'certificate or self-declaration</li><li>Bank account (Aadhaar-linked)</li><li>Stage proof: '
                   'vaccination card or school admission slip</li></ul>',
                   None),
                  ('you',
                   'Apply on the scheme portal',
                   'योजना पोर्टल पर आवेदन करें',
                   'Register on <b>mksy.up.gov.in</b> (citizen login), choose the stage, upload documents and submit.',
                   ('tip', 'Applying is <b>free</b>. Apply soon after each stage; late applications can be rejected.')),
                  ('gov',
                   'Verification',
                   'सत्यापन',
                   'The <b>BDO</b> (village) or <b>SDM</b> (town) office verifies the application.',
                   ('stuck', 'Sent back for correction? Log in, fix the marked document and resubmit.')),
                  ('gov',
                   'District approval',
                   'ज़िले से स्वीकृति',
                   'The <b>District Probation Officer</b> approves the instalment.',
                   None),
                  ('done',
                   'Money in the account',
                   'खाते में राशि',
                   'The instalment is paid by <b>DBT</b>. Log in again at the next stage to claim the next instalment.',
                   None)],
        'rights_t': 'Instalment stuck? Follow up.',
        'rights': 'Contact the <b>District Probation Officer</b> with your application number, or complain on <b>IGRS '
                  "Jansunwai</b> / <b>CM Helpline 1076</b>. Women's helpline <b>181</b> can guide you.",
        'help': '<b>Apply / status:</b> mksy.up.gov.in · Amounts and rules as reported; check the current '
                'notice<br><b>Applying is free</b> · <b>Use only official websites</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'कन्या सुमंगला योजना: बेटी के लिए छह चरणों में ₹25,000',
        'sub': None,
        'benefit': 'हर बेटी के लिए ₹25,000, जन्म से कॉलेज तक छह किस्तों में',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'किस्त मिली'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद (हर चरण पर दोहराएं)'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   '<ul><li>परिवार स्थायी रूप से उत्तर प्रदेश में रहता हो</li><li>पारिवारिक आय <b>₹3 लाख प्रति '
                   'वर्ष</b> तक</li><li>आमतौर पर एक परिवार की <b>अधिकतम दो बेटियां</b> (जुड़वां के लिए विशेष '
                   'नियम)</li><li>गोद ली गई बेटियां भी शामिल हो सकती हैं</li></ul>',
                   None),
                  ('you',
                   'छह चरण जानें',
                   None,
                   '<ul><li>जन्म पर: <b>₹5,000</b></li><li>एक वर्ष तक पूरा टीकाकरण: <b>₹2,000</b></li><li>कक्षा 1 में '
                   'प्रवेश: <b>₹3,000</b></li><li>कक्षा 6 में प्रवेश: <b>₹3,000</b></li><li>कक्षा 9 में प्रवेश: '
                   '<b>₹5,000</b></li><li>कक्षा 12 के बाद डिग्री या डिप्लोमा में प्रवेश: <b>₹7,000</b></li></ul>',
                   ('tip', 'राशि ₹25,000 किए जाने के बाद बताए गए अनुसार। वर्तमान बंटवारा पोर्टल पर देखें।')),
                  ('you',
                   'कागज़ तैयार रखें',
                   None,
                   '<ul><li>बेटी का <b>जन्म प्रमाण पत्र</b></li><li>माता/पिता का आधार और फोटो</li><li>आय प्रमाण पत्र '
                   'या स्व-घोषणा पत्र</li><li>बैंक खाता (आधार से जुड़ा)</li><li>चरण का प्रमाण: टीकाकरण कार्ड या स्कूल '
                   'प्रवेश पर्ची</li></ul>',
                   None),
                  ('you',
                   'योजना पोर्टल पर आवेदन करें',
                   None,
                   '<b>mksy.up.gov.in</b> पर (सिटिज़न लॉगिन) पंजीकरण करें, चरण चुनें, दस्तावेज़ अपलोड कर आवेदन जमा '
                   'करें।',
                   ('tip',
                    'आवेदन <b>मुफ़्त</b> है। हर चरण के बाद जल्दी आवेदन करें; देर से आवेदन अस्वीकार हो सकता है।')),
                  ('gov',
                   'सत्यापन',
                   None,
                   '<b>बीडीओ</b> (गांव) या <b>एसडीएम</b> (शहर) कार्यालय आवेदन की जांच करता है।',
                   ('stuck', 'सुधार के लिए लौटाया गया? लॉगिन कर चिह्नित दस्तावेज़ ठीक करें और दोबारा जमा करें।')),
                  ('gov', 'ज़िले से स्वीकृति', None, '<b>ज़िला प्रोबेशन अधिकारी</b> किस्त स्वीकृत करते हैं।', None),
                  ('done',
                   'खाते में राशि',
                   None,
                   'किस्त <b>डीबीटी</b> से मिलती है। अगली किस्त के लिए अगले चरण पर फिर लॉगिन करें।',
                   None)],
        'rights_t': 'किस्त अटकी? पाठपुरावा करें।',
        'rights': 'आवेदन संख्या के साथ <b>ज़िला प्रोबेशन अधिकारी</b> से संपर्क करें, या <b>आईजीआरएस जनसुनवाई</b> / '
                  '<b>मुख्यमंत्री हेल्पलाइन 1076</b> पर शिकायत करें। महिला हेल्पलाइन <b>181</b> भी मदद कर सकती है।',
        'help': '<b>आवेदन / स्थिति:</b> mksy.up.gov.in · राशि और नियम बताए गए अनुसार; वर्तमान सूचना देखें<br><b>आवेदन '
                'मुफ़्त है</b> · <b>केवल आधिकारिक वेबसाइट का उपयोग करें</b>'}}
