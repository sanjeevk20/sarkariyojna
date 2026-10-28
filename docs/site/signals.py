"""Public signals for the "Where are people stuck?" map: news reports of bribe arrests and payment delays.

Collected 28 Oct 2026 from news search results (linked). These are allegations and reports, not
findings: an arrest is not a conviction, and a news story about delays is not a count. District names
use the Census 2011 boundaries in geo/districts.json; ALIASES gives today's names for display.

kind: "bribe-arrest" (anti-corruption trap reported in the news) or "delay" (citizens reporting
stuck payments or services). district=None marks a state-wide signal, listed but not mapped.
"""

ALIASES = {"Aurangabad": "Chhatrapati Sambhajinagar", "Raigarh": "Raigad", "Bid": "Beed",
           "Mysore": "Mysuru", "Belgaum": "Belagavi", "Gulbarga": "Kalaburagi", "Bangalore": "Bengaluru",
           "Allahabad": "Prayagraj", "Faizabad": "Ayodhya"}


def sig(state, district, month, kind, service, summary, src, url):
    return dict(state=state, district=district, month=month, kind=kind, service=service,
                summary=summary, source=src, url=url)


SIGNALS = [
    # ---------------- Maharashtra
    sig("mh", "Satara", "2026-06", "bribe-arrest", "7/12 heirship entry (ferfar)",
        "ACB arrested a talathi in Karad tehsil taking ₹2,500 to record an heirship entry on a 7/12 after a grandmother's death.",
        "UNI", "https://uniindia.com/acb-officials-nab-talathi-for-accepting-bribe-of-rs-2500/west/news/3865144.html"),
    sig("mh", "Aurangabad", "2026-04", "bribe-arrest", "7/12 mutation entry (ferfar)",
        "ACB trapped a talathi in Sillod tehsil over ₹5,000 (₹7,000 demanded) to update a 7/12 mutation entry.",
        "Lokmat Times", "https://www.lokmattimes.com/aurangabad/talathi-trapped-accepting-rs-5000-bribe-1/amp"),
    sig("mh", "Ratnagiri", "2026-05", "bribe-arrest", "Land record update",
        "Two revenue staff arrested over a ₹20,000 bribe to update land records (date as shown on the page).",
        "ThePrint / PTI", "https://theprint.in/india/two-revenue-dept-personnel-caught-accepting-bribe-in-ratnagiri-arrested/2932079/"),
    sig("mh", None, "2026-04", "delay", "Ladki Bahin eKYC",
        "About 68 lakh Ladki Bahin accounts were closed after the eKYC deadline; nearly 20 lakh were later found eligible.",
        "The Week / PTI", "https://www.theweek.in/wire-updates/national/2026/04/02/68-lakh-ladki-bahin-accounts-in-maharashtra-closed-for-e-kyc-non-compliance.html"),
    sig("mh", None, "2026-02", "delay", "Ladki Bahin eKYC",
        "Women missing 3 to 4 months of payments were told their accounts were blocked for incomplete eKYC; portal glitches hindered corrections.",
        "Angel One news", "https://www.angelone.in/news/government-schemes/majhi-ladki-bahin-yojana-e-kyc-corrections-remain-challenging-after-portal-reopens"),
    # ---------------- Uttar Pradesh
    sig("up", "Rampur", "2026-07", "bribe-arrest", "Varasat (inheritance entry)",
        "Anti-corruption team arrested a lekhpal taking ₹5,000 to record a varasat (inheritance) entry.",
        "Patrika", "https://www.patrika.com/rampur-news/rampur-lekhpal-bribery-arrest-5000-trap-20480690"),
    sig("up", "Bahraich", "2026-07", "bribe-arrest", "Land documents",
        "A lekhpal was caught taking ₹10,000 for land-document work; the complainant said ₹70,000 had already been paid.",
        "Patrika", "https://www.patrika.com/bahraich-news/bahraich-anti-corruption-team-caught-lekhpal-taking-bribe-20616127"),
    sig("up", "Bareilly", "2026-07", "bribe-arrest", "Revenue work",
        "A lekhpal was arrested red-handed taking a ₹5,000 bribe; investigators are reviewing earlier demands.",
        "Patrika", "https://www.patrika.com/bareilly-news/big-action-by-anti-corruption-lekhpal-arrested-red-handed-while-taking-bribe-of-5-thousand-case-registered-19617693"),
    # ---------------- Karnataka
    sig("ka", "Dharwad", "2026-09", "bribe-arrest", "RTC correction",
        "Lokayukta trap: a tahsildar allegedly took ₹50 lakh (and sought an acre of land) to correct RTC records.",
        "The CSR Journal", "https://thecsrjournal.in/karnataka-official-detained-for-alleged-acceptance-of-rs-50-lakh-bribe"),
    sig("ka", "Bidar", "2025-12", "delay", "Gruha Lakshmi",
        "Residents said Gruha Lakshmi money had not been credited for three to four months.",
        "IANS", "https://ianslive.in/karnataka-gruha-lakshmi-beneficiaries-disappointed-over-delay-in-payouts--20251224165404"),
    sig("ka", "Mysore", "2025-12", "delay", "Gruha Lakshmi",
        "Beneficiaries reported Gruha Lakshmi delays of three to five months.",
        "IANS", "https://ianslive.in/karnataka-gruha-lakshmi-beneficiaries-disappointed-over-delay-in-payouts--20251224165404"),
    sig("ka", "Belgaum", "2025-12", "delay", "Gruha Lakshmi",
        "Women pressed the Women and Child Development Minister to release two months of pending funds.",
        "IANS", "https://ianslive.in/karnataka-gruha-lakhsmi-scheme-beneficiaries-share-pain-over-stalled-funds--20251223185403"),
    sig("ka", None, "2026-05", "delay", "Gruha Lakshmi",
        "The High Court issued notice to the state on a petition over delayed Gruha Lakshmi payments.",
        "Organiser", "https://organiser.org/2026/05/22/354656/bharat/karnataka-high-court-issues-notice-to-siddaramaiah-govt-over-delay-in-gruhalakshmi-payments/"),
]
