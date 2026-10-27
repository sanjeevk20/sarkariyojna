"""Gruha Lakshmi guide content (EN + KN)."""

OUT = "ka-gruha-lakshmi-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Gruha Lakshmi: ₹2,000 a month for the woman head of the family',
        'sub': 'ಗೃಹಲಕ್ಷ್ಮಿ: ಕುಟುಂಬದ ಯಜಮಾನಿಗೆ ತಿಂಗಳಿಗೆ ₹2,000',
        'benefit': '₹2,000 a month by DBT to one woman per family',
        'legend': ['You do this', 'Government does this (you wait)', 'Money received'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you can get it',
                   'ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ',
                   '<ul><li>You are the <b>woman head of the family</b> on an AAY, BPL or APL ration '
                   'card</li><li>Neither you nor your husband is a <b>government employee</b> or pays <b>income tax / '
                   'files GST returns</b></li></ul>',
                   None),
                  ('you',
                   'Keep these ready',
                   'ಇವುಗಳನ್ನು ಸಿದ್ಧವಾಗಿಡಿ',
                   '<ul><li>Ration card number</li><li>Aadhaar of you and your husband</li><li>Bank account <b>linked '
                   'to Aadhaar</b> with DBT on</li><li>Mobile linked to Aadhaar</li></ul>',
                   None),
                  ('you',
                   'Apply',
                   'ಅರ್ಜಿ ಸಲ್ಲಿಸಿ',
                   'Apply on <b>Seva Sindhu</b> or at a <b>Grama One</b>, <b>Karnataka One</b> or <b>Bapuji Seva '
                   'Kendra</b>. Keep the <b>acknowledgement number</b>.',
                   ('tip',
                    'Applying is <b>free</b>. Never share your OTP or bank details with anyone who says they can '
                    "'release' a payment.")),
                  ('gov',
                   'Verification',
                   'ಪರಿಶೀಲನೆ',
                   'The department checks the ration card, Aadhaar and tax records. A <b>biometric re-verification</b> '
                   'drive was reported in 2026.',
                   ('stuck',
                    'Asked to re-verify? Do it at the centre or during the door-to-door visit, or payments may stop.')),
                  ('done',
                   '₹2,000 every month',
                   'ಪ್ರತಿ ತಿಂಗಳು ₹2,000',
                   'Money arrives by DBT, often in the first half of the month. Check status on Seva Sindhu with your '
                   'acknowledgement number.',
                   ('stuck',
                    'Not received? Usually Aadhaar is not seeded to the active account or DBT is off. Fix it at the '
                    'bank, then check status again.'))],
        'rights_t': 'Still not paid? Ask for help.',
        'rights': 'Call the guarantee schemes helpline <b>1902</b>, visit the taluk <b>Women and Child Development</b> '
                  'office, or complain on <b>IPGRS</b>.',
        'help': '<b>Apply / status:</b> sevasindhugs.karnataka.gov.in, Grama One, Karnataka One · <b>Helpline:</b> '
                '1902<br><b>Applying is free</b> · <b>Never share your OTP</b>'},
 'kn': {'lang': 'kn',
        'font': "'Noto Sans Kannada','Noto Sans','FreeSans',sans-serif",
        'h1': 'ಗೃಹಲಕ್ಷ್ಮಿ: ಕುಟುಂಬದ ಯಜಮಾನಿಗೆ ತಿಂಗಳಿಗೆ ₹2,000',
        'sub': None,
        'benefit': 'ಪ್ರತಿ ಕುಟುಂಬದ ಒಬ್ಬ ಮಹಿಳೆಗೆ ತಿಂಗಳಿಗೆ ₹2,000 ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT)',
        'legend': ['ಇದನ್ನು ನೀವು ಮಾಡಿ', 'ಇದನ್ನು ಸರ್ಕಾರ ಮಾಡುತ್ತದೆ (ನೀವು ಕಾಯಿರಿ)', 'ಹಣ ಬಂದಿದೆ'],
        'phases': ['ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮೊದಲು', 'ಅರ್ಜಿ ಸಲ್ಲಿಸಿದ ನಂತರ'],
        'who': {'you': 'ನೀವು', 'gov': 'ಸರ್ಕಾರ', 'done': 'ಪೂರ್ಣ'},
        'stuck': 'ತೊಂದರೆಯೇ?',
        'tip': 'ಸಲಹೆ:',
        'steps': [('you',
                   'ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ',
                   None,
                   '<ul><li>ನೀವು AAY, BPL ಅಥವಾ APL ಪಡಿತರ ಚೀಟಿಯಲ್ಲಿ <b>ಕುಟುಂಬದ ಯಜಮಾನಿ</b> ಆಗಿರಬೇಕು</li><li>ನೀವು ಅಥವಾ '
                   'ನಿಮ್ಮ ಪತಿ <b>ಸರ್ಕಾರಿ ನೌಕರರು</b> ಆಗಿರಬಾರದು ಅಥವಾ <b>ಆದಾಯ ತೆರಿಗೆ / GST ರಿಟರ್ನ್</b> '
                   'ಸಲ್ಲಿಸುತ್ತಿರಬಾರದು</li></ul>',
                   None),
                  ('you',
                   'ಇವುಗಳನ್ನು ಸಿದ್ಧವಾಗಿಡಿ',
                   None,
                   '<ul><li>ಪಡಿತರ ಚೀಟಿ ಸಂಖ್ಯೆ</li><li>ನಿಮ್ಮ ಮತ್ತು ನಿಮ್ಮ ಪತಿಯ ಆಧಾರ್</li><li><b>ಆಧಾರ್\u200cಗೆ '
                   'ಜೋಡಣೆಯಾದ</b>, DBT ಸಕ್ರಿಯ ಬ್ಯಾಂಕ್ ಖಾತೆ</li><li>ಆಧಾರ್\u200cಗೆ ಜೋಡಣೆಯಾದ ಮೊಬೈಲ್</li></ul>',
                   None),
                  ('you',
                   'ಅರ್ಜಿ ಸಲ್ಲಿಸಿ',
                   None,
                   '<b>ಸೇವಾ ಸಿಂಧು</b>ವಿನಲ್ಲಿ ಅಥವಾ <b>ಗ್ರಾಮ ಒನ್</b>, <b>ಕರ್ನಾಟಕ ಒನ್</b> ಅಥವಾ <b>ಬಾಪೂಜಿ ಸೇವಾ '
                   'ಕೇಂದ್ರ</b>ದಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ. <b>ಸ್ವೀಕೃತಿ ಸಂಖ್ಯೆಯನ್ನು</b> ಜೋಪಾನವಾಗಿಡಿ.',
                   ('tip',
                    "ಅರ್ಜಿ <b>ಉಚಿತ</b>. ಹಣ 'ಬಿಡುಗಡೆ ಮಾಡಿಸುತ್ತೇವೆ' ಎನ್ನುವವರಿಗೆ OTP ಅಥವಾ ಬ್ಯಾಂಕ್ ವಿವರ ಎಂದಿಗೂ ಕೊಡಬೇಡಿ.")),
                  ('gov',
                   'ಪರಿಶೀಲನೆ',
                   None,
                   'ಇಲಾಖೆ ಪಡಿತರ ಚೀಟಿ, ಆಧಾರ್ ಮತ್ತು ತೆರಿಗೆ ದಾಖಲೆಗಳನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ. 2026ರಲ್ಲಿ <b>ಬಯೋಮೆಟ್ರಿಕ್ '
                   'ಮರುಪರಿಶೀಲನೆ</b> ಅಭಿಯಾನ ವರದಿಯಾಗಿದೆ.',
                   ('stuck',
                    'ಮರುಪರಿಶೀಲನೆ ಕೇಳಿದ್ದಾರೆಯೇ? ಕೇಂದ್ರದಲ್ಲಿ ಅಥವಾ ಮನೆ-ಮನೆ ಭೇಟಿಯ ವೇಳೆ ಮಾಡಿಸಿ, ಇಲ್ಲದಿದ್ದರೆ ಹಣ '
                    'ನಿಲ್ಲಬಹುದು.')),
                  ('done',
                   'ಪ್ರತಿ ತಿಂಗಳು ₹2,000',
                   None,
                   'ಹಣ DBT ಮೂಲಕ ಬರುತ್ತದೆ, ಹೆಚ್ಚಾಗಿ ತಿಂಗಳ ಮೊದಲಾರ್ಧದಲ್ಲಿ. ಸ್ವೀಕೃತಿ ಸಂಖ್ಯೆಯಿಂದ ಸೇವಾ ಸಿಂಧುವಿನಲ್ಲಿ ಸ್ಥಿತಿ '
                   'ನೋಡಿ.',
                   ('stuck',
                    'ಹಣ ಬಂದಿಲ್ಲವೇ? ಹೆಚ್ಚಾಗಿ ಆಧಾರ್ ಸಕ್ರಿಯ ಖಾತೆಗೆ ಜೋಡಣೆಯಾಗಿಲ್ಲ ಅಥವಾ DBT ಆಫ್ ಆಗಿರುತ್ತದೆ. ಬ್ಯಾಂಕಿನಲ್ಲಿ '
                    'ಸರಿಪಡಿಸಿ, ನಂತರ ಮತ್ತೆ ಸ್ಥಿತಿ ನೋಡಿ.'))],
        'rights_t': 'ಇನ್ನೂ ಹಣ ಬಂದಿಲ್ಲವೇ? ಸಹಾಯ ಪಡೆಯಿರಿ.',
        'rights': 'ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳ ಸಹಾಯವಾಣಿ <b>1902</b> ಗೆ ಕರೆ ಮಾಡಿ, ತಾಲೂಕು <b>ಮಹಿಳಾ ಮತ್ತು ಮಕ್ಕಳ ಅಭಿವೃದ್ಧಿ</b> '
                  'ಕಚೇರಿಗೆ ಭೇಟಿ ನೀಡಿ, ಅಥವಾ <b>IPGRS</b> ನಲ್ಲಿ ದೂರು ನೀಡಿ.',
        'help': '<b>ಅರ್ಜಿ / ಸ್ಥಿತಿ:</b> sevasindhugs.karnataka.gov.in, ಗ್ರಾಮ ಒನ್, ಕರ್ನಾಟಕ ಒನ್ · <b>ಸಹಾಯವಾಣಿ:</b> '
                '1902<br><b>ಅರ್ಜಿ ಉಚಿತ</b> · <b>OTP ಯಾರಿಗೂ ಕೊಡಬೇಡಿ</b>'}}
