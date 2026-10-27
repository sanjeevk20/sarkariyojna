# Sathi Workflow Guides - Karnataka

Step-by-step citizen guides (English + Kannada) and team system workflows for Karnataka services, including the five guarantee schemes. Same format as the Maharashtra and Uttar Pradesh guides.

> **Status:** 10 guides written on 27 Oct 2026 from news, district / central government pages and secondary sources. Karnataka state portals could not be opened from the research environment, so amounts and rules marked *reported* need checking against current government orders, and **Kannada text still needs native-speaker review**. Not covered yet for lack of reliable sources: Ayushman Bharat - Arogya Karnataka card, widow pension amount.

## Certificates and land

| Guide | Kannada name | For | English | Kannada |
|---|---|---|---|---|
| [Caste and income certificate (Karnataka)](ka-caste-income-certificate.md) | ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರ | Students, job seekers, anyone applying to welfare schemes | [EN](ka-caste-income-certificate-guide.png) | [KN](ka-caste-income-certificate-guide-kn.png) |
| [Land mutation and RTC update (Karnataka)](ka-land-mutation.md) | ಪಹಣಿ ಖಾತೆ ಬದಲಾವಣೆ (ಮ್ಯುಟೇಶನ್) | Land buyers, gift receivers, heirs | [EN](ka-land-mutation-guide.png) | [KN](ka-land-mutation-guide-kn.png) |

## Women and family

| Guide | Kannada name | For | English | Kannada |
|---|---|---|---|---|
| [Gruha Lakshmi](ka-gruha-lakshmi.md) | ಗೃಹಲಕ್ಷ್ಮಿ | Woman head of the family on the ration card | [EN](ka-gruha-lakshmi-guide.png) | [KN](ka-gruha-lakshmi-guide-kn.png) |
| [Shakti (free bus travel for women)](ka-shakti.md) | ಶಕ್ತಿ ಯೋಜನೆ | Women and transgender persons living in Karnataka | [EN](ka-shakti-guide.png) | [KN](ka-shakti-guide-kn.png) |

## Household utilities

| Guide | Kannada name | For | English | Kannada |
|---|---|---|---|---|
| [Gruha Jyothi (free electricity)](ka-gruha-jyothi.md) | ಗೃಹಜ್ಯೋತಿ | Households with a domestic electricity connection | [EN](ka-gruha-jyothi-guide.png) | [KN](ka-gruha-jyothi-guide-kn.png) |

## Pensions and food

| Guide | Kannada name | For | English | Kannada |
|---|---|---|---|---|
| [Ration card and Anna Bhagya (Karnataka)](ka-ration-card.md) | ಪಡಿತರ ಚೀಟಿ ಮತ್ತು ಅನ್ನಭಾಗ್ಯ | Low-income households | [EN](ka-ration-card-guide.png) | [KN](ka-ration-card-guide-kn.png) |
| [Old-age and widow pensions (Karnataka)](ka-social-pensions.md) | ವೃದ್ಧಾಪ್ಯ ಮತ್ತು ವಿಧವಾ ವೇತನ | Seniors and widows from low-income families | [EN](ka-social-pensions-guide.png) | [KN](ka-social-pensions-guide-kn.png) |

## Education and youth

| Guide | Kannada name | For | English | Kannada |
|---|---|---|---|---|
| [Yuva Nidhi (unemployment allowance)](ka-yuva-nidhi.md) | ಯುವನಿಧಿ | Unemployed graduates and diploma holders | [EN](ka-yuva-nidhi-guide.png) | [KN](ka-yuva-nidhi-guide-kn.png) |
| [SSP scholarship (Karnataka)](ka-ssp-scholarship.md) | ಎಸ್‌ಎಸ್‌ಪಿ ವಿದ್ಯಾರ್ಥಿ ವೇತನ | Pre-matric and post-matric students | [EN](ka-ssp-scholarship-guide.png) | [KN](ka-ssp-scholarship-guide-kn.png) |

## Farmers

| Guide | Kannada name | For | English | Kannada |
|---|---|---|---|---|
| [PM-KISAN (Karnataka, FRUITS)](ka-pm-kisan.md) | ಪಿಎಂ-ಕಿಸಾನ್ (ಕರ್ನಾಟಕ) | Landholding farmers in Karnataka | [EN](ka-pm-kisan-guide.png) | [KN](ka-pm-kisan-guide-kn.png) |

## Quick routers

- **Guarantees:** woman head of family → [Gruha Lakshmi](ka-gruha-lakshmi.md); electricity → [Gruha Jyothi](ka-gruha-jyothi.md); bus → [Shakti](ka-shakti.md); rice → [Anna Bhagya](ka-ration-card.md); graduates → [Yuva Nidhi](ka-yuva-nidhi.md)
- **Students:** [Caste and income certificate](ka-caste-income-certificate.md) → [SSP scholarship](ka-ssp-scholarship.md)
- **Farmers:** land not in your name → [Land mutation](ka-land-mutation.md), then [PM-KISAN (FRUITS)](ka-pm-kisan.md)
- **Seniors and widows:** [Social security pensions](ka-social-pensions.md)

## Adding a Karnataka guide

Run from this folder: `python3 ../gen_guide.py ka_<name>_content.py` writes `<out>.html` and `<out>-kn.html` here. Add a row above, then rebuild the website with `python3 ../../site/build_site.py`.
