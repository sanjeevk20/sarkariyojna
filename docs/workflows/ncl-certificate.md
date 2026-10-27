# Non-Creamy Layer (NCL) Certificate (Maharashtra) - End-to-End Workflow

For OBC, VJ / NT and SBC citizens. Official site: https://aaplesarkar.mahaonline.gov.in (Revenue Department). Requires a [caste certificate](caste-certificate.md) first.

## For citizens: step by step

Blue = you do this. Purple = government does this (you wait). Green = certificate ready. Red = what to do if stuck. Orange = your rights if it is late.

### English

![NCL certificate guide](ncl-certificate-guide.png)

### मराठी (Marathi)

![नॉन-क्रिमीलेयर प्रमाणपत्र मार्गदर्शक](ncl-certificate-guide-mr.png)

Sources: [`ncl-certificate-guide.html`](ncl-certificate-guide.html), [`ncl-certificate-guide-mr.html`](ncl-certificate-guide-mr.html), generated from [`ncl_certificate_content.py`](ncl_certificate_content.py) with `python3 gen_guide.py ncl_certificate_content.py`. Marathi text pending native-speaker review.

## For the Sathi team: system workflow

Yellow boxes = where Sathi plugs in. Red boxes = common blockers.

![NCL certificate system workflow](ncl-certificate.png)

<details><summary>Mermaid source (editable)</summary>

```mermaid
flowchart TD
    A([OBC / VJNT / SBC citizen needs NCL]) --> B{1. Eligible?<br/>family income below 8 lakh,<br/>parents not in high posts}
    B -- No --> X([Creamy layer: not eligible])
    B -- Yes --> CC{2. Has caste certificate?}
    CC -- No --> CG[Get caste certificate first<br/>see caste certificate workflow]
    CG --> CC
    CC -- Yes --> C[3. Gather documents<br/>caste cert, 3 years parents income proof,<br/>occupation details, ID, self-declaration]
    C --> D[4. Apply on Aaple Sarkar<br/>state or central format<br/>Application ID + RTS time limit]
    D --> E[5. Scrutiny at Tahsil / SDO office]
    E -- Income year missing / unclear --> F1[Sent back with remark]
    F1 -- Upload + resubmit --> E
    E --> H[6. SDO approves + digital signature]
    H -- Rejected --> F2[Rejected with reason]
    H --> I([7. Download certificate<br/>has validity date])
    I --> R[Expiry: renew before<br/>admission / job forms]
    E -. time limit crossed .-> T[First Appeal on Aaple Sarkar<br/>MH Right to Public Services Act 2015]

    S1[[Sathi: Creamy-layer calculator<br/>which income counts]]:::sathi -.-> B
    S2[[Sathi: Dependency check<br/>caste cert + income certs ready]]:::sathi -.-> CC
    S3[[Sathi: State vs central format advisor]]:::sathi -.-> D
    S4[[Sathi: Rights clock + draft First Appeal]]:::sathi -.-> T
    S5[[Sathi: Expiry alert before deadlines]]:::sathi -.-> R

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class F1,F2 blocked
```

</details>

## Stages

| # | Stage | Owner | Common blocker | Sathi action |
|---|---|---|---|---|
| 1 | Eligibility | Citizen | Wrongly assumes creamy layer (counts salary / farm income) | Creamy-layer calculator: which income counts |
| 2 | Caste certificate | Citizen | Doesn't have one yet | Dependency check; link to [caste certificate guide](caste-certificate.md) |
| 3 | Documents | Citizen | Missing one of 3 income years | Income-year checklist; link to [income certificate guide](income-certificate.md) |
| 4 | Apply | Citizen / Seva Kendra / college camp | Gets state format when central is needed | State vs central format advisor |
| 5 | Scrutiny | Tahsil / SDO office | Sent back: income proof missing | Decode remark in Marathi |
| 6 | Approval | SDO | Rejected | Explain reason |
| 7 | Download | Citizen | Expires before admission / job form | Expiry alert; feeds [MahaDBT scholarship](mahadbt-scholarship.md) |
| - | Late beyond time limit | Citizen | Doesn't know about appeal | Auto-draft First Appeal |

**Why this matters for Sathi:** NCL sits at the end of a dependency chain (caste certificate → 3 years of income proof → NCL → scholarship / admission) and it expires. That chain is exactly what a "readiness" engine is for: one family profile, every certificate's expiry tracked, the next missing link flagged before a deadline.

## Verification (27 Oct 2026, batch 2)

- **Confirmed (consistent across sources):** ₹8 lakh family income ceiling (from the central 2017 memorandum); applied via Aaple Sarkar under Revenue Department; Class-I / Group A parental posts are excluded while lower government cadres are judged by cadre, not income.
- **Unclear, so guide kept general:** which income counts (agricultural income excluded under central norms but Maharashtra practice may differ); **validity period** (sources say 1 year or 3 years). Guide tells users to check the validity date printed on the certificate.
- **Changed in guide:** issuing officer now reads "SDO, or the competent officer in your taluka".

Sources: [mahadocguide: NCL Maharashtra](https://mahadocguide.in/non-creamy-layer-certificate-maharashtra/) · [navimumbai.com: NCL](https://navimumbai.com/non-creamy-layer-certificate-maharashtra/) · [LegalRaasta: NCL Maharashtra](https://www.legalraasta.com/blog/maharashtra-non-creamy-layer-certificate/) · [IndiaFilings: NCL Maharashtra](https://www.indiafilings.com/learn/maharashtra-non-creamy-layer-certificate)
