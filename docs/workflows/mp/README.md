# Sathi Workflow Guides - Madhya Pradesh

Step-by-step citizen guides (English + Hindi) and team system workflows for Madhya Pradesh services. Most MP services start from the family Samagra ID, so read that guide first. Same format as the Maharashtra, Uttar Pradesh and Karnataka guides.

> **Status:** 10 guides written on 28 Oct 2026 from news, district / central government pages and secondary sources. MP state portals could not be opened from the research environment, so amounts and dates marked *reported* need checking against current government orders, and **Hindi text still needs native-speaker review**.

## Samagra, certificates and land

| Guide | Hindi name | For | English | Hindi |
|---|---|---|---|---|
| [Samagra ID (MP)](mp-samagra-id.md) | समग्र आईडी | Every MP family: needed for almost all schemes | [EN](mp-samagra-id-guide.png) | [HI](mp-samagra-id-guide-hi.png) |
| [Income certificate (MP)](mp-income-certificate.md) | आय प्रमाण पत्र | Anyone applying to income-based schemes, scholarships | [EN](mp-income-certificate-guide.png) | [HI](mp-income-certificate-guide-hi.png) |
| [Domicile certificate (MP)](mp-domicile-certificate.md) | मूल निवासी प्रमाण पत्र | Students and job seekers needing MP residence proof | [EN](mp-domicile-certificate-guide.png) | [HI](mp-domicile-certificate-guide-hi.png) |
| [Caste certificate (MP)](mp-caste-certificate.md) | जाति प्रमाण पत्र | SC / ST / OBC families | [EN](mp-caste-certificate-guide.png) | [HI](mp-caste-certificate-guide-hi.png) |
| [Land mutation / naamantaran (MP)](mp-land-mutation.md) | नामांतरण | Land buyers, gift receivers, heirs | [EN](mp-land-mutation-guide.png) | [HI](mp-land-mutation-guide-hi.png) |

## Women and girls

| Guide | Hindi name | For | English | Hindi |
|---|---|---|---|---|
| [Ladli Behna Yojana (MP)](mp-ladli-behna.md) | मुख्यमंत्री लाड़ली बहना योजना | Women 21–60 in Madhya Pradesh, family income up to ₹2.5 lakh | [EN](mp-ladli-behna-guide.png) | [HI](mp-ladli-behna-guide-hi.png) |
| [Ladli Laxmi Yojana (MP)](mp-ladli-laxmi.md) | लाड़ली लक्ष्मी योजना | Families with a daughter born on or after 1 Jan 2006 | [EN](mp-ladli-laxmi-guide.png) | [HI](mp-ladli-laxmi-guide-hi.png) |

## Farmers

| Guide | Hindi name | For | English | Hindi |
|---|---|---|---|---|
| [PM-KISAN + CM Kisan Kalyan (MP)](mp-kisan-kalyan.md) | पीएम-किसान + मुख्यमंत्री किसान कल्याण | Landholding farmers in Madhya Pradesh | [EN](mp-kisan-kalyan-guide.png) | [HI](mp-kisan-kalyan-guide-hi.png) |

## Pensions and food

| Guide | Hindi name | For | English | Hindi |
|---|---|---|---|---|
| [Old-age and widow pension (MP)](mp-social-pension.md) | वृद्धावस्था एवं कल्याणी पेंशन | Seniors 60+, widows (Kalyani), persons with disabilities | [EN](mp-social-pension-guide.png) | [HI](mp-social-pension-guide-hi.png) |
| [Ration eligibility slip (MP)](mp-ration-card.md) | पात्रता पर्ची (राशन) | Low-income households | [EN](mp-ration-card-guide.png) | [HI](mp-ration-card-guide-hi.png) |

## Quick routers

- **Start here:** almost everything needs a [Samagra ID](mp-samagra-id.md) with eKYC
- **Women and girls:** monthly support → [Ladli Behna](mp-ladli-behna.md); daughters → [Ladli Laxmi](mp-ladli-laxmi.md)
- **Certificates:** [Income](mp-income-certificate.md), [Domicile](mp-domicile-certificate.md), [Caste](mp-caste-certificate.md)
- **Farmers:** land not in your name → [Naamantaran](mp-land-mutation.md), then [PM-KISAN + CM Kisan Kalyan](mp-kisan-kalyan.md)
- **Seniors, widows, food:** [Pensions](mp-social-pension.md) · [Ration eligibility slip](mp-ration-card.md)

## Adding an MP guide

Run from this folder: `python3 ../gen_guide.py mp_<name>_content.py` writes `<out>.html` and `<out>-hi.html` here. Add a row above, then rebuild the website with `python3 ../../site/build_site.py`.
