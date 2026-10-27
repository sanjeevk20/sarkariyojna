# Mahatma Phule Backward Class Development Corporation (Loan Schemes) - End-to-End Workflow

Mahatma Phule Magasvargiya Vikas Mahamandal: business finance for **Scheduled Caste and Nav-Bauddha** families in Maharashtra. Three common routes by project size: **subsidy scheme** (small projects, subsidy + bank loan), **seed capital / margin money** (corporation share at low interest + bank loan), and **NSFDC term loans** routed through the corporation. Applied at the corporation's district office. For open-category communities, see [Annasaheb Patil loan scheme](annasaheb-patil.md).

## For citizens: step by step

Blue = you do this. Purple = corporation / bank does this (you wait). Green = business running. Red = what to do if stuck. Orange = how to escalate.

### English

![Mahatma Phule Mahamandal guide](mahatma-phule-mahamandal-guide.png)

### मराठी (Marathi)

![महात्मा फुले महामंडळ मार्गदर्शक](mahatma-phule-mahamandal-guide-mr.png)

Sources: [`mahatma-phule-mahamandal-guide.html`](mahatma-phule-mahamandal-guide.html), [`mahatma-phule-mahamandal-guide-mr.html`](mahatma-phule-mahamandal-guide-mr.html), generated from [`mahatma_phule_mahamandal_content.py`](mahatma_phule_mahamandal_content.py) with `python3 gen_guide.py mahatma_phule_mahamandal_content.py`. Marathi text pending native-speaker review.

## Official links

Use only these addresses. Checked on 27 Oct 2026 through search results; the government sites could not be opened directly from our build environment. "Third-party sites only" means several non-government sites agree on the address but no government page confirmed it yet, so open it and check before you share it.

| What | Link | Checked via |
| :--- | :--- | :--- |
| Mahatma Phule Mahamandal (MPBCDC) | <https://mpbcdc.maharashtra.gov.in> | Third-party sites only |

## For the Sathi team: system workflow

Yellow boxes = where Sathi plugs in. Red boxes = common blockers.

![Mahatma Phule Mahamandal system workflow](mahatma-phule-mahamandal.png)

<details><summary>Mermaid source (editable)</summary>

```mermaid
flowchart TD
    A([SC / Nav-Bauddha family wants a business]) --> E{1. Eligible?<br/>MH resident, age + income limit,<br/>no earlier default}
    E -- No --> X([Check other schemes])
    E -- Yes --> SCH{2. Project size}
    SCH -- Small --> S1A[Subsidy scheme<br/>subsidy + bank loan]
    SCH -- Medium --> S2A[Seed capital<br/>corporation share + bank loan]
    SCH -- Larger --> S3A[NSFDC term loan<br/>via corporation]
    S1A --> P[3. Business plan + quotations]
    S2A --> P
    S3A --> P
    P --> D[4. Documents<br/>caste + income cert, domicile, Aadhaar,<br/>project report, place proof, no-dues]
    D --> AP[5. Apply at district office<br/>acknowledgement]
    AP --> SC[6. Scrutiny + site visit]
    SC -- Missing quotation / place proof --> F1[Pending: fix and resubmit]
    SC --> CM{Sanction committee}
    CM -- Rejected --> F2[Rejected with reason]
    CM -- Sanctioned --> BK{Bank part needed?}
    BK -- Yes --> BANK[Bank sanctions its loan]
    BANK -- Delay --> F3[Bank delay:<br/>corporation follows up]
    BK -- No --> REL
    BANK --> REL[7. Release to supplier<br/>asset verification]
    REL --> RUN([8. Run business, repay EMIs])
    RUN -- Missed EMIs --> F4[Defaulter: future loans blocked]
    F1 -. stuck long .-> T[District manager / regional office /<br/>Lead Bank Manager]

    X1[[Sathi: Eligibility + scheme-size router]]:::sathi -.-> SCH
    X2[[Sathi: Project report + quotation checklist]]:::sathi -.-> P
    X3[[Sathi: Readiness: caste + income certs]]:::sathi -.-> D
    X4[[Sathi: Pending clock + escalation draft]]:::sathi -.-> T
    X5[[Sathi: EMI reminders]]:::sathi -.-> RUN

    classDef sathi fill:#FFF3CD,stroke:#E0A800,color:#000
    classDef blocked fill:#F8D7DA,stroke:#C82333,color:#000
    class F1,F2,F3,F4 blocked
```

</details>

## Stages

| # | Stage | Owner | Common blocker | Sathi action |
|---|---|---|---|---|
| 1 | Eligibility | Citizen | Earlier default; wrong corporation | Eligibility + corporation router |
| 2 | Choose scheme | Citizen | Doesn't know subsidy vs seed capital vs NSFDC | Scheme-size router |
| 3 | Plan + quotations | Citizen | No quotations / weak project report | Project report + quotation checklist |
| 4 | Documents | Citizen | Missing caste / income certificate | Readiness; links to [caste](caste-certificate.md) and [income](income-certificate.md) guides |
| 5 | Apply | Citizen | Agent fraud | Free-application messaging |
| 6 | Scrutiny + site visit + committee | District office | Pending on missing quotation / place proof; rejected | Pending clock + escalation draft |
| 7 | Release | Bank / corporation | Bank delays its share | Bank follow-up tracker |
| 8 | Repayment | Beneficiary | Missed EMIs → defaulter, future schemes blocked | EMI reminders |

**Why this matters for Sathi:** together with Annasaheb Patil (open category), this gives Sathi a **"which corporation is mine?"** router across community-specific development corporations, which is a common point of confusion. The same bank-readiness and EMI-tracker features apply to both.

## Verification (27 Oct 2026, batch 3)

- **Reported (secondary):** official website **mpbcdc.maharashtra.gov.in**; small-project subsidy scheme with 50% bank loan + corporation grant (figures unclear: around ₹10,000 grant, projects up to ~₹50,000).
- **Changed in guide:** official website added.
- **Not found:** age / income limits, NSFDC scheme details, online application steps. Guide keeps general wording.

Sources: [MahaBharti: Anudan Yojana for Backward Class (mpbcdc)](https://mahabharti.in/yojana/anudan-yojana-for-backward-class)
