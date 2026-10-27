# Ration card and Anna Bhagya (Karnataka) - End-to-End Workflow

ಪಡಿತರ ಚೀಟಿ ಮತ್ತು ಅನ್ನಭಾಗ್ಯ · For: Low-income households

## For citizens: step by step

Blue = you do this. Purple = government does this (you wait). Green = done. Red = what to do if stuck. Orange = your rights if it is late.

### English

![Ration card and Anna Bhagya (Karnataka) guide](ka-ration-card-guide.png)

### ಕನ್ನಡ (Kannada)

![ಪಡಿತರ ಚೀಟಿ ಮತ್ತು ಅನ್ನಭಾಗ್ಯ ಮಾರ್ಗದರ್ಶಿ](ka-ration-card-guide-kn.png)

Sources: [`ka-ration-card-guide.html`](ka-ration-card-guide.html), [`ka-ration-card-guide-kn.html`](ka-ration-card-guide-kn.html), generated from [`ka_ration_card_content.py`](ka_ration_card_content.py) with `python3 ../gen_guide.py ka_ration_card_content.py`. Kannada text pending native-speaker review.

## Official links

Use only these addresses. Checked on 27 Oct 2026 through search results; the government sites could not be opened directly from our build environment. "Third-party sites only" means several non-government sites agree on the address but no government page confirmed it yet, so open it and check before you share it.

| What | Link | Checked via |
| :--- | :--- | :--- |
| Ahara (Food and Civil Supplies): card status and lists | <https://ahara.karnataka.gov.in> | Government page |
| Chikkaballapur district: schemes page | <https://chikkaballapur.nic.in/schemes/> | Government page |
| Food helpline: 1967 | - | Third-party sites only |
| IPGRS: Karnataka grievance portal | <https://ipgrs.karnataka.gov.in> | Third-party sites only |

## For the Sathi team: system workflow

```mermaid
flowchart TD
    A([Household]) --> H{Already holds BPL or AAY card?}
    H -- Yes --> R([10 kg grain per person monthly at fair price shop])
    H -- No --> E{Excluded: government job, income-tax, four-wheeler, land or house limits?}
    E -- Yes --> X1[Not eligible for BPL: APL card only]
    E -- No --> W{New-card applications open?}
    W -- No --> F0[Wait for window, ask taluk food office]
    W -- Yes --> AP[Apply via Ahara at Grama One, Karnataka One or Bapuji Kendra]
    AP --> V{Food Inspector verification}
    V -- Rejected --> F1[Reason in writing, appeal to Deputy Director Food]
    V -- OK --> C[Card issued, linked to fair price shop]
    C --> R
    R -. Short supply or money demanded .-> F2[Receipt and call 1967]

    S1[[Sathi: exclusion check and window alerts]]:::sathi -.-> W
    S2[[Sathi: entitlement calculator per member]]:::sathi -.-> R
    S3[[Sathi: shortage complaint draft]]:::sathi -.-> F2

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class X1,F0,F1,F2 blocked
```

## Verification (27 Oct 2026)

- **Reported:** Anna Bhagya gives 10 kg per person per month to BPL / AAY cardholders with no separate registration; BPL exclusions (government job, income tax, four-wheeler, 3 ha dry land, 1,000 sq ft pucca house); helpline 1967; ahara.kar.nic.in now redirects to ahara.karnataka.gov.in (listed on a district site).
- **Conflicting:** whether new BPL applications can be made directly online; one guide says the direct online option was removed. The guide points to service centres when the window is open.
- **Left out:** card fees and issue time (unverified).

Sources: [Chikkaballapur district: schemes](https://chikkaballapur.nic.in/schemes/) · [schemesinindia: Anna Bhagya 2026](https://schemesinindia.in/blog/anna-bhagya-yojana-karnataka-10kg-free-rice-2026) · [ClearTax: Anna Bhagya scheme](https://cleartax.in/s/anna-bhagya-scheme) · [sarkariyojana.com: Ahara ration card](https://sarkariyojana.com/ahara-kar-nic-in-ration-card/)
