// Browser tests for the Sathi site, run against the built page (docs/site/dist/index.html).
//
//   python3 docs/site/build_site.py && node tests/browser_test.js
//
// Needs the `playwright` package and a Chromium browser (CI installs both). Checks, at phone width:
//   1. every "Am I stuck?" paste case in tests/paste_cases.json picks the expected stage;
//   2. every guide page opens with a title and no sideways scrolling;
//   3. the home page state filter, the checker page, the complaint letter, the map and the themes work;
//   4. no JavaScript errors anywhere.
// Exits with code 1 if anything fails, so a pull request that breaks the site shows a red check.
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

const ROOT = path.resolve(__dirname, '..');
const PAGE = 'file://' + path.resolve(process.argv[2] || path.join(ROOT, 'docs/site/dist/index.html'));
const CASES = JSON.parse(fs.readFileSync(path.join(__dirname, 'paste_cases.json'), 'utf8')).cases;

const failures = [];
let checks = 0;
function check(ok, what) {
  checks++;
  if (!ok) { failures.push(what); console.log('FAIL', what); }
}

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 390, height: 900 } });
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  const go = async hash => { await page.goto(PAGE + hash); await page.waitForTimeout(120); };
  const overflow = () => page.evaluate(() => document.documentElement.scrollWidth - innerWidth);

  // 1. Paste matching for every checker.
  await go('#');
  const trackers = await page.evaluate(() => DATA.trackers.map(t => t.guide));
  for (const g of trackers) check(CASES.some(c => c.guide === g), `checker ${g} has no paste cases in tests/paste_cases.json`);
  for (const c of CASES) {
    await go('#check-' + c.guide);
    await page.click('#lang-' + c.lang);
    await page.fill('#ck-paste', c.text);
    await page.click('#ck-find');
    await page.waitForTimeout(60);
    const got = await page.evaluate(() => { const r = document.querySelector('input[name=ck-stage]:checked'); return r ? r.value : null; });
    check(got === c.stage, `paste ${c.guide} [${c.lang}] "${c.text.slice(0, 50)}": expected ${c.stage}, got ${got}`);
    if (c.date) {
      const date = await page.$eval('#ck-date', e => e.value);
      check(date === c.date, `paste ${c.guide}: expected date ${c.date}, got ${date || 'none'}`);
    }
  }
  await page.click('#lang-en');

  // 2. Every guide page.
  await go('#');
  const posts = await page.evaluate(() => POSTS.map(p => p.slug));
  check(posts.length >= 60, `expected 60+ guides, found ${posts.length}`);
  for (const slug of posts) {
    await go('#' + slug);
    const h1 = await page.$eval('h1', e => e.textContent.trim()).catch(() => '');
    check(h1.length > 3, `guide ${slug} has no title`);
    check(await overflow() <= 0, `guide ${slug} scrolls sideways at phone width`);
  }

  // 3a. Home page and state filter.
  await go('#');
  const states = await page.evaluate(() => DATA.states.map(s => s.id));
  for (const st of states) {
    const chip = await page.$(`[data-st=${st}]`);
    check(!!chip, `no state filter chip for ${st}`);
    if (chip) {
      await chip.click();
      await page.waitForTimeout(80);
      const n = await page.evaluate(s => POSTS.filter(p => p.state === s).length, st);
      check(n > 0, `state ${st} has no guides`);
    }
  }
  check(await overflow() <= 0, 'home page scrolls sideways');

  // 3b. Checker page lists every checker; a stuck stage shows the complaint letter.
  await go('#check');
  const listed = await page.$eval('main', m => m.innerText);
  for (const g of trackers) {
    const title = await page.evaluate(s => (POSTS.find(p => p.slug === s) || {}).title, g);
    check(!!title && listed.includes(title), `checker page does not list ${g}`);
  }
  for (const g of trackers) {
    await go('#check-' + g);
    const stuck = await page.evaluate(() => {
      const t = DATA.trackers.find(x => location.hash.endsWith(x.guide));
      const s = t && t.stages.find(s => s.kind === 'stuck');
      return s ? s.id : null;
    });
    if (!stuck) continue;
    await page.check(`input[name=ck-stage][value="${stuck}"]`);
    await page.waitForTimeout(60);
    const text = await page.$eval('#ck-draft', e => e.value).catch(() => '');
    check(/Subject|विषय|ವಿಷಯ/.test(text), `checker ${g}: no complaint letter for stuck stage ${stuck}`);
    check(!/\{(to|subject|scheme|app|date|days|status|ask|name|mobile|today)\}/.test(text), `checker ${g}: unfilled {placeholder} in the complaint letter`);
  }

  // 3c. Map: every state draws its districts.
  await go('#map');
  for (const st of states) {
    const chip = await page.$(`[data-mst=${st}]`);
    check(!!chip, `map has no button for ${st}`);
    if (!chip) continue;
    await chip.click();
    await page.waitForTimeout(120);
    const n = await page.$$eval('.map path', a => a.length);
    check(n >= 20, `map for ${st} draws only ${n} districts`);
  }
  check(await overflow() <= 0, 'map page scrolls sideways');

  // 3d. Themes.
  await go('#');
  for (const theme of ['light', 'dark', 'contrast']) {
    await page.evaluate(t => { try { localStorage.setItem('sathi-theme', t); } catch (e) {} }, theme);
    await page.reload();
    await page.waitForTimeout(120);
    const bg = await page.evaluate(() => getComputedStyle(document.body).backgroundColor);
    check(!!bg && bg !== 'rgba(0, 0, 0, 0)', `theme ${theme}: page has no background`);
  }

  // 4. No JavaScript errors.
  check(errors.length === 0, `JavaScript errors: ${errors.slice(0, 3).join(' | ')}`);

  await browser.close();
  console.log(`\n${checks - failures.length}/${checks} checks passed (${CASES.length} paste cases, ${posts.length} guides, ${trackers.length} checkers, ${states.length} states)`);
  process.exit(failures.length ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
