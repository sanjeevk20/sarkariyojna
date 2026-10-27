"""Old-age and widow pensions (Karnataka) guide content (EN + KN)."""

OUT = "ka-social-pensions-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Social Security Pensions (Karnataka): Old-age and widow pension',
        'sub': 'ಸಾಮಾಜಿಕ ಭದ್ರತಾ ಪಿಂಚಣಿ: ವೃದ್ಧಾಪ್ಯ ಮತ್ತು ವಿಧವಾ ವೇತನ',
        'benefit': 'Monthly pension into your bank account (Sandhya Suraksha reported at ₹1,200)',
        'legend': ['You do this', 'Government does this (you wait)', 'Pension received'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Find your pension',
                   'ನಿಮ್ಮ ಪಿಂಚಣಿ ಯಾವುದು',
                   '<ul><li><b>Old-age pension</b> (with central share) for poor seniors</li><li><b>Sandhya '
                   'Suraksha</b> for seniors from low-income working families</li><li><b>Widow pension</b> for widows '
                   'from low-income families</li></ul>Ask the Nadakacheri which one fits your age and income.',
                   None),
                  ('you',
                   'Keep these papers ready',
                   'ದಾಖಲೆಗಳನ್ನು ಸಿದ್ಧವಾಗಿಡಿ',
                   '<ul><li>Aadhaar and <b>age proof</b></li><li><b>Income certificate</b> '
                   "(Nadakacheri)</li><li>Widows: <b>husband's death certificate</b></li><li>Bank passbook (account "
                   '<b>linked to Aadhaar</b>), photo</li></ul>',
                   None),
                  ('you',
                   'Apply',
                   'ಅರ್ಜಿ ಸಲ್ಲಿಸಿ',
                   'Apply on <b>Seva Sindhu</b> or at a <b>Nadakacheri</b> / <b>Grama One</b> centre. Keep the '
                   '<b>acknowledgement</b>.',
                   ('tip', "Applying is <b>free</b>. Do not pay anyone to 'sanction' a pension.")),
                  ('gov',
                   'Verification',
                   'ಪರಿಶೀಲನೆ',
                   'The <b>Village Accountant</b> and <b>Revenue Inspector</b> check age, income and family details.',
                   ('stuck',
                    'A 2025 review flagged many pensions as possibly ineligible. Keep your income certificate and age '
                    'proof current so your pension is not stopped.')),
                  ('gov',
                   'Tahsildar sanctions',
                   'ತಹಶೀಲ್ದಾರ್ ಮಂಜೂರಾತಿ',
                   'The <b>Tahsildar</b> sanctions the pension.',
                   None),
                  ('done',
                   'Pension every month',
                   'ಪ್ರತಿ ತಿಂಗಳು ಪಿಂಚಣಿ',
                   'The pension is paid into your account. Check that the amount matches the current rate.',
                   ('stuck',
                    'Payment stopped? Check Aadhaar seeding at the bank, then ask the taluk office whether your '
                    'pension was suspended after review.'))],
        'rights_t': 'Stopped or not sanctioned? Complain.',
        'rights': 'Write to the <b>Tahsildar</b> with your acknowledgement number, or complain on <b>IPGRS</b>. Ask '
                  'for the reason in writing if it was stopped.',
        'help': '<b>Apply:</b> sevasindhu.karnataka.gov.in, Nadakacheri, Grama One · Amounts change; check the current '
                'rate at the taluk office<br><b>Applying is free</b> · <b>Use only official websites</b>'},
 'kn': {'lang': 'kn',
        'font': "'Noto Sans Kannada','Noto Sans','FreeSans',sans-serif",
        'h1': 'ಸಾಮಾಜಿಕ ಭದ್ರತಾ ಪಿಂಚಣಿ (ಕರ್ನಾಟಕ): ವೃದ್ಧಾಪ್ಯ ಮತ್ತು ವಿಧವಾ ವೇತನ',
        'sub': None,
        'benefit': 'ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಮಾಸಿಕ ಪಿಂಚಣಿ (ಸಂಧ್ಯಾ ಸುರಕ್ಷಾ ₹1,200 ಎಂದು ವರದಿಯಾಗಿದೆ)',
        'legend': ['ಇದನ್ನು ನೀವು ಮಾಡಿ', 'ಇದನ್ನು ಸರ್ಕಾರ ಮಾಡುತ್ತದೆ (ನೀವು ಕಾಯಿರಿ)', 'ಪಿಂಚಣಿ ಬಂದಿದೆ'],
        'phases': ['ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮೊದಲು', 'ಅರ್ಜಿ ಸಲ್ಲಿಸಿದ ನಂತರ'],
        'who': {'you': 'ನೀವು', 'gov': 'ಸರ್ಕಾರ', 'done': 'ಪೂರ್ಣ'},
        'stuck': 'ತೊಂದರೆಯೇ?',
        'tip': 'ಸಲಹೆ:',
        'steps': [('you',
                   'ನಿಮ್ಮ ಪಿಂಚಣಿ ಯಾವುದು',
                   None,
                   '<ul><li>ಬಡ ಹಿರಿಯರಿಗೆ <b>ವೃದ್ಧಾಪ್ಯ ವೇತನ</b> (ಕೇಂದ್ರದ ಪಾಲಿನೊಂದಿಗೆ)</li><li>ಕಡಿಮೆ ಆದಾಯದ ದುಡಿಯುವ '
                   'ಕುಟುಂಬಗಳ ಹಿರಿಯರಿಗೆ <b>ಸಂಧ್ಯಾ ಸುರಕ್ಷಾ</b></li><li>ಕಡಿಮೆ ಆದಾಯದ ಕುಟುಂಬಗಳ ವಿಧವೆಯರಿಗೆ <b>ವಿಧವಾ '
                   'ವೇತನ</b></li></ul>ನಿಮ್ಮ ವಯಸ್ಸು ಮತ್ತು ಆದಾಯಕ್ಕೆ ಯಾವುದು ಸೂಕ್ತ ಎಂದು ನಾಡಕಚೇರಿಯಲ್ಲಿ ಕೇಳಿ.',
                   None),
                  ('you',
                   'ದಾಖಲೆಗಳನ್ನು ಸಿದ್ಧವಾಗಿಡಿ',
                   None,
                   '<ul><li>ಆಧಾರ್ ಮತ್ತು <b>ವಯಸ್ಸಿನ ಪುರಾವೆ</b></li><li><b>ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರ</b> '
                   '(ನಾಡಕಚೇರಿ)</li><li>ವಿಧವೆಯರಿಗೆ: <b>ಪತಿಯ ಮರಣ ಪ್ರಮಾಣ ಪತ್ರ</b></li><li>ಬ್ಯಾಂಕ್ ಪಾಸ್\u200cಬುಕ್ (ಖಾತೆ '
                   '<b>ಆಧಾರ್\u200cಗೆ ಜೋಡಣೆ</b>), ಫೋಟೋ</li></ul>',
                   None),
                  ('you',
                   'ಅರ್ಜಿ ಸಲ್ಲಿಸಿ',
                   None,
                   '<b>ಸೇವಾ ಸಿಂಧು</b>ವಿನಲ್ಲಿ ಅಥವಾ <b>ನಾಡಕಚೇರಿ</b> / <b>ಗ್ರಾಮ ಒನ್</b> ಕೇಂದ್ರದಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ. '
                   '<b>ಸ್ವೀಕೃತಿ</b> ಜೋಪಾನವಾಗಿಡಿ.',
                   ('tip', "ಅರ್ಜಿ <b>ಉಚಿತ</b>. ಪಿಂಚಣಿ 'ಮಂಜೂರು ಮಾಡಿಸಲು' ಯಾರಿಗೂ ಹಣ ಕೊಡಬೇಡಿ.")),
                  ('gov',
                   'ಪರಿಶೀಲನೆ',
                   None,
                   '<b>ಗ್ರಾಮ ಲೆಕ್ಕಾಧಿಕಾರಿ</b> ಮತ್ತು <b>ಕಂದಾಯ ನಿರೀಕ್ಷಕರು</b> ವಯಸ್ಸು, ಆದಾಯ ಮತ್ತು ಕುಟುಂಬದ ವಿವರ '
                   'ಪರಿಶೀಲಿಸುತ್ತಾರೆ.',
                   ('stuck',
                    '2025ರ ಪರಿಶೀಲನೆಯಲ್ಲಿ ಅನೇಕ ಪಿಂಚಣಿಗಳನ್ನು ಅನರ್ಹವಾಗಿರಬಹುದು ಎಂದು ಗುರುತಿಸಲಾಗಿದೆ. ನಿಮ್ಮ ಪಿಂಚಣಿ ನಿಲ್ಲದಂತೆ '
                    'ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರ ಮತ್ತು ವಯಸ್ಸಿನ ಪುರಾವೆ ಚಾಲ್ತಿಯಲ್ಲಿಡಿ.')),
                  ('gov', 'ತಹಶೀಲ್ದಾರ್ ಮಂಜೂರಾತಿ', None, '<b>ತಹಶೀಲ್ದಾರ್</b> ಪಿಂಚಣಿ ಮಂಜೂರು ಮಾಡುತ್ತಾರೆ.', None),
                  ('done',
                   'ಪ್ರತಿ ತಿಂಗಳು ಪಿಂಚಣಿ',
                   None,
                   'ಪಿಂಚಣಿ ನಿಮ್ಮ ಖಾತೆಗೆ ಜಮೆಯಾಗುತ್ತದೆ. ಮೊತ್ತ ಚಾಲ್ತಿ ದರಕ್ಕೆ ಹೊಂದಿಕೆಯಾಗುತ್ತದೆಯೇ ನೋಡಿ.',
                   ('stuck',
                    'ಪಾವತಿ ನಿಂತಿದೆಯೇ? ಬ್ಯಾಂಕಿನಲ್ಲಿ ಆಧಾರ್ ಜೋಡಣೆ ಪರಿಶೀಲಿಸಿ, ನಂತರ ಪರಿಶೀಲನೆಯ ಬಳಿಕ ನಿಮ್ಮ ಪಿಂಚಣಿ '
                    'ತಡೆಹಿಡಿಯಲಾಗಿದೆಯೇ ಎಂದು ತಾಲೂಕು ಕಚೇರಿಯಲ್ಲಿ ಕೇಳಿ.'))],
        'rights_t': 'ನಿಂತಿದೆಯೇ ಅಥವಾ ಮಂಜೂರಾಗಿಲ್ಲವೇ? ದೂರು ನೀಡಿ.',
        'rights': 'ಸ್ವೀಕೃತಿ ಸಂಖ್ಯೆಯೊಂದಿಗೆ <b>ತಹಶೀಲ್ದಾರ್</b> ಅವರಿಗೆ ಬರೆಯಿರಿ, ಅಥವಾ <b>IPGRS</b> ನಲ್ಲಿ ದೂರು ನೀಡಿ. '
                  'ನಿಲ್ಲಿಸಿದ್ದರೆ ಕಾರಣವನ್ನು ಲಿಖಿತವಾಗಿ ಕೇಳಿ.',
        'help': '<b>ಅರ್ಜಿ:</b> sevasindhu.karnataka.gov.in, ನಾಡಕಚೇರಿ, ಗ್ರಾಮ ಒನ್ · ಮೊತ್ತ ಬದಲಾಗುತ್ತದೆ; ಚಾಲ್ತಿ ದರ ತಾಲೂಕು '
                'ಕಚೇರಿಯಲ್ಲಿ ನೋಡಿ<br><b>ಅರ್ಜಿ ಉಚಿತ</b> · <b>ಅಧಿಕೃತ ವೆಬ್\u200cಸೈಟ್ ಮಾತ್ರ ಬಳಸಿ</b>'}}
