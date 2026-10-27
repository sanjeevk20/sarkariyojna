# Shiv Bhojan Thali - End-to-End Workflow

Maharashtra's subsidised meal scheme (Food, Civil Supplies and Consumer Protection Department): a full thali at a fixed low price at approved Shiv Bhojan centres, mainly near hospitals, bus stands, markets and government offices. No documents are needed to eat. This page covers two users: the **diner** and the **centre operator**.

## For citizens: step by step

Blue = you do this. Purple = centre does this. Green = meal served. Red = tips. Orange = how to complain.

### English

![Shiv Bhojan guide](shiv-bhojan-guide.png)

### मराठी (Marathi)

![शिवभोजन थाळी मार्गदर्शक](shiv-bhojan-guide-mr.png)

Sources: [`shiv-bhojan-guide.html`](shiv-bhojan-guide.html), [`shiv-bhojan-guide-mr.html`](shiv-bhojan-guide-mr.html), generated from [`shiv_bhojan_content.py`](shiv_bhojan_content.py) with `python3 gen_guide.py shiv_bhojan_content.py`. Marathi text pending native-speaker review.

## For the Sathi team: system workflow (diner + operator)

Yellow boxes = where Sathi plugs in. Red boxes = common blockers.

![Shiv Bhojan system workflow](shiv-bhojan.png)

<details><summary>Mermaid source (editable)</summary>

```mermaid
flowchart TD
    subgraph DINER [Citizen: eating a thali]
    A([Needs an affordable meal]) --> F[1. Find a Shiv Bhojan centre<br/>near hospital, bus stand, market]
    F --> O{Centre open +<br/>plates left?}
    O -- No --> F0[Closed / plates over:<br/>try next centre or come earlier]
    O -- Yes --> P[2. Pay fixed price]
    P --> R[3. Name + photo recorded<br/>in Shiv Bhojan app]
    R --> M([4. Meal served])
    P -- Charged more / poor food --> F1[Complaint to Tahsil /<br/>District Supply Officer]
    end

    subgraph OPS [Operator: running a centre]
    OA([NGO / SHG / mess owner]) --> AP[Apply to District Supply Office]
    AP --> SEL[Selection + onboarding<br/>premises, hygiene, app login]
    SEL --> SV[Daily serving<br/>plate quota, photo per diner]
    SV --> CL[Monthly claim from app records]
    CL -- Delayed --> F2[Subsidy payment delayed]
    CL --> PAY([Subsidy paid per plate])
    end

    R -. app data feeds .-> CL

    S1[[Sathi: Nearest open centre on map<br/>with timing]]:::sathi -.-> F
    S2[[Sathi: Fixed-price + rights card<br/>complaint draft]]:::sathi -.-> F1
    S3[[Sathi: Operator onboarding checklist]]:::sathi -.-> AP
    S4[[Sathi: Claim + payment tracker<br/>for operators]]:::sathi -.-> F2

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class F0,F1,F2 blocked
```

</details>

## Stages

| # | Stage | Owner | Common blocker | Sathi action |
|---|---|---|---|---|
| 1 | Find centre | Diner | Doesn't know nearest open centre; centre closed | Nearest open centre on map, with timing |
| 2 | Pay | Diner | Charged more than fixed price | Fixed-price + rights card |
| 3 | Photo / name recorded | Centre | Diner thinks photo is a charge or risk | Explain it is routine |
| 4 | Meal | Centre | Poor quality / refused | Complaint draft to Tahsil / District Supply Officer |
| Op-1 | Apply to run a centre | NGO / SHG / mess owner | Doesn't know process | Operator onboarding checklist |
| Op-2 | Monthly subsidy claim | Operator / DSO | Payment delayed | Claim + payment tracker |

**Why this matters for Sathi:** for diners this is a pure *location* problem ("which centre near me is open now?"), a clean geospatial use case. For operators (SHGs, NGOs) it is a classic government-payment-tracking problem, which opens a small B2B segment.

## Verification (27 Oct 2026, batch 1)

- **Confirmed:** the scheme is **continuing**: in March 2025 the Deputy CM told the Assembly there is no decision to discontinue it; the diner still pays **₹10** (actual cost about ₹50 urban / ₹35 rural, rest paid by the Food & Civil Supplies Department).
- **Confirmed:** **vendor payment delays** have been reported, which supports the operator claim/payment tracker idea.
- **Reported (secondary):** about 1,900 centres operating.
- **Changed in guide:** tip now says the scheme is running but individual centres can close.

Sources: [Free Press Journal: Govt won't discontinue Shiv Bhojan Thali](https://www.freepressjournal.in/mumbai/maha-govt-wont-discontinue-10-shiv-bhojan-thali-anandacha-shidha-schemes-dy-cm-ajit-pawar-confirms) · [Deccan Herald: schemes to continue](https://www.deccanherald.com/amp/story/india%2Fmaharashtra%2Fladki-bahin-yojana-ladka-bhau-yojana-shiv-bhojan-thali-anandacha-shidha-to-continue-maharashtra-government-3394717) · [Deccan Herald: ₹10 meal costs ₹50](https://www.deccanherald.com/amp/story/india%2Fmaharashtras-rs-10-shiv-bhojan-meal-actually-costs-rs-50-in-cities-govt-808884.html) · [sarkariyojana.com: Shiv Bhojan](https://sarkariyojana.com/shiv-bhojan-yojana/)
