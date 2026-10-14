// Extract every English text unit a reader can reach, by running the real site.
// Usage: node scripts/i18n/extract.mjs
// Writes i18n/source.json. New routes are found by following links, so new
// experiments and sections are picked up without configuration.
import { config, serve, browser, writeJSON, words } from './lib.mjs';
import { execFileSync } from 'node:child_process';

const cfg = config();
const exclude = cfg.crawl.exclude.map(r => new RegExp(r));
const srv = await serve();
const b = await browser();
const ctx = await b.newContext({ serviceWorkers: 'block' });
await ctx.addInitScript(() => { window.__SIDUS_I18N_MODE = 'collect'; });
const page = await ctx.newPage();
const errors = [];
page.on('pageerror', e => errors.push(String(e)));

function normalize(href, from) {
  let u;
  try { u = new URL(href, srv.url + (from.startsWith('#') ? '/index.html' + from : from)); } catch { return null; }
  if (u.origin !== srv.url) return null;
  let p = u.pathname;
  if (p === '/' || p === '/index.html') return u.hash.startsWith('#/') ? u.hash : (u.hash ? null : '#/home');
  if (!/\.[a-z0-9]+$/i.test(p) && !p.endsWith('/')) p += '/';
  if (!(p.endsWith('/') || p.endsWith('.html'))) return null;
  if (exclude.some(re => re.test(p))) return null;
  return p;
}

const units = new Map(), routes = new Map(), seen = new Set();
const queue = cfg.crawl.entries.map(e => normalize(e, '/')).filter(Boolean);
let onSpa = false;

async function visit(route) {
  if (route.startsWith('#/')) {
    if (!onSpa) { await page.goto(srv.url + '/index.html' + route); onSpa = true; }
    else {
      await page.evaluate(r => new Promise(res => {
        if (location.hash === r) return res();
        addEventListener('hashchange', () => setTimeout(res, 30), { once: true });
        location.hash = r;
      }), route);
    }
  } else {
    await page.goto(srv.url + route); onSpa = false;
  }
  await page.waitForFunction(() => window.__SIDUS_I18N && document.readyState === 'complete');
  return page.evaluate(() => window.__SIDUS_I18N.collect());
}

while (queue.length && seen.size < 3000) {
  const route = queue.shift();
  if (seen.has(route)) continue;
  seen.add(route);
  const res = await visit(route);
  const order = [];
  for (const u of res.units) {
    let rec = units.get(u.key);
    if (!rec) { rec = { t: u.skel, k: u.kind, pk: u.pk, g: u.tag, r: [] }; units.set(u.key, rec); }
    if (!rec.r.includes(route)) rec.r.push(route);
    if (!order.includes(u.key)) order.push(u.key);
  }
  routes.set(route, order);
  for (const h of res.links) {
    const n = normalize(h, route);
    if (n && !seen.has(n)) queue.push(n);
  }
}
await b.close(); srv.close();

// Units that differ only in their numbers ("Document I · 3 / 12") become one pattern.
const TOK = /(⟦\/?\d+⟧)/;
const digitsOf = s => s.split(TOK).filter((x, i) => i % 2 === 0).join(' ').match(/\d+/g) || [];
const template = s => { let n = 0; return s.split(TOK).map((x, i) => i % 2 ? x : x.replace(/\d+/g, () => '{' + n++ + '}')).join(''); };
const groups = new Map();
for (const [key, u] of units) {
  if (u.k === 't' || u.pk === key || /[{}]/.test(u.t)) continue;
  if (!groups.has(u.pk)) groups.set(u.pk, []);
  groups.get(u.pk).push(key);
}
const patterns = {}, member = new Map();
for (const [pk, keys] of groups) {
  const list = keys.map(k => units.get(k));
  const n = digitsOf(list[0].t).length;
  if (keys.length < cfg.patterns.minMembers || n === 0) continue;
  if (list.some(u => words(u.t) > cfg.patterns.maxWords || digitsOf(u.t).length !== n || template(u.t) !== template(list[0].t))) continue;
  patterns[pk] = { t: template(list[0].t), k: list[0].k, g: list[0].g, r: [...new Set(list.flatMap(u => u.r))], n: keys.length };
  keys.forEach(k => member.set(k, 'p:' + pk));
}

// Routes are stored once and referenced by index; "order" is reading order, used for translator context.
const routeList = [...routes.keys()], ri = new Map(routeList.map((r, i) => [r, i]));
const outUnits = {};
for (const [key, u] of units) if (!member.has(key)) outUnits[key] = { t: u.t, k: u.k, g: u.g, r: u.r.map(r => ri.get(r)) };
for (const p of Object.values(patterns)) p.r = p.r.map(r => ri.get(r));
const order = [];
for (const keys of routes.values()) for (const k of keys) { const id = member.get(k) || k; if (!order.includes(id)) order.push(id); }

let commit = '';
try { commit = execFileSync('git', ['rev-parse', '--short', 'HEAD'], { encoding: 'utf8' }).trim(); } catch { /* not a repo */ }
const totalWords = Object.values(outUnits).reduce((a, u) => a + words(u.t), 0) + Object.values(patterns).reduce((a, p) => a + words(p.t), 0);
writeJSON('i18n/source.json', {
  generated: new Date().toISOString(), commit,
  counts: { routes: routes.size, units: Object.keys(outUnits).length, patterns: Object.keys(patterns).length, words: totalWords },
  routes: routeList, units: outUnits, patterns, order
});
console.log(`Extracted ${Object.keys(outUnits).length} units and ${Object.keys(patterns).length} patterns (${totalWords} English words) from ${routes.size} routes.`);
if (errors.length) { console.error('Page errors during extraction:\n' + [...new Set(errors)].join('\n')); process.exitCode = 1; }
