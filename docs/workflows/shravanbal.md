# Shravanbal Seva Rajya Nivruttivetan Yojana - End-to-End Workflow

Maharashtra state pension for destitute senior citizens aged 65+. Two groups: families on the BPL list (state share + central Indira Gandhi National Old Age Pension) and families not on the BPL list (state pension). Applied through Aaple Sarkar or the Sanjay Gandhi Yojana branch at the Tahsil office. Below 65, see [Sanjay Gandhi Niradhar Yojana](sanjay-gandhi.md).

## For citizens: step by step

Blue = you / family do this. Purple = government does this (you wait). Green = pension received. Red = what to do if stuck. Orange = how to follow up.

### English

![Shravanbal Yojana guide](shravanbal-guide.png)

### मराठी (Marathi)

![श्रावणबाळ योजना मार्गदर्शक](shravanbal-guide-mr.png)

Sources: [`shravanbal-guide.html`](shravanbal-guide.html), [`shravanbal-guide-mr.html`](shravanbal-guide-mr.html), generated from [`shravanbal_content.py`](shravanbal_content.py) with `python3 gen_guide.py shravanbal_content.py`. Marathi text pending native-speaker review.

## For the Sathi team: system workflow

Yellow boxes = where Sathi plugs in. Red boxes = common blockers.

![Shravanbal Yojana system workflow](shravanbal.png)

<details><summary>Mermaid source (editable)</summary>

```mermaid
flowchart TD
    A([Elderly person needs pension]) --> AG{Age 65 or more?}
    AG -- No --> SG([Below 65: see Sanjay Gandhi Niradhar Yojana])
    AG -- Yes --> E{1. Eligible?<br/>MH resident, very low income}
    E -- No --> X([Not eligible])
    E -- Yes --> G{BPL list?}
    G -- Yes --> GB[Group B<br/>state + central IGNOAPS share]
    G -- No --> GA[Group A<br/>state pension]
    GA --> D[2. Documents<br/>age proof or govt doctor certificate,<br/>residence, income cert, BPL proof if any,<br/>Aadhaar, seeded bank a/c]
    GB --> D
    D --> AP[3. Apply free<br/>Aaple Sarkar / Tahsil SGY branch<br/>family can apply on behalf]
    AP --> SC[4. Tahsil scrutiny<br/>Talathi local inquiry]
    SC --> CM{5. Taluka SGY committee}
    CM -- Rejected --> F1[Rejected: ask reason in writing]
    CM -- Approved --> P[6. Monthly DBT pension]
    P -- Bank not seeded / inactive --> F2[Payment failed]
    P --> K[7. Keep running<br/>annual life certificate]
    K -- Life certificate missed --> F3[Pension stopped]
    SC -. pending long .-> T[Written application to Tahsildar SGY /<br/>Aaple Sarkar grievance]

    S1[[Sathi: Age + scheme router<br/>Shravanbal vs SGNY, Group A vs B]]:::sathi -.-> G
    S2[[Sathi: Readiness check<br/>age proof options, income cert, seeding]]:::sathi -.-> D
    S3[[Sathi: Assisted mode<br/>family / e-Seva operator applies]]:::sathi -.-> AP
    S4[[Sathi: Committee date + pending clock]]:::sathi -.-> T
    S5[[Sathi: Life-certificate reminder<br/>to family members]]:::sathi -.-> K

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class F1,F2,F3 blocked
```

</details>

## Stages

| # | Stage | Owner | Common blocker | Sathi action |
|---|---|---|---|---|
| 1 | Eligibility + group | Family | Under 65 applies here; unsure about BPL group | Age + scheme router (Shravanbal vs SGNY, Group A vs B) |
| 2 | Documents | Family | No birth / school record for age | Age-proof options incl. govt doctor certificate; link to [income certificate guide](income-certificate.md) |
| 3 | Apply | Family / e-Seva operator | Elderly person can't travel | Assisted mode: family member applies on behalf |
| 4 | Scrutiny + Talathi inquiry | Tahsil office | Extra papers asked | Explain what is missing |
| 5 | Taluka committee | SGY committee | Pending until next meeting; rejected | Committee-date + pending clock |
| 6 | Monthly DBT | Treasury / bank | Bank inactive / not seeded | Bank check |
| 7 | Keep running | Family | Life certificate missed → pension stopped | Annual life-certificate reminder sent to family members |

**Why this matters for Sathi:** the applicant is elderly but the *user* is usually a son, daughter or e-Seva operator. Sathi's family profile fits naturally: one person manages a parent's pension, a sibling's scholarship and their own certificates. The annual life-certificate reminder alone prevents the most common silent stoppage.

> Note: Working assumptions, not yet verified: benefit amount and Group A / B split, central IGNOAPS share, age and income limits, residence rule, accepted age proofs, committee process, and life-certificate rule. Verify against current Maharashtra Social Justice / Revenue GRs, NSAP guidelines and Aaple Sarkar before building.
