"""Caste and income certificate (Karnataka) guide content (EN + KN)."""

OUT = "ka-caste-income-certificate-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Caste and Income Certificate (Karnataka): Get it from Nadakacheri',
        'sub': 'ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರ: ನಾಡಕಚೇರಿಯಿಂದ ಪಡೆಯಿರಿ',
        'benefit': 'Needed for scholarships, reservation, fee concessions and most welfare schemes',
        'legend': ['You do this', 'Government does this (you wait)', 'Certificate ready'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Know where to apply',
                   'ಎಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಬೇಕು',
                   'Apply through <b>Nadakacheri</b> (Atalji Janasnehi Kendra): online on '
                   '<b>nadakacheri.karnataka.gov.in</b>, or at a Nadakacheri, <b>Grama One</b> or <b>Karnataka One</b> '
                   'centre.',
                   ('tip',
                    'Students usually need a combined <b>caste and income</b> certificate. Ask your college which form '
                    'it needs.')),
                  ('you',
                   'Keep these papers ready',
                   'ದಾಖಲೆಗಳನ್ನು ಸಿದ್ಧವಾಗಿಡಿ',
                   '<ul><li>Aadhaar</li><li>Ration card or other address proof</li><li>Income proof (salary slip, or a '
                   "self-declaration for farmers and daily-wage workers)</li><li>A family member's caste certificate, "
                   'if any</li><li>Registered mobile number</li></ul>',
                   None),
                  ('you',
                   'Submit and pay the fee',
                   'ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ಶುಲ್ಕ ಪಾವತಿಸಿ',
                   'Submit the form and pay the small fee. Keep the <b>application number</b>.',
                   ('tip', 'Reported fee: about <b>₹15</b> for an income certificate. Do not pay agents more.')),
                  ('gov',
                   'Village Accountant and Revenue Inspector check',
                   'ಗ್ರಾಮ ಲೆಕ್ಕಾಧಿಕಾರಿ ಮತ್ತು ಕಂದಾಯ ನಿರೀಕ್ಷಕರ ಪರಿಶೀಲನೆ',
                   'The <b>Village Accountant</b> and <b>Revenue Inspector</b> verify your caste, residence and income '
                   'and report to the taluk office.',
                   ('stuck',
                    'Report stuck? Meet the Village Accountant with your application number. Income written wrongly? '
                    'Ask for re-verification before it is signed.')),
                  ('gov',
                   'Taluk office signs',
                   'ತಾಲೂಕು ಕಚೇರಿಯಿಂದ ಸಹಿ',
                   'The <b>Deputy Tahsildar / Tahsildar</b> approves and the certificate is <b>digitally signed</b> '
                   'with an <b>RD number</b>.',
                   None),
                  ('done',
                   'Download or collect it',
                   'ಡೌನ್\u200cಲೋಡ್ ಮಾಡಿ ಅಥವಾ ಪಡೆಯಿರಿ',
                   'Download it with your application number, or collect it at the centre. Anyone can verify it online '
                   'with the <b>RD number</b>.',
                   ('tip',
                    'Income certificates are reported to be valid for <b>12 months</b>. Scholarships ask for the RD '
                    'number, so note it down.'))],
        'rights_t': 'Taking too long? Complain.',
        'rights': 'Certificates have time limits under <b>Sakala</b>. If yours is crossed, complain on <b>IPGRS</b> '
                  '(ipgrs.karnataka.gov.in) or at the taluk office with your application number.',
        'help': '<b>Apply / status:</b> nadakacheri.karnataka.gov.in, Grama One, Karnataka One · <b>Complaints:</b> '
                'ipgrs.karnataka.gov.in<br><b>Use only official websites</b> · <b>Never pay a tout</b>'},
 'kn': {'lang': 'kn',
        'font': "'Noto Sans Kannada','Noto Sans','FreeSans',sans-serif",
        'h1': 'ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರ (ಕರ್ನಾಟಕ): ನಾಡಕಚೇರಿಯಿಂದ ಪಡೆಯಿರಿ',
        'sub': None,
        'benefit': 'ವಿದ್ಯಾರ್ಥಿ ವೇತನ, ಮೀಸಲಾತಿ, ಶುಲ್ಕ ರಿಯಾಯಿತಿ ಮತ್ತು ಹೆಚ್ಚಿನ ಕಲ್ಯಾಣ ಯೋಜನೆಗಳಿಗೆ ಅಗತ್ಯ',
        'legend': ['ಇದನ್ನು ನೀವು ಮಾಡಿ', 'ಇದನ್ನು ಸರ್ಕಾರ ಮಾಡುತ್ತದೆ (ನೀವು ಕಾಯಿರಿ)', 'ಪ್ರಮಾಣ ಪತ್ರ ಸಿದ್ಧ'],
        'phases': ['ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮೊದಲು', 'ಅರ್ಜಿ ಸಲ್ಲಿಸಿದ ನಂತರ'],
        'who': {'you': 'ನೀವು', 'gov': 'ಸರ್ಕಾರ', 'done': 'ಪೂರ್ಣ'},
        'stuck': 'ತೊಂದರೆಯೇ?',
        'tip': 'ಸಲಹೆ:',
        'steps': [('you',
                   'ಎಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಬೇಕು',
                   None,
                   '<b>ನಾಡಕಚೇರಿ</b> (ಅಟಲ್\u200cಜೀ ಜನಸ್ನೇಹಿ ಕೇಂದ್ರ) ಮೂಲಕ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ: '
                   '<b>nadakacheri.karnataka.gov.in</b> ನಲ್ಲಿ ಆನ್\u200cಲೈನ್, ಅಥವಾ ನಾಡಕಚೇರಿ, <b>ಗ್ರಾಮ ಒನ್</b> ಅಥವಾ '
                   '<b>ಕರ್ನಾಟಕ ಒನ್</b> ಕೇಂದ್ರದಲ್ಲಿ.',
                   ('tip',
                    'ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಸಾಮಾನ್ಯವಾಗಿ <b>ಜಾತಿ ಮತ್ತು ಆದಾಯ</b> ಸೇರಿದ ಪ್ರಮಾಣ ಪತ್ರ ಬೇಕು. ಯಾವ ನಮೂನೆ ಬೇಕು ಎಂದು '
                    'ನಿಮ್ಮ ಕಾಲೇಜಿನಲ್ಲಿ ಕೇಳಿ.')),
                  ('you',
                   'ದಾಖಲೆಗಳನ್ನು ಸಿದ್ಧವಾಗಿಡಿ',
                   None,
                   '<ul><li>ಆಧಾರ್</li><li>ಪಡಿತರ ಚೀಟಿ ಅಥವಾ ಇತರ ವಿಳಾಸದ ಪುರಾವೆ</li><li>ಆದಾಯದ ಪುರಾವೆ (ಸಂಬಳ ಚೀಟಿ, ಅಥವಾ '
                   'ರೈತರು ಮತ್ತು ದಿನಗೂಲಿ ಕಾರ್ಮಿಕರಿಗೆ ಸ್ವಯಂ ಘೋಷಣೆ)</li><li>ಕುಟುಂಬದ ಸದಸ್ಯರ ಜಾತಿ ಪ್ರಮಾಣ ಪತ್ರ, '
                   'ಇದ್ದರೆ</li><li>ನೋಂದಾಯಿತ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ</li></ul>',
                   None),
                  ('you',
                   'ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ಶುಲ್ಕ ಪಾವತಿಸಿ',
                   None,
                   'ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ಸಣ್ಣ ಶುಲ್ಕ ಪಾವತಿಸಿ. <b>ಅರ್ಜಿ ಸಂಖ್ಯೆಯನ್ನು</b> ಜೋಪಾನವಾಗಿಡಿ.',
                   ('tip', 'ವರದಿಯಾದ ಶುಲ್ಕ: ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರಕ್ಕೆ ಸುಮಾರು <b>₹15</b>. ಮಧ್ಯವರ್ತಿಗಳಿಗೆ ಹೆಚ್ಚು ಹಣ ಕೊಡಬೇಡಿ.')),
                  ('gov',
                   'ಗ್ರಾಮ ಲೆಕ್ಕಾಧಿಕಾರಿ ಮತ್ತು ಕಂದಾಯ ನಿರೀಕ್ಷಕರ ಪರಿಶೀಲನೆ',
                   None,
                   '<b>ಗ್ರಾಮ ಲೆಕ್ಕಾಧಿಕಾರಿ</b> ಮತ್ತು <b>ಕಂದಾಯ ನಿರೀಕ್ಷಕರು</b> ನಿಮ್ಮ ಜಾತಿ, ವಾಸ ಮತ್ತು ಆದಾಯವನ್ನು ಪರಿಶೀಲಿಸಿ '
                   'ತಾಲೂಕು ಕಚೇರಿಗೆ ವರದಿ ನೀಡುತ್ತಾರೆ.',
                   ('stuck',
                    'ವರದಿ ತಡವಾಗಿದೆಯೇ? ಅರ್ಜಿ ಸಂಖ್ಯೆಯೊಂದಿಗೆ ಗ್ರಾಮ ಲೆಕ್ಕಾಧಿಕಾರಿಯನ್ನು ಭೇಟಿ ಮಾಡಿ. ಆದಾಯ ತಪ್ಪಾಗಿ ಬರೆದಿದೆಯೇ? '
                    'ಸಹಿ ಆಗುವ ಮೊದಲು ಮರುಪರಿಶೀಲನೆ ಕೇಳಿ.')),
                  ('gov',
                   'ತಾಲೂಕು ಕಚೇರಿಯಿಂದ ಸಹಿ',
                   None,
                   '<b>ಉಪ ತಹಶೀಲ್ದಾರ್ / ತಹಶೀಲ್ದಾರ್</b> ಅನುಮೋದಿಸುತ್ತಾರೆ ಮತ್ತು ಪ್ರಮಾಣ ಪತ್ರಕ್ಕೆ <b>RD ಸಂಖ್ಯೆ</b>ಯೊಂದಿಗೆ '
                   '<b>ಡಿಜಿಟಲ್ ಸಹಿ</b> ಆಗುತ್ತದೆ.',
                   None),
                  ('done',
                   'ಡೌನ್\u200cಲೋಡ್ ಮಾಡಿ ಅಥವಾ ಪಡೆಯಿರಿ',
                   None,
                   'ಅರ್ಜಿ ಸಂಖ್ಯೆಯಿಂದ ಡೌನ್\u200cಲೋಡ್ ಮಾಡಿ, ಅಥವಾ ಕೇಂದ್ರದಲ್ಲಿ ಪಡೆಯಿರಿ. <b>RD ಸಂಖ್ಯೆ</b>ಯಿಂದ ಯಾರಾದರೂ '
                   'ಆನ್\u200cಲೈನ್\u200cನಲ್ಲಿ ಪರಿಶೀಲಿಸಬಹುದು.',
                   ('tip',
                    'ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರ <b>12 ತಿಂಗಳು</b> ಮಾನ್ಯ ಎಂದು ವರದಿಯಾಗಿದೆ. ವಿದ್ಯಾರ್ಥಿ ವೇತನಕ್ಕೆ RD ಸಂಖ್ಯೆ '
                    'ಕೇಳುತ್ತಾರೆ, ಅದನ್ನು ಬರೆದಿಡಿ.'))],
        'rights_t': 'ತುಂಬಾ ತಡವಾಗುತ್ತಿದೆಯೇ? ದೂರು ನೀಡಿ.',
        'rights': '<b>ಸಕಾಲ</b> ಅಡಿಯಲ್ಲಿ ಪ್ರಮಾಣ ಪತ್ರಗಳಿಗೆ ಸಮಯ ಮಿತಿ ಇದೆ. ಅದು ಮೀರಿದರೆ ಅರ್ಜಿ ಸಂಖ್ಯೆಯೊಂದಿಗೆ <b>IPGRS</b> '
                  '(ipgrs.karnataka.gov.in) ನಲ್ಲಿ ಅಥವಾ ತಾಲೂಕು ಕಚೇರಿಯಲ್ಲಿ ದೂರು ನೀಡಿ.',
        'help': '<b>ಅರ್ಜಿ / ಸ್ಥಿತಿ:</b> nadakacheri.karnataka.gov.in, ಗ್ರಾಮ ಒನ್, ಕರ್ನಾಟಕ ಒನ್ · <b>ದೂರು:</b> '
                'ipgrs.karnataka.gov.in<br><b>ಅಧಿಕೃತ ವೆಬ್\u200cಸೈಟ್ ಮಾತ್ರ ಬಳಸಿ</b> · <b>ಮಧ್ಯವರ್ತಿಗೆ ಹಣ ಕೊಡಬೇಡಿ</b>'}}
