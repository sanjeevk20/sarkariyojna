"""PM-KISAN (Uttar Pradesh) guide content (EN + HI)."""

OUT = "up-pm-kisan-guide"
PHASE_BREAK = 5

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'PM-KISAN in UP: How to get ₹6,000 a year',
        'sub': 'पीएम-किसान (उत्तर प्रदेश): वर्ष में ₹6,000 कैसे पाएं',
        'benefit': '₹2,000 into your bank account, three times a year',
        'legend': ['You do this', 'Government does this (you wait)', 'Money received'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you can get it',
                   'पात्रता जांचें',
                   'Your name must be in the <b>khatauni</b> as a landholder. You <b>cannot</b> get it if someone in '
                   'the family pays income tax, holds a government job, or is a practising doctor, lawyer, CA or '
                   'engineer.',
                   ('stuck',
                    "Land still in a parent's name? Get <b>varasat</b> or <b>dakhil-kharij</b> done first. See the "
                    '<b>Dakhil-kharij (UP)</b> guide.')),
                  ('you',
                   'Get your Farmer ID',
                   'फार्मर आईडी बनवाएं',
                   'UP is enrolling farmers in the <b>Farmer Registry</b> through camps at the <b>Gram '
                   'Sachivalaya</b>, with the Lekhpal and Panchayat Sachiv. Take Aadhaar, khatauni and your mobile.',
                   ('tip', 'Without a Farmer ID, future instalments and other farm schemes can stop.')),
                  ('you',
                   'Keep these papers ready',
                   'कागज़ तैयार रखें',
                   '<ul><li>Khatauni</li><li>Aadhaar</li><li>Bank passbook (account <b>linked to '
                   'Aadhaar</b>)</li><li>Mobile number linked to Aadhaar</li></ul>',
                   None),
                  ('you',
                   'Register',
                   'पंजीकरण करें',
                   'Register on <b>pmkisan.gov.in</b> (New Farmer Registration) or at a Jan Seva Kendra. Note your '
                   '<b>registration number</b>.',
                   None),
                  ('gov',
                   'Land verification',
                   'भूमि सत्यापन',
                   'The Lekhpal / tehsil checks your name against the khatauni and the state approves you.',
                   ('stuck',
                    'Name spelling differs between Aadhaar, khatauni and bank? Correct it, then ask the Lekhpal to '
                    're-verify.')),
                  ('you',
                   'Do eKYC',
                   'ई-केवाईसी करें',
                   'Complete eKYC by OTP on pmkisan.gov.in, face authentication in the PM-KISAN app, or fingerprint at '
                   'a Jan Seva Kendra.',
                   ('stuck', 'Without eKYC, payments <b>stop</b>.')),
                  ('gov',
                   'Payment processed',
                   'भुगतान प्रक्रिया',
                   'Status shows <span class="status">RFT signed by State Govt</span>, then <span class="status">FTO '
                   'generated</span>. Just wait.',
                   None),
                  ('done',
                   '₹2,000 in your account',
                   'खाते में ₹2,000',
                   'You get an SMS. This repeats every four months while eKYC, land seeding and bank linking stay '
                   'correct.',
                   None)],
        'rights_t': 'Instalment missing? Complain.',
        'rights': 'Check status on pmkisan.gov.in, then contact the <b>district agriculture office</b> or the PM-KISAN '
                  'helpline <b>155261 / 011-24300606</b>. You can also use <b>IGRS Jansunwai</b>.',
        'help': '<b>Register / status:</b> pmkisan.gov.in · <b>Helpline:</b> 155261 / 011-24300606 · Farmer ID camps '
                'at Gram Sachivalaya<br><b>Use only official websites</b> · <b>Never pay an agent</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'उत्तर प्रदेश में पीएम-किसान: वर्ष में ₹6,000 कैसे पाएं',
        'sub': None,
        'benefit': 'साल में तीन बार ₹2,000 सीधे बैंक खाते में',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'राशि मिली'],
        'phases': ['आवेदन से पहले', 'आवेदन के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   '<b>खतौनी</b> में भूमिधर के रूप में आपका नाम होना चाहिए। परिवार में कोई आयकर देता हो, सरकारी नौकरी '
                   'में हो, या प्रैक्टिस करने वाला डॉक्टर, वकील, सीए या इंजीनियर हो तो लाभ <b>नहीं</b> मिलेगा।',
                   ('stuck',
                    'ज़मीन अभी माता-पिता के नाम? पहले <b>वरासत</b> या <b>दाखिल-खारिज</b> कराएं। <b>दाखिल-खारिज '
                    '(यूपी)</b> मार्गदर्शिका देखें।')),
                  ('you',
                   'फार्मर आईडी बनवाएं',
                   None,
                   'उत्तर प्रदेश में <b>ग्राम सचिवालय</b> पर शिविर लगाकर लेखपाल और पंचायत सचिव के साथ <b>फार्मर '
                   'रजिस्ट्री</b> हो रही है। आधार, खतौनी और मोबाइल साथ ले जाएं।',
                   ('tip', 'फार्मर आईडी के बिना आगे की किस्तें और अन्य कृषि योजनाएं रुक सकती हैं।')),
                  ('you',
                   'कागज़ तैयार रखें',
                   None,
                   '<ul><li>खतौनी</li><li>आधार</li><li>बैंक पासबुक (खाता <b>आधार से जुड़ा</b>)</li><li>आधार से जुड़ा '
                   'मोबाइल नंबर</li></ul>',
                   None),
                  ('you',
                   'पंजीकरण करें',
                   None,
                   '<b>pmkisan.gov.in</b> पर (New Farmer Registration) या जन सेवा केंद्र से पंजीकरण करें। <b>पंजीकरण '
                   'संख्या</b> लिख लें।',
                   None),
                  ('gov',
                   'भूमि सत्यापन',
                   None,
                   'लेखपाल / तहसील खतौनी से आपका नाम मिलाते हैं और राज्य स्वीकृति देता है।',
                   ('stuck',
                    'आधार, खतौनी और बैंक में नाम की वर्तनी अलग है? सुधार कराएं, फिर लेखपाल से दोबारा सत्यापन कराएं।')),
                  ('you',
                   'ई-केवाईसी करें',
                   None,
                   'pmkisan.gov.in पर ओटीपी से, पीएम-किसान ऐप में चेहरा प्रमाणीकरण से, या जन सेवा केंद्र पर अंगूठे से '
                   'ई-केवाईसी करें।',
                   ('stuck', 'ई-केवाईसी के बिना भुगतान <b>रुक जाता है</b>।')),
                  ('gov',
                   'भुगतान प्रक्रिया',
                   None,
                   'स्थिति में <span class="status">RFT signed by State Govt</span>, फिर <span class="status">FTO '
                   'generated</span> दिखता है। बस इंतज़ार करें।',
                   None),
                  ('done',
                   'खाते में ₹2,000',
                   None,
                   'आपको SMS आता है। ई-केवाईसी, भूमि सीडिंग और बैंक लिंक सही रहने तक यह हर चार महीने मिलता है।',
                   None)],
        'rights_t': 'किस्त नहीं आई? शिकायत करें।',
        'rights': 'pmkisan.gov.in पर स्थिति देखें, फिर <b>ज़िला कृषि कार्यालय</b> या पीएम-किसान हेल्पलाइन <b>155261 / '
                  '011-24300606</b> पर संपर्क करें। <b>आईजीआरएस जनसुनवाई</b> का भी उपयोग कर सकते हैं।',
        'help': '<b>पंजीकरण / स्थिति:</b> pmkisan.gov.in · <b>हेल्पलाइन:</b> 155261 / 011-24300606 · ग्राम सचिवालय पर '
                'फार्मर आईडी शिविर<br><b>केवल आधिकारिक वेबसाइट का उपयोग करें</b> · <b>एजेंट को पैसे न दें</b>'}}
