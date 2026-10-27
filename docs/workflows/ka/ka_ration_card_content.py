"""Ration card and Anna Bhagya (Karnataka) guide content (EN + KN)."""

OUT = "ka-ration-card-guide"
PHASE_BREAK = 5

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Ration Card and Anna Bhagya: 10 kg rice per person',
        'sub': 'ಪಡಿತರ ಚೀಟಿ ಮತ್ತು ಅನ್ನಭಾಗ್ಯ: ಪ್ರತಿ ವ್ಯಕ್ತಿಗೆ 10 ಕೆಜಿ ಅಕ್ಕಿ',
        'benefit': '10 kg food grain per person a month for BPL (PHH) and Antyodaya families',
        'legend': ['You do this', 'Government does this (you wait)', 'Ration received'],
        'phases': ['Before you apply', 'After you apply'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Already have a BPL or AAY card?',
                   'ಈಗಾಗಲೇ BPL ಅಥವಾ AAY ಚೀಟಿ ಇದೆಯೇ?',
                   'Then you need <b>no separate application</b> for Anna Bhagya. Collect rice at your fair price '
                   'shop.',
                   None),
                  ('you',
                   'Check if you can get a BPL card',
                   'BPL ಚೀಟಿಗೆ ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ',
                   '<ul><li>Permanent Karnataka resident, with no ration card anywhere else</li><li>No government '
                   'employee or income-tax payer in the family</li><li>No four-wheeler (livelihood vehicles like taxis '
                   'and tractors are exceptions)</li><li>Village: not more than <b>3 hectares</b> of dry land; town: '
                   'no pucca house over <b>1,000 sq ft</b></li></ul>',
                   None),
                  ('you',
                   'Keep these papers ready',
                   'ದಾಖಲೆಗಳನ್ನು ಸಿದ್ಧವಾಗಿಡಿ',
                   '<ul><li>Aadhaar of <b>every family member</b></li><li>Income certificate '
                   '(Nadakacheri)</li><li>Address proof, photo of the head of family</li></ul>',
                   None),
                  ('you',
                   'Apply',
                   'ಅರ್ಜಿ ಸಲ್ಲಿಸಿ',
                   'Apply for a BPL / AAY card through the <b>Ahara</b> department at a <b>Grama One</b>, <b>Karnataka '
                   'One</b> or <b>Bapuji Seva Kendra</b> when applications are open. Keep the acknowledgement.',
                   ('tip',
                    'New-card windows open and close; ask the centre or the taluk food office whether applications are '
                    'being accepted now.')),
                  ('gov',
                   'Verification',
                   'ಪರಿಶೀಲನೆ',
                   'The <b>Food Inspector</b> / taluk food office checks your family and income.',
                   ('stuck',
                    'Rejected? Ask for the reason in writing and appeal to the <b>Deputy Director, Food</b> of your '
                    'district.')),
                  ('gov',
                   'Card issued',
                   'ಚೀಟಿ ವಿತರಣೆ',
                   'The card is approved and the family is attached to a <b>fair price shop</b>.',
                   None),
                  ('done',
                   'Collect rice every month',
                   'ಪ್ರತಿ ತಿಂಗಳು ಅಕ್ಕಿ ಪಡೆಯಿರಿ',
                   'A member gives a <b>fingerprint</b> at the shop and collects grain for every person on the card.',
                   ('stuck',
                    'Shop gives less or demands money? Ask for a receipt and call the food helpline <b>1967</b>.'))],
        'rights_t': 'Shortage or card pending? Complain.',
        'rights': 'Call the food helpline <b>1967</b>, contact the taluk food office, or complain on <b>IPGRS</b>.',
        'help': '<b>Card status and lists:</b> ahara.karnataka.gov.in · <b>Helpline:</b> 1967<br><b>Ration is your '
                'right; never pay extra</b> · <b>Use only official websites</b>'},
 'kn': {'lang': 'kn',
        'font': "'Noto Sans Kannada','Noto Sans','FreeSans',sans-serif",
        'h1': 'ಪಡಿತರ ಚೀಟಿ ಮತ್ತು ಅನ್ನಭಾಗ್ಯ: ಪ್ರತಿ ವ್ಯಕ್ತಿಗೆ 10 ಕೆಜಿ ಅಕ್ಕಿ',
        'sub': None,
        'benefit': 'BPL (PHH) ಮತ್ತು ಅಂತ್ಯೋದಯ ಕುಟುಂಬಗಳಿಗೆ ಪ್ರತಿ ವ್ಯಕ್ತಿಗೆ ತಿಂಗಳಿಗೆ 10 ಕೆಜಿ ಆಹಾರ ಧಾನ್ಯ',
        'legend': ['ಇದನ್ನು ನೀವು ಮಾಡಿ', 'ಇದನ್ನು ಸರ್ಕಾರ ಮಾಡುತ್ತದೆ (ನೀವು ಕಾಯಿರಿ)', 'ಪಡಿತರ ಸಿಕ್ಕಿದೆ'],
        'phases': ['ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮೊದಲು', 'ಅರ್ಜಿ ಸಲ್ಲಿಸಿದ ನಂತರ'],
        'who': {'you': 'ನೀವು', 'gov': 'ಸರ್ಕಾರ', 'done': 'ಪೂರ್ಣ'},
        'stuck': 'ತೊಂದರೆಯೇ?',
        'tip': 'ಸಲಹೆ:',
        'steps': [('you',
                   'ಈಗಾಗಲೇ BPL ಅಥವಾ AAY ಚೀಟಿ ಇದೆಯೇ?',
                   None,
                   'ಹಾಗಿದ್ದರೆ ಅನ್ನಭಾಗ್ಯಕ್ಕೆ <b>ಪ್ರತ್ಯೇಕ ಅರ್ಜಿ ಬೇಕಿಲ್ಲ</b>. ನಿಮ್ಮ ನ್ಯಾಯಬೆಲೆ ಅಂಗಡಿಯಲ್ಲಿ ಅಕ್ಕಿ ಪಡೆಯಿರಿ.',
                   None),
                  ('you',
                   'BPL ಚೀಟಿಗೆ ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ',
                   None,
                   '<ul><li>ಕರ್ನಾಟಕದ ಖಾಯಂ ನಿವಾಸಿ, ಬೇರೆಲ್ಲೂ ಪಡಿತರ ಚೀಟಿ ಇರಬಾರದು</li><li>ಕುಟುಂಬದಲ್ಲಿ ಸರ್ಕಾರಿ ನೌಕರರು ಅಥವಾ '
                   'ಆದಾಯ ತೆರಿಗೆದಾರರು ಇರಬಾರದು</li><li>ನಾಲ್ಕು ಚಕ್ರದ ವಾಹನ ಇರಬಾರದು (ಟ್ಯಾಕ್ಸಿ, ಟ್ರ್ಯಾಕ್ಟರ್\u200cನಂತಹ '
                   'ಜೀವನೋಪಾಯ ವಾಹನಗಳಿಗೆ ವಿನಾಯಿತಿ)</li><li>ಗ್ರಾಮ: <b>3 ಹೆಕ್ಟೇರ್</b>ಗಿಂತ ಹೆಚ್ಚು ಒಣಭೂಮಿ ಇರಬಾರದು; ನಗರ: '
                   '<b>1,000 ಚದರ ಅಡಿ</b>ಗಿಂತ ದೊಡ್ಡ ಪಕ್ಕಾ ಮನೆ ಇರಬಾರದು</li></ul>',
                   None),
                  ('you',
                   'ದಾಖಲೆಗಳನ್ನು ಸಿದ್ಧವಾಗಿಡಿ',
                   None,
                   '<ul><li><b>ಕುಟುಂಬದ ಪ್ರತಿಯೊಬ್ಬರ</b> ಆಧಾರ್</li><li>ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರ (ನಾಡಕಚೇರಿ)</li><li>ವಿಳಾಸ ಪುರಾವೆ, '
                   'ಕುಟುಂಬದ ಮುಖ್ಯಸ್ಥರ ಫೋಟೋ</li></ul>',
                   None),
                  ('you',
                   'ಅರ್ಜಿ ಸಲ್ಲಿಸಿ',
                   None,
                   'ಅರ್ಜಿಗಳು ತೆರೆದಿರುವಾಗ <b>ಆಹಾರ</b> ಇಲಾಖೆಯ ಮೂಲಕ <b>ಗ್ರಾಮ ಒನ್</b>, <b>ಕರ್ನಾಟಕ ಒನ್</b> ಅಥವಾ <b>ಬಾಪೂಜಿ '
                   'ಸೇವಾ ಕೇಂದ್ರ</b>ದಲ್ಲಿ BPL / AAY ಚೀಟಿಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ. ಸ್ವೀಕೃತಿ ಜೋಪಾನವಾಗಿಡಿ.',
                   ('tip',
                    'ಹೊಸ ಚೀಟಿಯ ಅರ್ಜಿ ಅವಧಿ ತೆರೆಯುತ್ತದೆ ಮತ್ತು ಮುಚ್ಚುತ್ತದೆ; ಈಗ ಅರ್ಜಿ ಸ್ವೀಕರಿಸುತ್ತಿದ್ದಾರೆಯೇ ಎಂದು ಕೇಂದ್ರ '
                    'ಅಥವಾ ತಾಲೂಕು ಆಹಾರ ಕಚೇರಿಯಲ್ಲಿ ಕೇಳಿ.')),
                  ('gov',
                   'ಪರಿಶೀಲನೆ',
                   None,
                   '<b>ಆಹಾರ ನಿರೀಕ್ಷಕರು</b> / ತಾಲೂಕು ಆಹಾರ ಕಚೇರಿ ನಿಮ್ಮ ಕುಟುಂಬ ಮತ್ತು ಆದಾಯ ಪರಿಶೀಲಿಸುತ್ತಾರೆ.',
                   ('stuck',
                    'ತಿರಸ್ಕೃತವಾಯಿತೇ? ಕಾರಣವನ್ನು ಲಿಖಿತವಾಗಿ ಕೇಳಿ ಮತ್ತು ನಿಮ್ಮ ಜಿಲ್ಲೆಯ <b>ಆಹಾರ ಉಪನಿರ್ದೇಶಕರಿಗೆ</b> ಮೇಲ್ಮನವಿ '
                    'ಸಲ್ಲಿಸಿ.')),
                  ('gov',
                   'ಚೀಟಿ ವಿತರಣೆ',
                   None,
                   'ಚೀಟಿ ಮಂಜೂರಾಗುತ್ತದೆ ಮತ್ತು ಕುಟುಂಬವನ್ನು ಒಂದು <b>ನ್ಯಾಯಬೆಲೆ ಅಂಗಡಿ</b>ಗೆ ಜೋಡಿಸಲಾಗುತ್ತದೆ.',
                   None),
                  ('done',
                   'ಪ್ರತಿ ತಿಂಗಳು ಅಕ್ಕಿ ಪಡೆಯಿರಿ',
                   None,
                   'ಒಬ್ಬ ಸದಸ್ಯರು ಅಂಗಡಿಯಲ್ಲಿ <b>ಬೆರಳಚ್ಚು</b> ನೀಡಿ ಚೀಟಿಯಲ್ಲಿರುವ ಎಲ್ಲರ ಧಾನ್ಯ ಪಡೆಯುತ್ತಾರೆ.',
                   ('stuck',
                    'ಅಂಗಡಿಯವರು ಕಡಿಮೆ ಕೊಡುತ್ತಾರೆಯೇ ಅಥವಾ ಹಣ ಕೇಳುತ್ತಾರೆಯೇ? ರಸೀದಿ ಕೇಳಿ ಮತ್ತು ಆಹಾರ ಸಹಾಯವಾಣಿ <b>1967</b> ಗೆ '
                    'ಕರೆ ಮಾಡಿ.'))],
        'rights_t': 'ಕೊರತೆ ಅಥವಾ ಚೀಟಿ ಬಾಕಿಯೇ? ದೂರು ನೀಡಿ.',
        'rights': 'ಆಹಾರ ಸಹಾಯವಾಣಿ <b>1967</b> ಗೆ ಕರೆ ಮಾಡಿ, ತಾಲೂಕು ಆಹಾರ ಕಚೇರಿ ಸಂಪರ್ಕಿಸಿ, ಅಥವಾ <b>IPGRS</b> ನಲ್ಲಿ ದೂರು '
                  'ನೀಡಿ.',
        'help': '<b>ಚೀಟಿ ಸ್ಥಿತಿ ಮತ್ತು ಪಟ್ಟಿ:</b> ahara.karnataka.gov.in · <b>ಸಹಾಯವಾಣಿ:</b> 1967<br><b>ಪಡಿತರ ನಿಮ್ಮ '
                'ಹಕ್ಕು; ಹೆಚ್ಚುವರಿ ಹಣ ಕೊಡಬೇಡಿ</b> · <b>ಅಧಿಕೃತ ವೆಬ್\u200cಸೈಟ್ ಮಾತ್ರ ಬಳಸಿ</b>'}}
