"""SSP scholarship (Karnataka) guide content (EN + KN)."""

OUT = "ka-ssp-scholarship-guide"
PHASE_BREAK = 5

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': "SSP Scholarship: Karnataka's State Scholarship Portal",
        'sub': 'ಎಸ್\u200cಎಸ್\u200cಪಿ ವಿದ್ಯಾರ್ಥಿ ವೇತನ: ರಾಜ್ಯ ವಿದ್ಯಾರ್ಥಿ ವೇತನ ಪೋರ್ಟಲ್',
        'benefit': "Scholarship and fee concession paid into the student's bank account",
        'legend': ['You do this', 'Government does this (you wait)', 'Money received'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you can get it',
                   'ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ',
                   '<ul><li>Karnataka student in a recognised school or college</li><li>Mainly for <b>SC, ST, OBC and '
                   'minority</b> students; each department sets its own income limit</li><li>Income limits commonly '
                   'reported between <b>₹1 lakh and ₹2.5 lakh</b> by category; the portal is final</li></ul>',
                   None),
                  ('you',
                   'Keep these ready',
                   'ಇವುಗಳನ್ನು ಸಿದ್ಧವಾಗಿಡಿ',
                   "<ul><li>Student's and parents' Aadhaar</li><li><b>Caste and income certificate RD number</b> "
                   '(Nadakacheri)</li><li>SSLC register number</li><li><b>Aadhaar-seeded bank account</b> in the '
                   "student's name</li><li><b>Kutumba family ID</b></li></ul>",
                   ('stuck',
                    'No RD number? Get the caste and income certificate first. See the <b>Caste and income certificate '
                    '(Karnataka)</b> guide.')),
                  ('you',
                   'Register and apply',
                   'ನೋಂದಾಯಿಸಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ',
                   'On <b>ssp.karnataka.gov.in</b>, create an account with Aadhaar <b>eKYC</b>, then apply for '
                   "pre-matric or post-matric before your department's deadline.",
                   ('tip',
                    'Deadlines differ by department (Social Welfare, Backward Classes, Minorities, Tribal Welfare). '
                    'Check yours on the portal.')),
                  ('you',
                   'Give documents to your institution',
                   'ಸಂಸ್ಥೆಗೆ ದಾಖಲೆ ನೀಡಿ',
                   'Submit the printout and fee receipt to your school or college scholarship section if asked.',
                   None),
                  ('gov',
                   'Institution verifies',
                   'ಸಂಸ್ಥೆ ಪರಿಶೀಲಿಸುತ್ತದೆ',
                   'Your institution checks bonafide status, fees and marks online.',
                   ('stuck',
                    'Not verified by the college? Remind the scholarship clerk before the institution deadline.')),
                  ('gov',
                   'Department approves',
                   'ಇಲಾಖೆ ಅನುಮೋದನೆ',
                   'The department checks eligibility and approves the payment.',
                   None),
                  ('done',
                   'Money in your account',
                   'ಖಾತೆಗೆ ಹಣ',
                   'Paid by <b>DBT</b> to the Aadhaar-seeded account. Track status on the SSP portal.',
                   ('stuck',
                    'Payment failed? Usually an Aadhaar-seeding or NPCI-mapping problem. Fix it at the bank.'))],
        'rights_t': 'Not paid? Follow up.',
        'rights': "Contact your department's taluk / district office (Social Welfare, Backward Classes, Minorities or "
                  'Tribal Welfare), or complain on <b>IPGRS</b>.',
        'help': '<b>Apply / status:</b> ssp.karnataka.gov.in · Income limits and dates change each year; the portal is '
                'final<br><b>Applying is free</b> · <b>Use only official websites</b>'},
 'kn': {'lang': 'kn',
        'font': "'Noto Sans Kannada','Noto Sans','FreeSans',sans-serif",
        'h1': 'ಎಸ್\u200cಎಸ್\u200cಪಿ ವಿದ್ಯಾರ್ಥಿ ವೇತನ: ಕರ್ನಾಟಕ ರಾಜ್ಯ ವಿದ್ಯಾರ್ಥಿ ವೇತನ ಪೋರ್ಟಲ್',
        'sub': None,
        'benefit': 'ವಿದ್ಯಾರ್ಥಿ ವೇತನ ಮತ್ತು ಶುಲ್ಕ ರಿಯಾಯಿತಿ ವಿದ್ಯಾರ್ಥಿಯ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ',
        'legend': ['ಇದನ್ನು ನೀವು ಮಾಡಿ', 'ಇದನ್ನು ಸರ್ಕಾರ ಮಾಡುತ್ತದೆ (ನೀವು ಕಾಯಿರಿ)', 'ಹಣ ಬಂದಿದೆ'],
        'phases': ['ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮೊದಲು', 'ಅರ್ಜಿ ಸಲ್ಲಿಸಿದ ನಂತರ'],
        'who': {'you': 'ನೀವು', 'gov': 'ಸರ್ಕಾರ', 'done': 'ಪೂರ್ಣ'},
        'stuck': 'ತೊಂದರೆಯೇ?',
        'tip': 'ಸಲಹೆ:',
        'steps': [('you',
                   'ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ',
                   None,
                   '<ul><li>ಮಾನ್ಯತೆ ಪಡೆದ ಶಾಲೆ ಅಥವಾ ಕಾಲೇಜಿನ ಕರ್ನಾಟಕದ ವಿದ್ಯಾರ್ಥಿ</li><li>ಮುಖ್ಯವಾಗಿ <b>ಪರಿಶಿಷ್ಟ ಜಾತಿ, '
                   'ಪರಿಶಿಷ್ಟ ಪಂಗಡ, ಹಿಂದುಳಿದ ವರ್ಗ ಮತ್ತು ಅಲ್ಪಸಂಖ್ಯಾತ</b> ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ; ಪ್ರತಿ ಇಲಾಖೆ ತನ್ನದೇ ಆದಾಯ ಮಿತಿ '
                   'ನಿಗದಿಪಡಿಸುತ್ತದೆ</li><li>ವರ್ಗವಾರು ಆದಾಯ ಮಿತಿ ಸಾಮಾನ್ಯವಾಗಿ <b>₹1 ಲಕ್ಷದಿಂದ ₹2.5 ಲಕ್ಷ</b> ಎಂದು ವರದಿ; '
                   'ಪೋರ್ಟಲ್ ಅಂತಿಮ</li></ul>',
                   None),
                  ('you',
                   'ಇವುಗಳನ್ನು ಸಿದ್ಧವಾಗಿಡಿ',
                   None,
                   '<ul><li>ವಿದ್ಯಾರ್ಥಿ ಮತ್ತು ಪೋಷಕರ ಆಧಾರ್</li><li><b>ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರದ RD ಸಂಖ್ಯೆ</b> '
                   '(ನಾಡಕಚೇರಿ)</li><li>ಎಸ್\u200cಎಸ್\u200cಎಲ್\u200cಸಿ ನೋಂದಣಿ ಸಂಖ್ಯೆ</li><li>ವಿದ್ಯಾರ್ಥಿಯ ಹೆಸರಿನಲ್ಲಿ '
                   '<b>ಆಧಾರ್ ಜೋಡಣೆಯಾದ ಬ್ಯಾಂಕ್ ಖಾತೆ</b></li><li><b>ಕುಟುಂಬ ಐಡಿ</b></li></ul>',
                   ('stuck',
                    'RD ಸಂಖ್ಯೆ ಇಲ್ಲವೇ? ಮೊದಲು ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರ ಪಡೆಯಿರಿ. <b>ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರ '
                    '(ಕರ್ನಾಟಕ)</b> ಮಾರ್ಗದರ್ಶಿ ನೋಡಿ.')),
                  ('you',
                   'ನೋಂದಾಯಿಸಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ',
                   None,
                   '<b>ssp.karnataka.gov.in</b> ನಲ್ಲಿ ಆಧಾರ್ <b>ಇ-ಕೆವೈಸಿ</b>ಯೊಂದಿಗೆ ಖಾತೆ ತೆರೆಯಿರಿ, ನಂತರ ನಿಮ್ಮ ಇಲಾಖೆಯ '
                   'ಕೊನೆಯ ದಿನಾಂಕದೊಳಗೆ ಮೆಟ್ರಿಕ್ ಪೂರ್ವ ಅಥವಾ ಮೆಟ್ರಿಕ್ ನಂತರದ ವಿದ್ಯಾರ್ಥಿ ವೇತನಕ್ಕೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.',
                   ('tip',
                    'ಕೊನೆಯ ದಿನಾಂಕಗಳು ಇಲಾಖೆವಾರು ಬೇರೆ (ಸಮಾಜ ಕಲ್ಯಾಣ, ಹಿಂದುಳಿದ ವರ್ಗಗಳು, ಅಲ್ಪಸಂಖ್ಯಾತರು, ಪರಿಶಿಷ್ಟ ಪಂಗಡ '
                    'ಕಲ್ಯಾಣ). ನಿಮ್ಮದನ್ನು ಪೋರ್ಟಲ್\u200cನಲ್ಲಿ ನೋಡಿ.')),
                  ('you',
                   'ಸಂಸ್ಥೆಗೆ ದಾಖಲೆ ನೀಡಿ',
                   None,
                   'ಕೇಳಿದರೆ ಪ್ರಿಂಟ್\u200cಔಟ್ ಮತ್ತು ಶುಲ್ಕದ ರಸೀದಿಯನ್ನು ಶಾಲೆ ಅಥವಾ ಕಾಲೇಜಿನ ವಿದ್ಯಾರ್ಥಿ ವೇತನ ವಿಭಾಗಕ್ಕೆ ನೀಡಿ.',
                   None),
                  ('gov',
                   'ಸಂಸ್ಥೆ ಪರಿಶೀಲಿಸುತ್ತದೆ',
                   None,
                   'ನಿಮ್ಮ ಸಂಸ್ಥೆ ವ್ಯಾಸಂಗ ದೃಢೀಕರಣ, ಶುಲ್ಕ ಮತ್ತು ಅಂಕಗಳನ್ನು ಆನ್\u200cಲೈನ್\u200cನಲ್ಲಿ ಪರಿಶೀಲಿಸುತ್ತದೆ.',
                   ('stuck',
                    'ಕಾಲೇಜು ಪರಿಶೀಲಿಸಿಲ್ಲವೇ? ಸಂಸ್ಥೆಯ ಕೊನೆಯ ದಿನಾಂಕದ ಮೊದಲು ವಿದ್ಯಾರ್ಥಿ ವೇತನ ಗುಮಾಸ್ತರಿಗೆ ನೆನಪಿಸಿ.')),
                  ('gov', 'ಇಲಾಖೆ ಅನುಮೋದನೆ', None, 'ಇಲಾಖೆ ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ ಪಾವತಿ ಅನುಮೋದಿಸುತ್ತದೆ.', None),
                  ('done',
                   'ಖಾತೆಗೆ ಹಣ',
                   None,
                   'ಆಧಾರ್ ಜೋಡಣೆಯಾದ ಖಾತೆಗೆ <b>DBT</b> ಮೂಲಕ ಪಾವತಿ. ಎಸ್\u200cಎಸ್\u200cಪಿ ಪೋರ್ಟಲ್\u200cನಲ್ಲಿ ಸ್ಥಿತಿ ನೋಡಿ.',
                   ('stuck', 'ಪಾವತಿ ವಿಫಲವೇ? ಹೆಚ್ಚಾಗಿ ಆಧಾರ್ ಜೋಡಣೆ ಅಥವಾ NPCI ಮ್ಯಾಪಿಂಗ್ ಸಮಸ್ಯೆ. ಬ್ಯಾಂಕಿನಲ್ಲಿ ಸರಿಪಡಿಸಿ.'))],
        'rights_t': 'ಹಣ ಬಂದಿಲ್ಲವೇ? ಮತ್ತೆ ವಿಚಾರಿಸಿ.',
        'rights': 'ನಿಮ್ಮ ಇಲಾಖೆಯ ತಾಲೂಕು / ಜಿಲ್ಲಾ ಕಚೇರಿ (ಸಮಾಜ ಕಲ್ಯಾಣ, ಹಿಂದುಳಿದ ವರ್ಗಗಳು, ಅಲ್ಪಸಂಖ್ಯಾತರು ಅಥವಾ ಪರಿಶಿಷ್ಟ ಪಂಗಡ '
                  'ಕಲ್ಯಾಣ) ಸಂಪರ್ಕಿಸಿ, ಅಥವಾ <b>IPGRS</b> ನಲ್ಲಿ ದೂರು ನೀಡಿ.',
        'help': '<b>ಅರ್ಜಿ / ಸ್ಥಿತಿ:</b> ssp.karnataka.gov.in · ಆದಾಯ ಮಿತಿ ಮತ್ತು ದಿನಾಂಕಗಳು ಪ್ರತಿ ವರ್ಷ ಬದಲಾಗುತ್ತವೆ; '
                'ಪೋರ್ಟಲ್ ಅಂತಿಮ<br><b>ಅರ್ಜಿ ಉಚಿತ</b> · <b>ಅಧಿಕೃತ ವೆಬ್\u200cಸೈಟ್ ಮಾತ್ರ ಬಳಸಿ</b>'}}
