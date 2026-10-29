# Weekly scheme watch

Scheme rules change often: amounts, eKYC windows, deadlines and portals. Two weekly jobs keep the guides current.

| When (IST) | What | Output |
| :--- | :--- | :--- |
| Monday 06:12 | **GitHub Actions** ([`scheme-watch.yml`](../../.github/workflows/scheme-watch.yml)) runs [`scheme_watch.py`](scheme_watch.py): it opens every official link in the guides' "Official links" tables (89 links, 168 citations) and compares each with last week's run | An issue labelled `scheme-watch` when something changed, listing the items below. No issue when nothing changed |
| Monday 11:17 | **Claude scheduled task** reads that issue, searches the news for changes to the main schemes, and proposes guide updates | A pull request with the proposed updates and a source for each change, plus a comment on the issue. **Nothing goes live until you merge** |

The Monday issue lists:

- pages whose visible text changed, with the changed lines. A ⚠ marks pages where amounts or dates moved;
- new notices, orders, circulars or PDFs linked from a page;
- links that stopped working, and links working again.

## How the GitHub job works

- **Free.** It runs on GitHub's servers, which can reach most government sites. It uses the Python standard library only.
- **What it stores.** Each page's text, fingerprint and notice links go into `state.json` on the `scheme-watch-data` branch. Only the latest week is kept, and that branch never touches the site.
- **What it ignores.** It skips scripts, menus repeated on the page, visitor counters, clocks and "last updated" lines, so cosmetic churn rarely triggers a report.
- **Outages.** If a page is down one week, last week's good copy is kept. When the page comes back, only real changes show.
- **JavaScript-only pages.** Pages that load everything with JavaScript are only checked for whether they open.
- **First run.** It only records a baseline, and opens one issue that says so and lists any broken links.

Run it now from **Actions → Scheme watch (weekly) → Run workflow**, or locally:

```
python3 docs/watch/scheme_watch.py --state /tmp/state.json --report /tmp/report.md
```

## What the Claude task changes

When the task changes a fact, it updates every place that fact appears:

- the guide's `*_content.py` file, in English and the local language;
- its `.md` Official links and Verification notes;
- any checker stage in `docs/site/tracker.py`.

It then regenerates the guide HTML and PNGs and rebuilds the site.

It changes a fact only when either a government page or two independent reliable reports support it. Otherwise it marks the item *reported* or leaves it as a note in the PR. It never merges.

Manage the task in claude.ai under Scheduled tasks: "Sathi weekly scheme update".
