# MahaDBT Scholarship - End-to-End Workflow

Official site: https://mahadbt.maharashtra.gov.in (post-matric and higher-education scholarships across welfare departments).

## For students: step by step

Blue = you do this. Purple = college / government does this (you wait). Green = money received. Red = what to do if stuck. Orange = how to escalate.

### English

![MahaDBT scholarship guide](mahadbt-scholarship-guide.png)

### मराठी (Marathi)

![महाडीबीटी शिष्यवृत्ती मार्गदर्शक](mahadbt-scholarship-guide-mr.png)

Sources: [`mahadbt-scholarship-guide.html`](mahadbt-scholarship-guide.html), [`mahadbt-scholarship-guide-mr.html`](mahadbt-scholarship-guide-mr.html), generated from [`mahadbt_scholarship_content.py`](mahadbt_scholarship_content.py) with `python3 gen_guide.py mahadbt_scholarship_content.py`. Marathi text pending native-speaker review.

## Official links

Use only these addresses. Checked on 27 Oct 2026 through search results; the government sites could not be opened directly from our build environment. "Third-party sites only" means several non-government sites agree on the address but no government page confirmed it yet, so open it and check before you share it.

| What | Link | Checked via |
| :--- | :--- | :--- |
| MahaDBT: apply, track, grievance | <https://mahadbt.maharashtra.gov.in> | Government page |

## For the Sathi team: system workflow

Yellow boxes = where Sathi plugs in. Red boxes = common blockers.

![MahaDBT scholarship system workflow](mahadbt-scholarship.png)

<details><summary>Mermaid source (editable)</summary>

```mermaid
flowchart TD
    A([Student needs scholarship]) --> B[1. Find eligible scheme<br/>category, income, course]
    B --> C[2. Gather documents<br/>Aadhaar-bank seeding, current income cert,<br/>caste + validity, domicile, marksheet, fee receipt]
    C --> R[3. Register on MahaDBT<br/>complete full profile]
    R --> D[4. Apply before deadline<br/>Application ID]
    D --> E[5. College scrutiny<br/>scholarship desk]
    E -- Document issue --> F1[Sent back to applicant<br/>with remark]
    F1 -- Fix + resubmit --> E
    E -- Not acted --> F2[Pending at college]
    E -- Forwarded --> G[6. Department scrutiny + sanction<br/>Social Justice / OBC / Tribal / Higher Ed]
    G -- Rejected --> F3[Rejected with reason]
    G -- Sanctioned --> P[7. DBT payment via PFMS<br/>student a/c + fee to college where applicable]
    P -- Aadhaar not seeded / a/c inactive --> F4[Payment failed]
    P --> I([Money received])
    I --> N[Next academic year:<br/>renewal with pass result + new income cert]
    F2 --> T[Grievance on MahaDBT /<br/>district department office]

    S1[[Sathi: Scheme matcher<br/>best single scheme]]:::sathi -.-> B
    S2[[Sathi: Readiness check<br/>income cert expiry, bank seeding]]:::sathi -.-> C
    S3[[Sathi: Decode sent-back remark in Marathi]]:::sathi -.-> F1
    S4[[Sathi: Deadline + pending-at-college clock<br/>draft grievance]]:::sathi -.-> T
    S5[[Sathi: Renewal reminder]]:::sathi -.-> N

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class F1,F2,F3,F4 blocked
```

</details>

## Stages

| # | Stage | Owner | Common blocker | Sathi action |
|---|---|---|---|---|
| 1 | Find scheme | Student | Applies to wrong / multiple schemes | Scheme matcher: best single scheme |
| 2 | Documents | Student | Expired income certificate, bank not Aadhaar-seeded, caste validity missing | Readiness check; links to [income certificate guide](income-certificate.md) |
| 3 | Register + profile | Student | Incomplete profile, lost login | Profile checklist, credential reminder |
| 4 | Apply | Student | Deadline missed | Deadline countdown |
| 5 | College scrutiny | College scholarship desk | Sent back; pending at college | Decode remark in Marathi; pending clock |
| 6 | Department sanction | Welfare department | Rejected | Explain reason |
| 7 | DBT payment | PFMS / bank | Aadhaar not seeded, account inactive | Bank-side checklist |
| - | Renewal | Student | Forgets renewal; new income cert needed | Renewal reminder |

## Verification (27 Oct 2026, batch 3)

- **Reported (college notice, 2025-26):** income limits **SC/ST ₹2.5 lakh**, **OBC/SBC/VJNT/SEBC ₹8 lakh**; current-year income certificate from Tehsildar required.
- **Timing:** the 2025-26 cycle reportedly closed on 30 Nov 2025; 2026-27 expected to open. Check the portal for current dates.
- **No change needed** to the guide (it avoids fixed limits and stresses current-year income certificate and deadlines).
- **Still unverified:** one-scholarship rule, status wording ("pending at college"), grievance route, renewal pass rules (sources conflict).

Sources: [Tirpude College: Notice of Scholarship 2025](https://www.tirpude.edu.in/wp-content/uploads/2025/10/Notice-of-Scholarship-2025.pdf) · [IndiaScholarships: MahaDBT post-matric](https://www.indiascholarships.in/bn/scholarships/mahadbt-post-matric-scholarship-maharashtra) · [DJSCE: MahaDBT form filling](https://www.djsce.ac.in/docs/Process-of-MahaDBT-Scholarship-Form-Filling-1.pptx.pdf)
