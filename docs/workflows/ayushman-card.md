# Ayushman Bharat (PM-JAY) Card - End-to-End Workflow

How to make the free Ayushman Bharat health card for each family member and use it for cashless treatment at empanelled hospitals across India. Includes the Ayushman Vay Vandana card for everyone aged 70+. Card: Ayushman app / https://beneficiary.nha.gov.in. In Maharashtra the same card is used with [MJPJAY](mjpjay.md).

## For citizens: step by step

Blue = you do this. Purple = government does this (you wait). Green = card in use. Red = what to do if stuck. Orange = how to complain.

### English

![Ayushman card guide](ayushman-card-guide.png)

### मराठी (Marathi)

![आयुष्मान भारत कार्ड मार्गदर्शक](ayushman-card-guide-mr.png)

Sources: [`ayushman-card-guide.html`](ayushman-card-guide.html), [`ayushman-card-guide-mr.html`](ayushman-card-guide-mr.html), generated from [`ayushman_card_content.py`](ayushman_card_content.py) with `python3 gen_guide.py ayushman_card_content.py`. Marathi text pending native-speaker review.

## For the Sathi team: system workflow

Yellow boxes = where Sathi plugs in. Red boxes = common blockers.

![Ayushman card system workflow](ayushman-card.png)

<details><summary>Mermaid source (editable)</summary>

```mermaid
flowchart TD
    A([Family wants Ayushman card]) --> E{1. Eligible?<br/>check beneficiary.nha.gov.in / app}
    E -- Aged 70+ --> VV[Ayushman Vay Vandana card<br/>any income]
    E -- In family list / MJPJAY --> D[2. Keep ready<br/>Aadhaar each member,<br/>Aadhaar-linked mobile, ration card]
    E -- Not found --> F0[Not in list:<br/>check ration card / family ID,<br/>ask CSC or Ayushman Mitra]
    VV --> D
    D --> M[3. Make card free<br/>Ayushman app / CSC / hospital / ASHA]
    M --> K{Aadhaar eKYC<br/>OTP or face}
    K -- Fails / name mismatch --> F1[eKYC failed:<br/>update Aadhaar mobile or name]
    K -- OK --> P[Photo + submit]
    P --> SHA{4. State Health Agency approval}
    SHA -- Rejected / pending --> F2[Fix details via CSC / Ayushman Mitra]
    SHA -- Approved --> DL[5. Download card PDF]
    DL --> U([6. Cashless at any empanelled<br/>hospital in India])
    U -- Asked to pay --> F3[Illegal charge]
    F3 -.-> T[Ayushman helpline / portal grievance /<br/>district coordinator]

    S1[[Sathi: Eligibility check<br/>incl. 70+ Vay Vandana]]:::sathi -.-> E
    S2[[Sathi: Family card drive<br/>track which members have cards]]:::sathi -.-> M
    S3[[Sathi: eKYC failure explainer]]:::sathi -.-> F1
    S4[[Sathi: Nearest empanelled hospital<br/>across states, on map]]:::sathi -.-> U
    S5[[Sathi: Know your rights + complaint draft]]:::sathi -.-> T

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class F0,F1,F2,F3 blocked
```

</details>

## Stages

| # | Stage | Owner | Common blocker | Sathi action |
|---|---|---|---|---|
| 1 | Eligibility | Family | Not found in list; 70+ unaware of Vay Vandana | Eligibility check incl. 70+ |
| 2 | Keep ready | Family | Mobile not linked to Aadhaar | Explain face-auth option / Aadhaar mobile update |
| 3 | Make card + eKYC | Family / CSC / Ayushman Mitra / ASHA | eKYC fails on name mismatch; only one member done | eKYC failure explainer; family card drive tracker |
| 4 | SHA approval | State Health Agency | Pending / rejected | Explain reason, route to CSC |
| 5 | Download | Family | Card lost | Store in family vault |
| 6 | Use at hospital | Family / hospital | Asked to pay; doesn't know portability across states | Nearest empanelled hospital (any state); rights + complaint draft |

**Why this matters for Sathi:** the card is the gateway to both PM-JAY and MJPJAY. A "family card drive" (who in the family has a card, who doesn't) is a cheap, high-trust first action that brings every family member into the Sathi profile, and the 70+ Vay Vandana card is an easy win for elderly parents.

> Note: Working assumptions, not yet verified: eligibility lists, Maharashtra / MJPJAY integration, Vay Vandana rules for 70+, app steps and labels, SHA approval process, portability, and helpline / grievance channels. Verify against current NHA guidelines, beneficiary.nha.gov.in and State Health Assurance Society notifications before building.
