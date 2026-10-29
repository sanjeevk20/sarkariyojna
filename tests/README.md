# Tests

GitHub runs these on every pull request ([`.github/workflows/tests.yml`](../.github/workflows/tests.yml)). A red ✗ on the PR means something below broke. Open the failed step to see which check.

| File | Checks |
| :--- | :--- |
| [`test_data.py`](test_data.py) | Every checker points at a real guide and has a done stage. Every stage has English and local-language text. No match phrase is empty after clean-up. Complaint letters fill in without leftover placeholders. Map signals use district names that exist on the map. Every guide has Official links, a Verification section, its images, and text in both languages |
| [`test_tools.py`](test_tools.py) | Pilot scorecard: pass marks, Hindi and Marathi words, unreadable rows. Scheme watch: three weekly runs against a local test server that catch an amount change, a new order, a broken page and its recovery, while ignoring a visitor counter |
| [`browser_test.js`](browser_test.js) | In a real browser at phone width: every case in [`paste_cases.json`](paste_cases.json) picks the right stage; all guides open without sideways scrolling; the state filter, checker list, complaint letters, map (all states) and themes work; and no JavaScript errors occur |
| [`paste_cases.json`](paste_cases.json) | Status texts citizens paste, with the stage Sathi must pick. Every checker needs at least one case |

Run locally:

```
python3 -m unittest discover tests
python3 docs/site/build_site.py && node tests/browser_test.js
```

**When you add or change a checker** in `docs/site/tracker.py`, add the real portal or SMS wording to `paste_cases.json`. Do the same when an operator reports that Sathi picked the wrong stage: add the case first, watch it fail, then fix the match phrases.
