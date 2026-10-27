# Aaple Sarkar Income Certificate - End-to-End Workflow

Official site: https://aaplesarkar.mahaonline.gov.in (Revenue Department → Income Certificate).

## For citizens: step by step

Blue = you do this. Purple = government does this (you wait). Green = certificate ready. Red = what to do if stuck. Orange = your rights if it is late.

### English

![Income certificate guide](income-certificate-guide.png)

Source to edit: [`income-certificate-guide.html`](income-certificate-guide.html)

### मराठी (Marathi)

![उत्पन्नाचा दाखला मार्गदर्शक](income-certificate-guide-mr.png)

Source to edit: [`income-certificate-guide-mr.html`](income-certificate-guide-mr.html). Both guides are generated from [`income_certificate_content.py`](income_certificate_content.py) with `python3 gen_guide.py income_certificate_content.py`. Marathi text pending native-speaker review.

## For the Sathi team: system workflow

Yellow boxes = where Sathi plugs in. Red boxes = common blockers.

![Income certificate system workflow](income-certificate.png)

<details><summary>Mermaid source (editable)</summary>

```mermaid
flowchart TD
    A([Citizen needs income certificate]) --> B[1. Identify need<br/>Which year, whose name, which scheme]
    B --> C[2. Gather documents<br/>ID, address, income proof, self-declaration, photo]
    C --> D[3. Apply on Aaple Sarkar<br/>Portal or Seva Kendra, pay fee<br/>Get Application ID + RTS time limit]
    D --> E[4. Scrutiny at Tahsil office]
    E -- Document missing / wrong --> F1[Sent back to applicant<br/>with remark]
    F1 -- Upload + resubmit --> E
    E -- Farm / business income --> G[5. Talathi / Circle field report]
    G -- Pending long --> F2[Blocked at Talathi]
    G --> H
    E -- OK --> H[6. Tahsildar / Naib Tahsildar<br/>approves + digital signature]
    H -- Rejected --> F3[Rejected with reason]
    H --> I([7. Download digitally signed certificate])
    I --> L[Next financial year:<br/>renew from step 1]
    F2 --> T{RTS time limit crossed?}
    E -. any delay .-> T
    T -- Yes --> J[First Appeal on Aaple Sarkar<br/>MH Right to Public Services Act 2015]
    J --> K[Second Appeal / State RTS Commission]

    S1[[Sathi: Which certificate + document readiness check]]:::sathi -.-> B
    S2[[Sathi: Decode sent-back remark in Marathi<br/>what to upload, no visit needed]]:::sathi -.-> F1
    S3[[Sathi: Rights clock countdown<br/>auto-draft First Appeal]]:::sathi -.-> T
    S4[[Sathi: Expiry alert before scheme deadlines]]:::sathi -.-> L

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class F1,F2,F3 blocked
```

</details>

## Stages

| # | Stage | Owner | Common blocker | Sathi action |
|---|---|---|---|---|
| 1 | Identify need | Citizen | Wrong year or wrong name (self vs parent) | Ask scheme → tell which certificate |
| 2 | Gather documents | Citizen | Missing income proof; paying for affidavit unnecessarily | Readiness checklist by occupation |
| 3 | Apply | Citizen / Seva Kendra | Agent overcharging | Show official fee, note Application ID + time limit |
| 4 | Scrutiny | Tahsil office | Sent back with English remark | Decode remark in Marathi, what to upload |
| 5 | Field report (if needed) | Talathi / Circle officer | Pending at Talathi | Rights clock |
| 6 | Approval + digital signature | Tahsildar / Naib Tahsildar | Rejected | Explain reason, fix and re-apply |
| 7 | Download | Citizen | Expires before next scheme deadline | Expiry alert |
| - | Late beyond time limit | Citizen | Doesn't know about appeal | Auto-draft First Appeal (MH Right to Public Services Act, 2015) |

## Verification (27 Oct 2026, batch 3)

- **Confirmed (district list of notified Revenue services):** income certificate time limit **15 days**, designated officer **Tehsildar**.
- **Changed in guide:** "self-declaration is enough" softened to "ask whether a self-declaration is accepted", since a "with affidavit" service variant still exists and the replacement rule was not confirmed.
- **Still unverified:** fee amount, validity period, Talathi report requirement, exact status wording.

Sources: [Chanda district: notified services list](https://chanda.nic.in/?p=30380) · [India.gov.in: Maharashtra income certificate with affidavit](https://services.india.gov.in/service/detail/maharashtra-income-certificate-with-affidavit) · [Wikiprocedure: Maharashtra income certificate](https://wikiprocedure.com/index.php/Maharashtra_-_Apply_for_Income_Certificate)
