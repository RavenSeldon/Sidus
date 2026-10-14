// Shared helpers for the Sīdus translation layer (scripts/i18n/*).
import fs from 'node:fs';
import path from 'node:path';
import http from 'node:http';
import { fileURLToPath } from 'node:url';

export const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
export const rel = (...p) => path.join(ROOT, ...p);
export const readJSON = (p, fallback) => (fs.existsSync(rel(p)) ? JSON.parse(fs.readFileSync(rel(p), 'utf8')) : fallback);

// One entry per line keeps diffs readable for reviewers.
export function writeJSON(p, obj) {
  const file = rel(p);
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, stringify(obj) + '\n');
}
function stringify(v, depth = 0) {
  if (v === null || typeof v !== 'object') return JSON.stringify(v);
  const pad = '  '.repeat(depth + 1), end = '  '.repeat(depth);
  if (Array.isArray(v)) {
    if (v.every(x => x === null || typeof x !== 'object')) return JSON.stringify(v);
    return '[\n' + v.map(x => pad + stringify(x, depth + 1)).join(',\n') + '\n' + end + ']';
  }
  const keys = Object.keys(v);
  if (!keys.length) return '{}';
  if (depth >= 2) return JSON.stringify(v);
  return '{\n' + keys.map(k => pad + JSON.stringify(k) + ': ' + stringify(v[k], depth + 1)).join(',\n') + '\n' + end + '}';
}

export const config = () => readJSON('i18n/config.json');
export const catalog = () => readJSON('i18n/source.json', { units: {}, patterns: {}, routes: [], order: [] });
export const locale = code => readJSON(`i18n/locales/${code}.json`, { lang: code, entries: {} });
export const saveLocale = (code, data) => writeJSON(`i18n/locales/${code}.json`, data);
export const targets = (cfg = config()) => cfg.languages.filter(l => l.code !== cfg.source.code);

export function inScope(routes, patterns) {
  const res = patterns.map(p => new RegExp(p));
  return routes.some(r => res.some(re => re.test(r)));
}
// Every catalog item (unit or pattern) with its id, English skeleton and routes.
export function items(cat = catalog()) {
  const out = [], R = i => cat.routes[i];
  for (const [key, u] of Object.entries(cat.units)) out.push({ id: key, en: u.t, routes: u.r.map(R), kind: u.k, tag: u.g });
  for (const [pk, p] of Object.entries(cat.patterns)) out.push({ id: 'p:' + pk, en: p.t, routes: p.r.map(R), kind: 'p', tag: p.g });
  return out;
}

// ---- token validation: a translation must carry exactly the source's tokens ----
const TOKEN = /⟦(\/?)(\d+)⟧/g;
function tokenShape(s) {
  const paired = new Set(), all = new Set();
  for (const m of s.matchAll(TOKEN)) { all.add(+m[2]); if (m[1]) paired.add(+m[2]); }
  return { paired, all };
}
export function validate(en, tr, isPattern = false) {
  const problems = [];
  if (typeof tr !== 'string' || !tr.trim()) return ['empty translation'];
  const src = tokenShape(en);
  const seen = new Map(), stack = [];
  for (const m of tr.matchAll(TOKEN)) {
    const idx = +m[2], close = !!m[1];
    if (!src.all.has(idx)) { problems.push(`unknown token ⟦${idx}⟧`); continue; }
    if (close) {
      if (!src.paired.has(idx)) problems.push(`⟦${idx}⟧ is not a pair`);
      else if (stack.pop() !== idx) problems.push(`⟦/${idx}⟧ closes out of order`);
      continue;
    }
    seen.set(idx, (seen.get(idx) || 0) + 1);
    if (src.paired.has(idx)) stack.push(idx);
  }
  if (stack.length) problems.push(`unclosed ${stack.map(i => '⟦' + i + '⟧').join(' ')}`);
  for (const idx of src.all) {
    const n = seen.get(idx) || 0;
    if (n !== 1) problems.push(`⟦${idx}⟧ appears ${n} times`);
  }
  if (isPattern) {
    const want = [...en.matchAll(/\{(\d+)\}/g)].map(m => m[1]).sort().join();
    const got = [...tr.matchAll(/\{(\d+)\}/g)].map(m => m[1]).sort().join();
    if (want !== got) problems.push(`placeholders ${got || 'none'} ≠ ${want}`);
  }
  if (/⟪|⟫/.test(tr)) problems.push('stray ⟪⟫ marker');
  return problems;
}

// ---- a tiny static server for the extractor and the render check ----
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.webmanifest': 'application/manifest+json',
  '.md': 'text/markdown; charset=utf-8', '.pdf': 'application/pdf', '.txt': 'text/plain; charset=utf-8' };
export function serve(root = ROOT) {
  const server = http.createServer((req, res) => {
    let p = decodeURIComponent(new URL(req.url, 'http://x').pathname);
    let file = path.join(root, p);
    if (!file.startsWith(root)) { res.writeHead(403); return res.end(); }
    if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
    if (!fs.existsSync(file)) { res.writeHead(404); return res.end('not found'); }
    res.writeHead(200, { 'content-type': TYPES[path.extname(file)] || 'application/octet-stream', 'cache-control': 'no-store' });
    fs.createReadStream(file).pipe(res);
  });
  return new Promise(resolve => server.listen(0, '127.0.0.1', () => resolve({ url: `http://127.0.0.1:${server.address().port}`, close: () => server.close() })));
}

export async function browser() {
  let pw;
  try { pw = await import('playwright'); }
  catch { throw new Error('Playwright is needed for extraction and render checks. Run: npm install && npx playwright install chromium'); }
  return pw.chromium.launch();
}

export const words = s => (s.replace(/⟦\/?\d+⟧|\{\d+\}/g, ' ').match(/\p{L}+/gu) || []).length;
