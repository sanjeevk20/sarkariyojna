# PM-KISAN (Karnataka, FRUITS) - End-to-End Workflow

ಪಿಎಂ-ಕಿಸಾನ್ (ಕರ್ನಾಟಕ) · For: Landholding farmers in Karnataka

## For citizens: step by step

Blue = you do this. Purple = government does this (you wait). Green = done. Red = what to do if stuck. Orange = your rights if it is late.

### English

![PM-KISAN (Karnataka, FRUITS) guide](ka-pm-kisan-guide.png)

### ಕನ್ನಡ (Kannada)

![ಪಿಎಂ-ಕಿಸಾನ್ (ಕರ್ನಾಟಕ) ಮಾರ್ಗದರ್ಶಿ](ka-pm-kisan-guide-kn.png)

Sources: [`ka-pm-kisan-guide.html`](ka-pm-kisan-guide.html), [`ka-pm-kisan-guide-kn.html`](ka-pm-kisan-guide-kn.html), generated from [`ka_pm_kisan_content.py`](ka_pm_kisan_content.py) with `python3 ../gen_guide.py ka_pm_kisan_content.py`. Kannada text pending native-speaker review.

## Official links

Use only these addresses. Checked on 27 Oct 2026 through search results; the government sites could not be opened directly from our build environment. "Third-party sites only" means several non-government sites agree on the address but no government page confirmed it yet, so open it and check before you share it.

| What | Link | Checked via |
| :--- | :--- | :--- |
| PM-KISAN: register, eKYC, Know Your Status | <https://pmkisan.gov.in> | Government page |
| FRUITS: Karnataka farmer registry | <https://fruits.karnataka.gov.in> | Third-party sites only |
| NeGD: FRUITS state directory entry | <https://negd.gov.in/isl/Directory/statedata/408> | Government page |
| PM-KISAN helpline: 155261 / 011-24300606 | - | Government page |

## For the Sathi team: system workflow

```mermaid
flowchart TD
    A([Karnataka farmer]) --> K{Name on RTC and not excluded?}
    K -- Land in parent's name --> F0[Mutation first]
    K -- Yes --> FR[FRUITS ID at Raitha Samparka Kendra]
    FR --> REG[Register on PM-KISAN, Seva Sindhu or RSK]
    REG --> V{FRUITS matches RTC owner name with Aadhaar}
    V -- Mismatch --> F1[Correct Aadhaar or RTC, ask RSK to re-verify]
    V -- OK --> EK[eKYC: OTP, face app or fingerprint]
    EK --> RFT[State signs RFT, FTO generated]
    RFT --> PAY([Rs 2,000 by DBT every four months])
    PAY -. Instalment missing .-> F2[Check eKYC, land seeding, Aadhaar-bank link]

    S1[[Sathi: Aadhaar vs RTC name match check]]:::sathi -.-> V
    S2[[Sathi: status explainer for RFT and FTO]]:::sathi -.-> RFT
    S3[[Sathi: missing-instalment diagnosis]]:::sathi -.-> F2

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class F0,F1,F2 blocked
```

## Verification (27 Oct 2026)

- **Confirmed (government pages):** FRUITS built by DPAR (e-Governance) with NIC; integrated with Bhoomi to validate land and compare owner name with Aadhaar name; PM-KISAN runs with FRUITS in the background.
- **Left out:** the additional state ₹4,000 a year paid in earlier years; whether it continues was not confirmed.
- **Still unverified:** current FRUITS self-registration steps.

Sources: [NeGD: FRUITS](https://negd.gov.in/isl/Directory/statedata/408) · [AgroSpectrum: Karnataka unifies farmers' land data in FRUITS](https://agrospectrumindia.com/news/8/24708/karnataka-unifies-farmers-land-data-in-unique-fruits-portal.html) · [pmkisan.gov.in](https://pmkisan.gov.in/)
