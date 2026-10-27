# Caste Certificate (Maharashtra) - End-to-End Workflow

Official site: https://aaplesarkar.mahaonline.gov.in (Revenue Department → Caste Certificate). Issued by the Sub-Divisional Officer (SDO).

## For citizens: step by step

Blue = you do this. Purple = government does this (you wait). Green = certificate ready. Red = what to do if stuck. Orange = your rights if it is late.

### English

![Caste certificate guide](caste-certificate-guide.png)

### मराठी (Marathi)

![जातीचा दाखला मार्गदर्शक](caste-certificate-guide-mr.png)

Sources: [`caste-certificate-guide.html`](caste-certificate-guide.html), [`caste-certificate-guide-mr.html`](caste-certificate-guide-mr.html), generated from [`caste_certificate_content.py`](caste_certificate_content.py) with `python3 gen_guide.py caste_certificate_content.py`. Marathi text pending native-speaker review.

## For the Sathi team: system workflow

Yellow boxes = where Sathi plugs in. Red boxes = common blockers.

![Caste certificate system workflow](caste-certificate.png)

<details><summary>Mermaid source (editable)</summary>

```mermaid
flowchart TD
    A([Citizen needs caste certificate]) --> B[1. Identify need<br/>Caste cert vs Non-Creamy Layer vs Caste Validity]
    B --> C[2. Find pre-cut-off proof<br/>self / father / grandfather, paternal side<br/>SC 1950, ST 1950, VJNT 1961, OBC/SBC 1967]
    C -- No document found --> F0[Blocked: no old proof]
    F0 -- Search relatives, school + GP registers --> C
    C --> D[3. Supporting papers<br/>Aadhaar, own LC, family tree, affidavit, photo]
    D --> E[4. Apply on Aaple Sarkar<br/>Portal / Seva Kendra / school camp<br/>Application ID + RTS time limit]
    E --> S[5. Scrutiny at Tahsil / SDO office<br/>local inquiry if needed]
    S -- Proof or family tree unclear --> F1[Sent back with remark]
    F1 -- Upload clearer proof --> S
    S --> H[6. SDO approves + digital signature]
    H -- Rejected --> F2[Rejected with reason]
    F2 --> AP[Appeal]
    H --> I([7. Download certificate<br/>lifetime validity])
    I --> V[Next: Caste Validity<br/>District Caste Scrutiny Committee]
    I --> N[Next: Non-Creamy Layer<br/>for OBC / VJNT / SBC]
    S -. time limit crossed .-> T[First Appeal on Aaple Sarkar<br/>MH Right to Public Services Act 2015]

    S1[[Sathi: Which certificate do I need?]]:::sathi -.-> B
    S2[[Sathi: Old-proof finder<br/>cut-off date by category, where to search]]:::sathi -.-> C
    S3[[Sathi: Family tree builder<br/>links applicant to old proof]]:::sathi -.-> D
    S4[[Sathi: Rights clock + draft First Appeal]]:::sathi -.-> T
    S5[[Sathi: Validity + NCL reminders]]:::sathi -.-> V

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class F0,F1,F2 blocked
```

</details>

## Stages

| # | Stage | Owner | Common blocker | Sathi action |
|---|---|---|---|---|
| 1 | Identify need | Citizen | Confuses caste cert, NCL and caste validity | "Which certificate do I need?" |
| 2 | Old proof before cut-off date | Citizen | No pre-cut-off document in family | Old-proof finder: cut-off by category, where to search |
| 3 | Supporting papers | Citizen | Family tree doesn't link applicant to old proof | Family tree builder |
| 4 | Apply | Citizen / Seva Kendra / school camp | Agent "arranging" documents | Official fee, Application ID, time limit |
| 5 | Scrutiny + local inquiry | Tahsil / SDO office | Sent back: proof or family tree unclear | Decode remark in Marathi |
| 6 | Approval | SDO | Rejected | Explain reason, appeal route |
| 7 | Download | Citizen | Didn't plan for validity / NCL | Validity + NCL reminders; feeds [MahaDBT scholarship](mahadbt-scholarship.md) |
| - | Late beyond time limit | Citizen | Doesn't know about appeal | Auto-draft First Appeal |

**Why this matters for Sathi:** step 2 (finding pre-cut-off proof) is the hardest part for families and where agents charge the most. A guided "old-proof finder" plus family-tree builder is a strong, defensible feature and a candidate for narrow patent claims (linking applicant lineage to historical records).

> Note: Working assumptions, not yet verified: the cut-off dates by category, paternal-side rule, SDO as issuing authority, lifetime validity, that caste certificate is a notified service under the MH Right to Public Services Act, menu path and status wording. Verify against the Maharashtra Caste Certificate Act, 2000, its rules, current GRs and the live portal before building.
