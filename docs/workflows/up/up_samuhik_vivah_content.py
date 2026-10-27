"""Mukhyamantri Samuhik Vivah Yojana guide content (EN + HI)."""

OUT = "up-samuhik-vivah-guide"
PHASE_BREAK = 4

T = {'en': {'lang': 'en',
        'font': "'Noto Sans','FreeSans',sans-serif",
        'h1': "Samuhik Vivah Yojana (UP): Help for your daughter's wedding",
        'sub': 'मुख्यमंत्री सामूहिक विवाह योजना: बेटी की शादी में सहायता',
        'benefit': "Reported ₹1 lakh per couple: ₹60,000 to the bride's account, gifts and the ceremony at a group "
                   'wedding',
        'legend': ['You do this', 'Government does this (you wait)', 'Assistance received'],
        'phases': ['Before the wedding', 'At and after the wedding'],
        'who': {'you': 'You', 'gov': 'Government', 'done': 'Done'},
        'stuck': 'Stuck?',
        'tip': 'Tip:',
        'steps': [('you',
                   'Check if you can get it',
                   'पात्रता जांचें',
                   '<ul><li>Bride <b>18+</b>, groom <b>21+</b></li><li>Family living in UP</li><li>Family income '
                   'within the limit (reported <b>₹3 lakh</b>; earlier ₹2 lakh)</li><li>Widows and divorced women can '
                   'also apply</li><li>The wedding happens at a <b>group ceremony</b> organised by the '
                   'district</li></ul>',
                   None),
                  ('you',
                   'Keep these papers ready',
                   'कागज़ तैयार रखें',
                   '<ul><li>Aadhaar of bride and groom</li><li>Age proof of both</li><li>Income '
                   "certificate</li><li>Bride's bank account (Aadhaar-linked)</li><li>Photos; caste certificate if "
                   'asked</li></ul>',
                   None),
                  ('you',
                   'Register before the ceremony',
                   'समारोह से पहले पंजीकरण',
                   'Register on <b>cmsvy.upsdc.gov.in</b> or through the block / municipal office, with <b>Aadhaar '
                   'eKYC</b> of both. Keep the registration slip.',
                   ('tip', "Registration is <b>free</b>. Nobody can sell you a 'seat' in the ceremony.")),
                  ('gov',
                   'Verification and list',
                   'सत्यापन और सूची',
                   'The <b>BDO</b> or urban local body verifies, and the couple is added to the ceremony list.',
                   ('stuck', 'Name not on the list? Ask the block or municipal office which document is pending.')),
                  ('you',
                   'Attend the group wedding',
                   'सामूहिक विवाह में शामिल हों',
                   "Come on the announced date with the bride's and groom's IDs. The marriage is solemnised at the "
                   'venue.',
                   None),
                  ('done',
                   'Assistance received',
                   'सहायता मिली',
                   "Money reaches the <b>bride's bank account</b> by DBT; gifts are handed over at the venue.",
                   ('stuck',
                    'Money not received weeks later? Check the account is Aadhaar-linked, then contact the District '
                    'Social Welfare Officer.'))],
        'rights_t': 'Payment missing? Complain.',
        'rights': 'Complain to the <b>District Social Welfare Officer</b>, on <b>IGRS Jansunwai</b> or the <b>CM '
                  'Helpline 1076</b> with the registration number.',
        'help': '<b>Register:</b> cmsvy.upsdc.gov.in · Amounts and income limit as reported; check the current '
                'notice<br><b>Registration is free</b> · <b>Use only official websites</b>'},
 'hi': {'lang': 'hi',
        'font': "'Noto Sans Devanagari','Noto Sans','FreeSans',sans-serif",
        'h1': 'सामूहिक विवाह योजना (उत्तर प्रदेश): बेटी की शादी में सहायता',
        'sub': None,
        'benefit': 'बताए अनुसार प्रति जोड़ा ₹1 लाख: ₹60,000 वधू के खाते में, उपहार और सामूहिक विवाह में समारोह',
        'legend': ['यह आप करें', 'यह सरकार करती है (आप प्रतीक्षा करें)', 'सहायता मिली'],
        'phases': ['विवाह से पहले', 'विवाह के समय और बाद'],
        'who': {'you': 'आप', 'gov': 'सरकार', 'done': 'पूरा'},
        'stuck': 'अटक गए?',
        'tip': 'सुझाव:',
        'steps': [('you',
                   'पात्रता जांचें',
                   None,
                   '<ul><li>वधू <b>18+</b>, वर <b>21+</b> वर्ष</li><li>परिवार उत्तर प्रदेश में रहता '
                   'हो</li><li>पारिवारिक आय सीमा के भीतर (बताई गई <b>₹3 लाख</b>; पहले ₹2 लाख)</li><li>विधवा और '
                   'तलाकशुदा महिलाएं भी आवेदन कर सकती हैं</li><li>विवाह ज़िले द्वारा आयोजित <b>सामूहिक समारोह</b> में '
                   'होता है</li></ul>',
                   None),
                  ('you',
                   'कागज़ तैयार रखें',
                   None,
                   '<ul><li>वर और वधू का आधार</li><li>दोनों की उम्र का प्रमाण</li><li>आय प्रमाण पत्र</li><li>वधू का '
                   'बैंक खाता (आधार से जुड़ा)</li><li>फोटो; मांगे जाने पर जाति प्रमाण पत्र</li></ul>',
                   None),
                  ('you',
                   'समारोह से पहले पंजीकरण',
                   None,
                   '<b>cmsvy.upsdc.gov.in</b> पर या ब्लॉक / नगर निकाय कार्यालय से, दोनों के <b>आधार ई-केवाईसी</b> के '
                   'साथ पंजीकरण करें। पंजीकरण पर्ची रखें।',
                   ('tip', "पंजीकरण <b>मुफ़्त</b> है। समारोह में 'सीट' कोई नहीं बेच सकता।")),
                  ('gov',
                   'सत्यापन और सूची',
                   None,
                   '<b>बीडीओ</b> या नगर निकाय सत्यापन करता है और जोड़े को समारोह सूची में जोड़ा जाता है।',
                   ('stuck', 'सूची में नाम नहीं? ब्लॉक या नगर निकाय कार्यालय से पूछें कि कौन सा दस्तावेज़ बाकी है।')),
                  ('you',
                   'सामूहिक विवाह में शामिल हों',
                   None,
                   'घोषित तारीख पर वर-वधू के पहचान पत्र लेकर आएं। विवाह स्थल पर ही संपन्न होता है।',
                   None),
                  ('done',
                   'सहायता मिली',
                   None,
                   'राशि डीबीटी से <b>वधू के बैंक खाते</b> में आती है; उपहार समारोह स्थल पर दिए जाते हैं।',
                   ('stuck',
                    'हफ्तों बाद भी राशि नहीं? खाता आधार से जुड़ा है यह जांचें, फिर ज़िला समाज कल्याण अधिकारी से संपर्क '
                    'करें।'))],
        'rights_t': 'भुगतान नहीं मिला? शिकायत करें।',
        'rights': 'पंजीकरण संख्या के साथ <b>ज़िला समाज कल्याण अधिकारी</b>, <b>आईजीआरएस जनसुनवाई</b> या <b>मुख्यमंत्री '
                  'हेल्पलाइन 1076</b> पर शिकायत करें।',
        'help': '<b>पंजीकरण:</b> cmsvy.upsdc.gov.in · राशि और आय सीमा बताए अनुसार; वर्तमान सूचना देखें<br><b>पंजीकरण '
                'मुफ़्त है</b> · <b>केवल आधिकारिक वेबसाइट का उपयोग करें</b>'}}
