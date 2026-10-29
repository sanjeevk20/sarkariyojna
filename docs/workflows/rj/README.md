# Sathi Workflow Guides - Rajasthan

Step-by-step citizen guides (English + Hindi) and team system workflows for Rajasthan services. Most Rajasthan services start from the family Jan Aadhaar, so read that guide first. Same format as the Maharashtra, Uttar Pradesh, Karnataka and Madhya Pradesh guides.

> **Status:** 10 guides written on 28 Oct 2026 from news, district / central government pages and secondary sources. Rajasthan state portals could not be opened from the research environment, so amounts and dates marked *reported* need checking against current government orders, and **Hindi text still needs native-speaker review**.

## Jan Aadhaar, certificates and land

| Guide | Hindi name | For | English | Hindi |
|---|---|---|---|---|
| [Jan Aadhaar card (Rajasthan)](rj-jan-aadhaar.md) | जन आधार कार्ड | Every family living in Rajasthan | [EN](rj-jan-aadhaar-guide.png) | [HI](rj-jan-aadhaar-guide-hi.png) |
| [Income certificate (Rajasthan)](rj-income-certificate.md) | आय प्रमाण पत्र | Anyone in Rajasthan who needs proof of family income | [EN](rj-income-certificate-guide.png) | [HI](rj-income-certificate-guide-hi.png) |
| [Mool Niwas (domicile) certificate (Rajasthan)](rj-mool-niwas.md) | मूल निवास प्रमाण पत्र | Residents of Rajasthan applying for jobs, admissions or quotas | [EN](rj-mool-niwas-guide.png) | [HI](rj-mool-niwas-guide-hi.png) |
| [Caste certificate (Rajasthan)](rj-caste-certificate.md) | जाति प्रमाण पत्र | SC, ST, OBC, MBC families in Rajasthan | [EN](rj-caste-certificate-guide.png) | [HI](rj-caste-certificate-guide-hi.png) |
| [Land mutation / Namantaran (Rajasthan)](rj-land-mutation.md) | नामांतरण (भूमि दाखिल-खारिज) | Buyers, heirs, gift or partition receivers of farm land in Rajasthan | [EN](rj-land-mutation-guide.png) | [HI](rj-land-mutation-guide-hi.png) |

## Pensions and food

| Guide | Hindi name | For | English | Hindi |
|---|---|---|---|---|
| [Social security pension (Rajasthan)](rj-social-pension.md) | सामाजिक सुरक्षा पेंशन | Elderly, widowed, divorced / abandoned women and disabled people in Rajasthan | [EN](rj-social-pension-guide.png) | [HI](rj-social-pension-guide-hi.png) |
| [Ration card and food security (Rajasthan)](rj-ration-card.md) | राशन कार्ड और खाद्य सुरक्षा | Low-income families in Rajasthan | [EN](rj-ration-card-guide.png) | [HI](rj-ration-card-guide-hi.png) |

## Women and girls

| Guide | Hindi name | For | English | Hindi |
|---|---|---|---|---|
| [Lado Protsahan Yojana (Rajasthan)](rj-lado-protsahan.md) | लाडो प्रोत्साहन योजना | Families with a girl born in a government or approved hospital in Rajasthan | [EN](rj-lado-protsahan-guide.png) | [HI](rj-lado-protsahan-guide-hi.png) |

## Health

| Guide | Hindi name | For | English | Hindi |
|---|---|---|---|---|
| [MAA Yojana health cover (Rajasthan)](rj-maa-yojana.md) | मुख्यमंत्री आयुष्मान आरोग्य (मा) योजना | Families in Rajasthan; free for NFSA, SECC, small farmers and contract workers | [EN](rj-maa-yojana-guide.png) | [HI](rj-maa-yojana-guide-hi.png) |

## Farmers

| Guide | Hindi name | For | English | Hindi |
|---|---|---|---|---|
| [PM-KISAN + CM Kisan Samman Nidhi (Rajasthan)](rj-kisan-samman.md) | पीएम-किसान + मुख्यमंत्री किसान सम्मान निधि | Land-holding farmer families in Rajasthan | [EN](rj-kisan-samman-guide.png) | [HI](rj-kisan-samman-guide-hi.png) |

## Quick routers

- **Start here:** almost everything needs your family's [Jan Aadhaar](rj-jan-aadhaar.md), with names matching Aadhaar
- **Certificates:** [Income](rj-income-certificate.md), [Mool Niwas](rj-mool-niwas.md), [Caste](rj-caste-certificate.md)
- **Farmers:** land not in your name → [Namantaran](rj-land-mutation.md), then [PM-KISAN + CM Kisan Samman Nidhi](rj-kisan-samman.md)
- **Seniors, widows, food:** [Pension and yearly verification](rj-social-pension.md) · [Food security ration](rj-ration-card.md)
- **Daughters:** [Lado Protsahan ₹1.5 lakh](rj-lado-protsahan.md) · **Hospital:** [MAA Yojana](rj-maa-yojana.md)

## Adding a Rajasthan guide

Run from this folder: `python3 ../gen_guide.py rj_<name>_content.py` writes `<out>.html` and `<out>-hi.html` here. Add a row above, then rebuild the website with `python3 ../../site/build_site.py`.
