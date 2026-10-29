# MAA Yojana health cover (Rajasthan) - End-to-End Workflow

मुख्यमंत्री आयुष्मान आरोग्य (मा) योजना · For: Families in Rajasthan; free for NFSA, SECC, small farmers and contract workers

## For citizens: step by step

Blue = you do this. Purple = government does this (you wait). Green = done. Red = what to do if stuck. Orange = your rights if it is late.

### English

![MAA Yojana health cover (Rajasthan) guide](rj-maa-yojana-guide.png)

### हिंदी (Hindi)

![मुख्यमंत्री आयुष्मान आरोग्य (मा) योजना मार्गदर्शिका](rj-maa-yojana-guide-hi.png)

Sources: [`rj-maa-yojana-guide.html`](rj-maa-yojana-guide.html), [`rj-maa-yojana-guide-hi.html`](rj-maa-yojana-guide-hi.html), generated from [`rj_maa_yojana_content.py`](rj_maa_yojana_content.py) with `python3 ../gen_guide.py rj_maa_yojana_content.py`. Hindi text pending native-speaker review.

## Official links

Use only these addresses. Checked on 28 Oct 2026 through search results; the government sites could not be opened directly from our build environment. "Third-party sites only" means several non-government sites agree on the address but no government page confirmed it yet, so open it and check before you share it.

| What | Link | Checked via |
| :--- | :--- | :--- |
| MAA Yojana portal | <https://maayojana.rajasthan.gov.in> | Third-party sites only |
| Rajasthan SSO: one login for state services | <https://sso.rajasthan.gov.in> | Third-party sites only |
| Jan Aadhaar portal: family ID, update, eKYC | <https://janaadhaar.rajasthan.gov.in> | Third-party sites only |
| Rajasthan Sampark: grievances, also toll-free 181 | <https://sampark.rajasthan.gov.in> | Third-party sites only |

## For the Sathi team: system workflow

```mermaid
flowchart TD
    A([Family in Rajasthan]) --> C{Free category: NFSA, SECC, small farmer, contract worker?}
    C -- Yes --> R[Register on SSO with Jan Aadhaar and eKYC]
    C -- No --> P[Pay about Rs 850 per year, then register]
    P --> R
    R --> ACT[Cover active for the policy year]
    ACT --> H{Empanelled hospital MAA help desk}
    H -- Covered package --> T([Cashless treatment])
    H -- Asked to pay --> F1[Written refusal; Sampark 181]
    R -. Member not in Jan Aadhaar .-> F0[Add member to Jan Aadhaar first]

    S1[[Sathi: free-or-paid eligibility check]]:::sathi -.-> C
    S2[[Sathi: overcharge complaint draft]]:::sathi -.-> F1

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class F0,F1 blocked
```

## Verification (28 Oct 2026)

- Launched 1 May 2021 as Chiranjeevi; renamed MAAY in February 2024. ₹25 lakh cashless plus ₹10 lakh accident cover; free for NFSA, SECC 2011, small / marginal farmers, contract workers; ₹850 a year for others (Adda247, Joinditto, Coverfox).
- No 2026 notice of changes found; premium and categories marked as reported.

Sources: [Adda247: MAAY eligibility and how to apply](https://currentaffairs.adda247.com/rajasthan-mukhyamantri-ayushman-arogya-yojana-maay-eligibility-benefits-coverage-and-how-to-apply/) · [Joinditto: MAAY](https://www.joinditto.in/articles/health-insurance/mukhyamantri-ayushman-arogya-yojana/) · [Coverfox: MAAY](https://www.coverfox.com/government-schemes/health/mukhyamantri-ayushman-arogya-yojana-maay-rajasthan/)
