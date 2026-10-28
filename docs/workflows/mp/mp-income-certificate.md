# Income certificate (MP) - End-to-End Workflow

आय प्रमाण पत्र · For: Anyone applying to income-based schemes, scholarships

## For citizens: step by step

Blue = you do this. Purple = government does this (you wait). Green = done. Red = what to do if stuck. Orange = your rights if it is late.

### English

![Income certificate (MP) guide](mp-income-certificate-guide.png)

### हिंदी (Hindi)

![आय प्रमाण पत्र मार्गदर्शिका](mp-income-certificate-guide-hi.png)

Sources: [`mp-income-certificate-guide.html`](mp-income-certificate-guide.html), [`mp-income-certificate-guide-hi.html`](mp-income-certificate-guide-hi.html), generated from [`mp_income_certificate_content.py`](mp_income_certificate_content.py) with `python3 ../gen_guide.py mp_income_certificate_content.py`. Hindi text pending native-speaker review.

## Official links

Use only these addresses. Checked on 28 Oct 2026 through search results; the government sites could not be opened directly from our build environment. "Third-party sites only" means several non-government sites agree on the address but no government page confirmed it yet, so open it and check before you share it.

| What | Link | Checked via |
| :--- | :--- | :--- |
| MP e-District: certificates, status, download | <https://mpedistrict.gov.in> | Third-party sites only |
| Samagra portal: family / member ID, eKYC | <https://samagra.gov.in> | Third-party sites only |
| CM Helpline: 181 | - | Third-party sites only |

## For the Sathi team: system workflow

```mermaid
flowchart TD
    A([Citizen]) --> SG{Samagra member ID and eKYC done?}
    SG -- No --> F0[Get Samagra ID and do eKYC first]
    SG -- Yes --> D[Papers: Samagra ID, Aadhaar, income proof or self-declaration]
    D --> AP{Apply on MP e-District or at a Lok Seva Kendra}
    AP --> N[Application number and receipt]
    N --> V[Patwari / revenue inquiry if needed]
    V -- Report OK --> T[Tehsildar approves, digital signature]
    V -- Details do not match --> F1[Correct papers, ask for re-inquiry]
    T --> C([Certificate downloaded from e-District])
    N -. Lok Seva Guarantee time limit crossed .-> GR[First appeal, or CM Helpline 181]

    S1[[Sathi: Samagra readiness and papers checklist]]:::sathi -.-> SG
    S2[[Sathi: status tracker with time-limit alert]]:::sathi -.-> V
    S3[[Sathi: appeal or CM Helpline complaint draft]]:::sathi -.-> GR

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class F0,F1 blocked
```

## Verification (28 Oct 2026)

- **Reported:** apply on mpedistrict.gov.in (edistrict.mp.gov.in is a common wrong address) or at a Lok Seva Kendra; Samagra ID needed; free when applying online yourself, small fee at kiosks.
- **Conflicting, left out:** time limit (3 working days vs 30 days by source). The guide refers to the Lok Seva Guarantee time limit.
- **Still unverified:** current fee and notified time limit.

Sources: [CitizenNest: MP income certificate](https://www.citizennest.com/guide/mp-income-certificate-apply-online) · [Anantam IAS: e-District MP](https://anantamias.com/edistrict-mp/)
