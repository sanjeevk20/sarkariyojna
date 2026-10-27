# Sathi - Product Brief
### Solving Govt Department Pain Points for Common Customer
**Focus: Maharashtra + Central | Multi-language | Always Updated**

---

## Positioning: The Differentiator

> **Sathi tells you exactly what's blocking you, what to do next, and what the law says the office owes you, in your language, with the source GR shown.**

*MyScheme tells you what you're eligible for. Haqdarshak helps you apply. Sathi gets you unstuck.*

### Why not the obvious angles

| Angle | Why it isn't defensible |
| :--- | :--- |
| Scheme discovery | MyScheme.gov.in is free, official and improving |
| Multi-language | Bhashini / NLLB make translation cheap for everyone, a minimum requirement not a moat |
| Assisted apply | Haqdarshak already has the agent network, CSR money and govt ties |
| Scheme count | Already capped at 50 on purpose |

### Three pillars

1. **Status decoder that gives the next action** - Turn NSWS / MAITRI / Aaple Sarkar / Mahabhulekh status text into one plain sentence plus one action ("Your file is waiting for a fire NOC upload. Upload it here. No visit needed."). Input is whatever the user has: forwarded SMS, screenshot, query-letter photo. No dependency on portal APIs or scraping.
2. **Rights clock that makes delays enforceable** - Build on the Maharashtra Right to Public Services Act, 2015 (notified time limits + appeal process) and deemed-approval rules where they apply. Countdown per application; when the deadline passes, generate a ready-to-file first appeal / grievance in Marathi.
3. **Source-cited readiness (GR parser = moat)** - "Eligible for 3 schemes, but blocked: income certificate expired 12 days ago. Renew here. (Income limit per GR dated ...)". The versioned, dated, cited rules database built from scanned Marathi GRs is the hard-to-copy asset.

### Wedge: Land

7/12 Health Report + Ferfar Predictor + Rights clock, keyed on Gat number. High pain, people already pay agents, Rs 149 is justified, and GIS depth is an edge no civic-tech competitor has.

Candidate patent claims:
- Inferring e-mutation block reasons by linking parcels across IGR and Mahabhulekh records
- Extracting time-bound rules from scanned GRs into an executable eligibility and SLA graph

### Validate before committing

1. In the 15 office interviews, ask: "Would you pay Rs 99 to know *why* the file is stuck and get the appeal drafted?" Compare with willingness to pay for discovery.
2. Check how many of the 30 query letters map to fewer than ~20 missing-document patterns. If most do, the decoder scales.
3. Verify specific claims before marketing use: the "2025 GR", 90/120-day deemed-approval periods, and when a Talathi is still required. Trust is the product.

---

## 1. Origin - Real Pain You Faced

1. **Single Window Clearance Lag** - NSWS and MAITRI show "Pending at Department" but not what is missing. User has to visit department.
2. **Common Service by Common Map Without Officer** - Auto-approval route exists via CAF + KYA map, but user doesn't know if file is in auto route or stuck.
3. **Land Purchase + Talathi** - Why Talathi needed? Traditional role: maintains 7/12, 8A, Ferfar. Now digital 7/12 with QR, digital signature and 16-digit verification is legally valid without Talathi stamp. Auto e-mutation triggers after IGR registration. Still Talathi needed for inheritance, disputes, agriculturist proof.

**Insight:** Common customer needs 3 things - Where is my file stuck? What document is missing in my language? Do I really need to visit officer?

---

## 2. Common Customer Pain Buckets

- **Status Transparency:** NSWS / MAITRI / Mahabhulekh / Aaple Sarkar use different language. No plain Marathi/Hindi explanation.
- **Document Confusion:** Same doc called 3 names. Query letter is scanned English PDF.
- **Officer Visit Confusion:** After 2025 GR, many services are automatic, but people still pay agents for stamp.
- **Deemed Approval:** Factory plan 90 days, license 120 days auto, but no countdown timer shown.
- **Scheme Discovery:** Central schemes in English, State GRs in Marathi PDFs. No single source in user language.

---

## 3. Product Ideas - 12 Concepts

### A. Land & Revenue
1. **7/12 Health Report** - Enter Gat No, get red/green report: owner history, loan, stay, duplicate Ferfar. Rs 149/report.
2. **Ferfar Predictor** - After sale deed, track if auto e-mutation triggered or blocked and why.
3. **Talathi Queue App** - Live token system for Saza, shows leave status, books slot.

### B. Business & Single Window
4. **Query Letter Translator & Auto Reply** - OCR query letter, translate to Marathi/Hindi, draft reply with doc placeholders.
5. **Deemed Approval Clock** - Countdown for auto approval, auto-generates grievance on Day 91.
6. **Official Fee vs Agent Fee Calculator** - Shows official fee vs market agent fee for 50 common services.

### C. Citizen Certificates & Schemes
7. **Family Sarkar Vault** - Family-wise vault, expiry alerts, renewal link via Aaple Sarkar. Freemium Rs 199/year.
8. **Scheme Finder (Focus Product)** - See Section 4.
9. **Marathi Voice Sarkar Bot** - WhatsApp voice bot, user sends Marathi voice note, gets PDF + audio reply.

### D. System Level
10. **Chrome Plugin for MAITRI/NSWS** - Sidebar explains each field in Marathi, like Grammarly for govt portals. For CAs and e-Seva operators.
11. **Agent Rating & SLA Tracker** - Publish avg delay per department from anonymous tracker data.
12. **Appointment + Document Check Before Visit** - Verifies photo, self-declaration via camera before booking Tahsildar slot.

---

## 4. Deep Dive: Scheme Finder

### Why Scheme Finder Is Good But Not Alone

- **MyScheme.gov.in:** Official platform, 3-step process - enter demographic, income, category, shows relevant central+state schemes. Reduces time and effort.
- **Haqdarshak:** Assisted-tech model - users assess eligibility, consolidate docs, apply and track via digital tools + trained community agents (women). Revenue via beneficiary fees, commissions from govt, corporate CSR fees.

**Learning:** Discovery alone = no money. Discovery + Readiness + Assisted Apply = money.

### Make It Good

1.  **Niche Down:** Don't do 2000 schemes. Do 50 high-demand schemes: 20 Central + 30 Maharashtra.
2.  **Connect to Readiness:** "You are eligible for 3 schemes but blocked because income certificate expired"
3.  **Sell to B2B:** Banks for KCC loans, Corporates for blue-collar worker welfare, e-Seva Kendras for lead gen.

### Multi-language Strategy

- **UI Languages MVP:** Marathi, Hindi, English (covers 95% for Maharashtra)
- **Content Translation:** 
    - Title: Human translated
    - Benefit: Colloquial one-liner - "Mulila 18 varsha zalyavar 1 lakh miltat"
    - Eligibility: Icons + bullets, not paragraphs
    - Audio: 20 sec Marathi voice note per scheme
- **Location Aware:** If district=Thane, show Maharashtra schemes first, hide other state schemes.

### Update Frequency - The Moat

| Source | Frequency | How |
| :--- | :--- | :--- |
| Central - MyScheme, PIB | Weekly | RSS + Scraper |
| State - MahaDBT, Aaple Sarkar, GR site | Daily during budget/monsoon, Weekly otherwise | GR PDFs in Marathi scanned - OCR + LLM Parser |
| Eligibility / Amount Change | Same Day | Alert on keywords "Sudharit", "Anudan", "Vyapti" |
| Last Date / Portal Open-Close | Daily | What user cares most |

**Pipeline:**
1. Auto Pull: Cron pulls MyScheme + MahaDBT nightly
2. GR Parser: New GR PDF -> OCR -> LLM extracts scheme name, change type, date. Flag if confidence <80%
3. Human in Loop: 1 person 2 hrs/day approves top 50 schemes
4. Community: e-Seva operators can click "This scheme closed now"

**Trust Element:** Show changelog per scheme - "Updated 2 days ago - Income limit 2L to 3L - Source: GR dated..."

---

## 5. Product Name Options

### Umbrella Brand Recommended

**Top 3:**

1.  **Yojana Sathi** - Best for Maharashtra-first. Instantly understood. Tagline: "Tumchi Yojana, Tumchya Bhashet" Domain: yojanasathi.in
2.  **Scheme Sathi** - Best for Pan-India scalable. Works in Hindi/Marathi/English. Tagline: "Central or State, Your Scheme in Your Language"
3.  **Sathi** - Umbrella. App: Sathi - Sarkar Ka Sathi. Inside modules: Yojana Sathi, Jamin Sathi, Dakhla Sathi.

**Other Options:**
- Labh Mitra, Aapli Yojana, GR Sathi, Jan Labh, Yojana Setu, Khoj Sathi, Seva Sathi, Haq Sathi, Sathi, YojanaKhoj

**Naming Test:**
1. Say on phone to 5 people - can they spell without help?
2. Check .in domain + Instagram handle
3. Say "Mala Yojana Sathi var yojana bhetli" - natural in Marathi?

---

## 6. MVP - First 90 Days

**Phase 1 (Month 1): WhatsApp Tracker Bot**
- Input: Any govt application number OR Gat number OR scheme name
- Output: Plain language status + what to do next in Marathi
- Goal: 100 daily active users organically

**Phase 2 (Month 2): Scheme Finder 50**
- Central 20 + Maharashtra 30, in 3 languages, with audio, updated weekly
- Add Document Readiness Check

**Phase 3 (Month 3): Monetization**
- B2C: Free 2 tracks, Rs 99/mo unlimited + alerts
- B2B: Rs 999/mo for agents/CAs dashboard for 50 clients
- B2B2C: Tie-up with 5 e-Seva Kendras, Rs 30 per lead

---

## 7. Tech Stack Suggestion

- Frontend: React + Next.js, PWA for low-end phones
- Backend: Node.js / Python, PostgreSQL with JSONB for eligibility rules
- OCR: Google Vision / Tesseract for Marathi GRs
- Translation: NLLB + Human review memory
- WhatsApp: WhatsApp Business API
- Storage: DigiLocker integration for doc vault (don't store Aadhaar)
- Hosting: MeitY empanelled cloud if planning govt pitch

---

## 8. Next Steps

1. Interview 15 people outside Talathi / Sub-Registrar / MIDC office
2. Collect 30 real query letters - find repeat patterns
3. Build manual WhatsApp group - check status for free - validate language
4. Lock name and domain
5. Build GR parser for 1 department (e.g., Revenue) as POC

---

*Created: Oct 2026 | Location Focus: Maharashtra | Author: Sanjeev S*
