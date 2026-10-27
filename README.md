# Sathi - Sarkar Ka Sathi

**MyScheme tells you what you're eligible for. Haqdarshak helps you apply. Sathi gets you unstuck.**

Sathi tells common citizens in Maharashtra exactly what's blocking their government file, what to do next, and what the law says the office owes them, in Marathi, Hindi or English, with the source GR shown. It starts with land (7/12, Ferfar) and Maharashtra + Central schemes.

## Repo layout

| Path | What |
| :--- | :--- |
| `docs/workflows/README.md` | **Index of all workflow guides**, grouped by category, with quick routers |
| `docs/product-brief.md` | Product brief: pain points, differentiator, 12 concepts, Scheme Finder deep dive, MVP plan, tech stack |
| `docs/workflows/pm-kisan.md` | PM-KISAN: step-by-step farmer guide + system workflow with Sathi touchpoints |
| `docs/workflows/krushi-swavalamban.md` | Krushi Swavalamban Yojana (SC farmers, wells / irrigation): guide (EN + Marathi) + system workflow |
| `docs/workflows/birsa-munda.md` | Birsa Munda Krushi Kranti Yojana (ST farmers, wells / irrigation): guide (EN + Marathi) + system workflow |
| `docs/workflows/magel-tyala-shettale.md` | Magel Tyala Shettale (farm pond): guide (EN + Marathi) + system workflow |
| `docs/workflows/saur-krushi-pump.md` | Magel Tyala Saur Krushi Pump (solar pump): guide (EN + Marathi) + system workflow |
| `docs/workflows/income-certificate.md` | Aaple Sarkar income certificate: citizen guide (EN + Marathi) + system workflow |
| `docs/workflows/ferfar.md` | 7/12 Ferfar (mutation): citizen guide (EN + Marathi) + system workflow |
| `docs/workflows/mahadbt-scholarship.md` | MahaDBT scholarship: student guide (EN + Marathi) + system workflow |
| `docs/workflows/mjprf.md` | Mahatma Jyotiba Phule Research Fellowship (MahaJyoti PhD): guide (EN + Marathi) + system workflow |
| `docs/workflows/caste-certificate.md` | Caste certificate: citizen guide (EN + Marathi) + system workflow |
| `docs/workflows/domicile-certificate.md` | Domicile certificate: citizen guide (EN + Marathi) + system workflow |
| `docs/workflows/ncl-certificate.md` | Non-Creamy Layer certificate: citizen guide (EN + Marathi) + system workflow |
| `docs/workflows/caste-validity.md` | Caste validity certificate: citizen guide (EN + Marathi) + system workflow |
| `docs/workflows/ladki-bahin.md` | Ladki Bahin Yojana: citizen guide (EN + Marathi) + system workflow |
| `docs/workflows/pmay-gramin.md` | PM Awas Yojana - Gramin: citizen guide (EN + Marathi) + system workflow |
| `docs/workflows/pmay-urban.md` | PM Awas Yojana - Urban 2.0: citizen guide (EN + Marathi) + system workflow |
| `docs/workflows/ujjwala.md` | PM Ujjwala Yojana: citizen guide (EN + Marathi) + system workflow |
| `docs/workflows/sanjay-gandhi.md` | Sanjay Gandhi Niradhar Yojana: citizen guide (EN + Marathi) + system workflow |
| `docs/workflows/shravanbal.md` | Shravanbal Yojana (senior citizen pension): citizen guide (EN + Marathi) + system workflow |
| `docs/workflows/mjpjay.md` | Mahatma Jyotiba Phule Jan Arogya Yojana: citizen guide (EN + Marathi) + system workflow |
| `docs/workflows/ayushman-card.md` | Ayushman Bharat card: citizen guide (EN + Marathi) + system workflow |
| `docs/workflows/shiv-bhojan.md` | Shiv Bhojan Thali: diner guide (EN + Marathi) + diner / operator workflow |
| `docs/workflows/annasaheb-patil.md` | Annasaheb Patil interest-refund loan: citizen guide (EN + Marathi) + system workflow |
| `docs/workflows/mahatma-phule-mahamandal.md` | Mahatma Phule Mahamandal loans (SC / Nav-Bauddha): citizen guide (EN + Marathi) + system workflow |
| `docs/workflows/gen_guide.py` | Renders citizen guides from a `*_content.py` file |
| `docs/workflows/render.js` | Renders guide HTML and Mermaid diagrams to PNG (Playwright) |
