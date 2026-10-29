# Sathi pilot with CSC / e-Mitra operators

A 4-week field pilot in which Common Service Centre (CSC) and state kiosk operators use Sathi with walk-in customers whose government work is stuck. Operators already see these customers every day, so one trained operator reaches dozens of citizens. The pilot tests whether Sathi saves them time and gets more files unstuck, and produces the evidence for state startup programmes and investors.

| File | What |
| :--- | :--- |
| [`operator-handout-mr.pdf`](operator-handout-mr.pdf) | Operator guide + paper case log, **Marathi** (Maharashtra pilot). Print 2 pages, A4 |
| [`operator-handout-hi.pdf`](operator-handout-hi.pdf) | Same, **Hindi** (Uttar Pradesh pilot) |
| [`operator-handout-en.pdf`](operator-handout-en.pdf) | Same, English, for the team and partners |
| [`recruitment.md`](recruitment.md) | Messages to CSC district managers and operators (Marathi, Hindi, English), 5-minute demo script, answers to common questions, welcome message |
| [`case-log.csv`](case-log.csv) | Columns for typing the paper logs into a spreadsheet each week |
| [`pitch-one-pager.md`](pitch-one-pager.md) | One-page summary for MSInS, StartinUP and early investors |
| [`build_handout.py`](build_handout.py) | Regenerates the handouts; [`qr-check.svg`](qr-check.svg) opens the checker |

## 1. What we want to learn

| Question | Pass mark after 4 weeks |
| :--- | :--- |
| Do operators use it without being chased? | At least **15 logged cases per operator** (300 in total) |
| Does Sathi recognise the customer's status? | A stage is shown for **80%** or more of cases |
| Does the customer leave with a concrete step? | **90%** of cases have an action written (wait with a date, fix, or complaint) |
| Do stuck files move? | **40%** or more of "fix" and "complaint" cases are solved at the 30-day follow-up |
| Is it worth the operator's time? | Median **10 minutes or less** per case, and **70%** of operators want to keep using it |
| Is the content right? | Every error reported is fixed on the site within **7 days** |

Below half of any pass mark, stop and fix that part before expanding. All six met: move to more districts and to Madhya Pradesh / Rajasthan.

## 2. Where and who

| | Maharashtra | Uttar Pradesh |
| :--- | :--- | :--- |
| Proposed district | Chhatrapati Sambhajinagar | Bareilly |
| Why | Mixed rural and urban; land-record bribe and Ladki Bahin eKYC problems already on the Sathi map | Large rural caseload; lekhpal bribe arrests on the map; three UP checkers ready |
| Operators | 10 (CSC VLEs and Aaple Sarkar Seva Kendra operators) | 10 (CSC VLEs and Jan Seva Kendra operators) |
| Handout | Marathi | Hindi |
| Checkers most used | PM-KISAN, Ladki Bahin | PM-KISAN (UP), old-age pension, income certificate |

These are proposals: swap either district if you have stronger contacts elsewhere. Pick operators with a mix of busy town kiosks and village centres, and at least 3 run by women.

How to find operators (messages and demo script in [`recruitment.md`](recruitment.md)): the district CSC manager (CSC e-Governance Services) and the district e-governance society can introduce VLEs; also ask at the tehsil office kiosk cluster. Offer a short demo on their own customer's status.

## 3. Timeline

| Week | What happens |
| :--- | :--- |
| 0 (prep) | Recruit 20 operators. Fill the coordinator name and WhatsApp number in `build_handout.py`, rebuild and print 2 handouts per operator (plus 3 extra log pages). Create a WhatsApp group per district. Train each operator for 30–45 minutes at their kiosk, using a real customer if one walks in. |
| 1–4 | Operators use Sathi and fill the paper log. Coordinator collects a photo of each log page every Friday and types it into `case-log.csv`. A 20-minute group call each week: what confused customers, wrong content, ideas. |
| 5–8 | Follow-up: on each row's follow-up date, the operator asks the customer (when they return, or by the operator's own call) whether it was solved, and fills the last column. |
| 8 | Pilot report: the six pass marks, five short case stories (no names), content fixes made, operator quotes. |

## 4. The operator's routine

Exactly as on the handout: open the checker (QR code), choose the scheme, paste the status or pick it, read out the meaning and the next step, send the complaint letter if overdue, write one log line with a follow-up date 30 days ahead.

Training checklist (tick each with the operator):

- [ ] Opens the checker from the QR code and changes the language
- [ ] Pastes a real portal status and finds the stage
- [ ] Shows the customer the complaint letter and the "where to submit" line
- [ ] Knows never to type Aadhaar, bank, OTP or passwords into Sathi
- [ ] Fills one log line correctly, with no name or number
- [ ] Knows how to report a wrong guide (Report an error) and whom to WhatsApp

## 5. Data and privacy

- The paper log and `case-log.csv` hold **no names, Aadhaar, mobile or application numbers**: only scheme, stage, action, dates, outcome and minutes.
- The customer's contact for follow-up stays in the operator's own register, as it does today. Sathi never receives it.
- What is typed into Sathi stays in that browser. The anonymous district map receives a case only if the customer chooses "share this anonymously", and the map shows district counts only when there are at least 10.
- Ask before following up: "Can I ask you in a month whether this got solved?" Record only the answer.
- Bribe demands: tell the customer about the state anti-corruption helpline. Operators should never name officials in the log or the WhatsApp group.

## 6. Budget (estimate)

| Item | Amount |
| :--- | ---: |
| Operator thank-you, ₹1,500 × 20 for completing 4 weeks of logs and follow-ups | ₹30,000 |
| Printing: handouts and log pages | ₹3,000 |
| Travel for training and two field visits per district | ₹20,000 |
| Phone and data for the coordinator | ₹2,000 |
| Contingency (10%) | ₹5,500 |
| **Total** | **about ₹60,000** |

Do not pay per case: it rewards inventing rows. Pay for complete logs and follow-ups.

## 7. Risks

| Risk | What we do |
| :--- | :--- |
| Operators charge customers for "the Sathi service" | Rule on the handout; ask customers in follow-ups; drop operators who do |
| A guide is wrong and a customer is misled | Report an error on each guide; fix within 7 days; every guide shows its sources and check date |
| Portal wording changes and paste matching stops working | Operators tick the stage by hand; weekly call collects new wording; add it to `docs/site/tracker.py` |
| Low use after week 1 | Weekly call, share early success stories in the group, visit kiosks in week 2 |
| Officials object to the bribe map | The map shows news reports and anonymous counts only, never names; operators are not asked to report bribes |
| Hindi / Marathi wording unclear | Operators mark confusing lines on the handout; fix before any wider print run |

## 8. After the pilot

Write the report with the numbers from `case-log.csv`, then:

1. Fix every content and wording issue found.
2. If the pass marks are met, apply to the Maharashtra State Innovation Society (Startup Week) and StartinUP with the report. Check each programme's current call and terms first.
3. Offer the district administration a monthly summary of where cases get stuck (scheme and stage counts only).
4. Run the next pilot in Madhya Pradesh or Rajasthan with the same kit.

## Rebuilding the handouts

```
python3 docs/pilot/build_handout.py
```

To make the PDFs, open each `operator-handout-*.html` in Chrome and print to A4 with background graphics on, or use Playwright's `page.pdf({format: 'A4', printBackground: true})`. To change the QR target, regenerate `qr-check.svg` with any QR tool (the `qrcode` Python package was used).
