"""Land mutation and RTC update (Karnataka) guide content (EN + KN)."""

OUT = "ka-land-mutation-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': 'Land Mutation (Karnataka): Get your name on the RTC (pahani)',
        'sub': 'ಭೂ ಮ್ಯುಟೇಶನ್: ಪಹಣಿಯಲ್ಲಿ ನಿಮ್ಮ ಹೆಸರು ದಾಖಲಿಸಿ',
        'benefit': 'Your name in the land record, needed for crop loans, PM-KISAN, sale and compensation',
        'legend': ['You do this', 'Government does this (you wait)', 'Name on RTC'],
        'phases': ['At registration', 'After registration'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Register the sale or gift deed',
                   'ಕ್ರಯ ಅಥವಾ ದಾನ ಪತ್ರ ನೋಂದಾಯಿಸಿ',
                   'Register at the <b>Sub-Registrar office</b> (Kaveri 2.0). Make sure names and survey / hissa '
                   'numbers match the RTC exactly.',
                   ('stuck',
                    'A spelling or survey-number mismatch can make automatic mutation <b>fail silently</b>. Check the '
                    'deed against the RTC before you sign.')),
                  ('gov',
                   'Mutation starts automatically',
                   'ಮ್ಯುಟೇಶನ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಆರಂಭ',
                   'Registration sends a <b>J-slip</b> from Kaveri to <b>Bhoomi</b>, which opens a mutation entry '
                   '(MR).',
                   ('tip',
                    'For land you inherit, there is no deed. Ask the <b>Village Accountant</b> or Nadakacheri about '
                    'mutation by succession.')),
                  ('you',
                   'Watch for the MR entry',
                   'MR ನಮೂದನ್ನು ಗಮನಿಸಿ',
                   'On <b>landrecords.karnataka.gov.in</b> (View RTC and MR), search by district, taluk, hobli, '
                   'village and survey number.',
                   ('stuck',
                    'No MR entry two weeks after registration? Go to the <b>taluk Bhoomi centre</b> with the deed. The '
                    'system does not alert you.')),
                  ('gov',
                   'Notice and objection period',
                   'ನೋಟಿಸ್ ಮತ್ತು ಆಕ್ಷೇಪಣೆ ಅವಧಿ',
                   'Notice is issued to the parties. If nobody objects, the mutation is approved after the notice '
                   'period.',
                   ('stuck',
                    'Someone objected? The case becomes disputed and goes to the revenue officer for a hearing. Bring '
                    'the deed and witnesses.')),
                  ('gov',
                   'Mutation approved',
                   'ಮ್ಯುಟೇಶನ್ ಅನುಮೋದನೆ',
                   'The revenue officer certifies the mutation and Bhoomi updates the owner column.',
                   None),
                  ('done',
                   'Your name on the RTC',
                   'ಪಹಣಿಯಲ್ಲಿ ನಿಮ್ಮ ಹೆಸರು',
                   'Download the updated RTC and mutation extract from Bhoomi.',
                   ('stuck',
                    'Order wrong or rejected? An appeal usually lies with the <b>Assistant Commissioner</b>. Ask the '
                    'taluk office for the time limit.'))],
        'rights_t': 'Stuck for weeks? Escalate.',
        'rights': 'Visit the <b>Tahsildar</b> with the registration number and RTC copy, or complain on <b>IPGRS</b>.',
        'help': '<b>RTC and MR:</b> landrecords.karnataka.gov.in · <b>Registration:</b> Kaveri 2.0 · Urban khata '
                'updates on a separate system<br><b>Use only official websites</b> · <b>Never pay a tout</b>'},
 'kn': {'lang': 'kn',
        'font': "'Noto Sans Kannada','Noto Sans','FreeSans',sans-serif",
        'h1': 'ಭೂ ಮ್ಯುಟೇಶನ್ (ಕರ್ನಾಟಕ): ಪಹಣಿಯಲ್ಲಿ (RTC) ನಿಮ್ಮ ಹೆಸರು ದಾಖಲಿಸಿ',
        'sub': None,
        'benefit': 'ಭೂ ದಾಖಲೆಯಲ್ಲಿ ನಿಮ್ಮ ಹೆಸರು; ಬೆಳೆ ಸಾಲ, ಪಿಎಂ-ಕಿಸಾನ್, ಮಾರಾಟ ಮತ್ತು ಪರಿಹಾರಕ್ಕೆ ಅಗತ್ಯ',
        'legend': ['ಇದನ್ನು ನೀವು ಮಾಡಿ', 'ಇದನ್ನು ಸರ್ಕಾರ ಮಾಡುತ್ತದೆ (ನೀವು ಕಾಯಿರಿ)', 'ಪಹಣಿಯಲ್ಲಿ ಹೆಸರು'],
        'phases': ['ನೋಂದಣಿ ಸಮಯದಲ್ಲಿ', 'ನೋಂದಣಿಯ ನಂತರ'],
        'who': {'you': 'ನೀವು', 'gov': 'ಸರ್ಕಾರ', 'done': 'ಪೂರ್ಣ'},
        'stuck': 'ತೊಂದರೆಯೇ?',
        'tip': 'ಸಲಹೆ:',
        'steps': [('you',
                   'ಕ್ರಯ ಅಥವಾ ದಾನ ಪತ್ರ ನೋಂದಾಯಿಸಿ',
                   None,
                   '<b>ಉಪ ನೋಂದಣಾಧಿಕಾರಿ ಕಚೇರಿಯಲ್ಲಿ</b> (ಕಾವೇರಿ 2.0) ನೋಂದಾಯಿಸಿ. ಹೆಸರುಗಳು ಮತ್ತು ಸರ್ವೆ / ಹಿಸ್ಸಾ ಸಂಖ್ಯೆಗಳು '
                   'ಪಹಣಿಯೊಂದಿಗೆ ಸರಿಯಾಗಿ ಹೊಂದಿಕೆಯಾಗಲಿ.',
                   ('stuck',
                    'ಹೆಸರಿನ ಕಾಗುಣಿತ ಅಥವಾ ಸರ್ವೆ ಸಂಖ್ಯೆ ಹೊಂದಿಕೆಯಾಗದಿದ್ದರೆ ಸ್ವಯಂ ಮ್ಯುಟೇಶನ್ <b>ಸದ್ದಿಲ್ಲದೆ '
                    'ವಿಫಲವಾಗಬಹುದು</b>. ಸಹಿ ಮಾಡುವ ಮೊದಲು ಪತ್ರವನ್ನು ಪಹಣಿಯೊಂದಿಗೆ ಹೋಲಿಸಿ.')),
                  ('gov',
                   'ಮ್ಯುಟೇಶನ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಆರಂಭ',
                   None,
                   'ನೋಂದಣಿಯಾದಾಗ ಕಾವೇರಿಯಿಂದ <b>ಭೂಮಿ</b>ಗೆ <b>ಜೆ-ಸ್ಲಿಪ್</b> ಹೋಗುತ್ತದೆ, ಅದು ಮ್ಯುಟೇಶನ್ ನಮೂದು (MR) '
                   'ತೆರೆಯುತ್ತದೆ.',
                   ('tip',
                    'ಪಿತ್ರಾರ್ಜಿತ ಭೂಮಿಗೆ ಪತ್ರ ಇರುವುದಿಲ್ಲ. ವಾರಸಾ ಮ್ಯುಟೇಶನ್ ಬಗ್ಗೆ <b>ಗ್ರಾಮ ಲೆಕ್ಕಾಧಿಕಾರಿ</b> ಅಥವಾ '
                    'ನಾಡಕಚೇರಿಯಲ್ಲಿ ಕೇಳಿ.')),
                  ('you',
                   'MR ನಮೂದನ್ನು ಗಮನಿಸಿ',
                   None,
                   '<b>landrecords.karnataka.gov.in</b> ನಲ್ಲಿ (View RTC and MR) ಜಿಲ್ಲೆ, ತಾಲೂಕು, ಹೋಬಳಿ, ಗ್ರಾಮ ಮತ್ತು '
                   'ಸರ್ವೆ ಸಂಖ್ಯೆಯಿಂದ ಹುಡುಕಿ.',
                   ('stuck',
                    'ನೋಂದಣಿಯ ಎರಡು ವಾರಗಳ ನಂತರವೂ MR ನಮೂದು ಇಲ್ಲವೇ? ಪತ್ರದೊಂದಿಗೆ <b>ತಾಲೂಕು ಭೂಮಿ ಕೇಂದ್ರಕ್ಕೆ</b> ಹೋಗಿ. '
                    'ವ್ಯವಸ್ಥೆ ನಿಮಗೆ ತಿಳಿಸುವುದಿಲ್ಲ.')),
                  ('gov',
                   'ನೋಟಿಸ್ ಮತ್ತು ಆಕ್ಷೇಪಣೆ ಅವಧಿ',
                   None,
                   'ಸಂಬಂಧಿಸಿದವರಿಗೆ ನೋಟಿಸ್ ಹೋಗುತ್ತದೆ. ಯಾರೂ ಆಕ್ಷೇಪಿಸದಿದ್ದರೆ ನೋಟಿಸ್ ಅವಧಿಯ ನಂತರ ಮ್ಯುಟೇಶನ್ '
                   'ಅನುಮೋದನೆಯಾಗುತ್ತದೆ.',
                   ('stuck',
                    'ಯಾರಾದರೂ ಆಕ್ಷೇಪಿಸಿದರೆ? ಪ್ರಕರಣ ವಿವಾದಿತವಾಗಿ ಕಂದಾಯ ಅಧಿಕಾರಿಯ ಮುಂದೆ ವಿಚಾರಣೆಗೆ ಹೋಗುತ್ತದೆ. ಪತ್ರ ಮತ್ತು '
                    'ಸಾಕ್ಷಿಗಳನ್ನು ತನ್ನಿ.')),
                  ('gov',
                   'ಮ್ಯುಟೇಶನ್ ಅನುಮೋದನೆ',
                   None,
                   'ಕಂದಾಯ ಅಧಿಕಾರಿ ಮ್ಯುಟೇಶನ್ ದೃಢೀಕರಿಸುತ್ತಾರೆ ಮತ್ತು ಭೂಮಿಯಲ್ಲಿ ಮಾಲೀಕರ ಕಾಲಂ ನವೀಕರಣವಾಗುತ್ತದೆ.',
                   None),
                  ('done',
                   'ಪಹಣಿಯಲ್ಲಿ ನಿಮ್ಮ ಹೆಸರು',
                   None,
                   'ನವೀಕೃತ ಪಹಣಿ ಮತ್ತು ಮ್ಯುಟೇಶನ್ ಉದ್ಧರಣೆಯನ್ನು ಭೂಮಿಯಿಂದ ಡೌನ್\u200cಲೋಡ್ ಮಾಡಿ.',
                   ('stuck',
                    'ಆದೇಶ ತಪ್ಪಾಗಿದೆಯೇ ಅಥವಾ ತಿರಸ್ಕೃತವೇ? ಸಾಮಾನ್ಯವಾಗಿ <b>ಸಹಾಯಕ ಆಯುಕ್ತರಿಗೆ</b> ಮೇಲ್ಮನವಿ ಸಲ್ಲಿಸಬಹುದು. ಸಮಯ '
                    'ಮಿತಿಯನ್ನು ತಾಲೂಕು ಕಚೇರಿಯಲ್ಲಿ ಕೇಳಿ.'))],
        'rights_t': 'ವಾರಗಳಿಂದ ಅಡಚಣೆಯೇ? ಮೇಲಕ್ಕೆ ಕೊಂಡೊಯ್ಯಿರಿ.',
        'rights': 'ನೋಂದಣಿ ಸಂಖ್ಯೆ ಮತ್ತು ಪಹಣಿ ಪ್ರತಿಯೊಂದಿಗೆ <b>ತಹಶೀಲ್ದಾರ್</b> ಅವರನ್ನು ಭೇಟಿ ಮಾಡಿ, ಅಥವಾ <b>IPGRS</b> ನಲ್ಲಿ '
                  'ದೂರು ನೀಡಿ.',
        'help': '<b>ಪಹಣಿ ಮತ್ತು MR:</b> landrecords.karnataka.gov.in · <b>ನೋಂದಣಿ:</b> ಕಾವೇರಿ 2.0 · ನಗರದ ಖಾತೆ ಬೇರೆ '
                'ವ್ಯವಸ್ಥೆಯಲ್ಲಿ ನವೀಕರಣವಾಗುತ್ತದೆ<br><b>ಅಧಿಕೃತ ವೆಬ್\u200cಸೈಟ್ ಮಾತ್ರ ಬಳಸಿ</b> · <b>ಮಧ್ಯವರ್ತಿಗೆ ಹಣ '
                'ಕೊಡಬೇಡಿ</b>'}}
