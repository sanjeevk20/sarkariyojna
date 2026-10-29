"""Weekly scorecard for the Sathi operator pilot: reads case-log.csv and checks the six pass marks.

Type each Friday's paper log photos into case-log.csv (one row per case), then run:

    python3 docs/pilot/scorecard.py                       # whole pilot so far
    python3 docs/pilot/scorecard.py --week 2              # pro-rates the case target to week 2 of 4
    python3 docs/pilot/scorecard.py --continue 15/19 --errors 6/7 --out docs/pilot/scorecard-week2.md

--continue  operators who said they want to keep using Sathi / operators asked (from the weekly call)
--errors    reported errors fixed within 7 days / errors reported (from the GitHub issues)

Columns: operator_code, district, row, date, scheme, stage_shown, action_today, follow_up_date,
outcome_30_days, minutes. Use English codes where you can (wait / fix / complaint, solved / stuck / unknown);
common Hindi and Marathi words from the paper log are understood too. The log holds no personal data, and
this script never needs any.
"""
import argparse, csv, datetime as dt, pathlib, statistics, sys
from collections import Counter, defaultdict

HERE = pathlib.Path(__file__).resolve().parent
TARGET_CASES, TARGET_PER_OP, WEEKS = 300, 15, 4

ACTION = {"wait": "wait", "fix": "fix", "complaint": "complaint",
          "प्रतीक्षा": "wait", "इंतज़ार": "wait", "इंतजार": "wait", "थांबा": "wait", "वाट": "wait",
          "सुधार": "fix", "दुरुस्ती": "fix", "ठीक": "fix",
          "शिकायत": "complaint", "तक्रार": "complaint"}
OUTCOME = {"not solved": "stuck", "unsolved": "stuck", "हल नहीं": "stuck", "नहीं सुलझा": "stuck", "सुटले नाही": "stuck",
           "solved": "solved", "stuck": "stuck", "still stuck": "stuck", "unknown": "unknown", "not known": "unknown",
           "हल": "solved", "सुलझा": "solved", "सुटले": "solved", "झाले": "solved",
           "अटका": "stuck", "अब भी अटका": "stuck", "अडकले": "stuck", "अजून अडकले": "stuck",
           "पता नहीं": "unknown", "माहीत नाही": "unknown"}
EMPTY = {"", "-", "none", "no", "na", "n/a", "नहीं", "नाही"}


def norm(value, table):
    v = (value or "").strip().lower()
    if v in table:
        return table[v]
    for k, code in table.items():  # tolerate extra words, e.g. "complaint sent"; negated forms are listed first
        if k in v:
            return code
    return None


def parse_date(s):
    s = (s or "").strip()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%d.%m.%Y", "%d/%m/%y"):
        try:
            return dt.datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    return None


def ratio(arg):
    if not arg:
        return None
    a, b = arg.split("/")
    return int(a), int(b)


def verdict(value, target, higher_is_better=True):
    """PASS, ON TRACK (at least half way), or STOP AND FIX (below half the mark, per the pilot plan)."""
    if value is None:
        return "NO DATA"
    if higher_is_better:
        return "PASS" if value >= target else ("ON TRACK" if value >= target / 2 else "STOP AND FIX")
    return "PASS" if value <= target else ("ON TRACK" if value <= target * 2 else "STOP AND FIX")


def pct(n, d):
    return None if not d else n / d


def fmt_pct(x):
    return "-" if x is None else f"{x:.0%}"


def score(rows, week=None, cont=None, errors=None):
    out, problems = [], []
    for i, r in enumerate(rows, 2):
        r["_action"] = norm(r.get("action_today"), ACTION)
        r["_outcome"] = norm(r.get("outcome_30_days"), OUTCOME)
        r["_date"] = parse_date(r.get("date"))
        r["_stage"] = (r.get("stage_shown") or "").strip().lower() not in EMPTY
        try:
            r["_min"] = float(r.get("minutes") or "")
        except ValueError:
            r["_min"] = None
        if r.get("action_today", "").strip() and not r["_action"]:
            problems.append(f"line {i}: action '{r['action_today']}' not recognised (use wait / fix / complaint)")
        if r.get("outcome_30_days", "").strip() and not r["_outcome"]:
            problems.append(f"line {i}: outcome '{r['outcome_30_days']}' not recognised (use solved / stuck / unknown)")
        if r.get("date", "").strip() and not r["_date"]:
            problems.append(f"line {i}: date '{r['date']}' not recognised (use YYYY-MM-DD or DD/MM/YYYY)")

    n = len(rows)
    case_target = TARGET_CASES if not week else round(TARGET_CASES * min(week, WEEKS) / WEEKS)
    ops = Counter(r.get("operator_code", "").strip() or "?" for r in rows)
    per_op_target = TARGET_PER_OP if not week else round(TARGET_PER_OP * min(week, WEEKS) / WEEKS)
    ops_ok = sum(1 for c in ops.values() if c >= per_op_target)
    stage = pct(sum(r["_stage"] for r in rows), n)
    action = pct(sum(1 for r in rows if r["_action"]), n)
    acted = [r for r in rows if r["_action"] in ("fix", "complaint")]
    known = [r for r in acted if r["_outcome"] in ("solved", "stuck")]
    solved = pct(sum(1 for r in known if r["_outcome"] == "solved"), len(known))
    mins = [r["_min"] for r in rows if r["_min"] is not None]
    median = statistics.median(mins) if mins else None
    cont_r = pct(*cont) if cont else None
    err_r = pct(*errors) if errors else None

    marks = [
        ("Cases logged", f"{n} (target {case_target}; {ops_ok}/{len(ops)} operators at {per_op_target}+)",
         verdict(n, case_target) if n else "NO DATA"),
        ("Stage shown by Sathi", f"{fmt_pct(stage)} (target 80%)", verdict(stage, 0.80)),
        ("Action written", f"{fmt_pct(action)} (target 90%)", verdict(action, 0.90)),
        ("Stuck files solved at 30 days", f"{fmt_pct(solved)} of {len(known)} followed up "
         f"(target 40%; {len(acted) - len(known)} fix/complaint cases still awaiting follow-up)", verdict(solved, 0.40)),
        ("Median minutes per case", "-" if median is None else f"{median:g} (target 10 or less)",
         verdict(median, 10, higher_is_better=False)),
        ("Operators who want to continue", f"{fmt_pct(cont_r)} (target 70%)" + (f", {cont[0]}/{cont[1]}" if cont else ", pass --continue"),
         verdict(cont_r, 0.70)),
        ("Errors fixed within 7 days", f"{fmt_pct(err_r)} (target 100%)" + (f", {errors[0]}/{errors[1]}" if errors else ", pass --errors"),
         verdict(err_r, 1.0)),
    ]

    title = "Sathi pilot scorecard" + (f", week {week} of {WEEKS}" if week else "")
    out += [f"# {title}", "", f"Generated {dt.date.today().isoformat()} from case-log.csv ({n} cases).", "",
            "| Pass mark | Result | Status |", "| :--- | :--- | :--- |"]
    out += [f"| {a} | {b} | **{c}** |" for a, b, c in marks]
    out += ["", "PASS = mark met. ON TRACK = at least half way. STOP AND FIX = below half: fix that part before expanding.", ""]

    by_d = defaultdict(list)
    for r in rows:
        by_d[r.get("district", "").strip() or "?"].append(r)
    out += ["## By district", "", "| District | Operators | Cases | Stage shown | Action written | Solved (followed up) | Median minutes |",
            "| :--- | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for d, rs in sorted(by_d.items()):
        a = [r for r in rs if r["_action"] in ("fix", "complaint")]
        k = [r for r in a if r["_outcome"] in ("solved", "stuck")]
        m = [r["_min"] for r in rs if r["_min"] is not None]
        out.append(f"| {d} | {len({r.get('operator_code') for r in rs})} | {len(rs)} | "
                   f"{fmt_pct(pct(sum(r['_stage'] for r in rs), len(rs)))} | {fmt_pct(pct(sum(1 for r in rs if r['_action']), len(rs)))} | "
                   f"{fmt_pct(pct(sum(1 for r in k if r['_outcome'] == 'solved'), len(k)))} ({len(k)}) | "
                   f"{'-' if not m else f'{statistics.median(m):g}'} |")

    out += ["", "## By operator", "", "| Operator | District | Cases | Stage shown | Follow-ups done |", "| :--- | :--- | ---: | ---: | ---: |"]
    by_op = defaultdict(list)
    for r in rows:
        by_op[r.get("operator_code", "").strip() or "?"].append(r)
    for o, rs in sorted(by_op.items()):
        fu = sum(1 for r in rs if r["_outcome"])
        flag = " ⚠" if len(rs) < per_op_target else ""
        out.append(f"| {o}{flag} | {rs[0].get('district', '')} | {len(rs)} | "
                   f"{fmt_pct(pct(sum(r['_stage'] for r in rs), len(rs)))} | {fu}/{len(rs)} |")
    out += ["", f"⚠ = below {per_op_target} cases; call or visit this operator.", ""]

    schemes = Counter((r.get("scheme") or "?").strip() for r in rows)
    stages = Counter(((r.get("scheme") or "?").strip(), (r.get("stage_shown") or "").strip()) for r in rows if r["_stage"])
    out += ["## Where people are stuck", "", "| Scheme | Cases | Most common stage |", "| :--- | ---: | :--- |"]
    for s, c in schemes.most_common():
        top = [(st, k) for (sc, st), k in stages.most_common() if sc == s]
        out.append(f"| {s} | {c} | {top[0][0] + f' ({top[0][1]})' if top else '-'} |")

    weeks = Counter(r["_date"].isocalendar()[:2] for r in rows if r["_date"])
    if weeks:
        out += ["", "## Cases per week", "", "| Week starting | Cases |", "| :--- | ---: |"]
        for (y, w), c in sorted(weeks.items()):
            out.append(f"| {dt.date.fromisocalendar(y, w, 1).isoformat()} | {c} |")

    due = [r for r in rows if not r["_outcome"] and parse_date(r.get("follow_up_date")) and parse_date(r.get("follow_up_date")) <= dt.date.today()]
    out += ["", "## Follow-ups due now", "",
            f"{len(due)} cases have a follow-up date today or earlier and no outcome yet." +
            ("" if not due else " Ask these operators: " + ", ".join(f"{o} ({c})" for o, c in Counter(r.get('operator_code') for r in due).most_common()) + ".")]
    if problems:
        out += ["", "## Rows to correct", ""] + [f"- {p}" for p in problems[:50]]
    return "\n".join(out) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("csv", nargs="?", default=str(HERE / "case-log.csv"))
    ap.add_argument("--week", type=int, help="pilot week (1-4) to pro-rate the case targets")
    ap.add_argument("--continue", dest="cont", help="operators wanting to continue / asked, e.g. 15/19")
    ap.add_argument("--errors", help="errors fixed within 7 days / reported, e.g. 6/7")
    ap.add_argument("--out", help="also write the report to this Markdown file")
    a = ap.parse_args(argv)
    with open(a.csv, newline="", encoding="utf-8-sig") as f:
        rows = [r for r in csv.DictReader(f) if any((v or "").strip() for v in r.values())]
    report = score(rows, a.week, ratio(a.cont), ratio(a.errors))
    sys.stdout.write(report)
    if a.out:
        pathlib.Path(a.out).write_text(report, encoding="utf-8")


if __name__ == "__main__":
    main()
