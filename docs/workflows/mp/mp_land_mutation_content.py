"""Land mutation / naamantaran (MP) guide content (EN + HI)."""

OUT = "mp-land-mutation-guide"
PHASE_BREAK = 3

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Naamantaran (MP): Get your name into the land record',
        'sub': 'नामांतरण (मध्य प्रदेश): भू-अभिलेख में अपना नाम दर्ज कराएं',
        'benefit': 'Your name in the khasra / B-1 record, needed for loans, PM-KISAN, sale and compensation',
        'legend': ['You do this', 'Government does this (you wait)', 'Name recorded'],
        'phases': ['At registration', 'After registration'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Register the deed on Sampada',
                   'संपदा पर रजिस्ट्री कराएं',
                   'Register the sale or gift deed at the sub-registrar office (<b>Sampada 2.0</b>). Make sure khasra '
                   'numbers and names match the land record.',
                   ('tip',
                    'If you buy a <b>whole khasra</b> with no dispute, <b>Cyber Tehsil</b> can do the naamantaran '
                    'automatically, without a tehsil visit.')),
                  ('gov',
                   'Cyber Tehsil or tehsil case',
                   'साइबर तहसील या तहसील प्रकरण',
                   'Sampada sends the deed to the revenue system (RCMS). Whole-khasra, undisputed sales go to <b>Cyber '
                   'Tehsil</b>; part-sales, inheritance and disputed cases become a <b>case before the Tehsildar</b>.',
                   None),
                  ('gov',
                   'Notice for objections',
                   'आपत्ति के लिए सूचना',
                   'A public notice gives others a chance to object before the order.',
                   ('stuck',
                    'Someone objected? The case goes to a hearing before the Tehsildar. Bring the deed and '
                    'witnesses.')),
                  ('gov',
                   'Order passed',
                   'आदेश पारित',
                   'Simple Cyber Tehsil cases are reported to finish in about <b>15 days</b>; tehsil cases take '
                   'longer.',
                   ('stuck',
                    'Nothing after a month? Check the case on RCMS with your registry number, then visit the tehsil.')),
                  ('done',
                   'Your name in the record',
                   'रिकॉर्ड में आपका नाम',
                   'Check the updated khasra / B-1 on the MP land records portal and download a copy.',
                   ('tip',
                    'Inheritance (fauti naamantaran) is always a tehsil case: apply with the death certificate and '
                    "heirs' details."))],
        'rights_t': 'Stuck for weeks? Escalate.',
        'rights': 'Naamantaran is a time-bound service. Ask the <b>Tehsildar</b> for the case status, file a first '
                  'appeal if the limit is crossed, or complain on the <b>CM Helpline 181</b>.',
        'help': '<b>Registration:</b> Sampada 2.0 · <b>Case status:</b> RCMS · <b>Records:</b> MP land records '
                'portal<br><b>Use only official websites</b> · <b>Never pay a tout</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'नामांतरण (मध्य प्रदेश): भू-अभिलेख में अपना नाम दर्ज कराएं',
        'sub': None,
        'benefit': 'खसरा / बी-1 में आपका नाम, जो ऋण, पीएम-किसान, बिक्री और मुआवज़े के लिए ज़रूरी है',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'नाम दर्ज'],
        'phases': ['रजिस्ट्री के समय', 'रजिस्ट्री के बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'संपदा पर रजिस्ट्री कराएं',
                   None,
                   'उप-पंजीयक कार्यालय (<b>संपदा 2.0</b>) पर बिक्री या दान पत्र की रजिस्ट्री कराएं। ध्यान रखें कि खसरा '
                   'नंबर और नाम भू-अभिलेख से मेल खाएं।',
                   ('tip',
                    'अगर आप बिना विवाद का <b>पूरा खसरा</b> खरीदते हैं, तो <b>साइबर तहसील</b> बिना तहसील गए अपने आप '
                    'नामांतरण कर सकती है।')),
                  ('gov',
                   'साइबर तहसील या तहसील प्रकरण',
                   None,
                   'संपदा रजिस्ट्री को राजस्व प्रणाली (आरसीएमएस) में भेजता है। पूरे खसरे की निर्विवाद बिक्री <b>साइबर '
                   'तहसील</b> में जाती है; आंशिक बिक्री, फ़ौती और विवादित मामले <b>तहसीलदार के समक्ष प्रकरण</b> बनते '
                   'हैं।',
                   None),
                  ('gov',
                   'आपत्ति के लिए सूचना',
                   None,
                   'आदेश से पहले सार्वजनिक सूचना से दूसरों को आपत्ति का मौका मिलता है।',
                   ('stuck',
                    'किसी ने आपत्ति की? मामला तहसीलदार के समक्ष सुनवाई में जाएगा। रजिस्ट्री और गवाह साथ लाएं।')),
                  ('gov',
                   'आदेश पारित',
                   None,
                   'साइबर तहसील के सरल मामले बताए अनुसार लगभग <b>15 दिन</b> में पूरे होते हैं; तहसील प्रकरणों में '
                   'ज़्यादा समय लगता है।',
                   ('stuck', 'एक महीने बाद भी कुछ नहीं? रजिस्ट्री नंबर से आरसीएमएस पर प्रकरण देखें, फिर तहसील जाएं।')),
                  ('done',
                   'रिकॉर्ड में आपका नाम',
                   None,
                   'मप्र भू-अभिलेख पोर्टल पर अद्यतन खसरा / बी-1 देखें और कॉपी डाउनलोड करें।',
                   ('tip',
                    'फ़ौती नामांतरण (विरासत) हमेशा तहसील प्रकरण होता है: मृत्यु प्रमाण पत्र और वारिसों के विवरण के साथ '
                    'आवेदन करें।'))],
        'rights_t': 'हफ़्तों से अटके? आगे बढ़ाएं।',
        'rights': 'नामांतरण समय-बद्ध सेवा है। <b>तहसीलदार</b> से प्रकरण की स्थिति पूछें, समय-सीमा निकलने पर प्रथम अपील '
                  'करें, या <b>सीएम हेल्पलाइन 181</b> पर शिकायत करें।',
        'help': '<b>रजिस्ट्री:</b> संपदा 2.0 · <b>प्रकरण स्थिति:</b> आरसीएमएस · <b>रिकॉर्ड:</b> मप्र भू-अभिलेख '
                'पोर्टल<br><b>केवल आधिकारिक वेबसाइट का उपयोग करें</b> · <b>दलाल को पैसे न दें</b>'}}
