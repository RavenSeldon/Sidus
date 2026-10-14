// Check the translation layer.
//   node scripts/i18n/check.mjs              frozen canon, translation memory, bundles, coverage
//   node scripts/i18n/check.mjs --render     also load every page of the current wave in every language
//   node scripts/i18n/check.mjs --render --shots i18n/shots   and save screenshots for review
//   --strict fails when the current wave is not fully translated
import fs from 'node:fs';
import vm from 'node:vm';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { config, catalog, locale, targets, items, inScope, validate, rel, serve, browser } from './lib.mjs';

const args = process.argv.slice(2), has = f => args.includes(f);
const cfg = config(), cat = catalog(), all = items(cat), wave = cfg.currentWave || 'wave1';
const fail = [], warn = [];

// 1. The frozen canon is untouched.
for (const line of fs.readFileSync(rel('SOURCE_SHA256.txt'), 'utf8').trim().split('\n')) {
  const [sum, name] = line.split(/\s+/);
  const got = createHash('sha256').update(fs.readFileSync(rel('source', name))).digest('hex');
  if (got !== sum) fail.push(`frozen source changed: source/${name}`);
}
const PROTECTED = ['source', 'SOURCE_SHA256.txt', 'assets/content.js', 'assets/atlas.js', 'assets/app.js', 'assets/results',
  'e0a.html', 'Sidus_Dossier_Standalone.html', 'downloads', 'paper', 'scripts/rebuild.py', 'scripts/build_e0a.py', 'scripts/build_e0b.py'];
try {
  const base = ['github/main', 'origin/main', 'main'].map(b => { try { return execFileSync('git', ['merge-base', 'HEAD', b], { cwd: rel(), encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).trim(); } catch { return ''; } }).find(Boolean);
  if (!base) warn.push('no main branch found: skipped the protected-files comparison');
  else {
    const changed = execFileSync('git', ['diff', '--name-only', base, '--', ...PROTECTED], { cwd: rel(), encoding: 'utf8' }).trim();
    if (changed) fail.push('protected files differ from ' + base.slice(0, 7) + ': ' + changed.split('\n').join(', '));
  }
} catch { warn.push('git unavailable: skipped the protected-files comparison'); }

// 2. Translation memory is valid, and 3. the shipped dictionaries match it.
const coverage = {};
for (const l of targets(cfg).filter(l => l.enabled)) {
  const loc = locale(l.code), expect = { u: {}, p: {} };
  let scope = 0, done = 0, stale = 0;
  for (const it of all) {
    const e = loc.entries[it.id], inWave = inScope(it.routes, cfg.waves[wave]);
    if (inWave) scope++;
    if (!e) continue;
    if (e.s !== it.en) { stale++; continue; }
    const problems = validate(it.en, e.t, it.kind === 'p');
    if (problems.length) { fail.push(`${l.code} ${it.id}: ${problems.join('; ')}`); continue; }
    if (it.kind === 'p') expect.p[it.id.slice(2)] = e.t; else expect.u[it.id] = e.t;
    if (inWave) done++;
  }
  coverage[l.code] = { scope, done, stale };
  const file = rel('assets/i18n', l.code + '.js');
  if (!fs.existsSync(file)) { fail.push(`${l.code}: dictionary not built (run node scripts/i18n/build.mjs)`); continue; }
  const ctx = { window: {} }; vm.runInNewContext(fs.readFileSync(file, 'utf8'), ctx);
  const got = ctx.window.SIDUS_I18N_DICT || {};
  if (JSON.stringify(got.u) !== JSON.stringify(expect.u) || JSON.stringify(got.p) !== JSON.stringify(expect.p)) fail.push(`${l.code}: dictionary is out of date (run node scripts/i18n/build.mjs)`);
  if (done < scope) (has('--strict') ? fail : warn).push(`${l.code}: ${wave} has ${scope - done} of ${scope} items untranslated`);
  if (stale) warn.push(`${l.code}: ${stale} translations are stale (the English changed); they show in English until retranslated`);
}

// 4. Every page of the wave renders in every language with no errors and no stray English.
if (has('--render')) {
  const shots = args.includes('--shots') ? args[args.indexOf('--shots') + 1] : null;
  const routes = cat.routes.filter(r => inScope([r], cfg.waves[wave]));
  const srv = await serve(), b = await browser();
  for (const l of [cfg.source, ...targets(cfg).filter(l => l.enabled)]) {
    const ctx = await b.newContext({ serviceWorkers: 'block', viewport: { width: 1280, height: 900 } });
    const page = await ctx.newPage(), errs = [];
    page.on('pageerror', e => errs.push(String(e)));
    page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    const loc = locale(l.code);
    const same = new Set(Object.entries(loc.entries).filter(([, e]) => e.t === e.s).map(([id]) => id));
    for (const r of routes) {
      const url = srv.url + (r.startsWith('#') ? '/index.html' : r) + `?lang=${l.code}` + (r.startsWith('#') ? r : '');
      await page.goto(url);
      await page.waitForFunction(() => window.__SIDUS_I18N && !document.documentElement.classList.contains('i18n-pending'));
      await page.waitForTimeout(60);
      if (l.code !== cfg.source.code) {
        const left = (await page.evaluate(() => window.__SIDUS_I18N.units()))
          // Still English = the unit kept its English key and has no deliberately identical translation.
          .filter(u => u.kind !== 't' && (cat.units[u.key] ? !same.has(u.key) : !!cat.patterns[u.pk] && !same.has('p:' + u.pk)));
        const english = left.filter(u => inScope((cat.units[u.key] || cat.patterns[u.pk] || { r: [] }).r.map(i => cat.routes[i]), cfg.waves[wave]));
        if (english.length) (has('--strict') ? fail : warn).push(`${l.code} ${r}: ${english.length} units still in English, e.g. "${english[0].skel.slice(0, 70)}"`);
      }
      if (shots && ['#/home', '#/primer', '#/atlas', '/research/', '#/document/0/frontpiece'].includes(r)) {
        fs.mkdirSync(path.resolve(rel(), shots), { recursive: true });
        await page.screenshot({ path: path.resolve(rel(), shots, `${l.code}_${r.replace(/[#/]+/g, '_').replace(/^_|_$/g, '') || 'root'}.png`) });
      }
    }
    if (errs.length) fail.push(`${l.code}: page errors: ${[...new Set(errs)].slice(0, 3).join(' | ')}`);
    await ctx.close();
  }
  await b.close(); srv.close();
}

for (const [code, c] of Object.entries(coverage)) console.log(`${code.padEnd(8)} ${wave}: ${c.done}/${c.scope}${c.stale ? `, ${c.stale} stale` : ''}`);
warn.forEach(w => console.log('warn  ' + w));
fail.forEach(f => console.log('FAIL  ' + f));
console.log(fail.length ? `\n${fail.length} problem(s).` : '\nAll translation checks passed.');
process.exitCode = fail.length ? 1 : 0;
