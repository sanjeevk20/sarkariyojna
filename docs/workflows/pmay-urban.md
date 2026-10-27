# PM Awas Yojana - Urban 2.0 (PMAY-U 2.0) - End-to-End Workflow

Urban housing for EWS / LIG / MIG families with four options: build on own land (BLC), buy in a partner project (AHP), interest subsidy on a home loan (ISS), or affordable rental (ARH). Official site: https://pmay-urban.gov.in. Rural families use [PMAY-Gramin](pmay-gramin.md).

## For citizens: step by step

Blue = you do this. Purple = government / bank does this (you wait). Green = home ready. Red = what to do if stuck. Orange = how to complain.

### English

![PMAY-Urban 2.0 guide](pmay-urban-guide.png)

### मराठी (Marathi)

![प्रधानमंत्री आवास योजना शहरी 2.0 मार्गदर्शक](pmay-urban-guide-mr.png)

Sources: [`pmay-urban-guide.html`](pmay-urban-guide.html), [`pmay-urban-guide-mr.html`](pmay-urban-guide-mr.html), generated from [`pmay_urban_content.py`](pmay_urban_content.py) with `python3 gen_guide.py pmay_urban_content.py`. Marathi text pending native-speaker review.

## For the Sathi team: system workflow

Yellow boxes = where Sathi plugs in. Red boxes = common blockers.

![PMAY-Urban 2.0 system workflow](pmay-urban.png)

<details><summary>Mermaid source (editable)</summary>

```mermaid
flowchart TD
    A([Urban family without pucca house]) --> E{1. Eligible?<br/>no pucca house in India,<br/>EWS / LIG / MIG income}
    E -- No --> X([Not eligible])
    E -- Yes --> V{2. Which vertical?}
    V -- Own land --> BLC[BLC: build on own plot]
    V -- Buy flat in project --> AHP[AHP: partner project]
    V -- Home loan --> ISS[ISS: interest subsidy via lender]
    V -- Rent --> ARH([ARH: affordable rental])
    BLC --> D[3. Documents<br/>Aadhaar all members, income proof,<br/>seeded bank a/c, no-pucca-house declaration,<br/>land / property card for BLC]
    AHP --> D
    ISS --> D
    D --> AP[4. Apply free<br/>pmay-urban.gov.in / ULB PMAY cell / lender<br/>application number]
    AP --> VR[5. ULB verification<br/>site check for BLC]
    VR -- Pucca house found / income mismatch --> F1[Rejected with reason]
    VR -- OK --> S{6. Approved}
    S -- BLC --> B1[Stage-wise instalments<br/>geo-tagged photos]
    B1 -- Photo missing --> F2[Instalment stuck]
    S -- AHP --> A1[Allotment, often by lottery<br/>beneficiary contribution]
    S -- ISS --> I1[Subsidy credited to loan account<br/>yearly instalments]
    B1 --> DONE([7. Home ready])
    A1 --> DONE
    I1 --> DONE
    F2 -. stuck long .-> T[Complaint: ULB PMAY cell /<br/>bank / CPGRAMS]

    S1[[Sathi: Eligibility + vertical chooser]]:::sathi -.-> V
    S2[[Sathi: Readiness check<br/>income cert, property card, seeding]]:::sathi -.-> D
    S3[[Sathi: Fake-site and agent warning]]:::sathi -.-> AP
    S4[[Sathi: Stage tracker for BLC]]:::sathi -.-> B1
    S5[[Sathi: Stuck clock + draft complaint]]:::sathi -.-> T

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class F1,F2 blocked
```

</details>

## Stages

| # | Stage | Owner | Common blocker | Sathi action |
|---|---|---|---|---|
| 1 | Eligibility | Citizen | Family member owns a pucca house elsewhere; wrong income band | Eligibility check incl. "anywhere in India" rule |
| 2 | Choose vertical | Citizen | Doesn't know BLC / AHP / ISS / ARH differences | Vertical chooser in plain Marathi |
| 3 | Documents | Citizen | No income certificate; plot not in family name | Readiness; links to [income](income-certificate.md) and [ferfar](ferfar.md) guides |
| 4 | Apply | Citizen / ULB / lender | Fake PMAY websites and agents | Official-link only, fraud warning |
| 5 | ULB verification | Urban Local Body | Rejected: pucca house found / income mismatch | Decode reason |
| 6 | Approval + money | ULB / lender / CNA | BLC stage photo missing; ISS subsidy not credited | BLC stage tracker; ISS subsidy tracker |
| 7 | Home ready | Citizen | - | Family vault for allotment / sanction letters |
| - | Stuck | Citizen | No escalation path | Draft complaint to ULB PMAY cell / bank / CPGRAMS |

**Why this matters for Sathi:** PMAY-U 2.0 has four very different paths behind one name, and fake "PMAY" websites are common. A trusted vertical chooser plus readiness check is high-value; ISS also opens a B2B channel with banks and housing finance companies.

## Verification (27 Oct 2026, batch 1)

- **Confirmed (official):** income bands EWS up to ₹3 lakh, LIG ₹3-6 lakh, MIG ₹6-9 lakh; no pucca house anywhere in India; four verticals BLC / AHP / ARH / ISS; beneficiary picks **one** vertical; ISS maximum subsidy **₹1.80 lakh** for income up to ₹9 lakh.
- **Added to guide:** "only one option" rule and ISS figures (₹1.80 lakh subsidy, loans up to ₹25 lakh, houses up to ₹35 lakh). The ₹25 lakh / ₹35 lakh caps and "4% on first ₹8 lakh over 5 yearly instalments" come from lender sites and are consistent across them.
- **Still unverified:** BLC / AHP assistance amounts, carpet-area limits (sources differ), female-ownership rule, application channels and status labels.

Sources: [PM India: Cabinet approves PMAY-U 2.0](https://www.pmindia.gov.in/en/news_updates/cabinet-approves-pradhan-mantri-awas-yojana-urban-2-0-scheme/) · [MoHUA PMAY-U FAQ](https://pmaymis.gov.in/pmaymis2_2024/faq.html) · [Tata Capital: PMAY 2.0](https://www.tatacapital.com/home-loan/pmay.html) · [IIFL Home Loans: PMAY-U 2.0](https://www.iiflhomeloans.com/pmay-urban)
