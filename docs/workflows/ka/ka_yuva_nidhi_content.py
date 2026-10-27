"""Yuva Nidhi (unemployment allowance) guide content (EN + KN)."""

OUT = "ka-yuva-nidhi-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Yuva Nidhi: Monthly allowance for unemployed graduates',
        'sub': 'ಯುವನಿಧಿ: ನಿರುದ್ಯೋಗಿ ಪದವೀಧರರಿಗೆ ಮಾಸಿಕ ಭತ್ಯೆ',
        'benefit': '₹3,000 a month for graduates, ₹1,500 for diploma holders, for up to two years',
        'legend': ['You do this', 'Government does this (you wait)', 'Allowance received'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you can get it',
                   'ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ',
                   '<ul><li>Karnataka domicile, graduate or diploma holder</li><li><b>Unemployed for six months</b> '
                   'after passing</li><li>Not in higher studies, not getting apprenticeship stipend, not self-employed '
                   'with a government-scheme loan, no government job</li></ul>',
                   None),
                  ('you',
                   'Keep these ready',
                   'ಇವುಗಳನ್ನು ಸಿದ್ಧವಾಗಿಡಿ',
                   '<ul><li>Aadhaar and an <b>Aadhaar-seeded bank account</b></li><li>Degree or diploma certificate '
                   'and marks cards</li><li>Domicile proof (study in Karnataka or residence)</li></ul>',
                   None),
                  ('you',
                   'Apply on Seva Sindhu',
                   'ಸೇವಾ ಸಿಂಧುವಿನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ',
                   'Register on <b>Seva Sindhu</b> (Yuva Nidhi), upload documents and sign the <b>self-declaration</b> '
                   'that you are unemployed.',
                   ('stuck',
                    'False declarations can lead to recovery and penalty. Tell the department as soon as you get a '
                    'job.')),
                  ('gov',
                   'Verification',
                   'ಪರಿಶೀಲನೆ',
                   'The Skill Development department checks your degree (including on the <b>NAD</b> academic '
                   'database) and eligibility.',
                   ('stuck',
                    'Degree not found on NAD? Ask your university to upload it, then inform the district employment '
                    'office.')),
                  ('you',
                   'Confirm every month',
                   'ಪ್ರತಿ ತಿಂಗಳು ದೃಢೀಕರಿಸಿ',
                   'Keep confirming that you are still unemployed, as the portal asks, so the allowance continues.',
                   None),
                  ('done',
                   'Allowance in your account',
                   'ಖಾತೆಗೆ ಭತ್ಯೆ',
                   'Paid by DBT until you get a job or for a <b>maximum of two years</b>.',
                   None)],
        'rights_t': 'Not paid? Ask for help.',
        'rights': 'Contact the <b>district employment exchange</b> / Skill Development office, call <b>1902</b>, or '
                  'complain on <b>IPGRS</b>.',
        'help': '<b>Apply:</b> sevasindhugs.karnataka.gov.in · <b>Helpline:</b> 1902 · Rules as at launch; check the '
                'current notice<br><b>Applying is free</b> · <b>Use only official websites</b>'},
 'kn': {'lang': 'kn',
        'font': "'Noto Sans Kannada','Noto Sans','FreeSans',sans-serif",
        'h1': 'ಯುವನಿಧಿ: ನಿರುದ್ಯೋಗಿ ಪದವೀಧರರಿಗೆ ಮಾಸಿಕ ಭತ್ಯೆ',
        'sub': None,
        'benefit': 'ಪದವೀಧರರಿಗೆ ತಿಂಗಳಿಗೆ ₹3,000, ಡಿಪ್ಲೊಮಾದವರಿಗೆ ₹1,500, ಗರಿಷ್ಠ ಎರಡು ವರ್ಷ',
        'legend': ['ಇದನ್ನು ನೀವು ಮಾಡಿ', 'ಇದನ್ನು ಸರ್ಕಾರ ಮಾಡುತ್ತದೆ (ನೀವು ಕಾಯಿರಿ)', 'ಭತ್ಯೆ ಬಂದಿದೆ'],
        'phases': ['ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮೊದಲು', 'ಅರ್ಜಿ ಸಲ್ಲಿಸಿದ ನಂತರ'],
        'who': {'you': 'ನೀವು', 'gov': 'ಸರ್ಕಾರ', 'done': 'ಪೂರ್ಣ'},
        'stuck': 'ತೊಂದರೆಯೇ?',
        'tip': 'ಸಲಹೆ:',
        'steps': [('you',
                   'ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ',
                   None,
                   '<ul><li>ಕರ್ನಾಟಕದ ನಿವಾಸಿ, ಪದವೀಧರ ಅಥವಾ ಡಿಪ್ಲೊಮಾ ಹೊಂದಿದವರು</li><li>ಉತ್ತೀರ್ಣರಾದ ನಂತರ <b>ಆರು ತಿಂಗಳು '
                   'ನಿರುದ್ಯೋಗಿ</b></li><li>ಉನ್ನತ ವ್ಯಾಸಂಗದಲ್ಲಿ ಇರಬಾರದು, ಅಪ್ರೆಂಟಿಸ್ ಶಿಷ್ಯವೇತನ ಪಡೆಯಬಾರದು, ಸರ್ಕಾರಿ ಯೋಜನೆಯ '
                   'ಸಾಲದೊಂದಿಗೆ ಸ್ವಯಂ ಉದ್ಯೋಗಿ ಆಗಿರಬಾರದು, ಸರ್ಕಾರಿ ಉದ್ಯೋಗ ಇರಬಾರದು</li></ul>',
                   None),
                  ('you',
                   'ಇವುಗಳನ್ನು ಸಿದ್ಧವಾಗಿಡಿ',
                   None,
                   '<ul><li>ಆಧಾರ್ ಮತ್ತು <b>ಆಧಾರ್ ಜೋಡಣೆಯಾದ ಬ್ಯಾಂಕ್ ಖಾತೆ</b></li><li>ಪದವಿ ಅಥವಾ ಡಿಪ್ಲೊಮಾ ಪ್ರಮಾಣ ಪತ್ರ '
                   'ಮತ್ತು ಅಂಕಪಟ್ಟಿಗಳು</li><li>ನಿವಾಸದ ಪುರಾವೆ (ಕರ್ನಾಟಕದಲ್ಲಿ ವ್ಯಾಸಂಗ ಅಥವಾ ವಾಸ)</li></ul>',
                   None),
                  ('you',
                   'ಸೇವಾ ಸಿಂಧುವಿನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ',
                   None,
                   '<b>ಸೇವಾ ಸಿಂಧು</b>ವಿನಲ್ಲಿ (ಯುವನಿಧಿ) ನೋಂದಾಯಿಸಿ, ದಾಖಲೆಗಳನ್ನು ಅಪ್\u200cಲೋಡ್ ಮಾಡಿ ಮತ್ತು ನೀವು ನಿರುದ್ಯೋಗಿ '
                   'ಎಂಬ <b>ಸ್ವಯಂ ಘೋಷಣೆ</b>ಗೆ ಸಹಿ ಮಾಡಿ.',
                   ('stuck', 'ಸುಳ್ಳು ಘೋಷಣೆಗೆ ವಸೂಲಾತಿ ಮತ್ತು ದಂಡ ಆಗಬಹುದು. ಉದ್ಯೋಗ ಸಿಕ್ಕ ತಕ್ಷಣ ಇಲಾಖೆಗೆ ತಿಳಿಸಿ.')),
                  ('gov',
                   'ಪರಿಶೀಲನೆ',
                   None,
                   'ಕೌಶಲ್ಯಾಭಿವೃದ್ಧಿ ಇಲಾಖೆ ನಿಮ್ಮ ಪದವಿಯನ್ನು (<b>NAD</b> ಶೈಕ್ಷಣಿಕ ದತ್ತಾಂಶದಲ್ಲೂ) ಮತ್ತು ಅರ್ಹತೆಯನ್ನು '
                   'ಪರಿಶೀಲಿಸುತ್ತದೆ.',
                   ('stuck',
                    'NAD ನಲ್ಲಿ ಪದವಿ ಇಲ್ಲವೇ? ನಿಮ್ಮ ವಿಶ್ವವಿದ್ಯಾಲಯಕ್ಕೆ ಅಪ್\u200cಲೋಡ್ ಮಾಡಲು ಕೇಳಿ, ನಂತರ ಜಿಲ್ಲಾ ಉದ್ಯೋಗ '
                    'ಕಚೇರಿಗೆ ತಿಳಿಸಿ.')),
                  ('you',
                   'ಪ್ರತಿ ತಿಂಗಳು ದೃಢೀಕರಿಸಿ',
                   None,
                   'ಪೋರ್ಟಲ್ ಕೇಳಿದಂತೆ ನೀವು ಇನ್ನೂ ನಿರುದ್ಯೋಗಿ ಎಂದು ದೃಢೀಕರಿಸುತ್ತಿರಿ, ಆಗ ಭತ್ಯೆ ಮುಂದುವರಿಯುತ್ತದೆ.',
                   None),
                  ('done',
                   'ಖಾತೆಗೆ ಭತ್ಯೆ',
                   None,
                   'ಉದ್ಯೋಗ ಸಿಗುವವರೆಗೆ ಅಥವಾ <b>ಗರಿಷ್ಠ ಎರಡು ವರ್ಷ</b> DBT ಮೂಲಕ ಪಾವತಿಯಾಗುತ್ತದೆ.',
                   None)],
        'rights_t': 'ಹಣ ಬಂದಿಲ್ಲವೇ? ಸಹಾಯ ಪಡೆಯಿರಿ.',
        'rights': '<b>ಜಿಲ್ಲಾ ಉದ್ಯೋಗ ವಿನಿಮಯ</b> / ಕೌಶಲ್ಯಾಭಿವೃದ್ಧಿ ಕಚೇರಿ ಸಂಪರ್ಕಿಸಿ, <b>1902</b> ಗೆ ಕರೆ ಮಾಡಿ, ಅಥವಾ '
                  '<b>IPGRS</b> ನಲ್ಲಿ ದೂರು ನೀಡಿ.',
        'help': '<b>ಅರ್ಜಿ:</b> sevasindhugs.karnataka.gov.in · <b>ಸಹಾಯವಾಣಿ:</b> 1902 · ಆರಂಭದ ನಿಯಮಗಳು; ಚಾಲ್ತಿ ಸೂಚನೆ '
                'ನೋಡಿ<br><b>ಅರ್ಜಿ ಉಚಿತ</b> · <b>ಅಧಿಕೃತ ವೆಬ್\u200cಸೈಟ್ ಮಾತ್ರ ಬಳಸಿ</b>'}}
