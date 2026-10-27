// Render an HTML guide (or a page containing a Mermaid SVG) to PNG.
// Usage: node render.js <input.html> <output.png> [css-selector]
//   Guides:   node render.js ferfar-guide.html ferfar-guide.png '#page'
//   Diagrams: node render.js diagram.html ferfar.png svg
// Requires Playwright with Chromium installed.
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const [input, output, selector = 'svg'] = process.argv.slice(2);
  if (!input || !output) {
    console.error('Usage: node render.js <input.html> <output.png> [css-selector]');
    process.exit(1);
  }
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1400, height: 800 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.resolve(input));
  await page.waitForLoadState('networkidle').catch(() => {});
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(500);
  const el = await page.$(selector);
  if (!el) {
    console.error(`No element matches "${selector}" in ${input}`);
    await browser.close();
    process.exit(1);
  }
  await el.screenshot({ path: output });
  await browser.close();
})();
