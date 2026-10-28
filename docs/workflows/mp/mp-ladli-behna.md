# Ladli Behna Yojana (MP) - End-to-End Workflow

मुख्यमंत्री लाड़ली बहना योजना · For: Women 21–60 in Madhya Pradesh, family income up to ₹2.5 lakh

## For citizens: step by step

Blue = you do this. Purple = government does this (you wait). Green = done. Red = what to do if stuck. Orange = your rights if it is late.

### English

![Ladli Behna Yojana (MP) guide](mp-ladli-behna-guide.png)

### हिंदी (Hindi)

![मुख्यमंत्री लाड़ली बहना योजना मार्गदर्शिका](mp-ladli-behna-guide-hi.png)

Sources: [`mp-ladli-behna-guide.html`](mp-ladli-behna-guide.html), [`mp-ladli-behna-guide-hi.html`](mp-ladli-behna-guide-hi.html), generated from [`mp_ladli_behna_content.py`](mp_ladli_behna_content.py) with `python3 ../gen_guide.py mp_ladli_behna_content.py`. Hindi text pending native-speaker review.

## Official links

Use only these addresses. Checked on 28 Oct 2026 through search results; the government sites could not be opened directly from our build environment. "Third-party sites only" means several non-government sites agree on the address but no government page confirmed it yet, so open it and check before you share it.

| What | Link | Checked via |
| :--- | :--- | :--- |
| Ladli Behna portal: status, instalment history | <https://cmladlibahna.mp.gov.in> | Third-party sites only |
| Samagra portal: family / member ID, eKYC | <https://samagra.gov.in> | Third-party sites only |
| CM Helpline: 181 | - | Third-party sites only |

## For the Sathi team: system workflow

```mermaid
flowchart TD
    A([Woman 21 to 60 in MP]) --> E{Income and family conditions met?}
    E -- No --> X1[Not eligible]
    E -- Yes --> W{Registration window open?}
    W -- No --> F0[Wait; ask Gram Panchayat or ward office]
    W -- Yes --> AP[Register at camp with Samagra eKYC, Aadhaar, bank]
    AP --> V{Verification against Samagra, income, tax data}
    V -- Rejected --> F1[Ask reason; complain on CM Helpline 181 if wrong]
    V -- Approved --> K[Yearly eKYC and active Aadhaar-linked bank]
    K --> PAY([Rs 1,500 a month by DBT])
    PAY -. Not received .-> F2[Check portal, bank seeding, DBT; then 181]

    S1[[Sathi: window alerts and eligibility check]]:::sathi -.-> W
    S2[[Sathi: eKYC reminder before each window]]:::sathi -.-> K
    S3[[Sathi: missed-instalment diagnosis and 181 complaint]]:::sathi -.-> F2

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class X1,F0,F1,F2 blocked
```

## Verification (28 Oct 2026)

- **Reported (2026):** ₹1,500 a month (41st instalment in Oct 2026, Outlook Money); women 21 to 60, family income up to ₹2.5 lakh; yearly eKYC window 1 June to 15 July 2026; 39th instalment was delayed in August 2026.
- **Conflicting:** some pages still list ₹1,250, and whether new registration is open (mostly closed since August 2023, with occasional windows). The guide says to ask the Gram Panchayat / ward office first.
- **Still unverified:** the scheme helpline number listed by one source (0755-2700800).

Sources: [Outlook Money: 41st instalment of ₹1,500](https://www.outlookmoney.com/news/ladli-behna-yojana-madhya-pradesh-releases-41st-instalment-of-rs-1500) · [Outlook Money: 39th instalment pending](https://www.outlookmoney.com/news/ladli-behna-yojana-39th-instalment-august-payment-date-amount-and-status-check) · [Bajaj Finserv: Ladli Behna guide](https://www.bajajfinserv.in/chief-minister-ladli-behna-yojana-guide) · [LegalDev: Ladli Behna 2026](https://legaldev.in/latest/ladli-behna-yojana) · [Free Press Journal: 35th instalment](https://www.freepressjournal.in/bhopal/madhya-pradesh-cm-mohan-yadav-transfers-1836-crore-35th-installment-of-ladli-behna-yojana-in-ashta-video)
