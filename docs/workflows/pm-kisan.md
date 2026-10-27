# PM-KISAN - End-to-End Workflow

Official site: https://pmkisan.gov.in (Operational Guidelines PDF + "Know Your Status").

## For farmers: step by step

Blue = you do this. Purple = government does this (you wait). Green = money received. Red = what to do if stuck.

![PM-KISAN farmer guide](pm-kisan-farmer-guide.png)

Source to edit: [`pm-kisan-farmer-guide.html`](pm-kisan-farmer-guide.html)

### मराठी (Marathi)

![पीएम-किसान मार्गदर्शक](pm-kisan-farmer-guide-mr.png)

Source to edit: [`pm-kisan-farmer-guide-mr.html`](pm-kisan-farmer-guide-mr.html). Marathi text pending native-speaker review.

## For the Sathi team: system workflow

Yellow boxes = where Sathi plugs in. Red boxes = common blockers.

![PM-KISAN end-to-end workflow](pm-kisan.png)

<details><summary>Mermaid source (editable)</summary>


```mermaid
flowchart TD
    A([Farmer wants PM-KISAN]) --> B{Eligible?<br/>Owns cultivable land<br/>Not income-tax payer / govt employee / pensioner above limit}
    B -- No --> X1([Not eligible])
    B -- Yes --> C[1. Registration<br/>pmkisan.gov.in / App / CSC / Talathi]
    C --> D[2. Land record verification<br/>State Revenue: 7/12, Gat no.]
    D -- Land not in name /<br/>Ferfar pending --> F1[Blocked: Fix 7/12 or mutation]
    F1 --> D
    D -- OK --> E[3. Aadhaar validation<br/>UIDAI]
    E -- Name mismatch --> F2[Blocked: Correct Aadhaar or record]
    F2 --> E
    E -- OK --> G[4. Bank account validation<br/>PFMS]
    G -- Aadhaar not seeded /<br/>DBT off / account closed --> F3[Blocked: Fix at bank]
    F3 --> G
    G -- OK --> H[5. eKYC<br/>OTP or Face auth]
    H -- Not done --> F4[Instalment on hold]
    F4 --> H
    H -- Done --> I[6. State approval<br/>Status: RFT signed by State Govt]
    I --> J[7. Payment order<br/>Status: FTO generated, payment confirmation pending]
    J -- Bank rejects --> F3
    J --> K([8. Payment success<br/>Rs 2,000 per instalment, 3 per year])
    K --> L{Next instalment cycle}
    L -- eKYC / land / bank still valid --> I
    L -- Something changed --> F4

    S1[[Sathi: Eligibility + document readiness check]]:::sathi -.-> B
    S2[[Sathi: Ferfar Predictor + 7/12 Health Report]]:::sathi -.-> F1
    S3[[Sathi: Plain Marathi status decoder<br/>what RFT / FTO means + next action]]:::sathi -.-> I
    S4[[Sathi: Rights clock + grievance draft<br/>pmkisan helpdesk / CPGRAMS]]:::sathi -.-> J
    S5[[Sathi: eKYC and bank-seeding alerts<br/>before each instalment]]:::sathi -.-> L

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class F1,F2,F3,F4 blocked
```

</details>

## Stages

| # | Stage | Owner | Status text farmer sees | Common blocker | Sathi action |
|---|---|---|---|---|---|
| 1 | Registration | Farmer / CSC / Talathi | Registration | Wrong name or Aadhaar | Readiness check before applying |
| 2 | Land record verification | State Revenue | Land seeding | Land not in name, Ferfar pending, Gat mismatch | 7/12 Health Report, Ferfar Predictor |
| 3 | Aadhaar validation | UIDAI | Aadhaar validation | Name mismatch Aadhaar vs 7/12 | Show exact mismatch, how to fix |
| 4 | Bank validation | PFMS | Bank / Aadhaar seeding | Not seeded, DBT off, account closed | Bank-side checklist in Marathi |
| 5 | eKYC | Farmer | eKYC | Not done, instalment on hold | Alert before each instalment |
| 6 | State approval | State nodal officer | RFT signed by State Govt | Stuck at state | Decode status, rights clock |
| 7 | Payment order | Centre / PFMS | FTO generated, payment confirmation pending | Bank rejects | Grievance draft (helpdesk / CPGRAMS) |
| 8 | Payment | Bank | Payment success | Missed instalments | Instalment history check |

Helpline: 155261 / 011-24300606

## Verification (27 Oct 2026, batch 3)

- **Confirmed:** "RFT signed by State Govt" = state has verified and requested release; "FTO generated, payment confirmation pending" = transfer order created, money due soon. A "temporary hold" status is also reported.
- **No change needed** to the guide.
- **Still unverified:** exclusion list incl. ₹10,000 pension threshold, helpline numbers, eKYC rule details.

Sources: [AgriFarming: FTO processed but money not received](https://www.agrifarming.in/pm-kisan-fto-processed-but-money-not-received) · [BiharHelp: RFT signed by state](https://biharhelp.in/pm-kisan-rft-signed-by-state/) · [GovtSchemes: temporary hold](https://www.govtschemes.in/pm-kissan-temporary-hold)
