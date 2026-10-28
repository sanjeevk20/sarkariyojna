"""Ladli Laxmi Yojana (MP) guide content (EN + HI)."""

OUT = "mp-ladli-laxmi-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Ladli Laxmi Yojana: Support for your daughter from school to 21',
        'sub': 'लाड़ली लक्ष्मी योजना: स्कूल से 21 वर्ष तक बेटी के लिए सहायता',
        'benefit': "An assurance certificate of about ₹1.43 lakh in the girl's name, paid in stages",
        'legend': ['You do this', 'Government does this (you wait)', 'Instalment received'],
        'phases': ['Register', 'At each stage'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you can get it',
                   'पात्रता जांचें',
                   '<ul><li>Girl born on or after <b>1 January 2006</b> to an MP family</li><li>Birth '
                   '<b>registered</b> (ideally within a year)</li><li>Parents not income-tax payers; family limits '
                   'apply (usually up to two daughters)</li></ul>',
                   None),
                  ('you',
                   'Register the girl',
                   'बेटी का पंजीकरण करें',
                   'Register on <b>ladlilaxmi.mp.gov.in</b>, at your <b>Anganwadi</b> centre, or at a Lok Seva Kendra. '
                   'The girl and the family need a <b>Samagra ID with eKYC</b>.',
                   ('tip',
                    'Registration is <b>free</b>. Keep the registration number and the printed assurance certificate '
                    'safe.')),
                  ('gov',
                   'Approval and certificate',
                   'स्वीकृति और प्रमाण पत्र',
                   'The Women and Child Development department checks the application and issues the <b>assurance '
                   "certificate</b> in the girl's name.",
                   ('stuck',
                    'Pending for months? Ask the Anganwadi supervisor or the project office (CDPO) with the '
                    'registration number.')),
                  ('you',
                   'At each school stage, keep records updated',
                   'हर स्कूल चरण पर रिकॉर्ड अपडेट रखें',
                   'Stage payments are linked to <b>admission in Class 6, 9, 11 and 12</b>. Make sure the school '
                   'enters her admission and her bank account is ready.',
                   ('tip',
                    'Exact stage amounts differ between sources and changed under Ladli Laxmi 2.0. Check the current '
                    'table on the portal.')),
                  ('done',
                   'Stage money and final amount',
                   'चरण राशि और अंतिम राशि',
                   'Stage amounts reach her account by DBT. The final amount is paid after age 21 if she is unmarried '
                   'until 18 and meets the study conditions.',
                   ('stuck',
                    'Stage payment missing? Check that the school admission is recorded and Samagra eKYC is done; then '
                    'contact the CDPO.'))],
        'rights_t': 'Payment stuck? Complain.',
        'rights': "Contact the <b>Anganwadi supervisor / CDPO</b>, the women's helpline <b>181</b>, or the <b>CM "
                  'Helpline 181</b> with the registration number.',
        'help': '<b>Register / status:</b> ladlilaxmi.mp.gov.in, Anganwadi, Lok Seva Kendra · Amounts and conditions '
                'as reported; check the portal<br><b>Registration is free</b> · <b>Use only official websites</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'लाड़ली लक्ष्मी योजना: स्कूल से 21 वर्ष तक बेटी के लिए सहायता',
        'sub': None,
        'benefit': 'बेटी के नाम लगभग ₹1.43 लाख का आश्वासन प्रमाण पत्र, चरणों में भुगतान',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'किस्त मिली'],
        'phases': ['पंजीकरण', 'हर चरण पर'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   '<ul><li><b>1 जनवरी 2006</b> या उसके बाद जन्मी, मध्य प्रदेश के परिवार की बेटी</li><li>जन्म '
                   '<b>पंजीकृत</b> हो (बेहतर हो एक वर्ष के भीतर)</li><li>माता-पिता आयकरदाता न हों; परिवार की सीमा लागू '
                   '(आमतौर पर अधिकतम दो बेटियां)</li></ul>',
                   None),
                  ('you',
                   'बेटी का पंजीकरण करें',
                   None,
                   '<b>ladlilaxmi.mp.gov.in</b> पर, अपने <b>आंगनवाड़ी</b> केंद्र या लोक सेवा केंद्र पर पंजीकरण करें। '
                   'बेटी और परिवार की <b>ई-केवाईसी वाली समग्र आईडी</b> होनी चाहिए।',
                   ('tip', 'पंजीकरण <b>मुफ़्त</b> है। पंजीकरण संख्या और छपा हुआ आश्वासन प्रमाण पत्र संभाल कर रखें।')),
                  ('gov',
                   'स्वीकृति और प्रमाण पत्र',
                   None,
                   'महिला एवं बाल विकास विभाग आवेदन जांचकर बेटी के नाम <b>आश्वासन प्रमाण पत्र</b> जारी करता है।',
                   ('stuck',
                    'महीनों से लंबित? पंजीकरण संख्या के साथ आंगनवाड़ी पर्यवेक्षक या परियोजना कार्यालय (सीडीपीओ) से '
                    'पूछें।')),
                  ('you',
                   'हर स्कूल चरण पर रिकॉर्ड अपडेट रखें',
                   None,
                   'चरण भुगतान <b>कक्षा 6, 9, 11 और 12 में प्रवेश</b> से जुड़े हैं। ध्यान रखें कि स्कूल उसका प्रवेश '
                   'दर्ज करे और उसका बैंक खाता तैयार हो।',
                   ('tip',
                    'चरण राशियां स्रोतों में अलग हैं और लाड़ली लक्ष्मी 2.0 में बदली हैं। वर्तमान तालिका पोर्टल पर '
                    'देखें।')),
                  ('done',
                   'चरण राशि और अंतिम राशि',
                   None,
                   'चरण राशि डीबीटी से उसके खाते में आती है। अंतिम राशि 21 वर्ष के बाद मिलती है, अगर 18 वर्ष तक विवाह '
                   'न हुआ हो और पढ़ाई की शर्तें पूरी हों।',
                   ('stuck',
                    'चरण भुगतान नहीं आया? जांचें कि स्कूल प्रवेश दर्ज है और समग्र ई-केवाईसी हुआ है; फिर सीडीपीओ से '
                    'संपर्क करें।'))],
        'rights_t': 'भुगतान अटका? शिकायत करें।',
        'rights': 'पंजीकरण संख्या के साथ <b>आंगनवाड़ी पर्यवेक्षक / सीडीपीओ</b>, महिला हेल्पलाइन <b>181</b> या <b>सीएम '
                  'हेल्पलाइन 181</b> से संपर्क करें।',
        'help': '<b>पंजीकरण / स्थिति:</b> ladlilaxmi.mp.gov.in, आंगनवाड़ी, लोक सेवा केंद्र · राशि और शर्तें बताए '
                'अनुसार; पोर्टल देखें<br><b>पंजीकरण मुफ़्त है</b> · <b>केवल आधिकारिक वेबसाइट का उपयोग करें</b>'}}
