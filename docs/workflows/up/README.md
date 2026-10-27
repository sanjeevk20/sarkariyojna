# Sathi Workflow Guides - Uttar Pradesh

Step-by-step citizen guides (English + Hindi) and team system workflows for Uttar Pradesh services. Same format as the Maharashtra guides in the parent folder.

> **Status:** 12 guides written on 27 Oct 2026 from news, district / central government pages and secondary sources. UP state portals could not be opened from the research environment, so amounts and limits marked *reported* need checking against the current government orders, and **Hindi text still needs native-speaker review**.

## Certificates and land

| Guide | Hindi name | For | English | Hindi |
|---|---|---|---|---|
| [Income certificate (UP)](up-income-certificate.md) | आय प्रमाण पत्र | Anyone applying to income-based schemes, scholarships, pensions | [EN](up-income-certificate-guide.png) | [HI](up-income-certificate-guide-hi.png) |
| [Caste certificate (UP)](up-caste-certificate.md) | जाति प्रमाण पत्र | SC / ST / OBC families | [EN](up-caste-certificate-guide.png) | [HI](up-caste-certificate-guide-hi.png) |
| [Domicile certificate (UP)](up-domicile-certificate.md) | निवास प्रमाण पत्र | Students and job seekers needing UP residence proof | [EN](up-domicile-certificate-guide.png) | [HI](up-domicile-certificate-guide-hi.png) |
| [Dakhil-kharij (UP land mutation)](up-dakhil-kharij.md) | दाखिल-खारिज | Land buyers, gift receivers (heirs: varasat) | [EN](up-dakhil-kharij-guide.png) | [HI](up-dakhil-kharij-guide-hi.png) |

## Pensions and food

| Guide | Hindi name | For | English | Hindi |
|---|---|---|---|---|
| [Vridhavastha Pension (UP old-age pension)](up-old-age-pension.md) | वृद्धावस्था पेंशन | Seniors 60+ with low income | [EN](up-old-age-pension-guide.png) | [HI](up-old-age-pension-guide-hi.png) |
| [Nirashrit Mahila Pension (UP widow pension)](up-widow-pension.md) | निराश्रित महिला पेंशन | Widows 18+ with low family income | [EN](up-widow-pension-guide.png) | [HI](up-widow-pension-guide-hi.png) |
| [Ration card (UP, NFSA)](up-ration-card.md) | राशन कार्ड | Low-income households | [EN](up-ration-card-guide.png) | [HI](up-ration-card-guide-hi.png) |

## Women and girls

| Guide | Hindi name | For | English | Hindi |
|---|---|---|---|---|
| [Kanya Sumangala Yojana](up-kanya-sumangala.md) | मुख्यमंत्री कन्या सुमंगला योजना | Families with daughters, income up to ₹3 lakh | [EN](up-kanya-sumangala-guide.png) | [HI](up-kanya-sumangala-guide-hi.png) |
| [Mukhyamantri Samuhik Vivah Yojana](up-samuhik-vivah.md) | मुख्यमंत्री सामूहिक विवाह योजना | Low-income families marrying a daughter | [EN](up-samuhik-vivah-guide.png) | [HI](up-samuhik-vivah-guide-hi.png) |

## Education

| Guide | Hindi name | For | English | Hindi |
|---|---|---|---|---|
| [UP Scholarship (pre and post-matric)](up-scholarship.md) | यूपी छात्रवृत्ति | Students from Class 9 to college | [EN](up-scholarship-guide.png) | [HI](up-scholarship-guide-hi.png) |

## Farmers

| Guide | Hindi name | For | English | Hindi |
|---|---|---|---|---|
| [PM-KISAN (Uttar Pradesh)](up-pm-kisan.md) | पीएम-किसान (उत्तर प्रदेश) | Landholding farmers in UP | [EN](up-pm-kisan-guide.png) | [HI](up-pm-kisan-guide-hi.png) |

## Business loans

| Guide | Hindi name | For | English | Hindi |
|---|---|---|---|---|
| [CM-YUVA (Yuva Udyami loan)](up-cm-yuva.md) | मुख्यमंत्री युवा उद्यमी विकास अभियान | Young people 21–40 starting a small business | [EN](up-cm-yuva-guide.png) | [HI](up-cm-yuva-guide-hi.png) |

## Quick routers

- **Certificates chain:** [Income](up-income-certificate.md) → [Caste](up-caste-certificate.md) → [Domicile](up-domicile-certificate.md) → [Scholarship](up-scholarship.md)
- **Pensions:** 60+ → [Old-age pension](up-old-age-pension.md); widow → [Nirashrit Mahila Pension](up-widow-pension.md)
- **Daughters:** birth to college → [Kanya Sumangala](up-kanya-sumangala.md); wedding → [Samuhik Vivah](up-samuhik-vivah.md)
- **Farmers:** land not in your name → [Dakhil-kharij](up-dakhil-kharij.md), then [PM-KISAN (UP)](up-pm-kisan.md)
- **Food:** [Ration card](up-ration-card.md) · **Business:** [CM-YUVA loan](up-cm-yuva.md)

## Adding a UP guide

Same steps as the Maharashtra guides, run from this folder: `python3 ../gen_guide.py up_<name>_content.py` writes `<out>.html` and `<out>-hi.html` here. Add a row above, then rebuild the website with `python3 ../../site/build_site.py`.
