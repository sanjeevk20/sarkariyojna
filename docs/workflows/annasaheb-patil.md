# Annasaheb Patil Loan Scheme (Interest Refund) - End-to-End Workflow

Annasaheb Patil Arthik Magas Vikas Mahamandal: for economically backward families of communities not covered by another state development corporation (e.g. Maratha and other open-category communities). The beneficiary takes a **bank** loan for a business; the corporation **refunds the interest** for EMIs paid on time. Individual and group loan options. Portal: https://udyog.mahaswayam.gov.in.

## For citizens: step by step

Blue = you do this. Purple = corporation / bank does this (you wait). Green = interest refunded. Red = what to do if stuck. Orange = how to escalate.

### English

![Annasaheb Patil loan guide](annasaheb-patil-guide.png)

### मराठी (Marathi)

![अण्णासाहेब पाटील कर्ज योजना मार्गदर्शक](annasaheb-patil-guide-mr.png)

Sources: [`annasaheb-patil-guide.html`](annasaheb-patil-guide.html), [`annasaheb-patil-guide-mr.html`](annasaheb-patil-guide-mr.html), generated from [`annasaheb_patil_content.py`](annasaheb_patil_content.py) with `python3 gen_guide.py annasaheb_patil_content.py`. Marathi text pending native-speaker review.

## For the Sathi team: system workflow

Yellow boxes = where Sathi plugs in. Red boxes = common blockers.

![Annasaheb Patil loan system workflow](annasaheb-patil.png)

<details><summary>Mermaid source (editable)</summary>

```mermaid
flowchart TD
    A([Wants to start / expand a business]) --> E{1. Eligible?<br/>MH resident, community without other corporation,<br/>economically backward, age + income limit}
    E -- No --> X([Check other corporations / schemes])
    E -- Yes --> PL[2. Plan business + project report]
    PL --> D[3. Documents<br/>Aadhaar, income cert / ITR, domicile,<br/>age + community proof, bank details]
    D --> R[4. Register on udyog.mahaswayam.gov.in<br/>apply for LOI]
    R --> LOI{5. Corporation scrutiny}
    LOI -- Doc issue --> F1[Sent back: re-upload]
    LOI -- OK --> L[LOI / eligibility certificate issued]
    L --> B{6. Bank appraisal}
    B -- Refused --> F2[Bank refusal:<br/>another bank / better report / credit score]
    B -- Sanctioned --> S[Loan disbursed<br/>upload sanction letter]
    S --> EMI[7. Pay EMIs on time<br/>upload loan statement]
    EMI -- Late / missed EMI --> F3[No refund for that period]
    EMI -- Regular --> IR([8. Interest refunded<br/>up to cap, for set years])
    F2 -. still stuck .-> T[District coordinator /<br/>bank grievance / Lead Bank Manager]

    S1[[Sathi: Eligibility + corporation router]]:::sathi -.-> E
    S2[[Sathi: Project report template<br/>EMI affordability check]]:::sathi -.-> PL
    S3[[Sathi: Bank-readiness check<br/>credit score, documents, which banks lend]]:::sathi -.-> B
    S4[[Sathi: EMI reminders +<br/>monthly refund-claim tracker]]:::sathi -.-> EMI
    S5[[Sathi: Escalation draft]]:::sathi -.-> T

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class F1,F2,F3 blocked
```

</details>

## Stages

| # | Stage | Owner | Common blocker | Sathi action |
|---|---|---|---|---|
| 1 | Eligibility | Citizen | Wrong corporation for their community | Eligibility + corporation router |
| 2 | Business plan | Citizen | Weak / no project report | Project report template, EMI affordability check |
| 3 | Documents | Citizen | Missing income / domicile certificate | Readiness; links to [income](income-certificate.md) and [domicile](domicile-certificate.md) guides |
| 4 | Register + LOI request | Citizen | Agent fraud | Free-registration messaging |
| 5 | LOI issued | Corporation | Sent back for documents | Decode reason |
| 6 | Bank sanction | Bank | **Bank refusal** (biggest drop-off) | Bank-readiness check: credit score, documents, which banks are lending |
| 7 | EMI + claim | Beneficiary | Late EMI → refund lost; forgets monthly claim | EMI reminders + refund-claim tracker |
| 8 | Interest refund | Corporation | Refund delayed | Escalation draft to district coordinator |

**Why this matters for Sathi:** this is the first scheme in the set where the money comes from a **bank**, not the government. The real bottleneck is bank sanction, not the corporation's LOI. A bank-readiness score (documents, credit, project report quality) and an EMI/refund tracker are high-value features, and they open a B2B channel with banks and CAs, matching the brief's "Banks for loans" idea.

> Note: Working assumptions, not yet verified: eligible communities, age and income limits, loan and interest-refund caps, refund period, group-loan options, portal name and flow, claim frequency, and escalation channels. Verify against current Annasaheb Patil Mahamandal GRs and udyog.mahaswayam.gov.in before building.
