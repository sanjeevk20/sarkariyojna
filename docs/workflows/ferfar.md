# 7/12 Ferfar (Mutation) - End-to-End Workflow

Covers both paths: **sale** (auto e-mutation after IGR registration) and **inheritance / gift / partition** (citizen applies).

## For citizens: step by step

Blue = you do this. Purple = government does this (you wait). Green = name on 7/12. Red = what to do if stuck. Orange = what to do if it is late.

### English

![Ferfar guide](ferfar-guide.png)

### मराठी (Marathi)

![फेरफार मार्गदर्शक](ferfar-guide-mr.png)

Sources: [`ferfar-guide.html`](ferfar-guide.html), [`ferfar-guide-mr.html`](ferfar-guide-mr.html), generated from [`ferfar_content.py`](ferfar_content.py) with `python3 gen_guide.py ferfar_content.py`. Marathi text pending native-speaker review.

## For the Sathi team: system workflow

Yellow boxes = where Sathi plugs in. Red boxes = common blockers.

![Ferfar system workflow](ferfar.png)

<details><summary>Mermaid source (editable)</summary>

```mermaid
flowchart TD
    A([Land changes hands]) --> B{1. Ferfar type?}
    B -- Sale --> R[Sale deed registered<br/>at Sub-Registrar - IGR]
    R -- Auto data transfer --> E
    B -- Inheritance / gift / partition --> C[2. Apply with documents<br/>e-Hakk online or Talathi office<br/>death cert, all heirs, 7/12, 8A, declaration]
    C --> E[3. Talathi creates ferfar entry<br/>ferfar number assigned]
    E -- Entry not created --> F1[Blocked: no entry]
    E --> N[4. Notice to all interested parties<br/>seller, heirs, bank]
    N --> W{15-day objection window}
    W -- Objection --> D[Dispute case<br/>Circle Officer hearing]
    D -- Decision --> P{Approved?}
    W -- No objection --> P
    P -- No --> F2[Rejected with reason]
    F2 --> AP[Appeal to SDO / reapply]
    P -- Yes --> H[5. Circle Officer certifies ferfar]
    H --> I([6. 7/12 updated with new name<br/>Digital signed 7/12 download])
    W -. window over, still pending .-> T[Written application to Tahsildar<br/>with ferfar no., take acknowledgement]

    S1[[Sathi: Ferfar Predictor<br/>auto-entry check after registration]]:::sathi -.-> R
    S2[[Sathi: Heir checklist<br/>no missing heir]]:::sathi -.-> C
    S3[[Sathi: 15-day countdown<br/>+ draft application to Tahsildar]]:::sathi -.-> T
    S4[[Sathi: 7/12 Health Report<br/>verify name, loan, stay]]:::sathi -.-> I

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class F1,F2,D blocked
```

</details>

## Stages

| # | Stage | Owner | Common blocker | Sathi action |
|---|---|---|---|---|
| 1 | Identify ferfar type | Citizen | Pays agent to "start" an automatic sale ferfar | Explain auto path vs apply path |
| 2 | Apply (inheritance / gift / partition) | Citizen | Missing heir, incomplete papers | Heir checklist, document readiness |
| 3 | Ferfar entry created | Talathi (auto from IGR for sale) | Entry never created | Ferfar Predictor: check entry after registration |
| 4 | Notice + 15-day objection window | Talathi | Objection → dispute case | Countdown, explain hearing process |
| 5 | Certification | Circle Officer | Pending after window, or rejected | Draft written application to Tahsildar; appeal guidance (SDO) |
| 6 | 7/12 updated | System | Wrong name / old encumbrance still shown | 7/12 Health Report |

> Note: Working assumptions, not yet verified: the 15-day notice period, e-Hakk as the online channel for inheritance, Mahabhumi as the status-check portal, Circle Officer as certifying authority, appeal to SDO, and digitalsatbara.mahabhumi.gov.in for signed 7/12. Verify against the Maharashtra Land Revenue Code and live portals before building.
