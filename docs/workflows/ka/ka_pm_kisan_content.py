"""PM-KISAN (Karnataka, FRUITS) guide content (EN + KN)."""

OUT = "ka-pm-kisan-guide"
PHASE_BREAK = 5

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'PM-KISAN in Karnataka: Register through FRUITS',
        'sub': 'ಕರ್ನಾಟಕದಲ್ಲಿ ಪಿಎಂ-ಕಿಸಾನ್: ಫ್ರೂಟ್ಸ್ ಮೂಲಕ ನೋಂದಣಿ',
        'benefit': '₹2,000 into your bank account, three times a year',
        'legend': ['You do this', 'Government does this (you wait)', 'Money received'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you can get it',
                   'ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ',
                   'Your name must be on the <b>RTC (pahani)</b>. You <b>cannot</b> get it if someone in the family '
                   'pays income tax, holds a government job, or is a practising doctor, lawyer, CA or engineer.',
                   ('stuck',
                    "Land still in a parent's name? Get the mutation done first. See the <b>Land mutation "
                    '(Karnataka)</b> guide.')),
                  ('you',
                   'Get your FRUITS ID',
                   'ಫ್ರೂಟ್ಸ್ ಐಡಿ ಪಡೆಯಿರಿ',
                   'Karnataka uses <b>FRUITS</b>, a farmer database linked to <b>Bhoomi</b>, to match your Aadhaar '
                   'name with the RTC. Register at the <b>Raitha Samparka Kendra</b> or on fruits.karnataka.gov.in.',
                   ('tip',
                    'Your FRUITS ID is also used for crop insurance, input subsidies and crop loans. Keep it handy.')),
                  ('you',
                   'Keep these papers ready',
                   'ದಾಖಲೆಗಳನ್ನು ಸಿದ್ಧವಾಗಿಡಿ',
                   '<ul><li>RTC (pahani)</li><li>Aadhaar</li><li>Bank passbook (account <b>linked to '
                   'Aadhaar</b>)</li><li>Mobile linked to Aadhaar</li></ul>',
                   None),
                  ('you',
                   'Register for PM-KISAN',
                   'ಪಿಎಂ-ಕಿಸಾನ್\u200cಗೆ ನೋಂದಾಯಿಸಿ',
                   'Register on <b>pmkisan.gov.in</b>, through <b>Seva Sindhu</b>, or at the Raitha Samparka Kendra. '
                   'Note your <b>registration number</b>.',
                   None),
                  ('gov',
                   'Land and name verification',
                   'ಭೂಮಿ ಮತ್ತು ಹೆಸರಿನ ಪರಿಶೀಲನೆ',
                   'FRUITS compares the RTC owner name with your Aadhaar name; the state then approves you.',
                   ('stuck',
                    'Name mismatch between Aadhaar and RTC? Correct one of them (Aadhaar centre or taluk office), then '
                    'ask the Raitha Samparka Kendra to re-verify.')),
                  ('you',
                   'Do eKYC',
                   'ಇ-ಕೆವೈಸಿ ಮಾಡಿ',
                   'Complete eKYC by OTP on pmkisan.gov.in, face authentication in the PM-KISAN app, or fingerprint at '
                   'a CSC.',
                   ('stuck', 'Without eKYC, payments <b>stop</b>.')),
                  ('gov',
                   'Payment processed',
                   'ಪಾವತಿ ಪ್ರಕ್ರಿಯೆ',
                   'Status shows <span class="status">RFT signed by State Govt</span>, then <span class="status">FTO '
                   'generated</span>. Just wait.',
                   None),
                  ('done',
                   '₹2,000 in your account',
                   'ಖಾತೆಗೆ ₹2,000',
                   'You get an SMS. This repeats every four months while eKYC, land seeding and bank linking stay '
                   'correct.',
                   None)],
        'rights_t': 'Instalment missing? Complain.',
        'rights': 'Check status on pmkisan.gov.in, then contact the <b>Raitha Samparka Kendra</b> / Assistant Director '
                  'of Agriculture, or the PM-KISAN helpline <b>155261 / 011-24300606</b>.',
        'help': '<b>Register / status:</b> pmkisan.gov.in · <b>FRUITS:</b> fruits.karnataka.gov.in · <b>Helpline:</b> '
                '155261 / 011-24300606<br><b>Use only official websites</b> · <b>Never pay an agent</b>'},
 'kn': {'lang': 'kn',
        'font': "'Noto Sans Kannada','Noto Sans','FreeSans',sans-serif",
        'h1': 'ಕರ್ನಾಟಕದಲ್ಲಿ ಪಿಎಂ-ಕಿಸಾನ್: ಫ್ರೂಟ್ಸ್ ಮೂಲಕ ನೋಂದಣಿ',
        'sub': None,
        'benefit': 'ವರ್ಷಕ್ಕೆ ಮೂರು ಬಾರಿ ₹2,000 ನೇರವಾಗಿ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ',
        'legend': ['ಇದನ್ನು ನೀವು ಮಾಡಿ', 'ಇದನ್ನು ಸರ್ಕಾರ ಮಾಡುತ್ತದೆ (ನೀವು ಕಾಯಿರಿ)', 'ಹಣ ಬಂದಿದೆ'],
        'phases': ['ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮೊದಲು', 'ಅರ್ಜಿ ಸಲ್ಲಿಸಿದ ನಂತರ'],
        'who': {'you': 'ನೀವು', 'gov': 'ಸರ್ಕಾರ', 'done': 'ಪೂರ್ಣ'},
        'stuck': 'ತೊಂದರೆಯೇ?',
        'tip': 'ಸಲಹೆ:',
        'steps': [('you',
                   'ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ',
                   None,
                   'ನಿಮ್ಮ ಹೆಸರು <b>ಪಹಣಿ (RTC)</b>ಯಲ್ಲಿ ಇರಬೇಕು. ಕುಟುಂಬದಲ್ಲಿ ಯಾರಾದರೂ ಆದಾಯ ತೆರಿಗೆ ಕಟ್ಟುತ್ತಿದ್ದರೆ, ಸರ್ಕಾರಿ '
                   'ಉದ್ಯೋಗದಲ್ಲಿದ್ದರೆ, ಅಥವಾ ವೃತ್ತಿನಿರತ ವೈದ್ಯ, ವಕೀಲ, CA ಅಥವಾ ಎಂಜಿನಿಯರ್ ಆಗಿದ್ದರೆ ಸೌಲಭ್ಯ '
                   '<b>ಸಿಗುವುದಿಲ್ಲ</b>.',
                   ('stuck',
                    'ಭೂಮಿ ಇನ್ನೂ ಪೋಷಕರ ಹೆಸರಿನಲ್ಲಿದೆಯೇ? ಮೊದಲು ಮ್ಯುಟೇಶನ್ ಮಾಡಿಸಿ. <b>ಭೂ ಮ್ಯುಟೇಶನ್ (ಕರ್ನಾಟಕ)</b> ಮಾರ್ಗದರ್ಶಿ '
                    'ನೋಡಿ.')),
                  ('you',
                   'ಫ್ರೂಟ್ಸ್ ಐಡಿ ಪಡೆಯಿರಿ',
                   None,
                   'ಕರ್ನಾಟಕವು ನಿಮ್ಮ ಆಧಾರ್ ಹೆಸರನ್ನು ಪಹಣಿಯೊಂದಿಗೆ ಹೋಲಿಸಲು <b>ಭೂಮಿ</b>ಗೆ ಜೋಡಿಸಿದ ರೈತ ದತ್ತಾಂಶ <b>ಫ್ರೂಟ್ಸ್ '
                   '(FRUITS)</b> ಬಳಸುತ್ತದೆ. <b>ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ</b>ದಲ್ಲಿ ಅಥವಾ fruits.karnataka.gov.in ನಲ್ಲಿ '
                   'ನೋಂದಾಯಿಸಿ.',
                   ('tip', 'ನಿಮ್ಮ ಫ್ರೂಟ್ಸ್ ಐಡಿ ಬೆಳೆ ವಿಮೆ, ಸಹಾಯಧನ ಮತ್ತು ಬೆಳೆ ಸಾಲಕ್ಕೂ ಬಳಕೆಯಾಗುತ್ತದೆ. ಕೈಯಲ್ಲಿಡಿ.')),
                  ('you',
                   'ದಾಖಲೆಗಳನ್ನು ಸಿದ್ಧವಾಗಿಡಿ',
                   None,
                   '<ul><li>ಪಹಣಿ (RTC)</li><li>ಆಧಾರ್</li><li>ಬ್ಯಾಂಕ್ ಪಾಸ್\u200cಬುಕ್ (ಖಾತೆ <b>ಆಧಾರ್\u200cಗೆ '
                   'ಜೋಡಣೆ</b>)</li><li>ಆಧಾರ್\u200cಗೆ ಜೋಡಣೆಯಾದ ಮೊಬೈಲ್</li></ul>',
                   None),
                  ('you',
                   'ಪಿಎಂ-ಕಿಸಾನ್\u200cಗೆ ನೋಂದಾಯಿಸಿ',
                   None,
                   '<b>pmkisan.gov.in</b> ನಲ್ಲಿ, <b>ಸೇವಾ ಸಿಂಧು</b> ಮೂಲಕ, ಅಥವಾ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರದಲ್ಲಿ ನೋಂದಾಯಿಸಿ. '
                   '<b>ನೋಂದಣಿ ಸಂಖ್ಯೆ</b> ಬರೆದಿಡಿ.',
                   None),
                  ('gov',
                   'ಭೂಮಿ ಮತ್ತು ಹೆಸರಿನ ಪರಿಶೀಲನೆ',
                   None,
                   'ಫ್ರೂಟ್ಸ್ ಪಹಣಿಯ ಮಾಲೀಕರ ಹೆಸರನ್ನು ನಿಮ್ಮ ಆಧಾರ್ ಹೆಸರಿನೊಂದಿಗೆ ಹೋಲಿಸುತ್ತದೆ; ನಂತರ ರಾಜ್ಯ ಅನುಮೋದಿಸುತ್ತದೆ.',
                   ('stuck',
                    'ಆಧಾರ್ ಮತ್ತು ಪಹಣಿಯಲ್ಲಿ ಹೆಸರು ಹೊಂದಿಕೆಯಿಲ್ಲವೇ? ಒಂದನ್ನು ಸರಿಪಡಿಸಿ (ಆಧಾರ್ ಕೇಂದ್ರ ಅಥವಾ ತಾಲೂಕು ಕಚೇರಿ), '
                    'ನಂತರ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರದಲ್ಲಿ ಮರುಪರಿಶೀಲನೆ ಕೇಳಿ.')),
                  ('you',
                   'ಇ-ಕೆವೈಸಿ ಮಾಡಿ',
                   None,
                   'pmkisan.gov.in ನಲ್ಲಿ OTP ಮೂಲಕ, ಪಿಎಂ-ಕಿಸಾನ್ ಆ್ಯಪ್\u200cನಲ್ಲಿ ಮುಖ ದೃಢೀಕರಣದ ಮೂಲಕ, ಅಥವಾ CSC ಯಲ್ಲಿ '
                   'ಬೆರಳಚ್ಚಿನ ಮೂಲಕ ಇ-ಕೆವೈಸಿ ಮಾಡಿ.',
                   ('stuck', 'ಇ-ಕೆವೈಸಿ ಇಲ್ಲದೆ ಪಾವತಿ <b>ನಿಲ್ಲುತ್ತದೆ</b>.')),
                  ('gov',
                   'ಪಾವತಿ ಪ್ರಕ್ರಿಯೆ',
                   None,
                   'ಸ್ಥಿತಿಯಲ್ಲಿ <span class="status">RFT signed by State Govt</span>, ನಂತರ <span class="status">FTO '
                   'generated</span> ತೋರಿಸುತ್ತದೆ. ಕಾಯಿರಿ.',
                   None),
                  ('done',
                   'ಖಾತೆಗೆ ₹2,000',
                   None,
                   'ನಿಮಗೆ SMS ಬರುತ್ತದೆ. ಇ-ಕೆವೈಸಿ, ಭೂಮಿ ಜೋಡಣೆ ಮತ್ತು ಬ್ಯಾಂಕ್ ಜೋಡಣೆ ಸರಿಯಾಗಿರುವವರೆಗೆ ಪ್ರತಿ ನಾಲ್ಕು '
                   'ತಿಂಗಳಿಗೊಮ್ಮೆ ಬರುತ್ತದೆ.',
                   None)],
        'rights_t': 'ಕಂತು ಬಂದಿಲ್ಲವೇ? ದೂರು ನೀಡಿ.',
        'rights': 'pmkisan.gov.in ನಲ್ಲಿ ಸ್ಥಿತಿ ನೋಡಿ, ನಂತರ <b>ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ</b> / ಸಹಾಯಕ ಕೃಷಿ ನಿರ್ದೇಶಕರು, ಅಥವಾ '
                  'ಪಿಎಂ-ಕಿಸಾನ್ ಸಹಾಯವಾಣಿ <b>155261 / 011-24300606</b> ಸಂಪರ್ಕಿಸಿ.',
        'help': '<b>ನೋಂದಣಿ / ಸ್ಥಿತಿ:</b> pmkisan.gov.in · <b>ಫ್ರೂಟ್ಸ್:</b> fruits.karnataka.gov.in · <b>ಸಹಾಯವಾಣಿ:</b> '
                '155261 / 011-24300606<br><b>ಅಧಿಕೃತ ವೆಬ್\u200cಸೈಟ್ ಮಾತ್ರ ಬಳಸಿ</b> · <b>ಏಜೆಂಟ್\u200cಗೆ ಹಣ ಕೊಡಬೇಡಿ</b>'}}
