# Caste certificate (MP) - End-to-End Workflow

जाति प्रमाण पत्र · For: SC / ST / OBC families

## For citizens: step by step

Blue = you do this. Purple = government does this (you wait). Green = done. Red = what to do if stuck. Orange = your rights if it is late.

### English

![Caste certificate (MP) guide](mp-caste-certificate-guide.png)

### हिंदी (Hindi)

![जाति प्रमाण पत्र मार्गदर्शिका](mp-caste-certificate-guide-hi.png)

Sources: [`mp-caste-certificate-guide.html`](mp-caste-certificate-guide.html), [`mp-caste-certificate-guide-hi.html`](mp-caste-certificate-guide-hi.html), generated from [`mp_caste_certificate_content.py`](mp_caste_certificate_content.py) with `python3 ../gen_guide.py mp_caste_certificate_content.py`. Hindi text pending native-speaker review.

## Official links

Use only these addresses. Checked on 28 Oct 2026 through search results; the government sites could not be opened directly from our build environment. "Third-party sites only" means several non-government sites agree on the address but no government page confirmed it yet, so open it and check before you share it.

| What | Link | Checked via |
| :--- | :--- | :--- |
| MP e-District: certificates, status, download | <https://mpedistrict.gov.in> | Third-party sites only |
| Samagra portal: family / member ID, eKYC | <https://samagra.gov.in> | Third-party sites only |
| CM Helpline: 181 | - | Third-party sites only |
| Panna district: caste certificate service page | <https://panna.nic.in/en/service/caste-certificate/> | Government page |

## For the Sathi team: system workflow

```mermaid
flowchart TD
    A([Citizen]) --> SG{Samagra member ID and eKYC done?}
    SG -- No --> F0[Get Samagra ID and do eKYC first]
    SG -- Yes --> D[Papers: Samagra ID, Aadhaar, family caste records]
    D --> AP{Apply on MP e-District or at a Lok Seva Kendra}
    AP --> N[Application number and receipt]
    N --> V[Patwari / revenue inquiry if needed]
    V -- Report OK --> T[SDM approves, digital signature]
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

- **Reported:** apply on mpedistrict.gov.in or at a Lok Seva Kendra; Samagra ID a prerequisite; approval in about 15 to 30 days.
- **Still unverified:** issuing officer per category under the current notification (SDM shown, as commonly described); district service page (Panna) lists the service.

Sources: [Panna district: caste certificate service](https://panna.nic.in/en/service/caste-certificate/) · [CitizenNest: MP caste certificate](https://www.citizennest.com/guide/mp-caste-certificate-apply-online) · [Testbook: caste certificate MP](https://testbook.com/articles/caste-certificate-mp)
