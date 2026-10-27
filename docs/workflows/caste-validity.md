# Caste Validity Certificate (Maharashtra) - End-to-End Workflow

Issued by the **District Caste Certificate Scrutiny Committee** (जिल्हा जात प्रमाणपत्र पडताळणी समिती). Applied for online on the state's caste validity portal (CCVIS). Requires a [caste certificate](caste-certificate.md) first.

## For citizens: step by step

Blue = you do this. Purple = committee does this (you wait). Green = validity ready. Red = what to do if stuck. Orange = how to follow up.

### English

![Caste validity guide](caste-validity-guide.png)

### मराठी (Marathi)

![जात वैधता प्रमाणपत्र मार्गदर्शक](caste-validity-guide-mr.png)

Sources: [`caste-validity-guide.html`](caste-validity-guide.html), [`caste-validity-guide-mr.html`](caste-validity-guide-mr.html), generated from [`caste_validity_content.py`](caste_validity_content.py) with `python3 gen_guide.py caste_validity_content.py`. Marathi text pending native-speaker review.

## For the Sathi team: system workflow

Yellow boxes = where Sathi plugs in. Red boxes = common blockers.

![Caste validity system workflow](caste-validity.png)

<details><summary>Mermaid source (editable)</summary>

```mermaid
flowchart TD
    A([Needs caste validity<br/>admission / reserved job / election]) --> CC{1. Has caste certificate?}
    CC -- No --> CG[Get caste certificate first<br/>see caste certificate workflow,<br/>then continue]
    CG -.-> C
    CC -- Yes --> C[2. Gather documents<br/>caste cert, LC, pre-cut-off proof,<br/>family tree, prescribed affidavit, college form]
    C --> BR{Blood relative already has validity?}
    BR -- Yes --> BRY[Attach relative's validity<br/>strongest proof, fast track]
    BR -- No --> D
    BRY --> D[3. Apply online on CCVIS<br/>print + submit to District Caste<br/>Certificate Scrutiny Committee]
    D --> K[Acknowledgement / token<br/>used for provisional admission]
    K --> E[4. Committee scrutiny]
    E -- Proof weak --> V[Vigilance cell inquiry<br/>local / village visit]
    E -- Needs clarification --> HN[Hearing notice<br/>attend with originals]
    V --> DEC
    HN --> DEC
    E -- Proof clear --> DEC{5. Committee decision}
    DEC -- Valid --> I([6. Caste validity certificate<br/>lifetime, proof for family])
    DEC -- Invalid --> F1[Claim invalidated]
    F1 --> HC[Challenge in High Court]
    E -. pending long .-> T[Written reminder to Member Secretary<br/>with token no. + deadline]

    S1[[Sathi: Start-early alert<br/>11th / 12th students]]:::sathi -.-> A
    S2[[Sathi: Family validity finder<br/>does any blood relative have one?]]:::sathi -.-> BR
    S3[[Sathi: Hearing reminder<br/>originals checklist]]:::sathi -.-> HN
    S4[[Sathi: Pending clock + draft reminder]]:::sathi -.-> T
    S5[[Sathi: Family vault<br/>reuse validity for siblings, children]]:::sathi -.-> I

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class F1 blocked
```

</details>

## Stages

| # | Stage | Owner | Common blocker | Sathi action |
|---|---|---|---|---|
| 1 | Need + caste certificate | Student / candidate | Starts after CET result; no caste certificate | Start-early alert in 11th / 12th; link to [caste certificate guide](caste-certificate.md) |
| 2 | Documents | Citizen | Weak old proof; family tree gaps | Family validity finder (blood relative's validity = fast track) |
| 3 | Apply + submit | Citizen / college | Lost acknowledgement; misses provisional admission | Store token in family vault |
| 4 | Scrutiny, vigilance, hearing | Scrutiny Committee | Misses hearing; vigilance inquiry delays | Hearing reminder + originals checklist |
| 5 | Decision | Scrutiny Committee | Claim invalidated | Explain High Court route; recommend legal advice |
| 6 | Validity issued | Citizen | Family doesn't reuse it | Family vault: reuse for siblings and children |
| - | Pending too long | Citizen | No escalation path known | Pending clock + draft reminder to Member Secretary |

**Why this matters for Sathi:** caste validity is the slowest, highest-stakes certificate in the chain (caste → validity → admission / job), and a blood relative's validity is the single biggest accelerator. A family-level vault that knows "your cousin already has validity" turns a months-long process into a fast one. Combined with the caste certificate's old-proof finder, this is a strong candidate for narrow patent claims around lineage-linked document reuse.

> Note: Working assumptions, not yet verified: portal name (CCVIS) and URL, online + physical submission flow, prescribed affidavit / form numbers, vigilance and hearing process, provisional-admission practice, lifetime validity, blood-relative rule, and the High Court remedy. Verify against the Maharashtra Caste Certificate Act, 2000, the 2012 Rules, current GRs and the live portal before building.
