// Translate whatever is missing or stale, for each language, within a wave.
//
//   node scripts/i18n/translate.mjs                       translate the current wave with the best available translator
//   node scripts/i18n/translate.mjs --lang fr,ja --wave wave2
//   node scripts/i18n/translate.mjs --backend packets     write i18n/work/<code>.todo.json for any agent or person to fill
//   node scripts/i18n/translate.mjs --import i18n/work/fr.done.json [--by "name"]   (JSON, or a filled .tsv)
//   node scripts/i18n/translate.mjs --qa --lang fr        cold back-translation report in i18n/qa/
//   node scripts/i18n/translate.mjs --export --lang fr    review sheet i18n/work/fr.review.tsv (English + current translation)
//   node scripts/i18n/translate.mjs --import i18n/work/fr.review.tsv --reviewed --by "Name"   corrections back, marked reviewed
//
// Backends: "claude" (the Claude Code CLI, uses your Claude login), "api" (ANTHROPIC_API_KEY),
// "packets" (no model: export work for later import). "auto" picks the first that is available.
// Progress is saved after every batch, so an interrupted run resumes where it stopped.
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { config, catalog, locale, saveLocale, targets, items, inScope, validate, readJSON, writeJSON, rel, words } from './lib.mjs';

const args = process.argv.slice(2);
const opt = (name, def) => { const i = args.indexOf('--' + name); return i < 0 ? def : (args[i + 1] && !args[i + 1].startsWith('--') ? args[i + 1] : true); };
const cfg = config(), cat = catalog();
const today = new Date().toISOString().slice(0, 10);
const wave = opt('wave', cfg.currentWave || 'wave1');
const langList = (opt('lang', 'all') === 'all' ? targets(cfg).filter(l => l.enabled) : opt('lang').split(',').map(c => cfg.languages.find(l => l.code === c)))
  .filter(Boolean);
const glossary = readJSON('i18n/glossary.json', { terms: [] });

// ---- what needs doing --------------------------------------------------------------
const byId = new Map(items(cat).map(it => [it.id, it]));
const scope = cat.order.map(id => byId.get(id)).filter(it => it && inScope(it.routes, cfg.waves[wave]));
const pos = new Map(cat.order.map((id, i) => [id, i]));
function context(id) {
  const i = pos.get(id), near = j => (byId.get(cat.order[j]) || {}).en || '';
  return { route: (byId.get(id) || { routes: [] }).routes[0], before: near(i - 1).slice(0, 160), after: near(i + 1).slice(0, 160) };
}
const todo = l => { const loc = locale(l.code); return scope.filter(it => !loc.entries[it.id] || loc.entries[it.id].s !== it.en); };

// ---- import a filled packet -----------------------------------------------------------
// JSON: {"lang":"fr","by":"…","translations":{id: text}}.
// TSV (spreadsheet-friendly): one item per line, last column the translation. Rows exported by this script
// (row, id, kind, english, translation) are matched by their id; two-column rows "row<TAB>text" refer to
// i18n/work/<code>.todo.json. The language comes from --lang or the file name (fr.anything.tsv).
// --reviewed stores the imported items as reviewed instead of draft.
if (opt('import')) {
  const file = opt('import'), bad = [];
  let code, by, tr;
  if (file.endsWith('.tsv')) {
    code = typeof opt('lang') === 'string' ? opt('lang') : path.basename(file).split('.')[0];
    by = opt('by', 'unknown');
    const rows = readJSON(`i18n/work/${code}.todo.json`, { items: [] }).items;
    tr = {};
    for (const line of fs.readFileSync(file, 'utf8').split(/\r?\n/)) {
      const f = line.split('\t'), key = f[0].trim();
      if (f.length < 2 || !key || key === 'row') continue;
      let text = f[f.length - 1].trim();
      if (/^".*"$/s.test(text)) text = text.slice(1, -1).replace(/""/g, '"');
      if (!text) continue;
      const id = f.length >= 3 ? f[1].trim() : /^\d+$/.test(key) ? (rows[+key - 1] || {}).id : key;
      if (id) tr[id] = text; else bad.push(`row ${key}: not in i18n/work/${code}.todo.json`);
    }
  } else {
    const data = JSON.parse(fs.readFileSync(file, 'utf8'));
    code = data.lang; by = opt('by', data.by || 'unknown');
    tr = Array.isArray(data.translations) ? Object.fromEntries(data.translations.map(x => [x.id, x.tr])) : data.translations;
  }
  const loc = locale(code);
  let ok = 0;
  for (const [id, t] of Object.entries(tr)) {
    const it = byId.get(id);
    if (!it) { bad.push(`${id}: not in the current English catalog`); continue; }
    const problems = validate(it.en, t, it.kind === 'p');
    if (problems.length) { bad.push(`${id}: ${problems.join('; ')}`); continue; }
    const prev = loc.entries[id];
    if (!opt('reviewed') && prev && prev.s === it.en && prev.t === t) continue;   // unchanged row of a review sheet
    loc.entries[id] = { s: it.en, t, st: opt('reviewed') ? 'reviewed' : 'draft', by, at: today };
    ok++;
  }
  saveLocale(code, loc);
  console.log(`${code}: imported ${ok}, rejected ${bad.length}`);
  if (bad.length) { console.log(bad.join('\n')); process.exitCode = 1; }
  process.exit();
}

// ---- review sheet ------------------------------------------------------------------------
if (opt('export')) {
  for (const l of langList) {
    const loc = locale(l.code);
    fs.writeFileSync(rel(`i18n/work/${l.code}.review.tsv`), 'row\tid\tkind\tenglish\ttranslation\n' +
      scope.map((it, i) => [i + 1, it.id, it.kind || '', it.en, (loc.entries[it.id] || {}).t || ''].join('\t')).join('\n') + '\n');
    console.log(`${l.code}: ${scope.length} rows → i18n/work/${l.code}.review.tsv. Correct the last column, then --import it with --reviewed --by "Name".`);
  }
  process.exit();
}

// ---- prompts ---------------------------------------------------------------------------
function glossaryFor(l, batch) {
  const text = batch.map(it => it.en.toLowerCase()).join(' ');
  return glossary.terms.filter(g => text.includes(g.en.toLowerCase()) && g[l.code])
    .map(g => `- ${g.en} → ${g[l.code]}${g.note ? ' (' + g.note + ')' : ''}`).join('\n') || '(none in this batch)';
}
function prompt(l, batch) {
  const style = (glossary.style && (glossary.style[l.code] || '')) || '';
  return `You are translating the website of Sīdus, an independent research programme on bounded self-monitoring (cognitive science and machine learning), from English into ${l.name} (${l.lang}${l.note ? ', ' + l.note : ''}).

Rules:
1. Translate faithfully for an educated reader who is not a specialist. Keep the register precise and formal but readable. Never add, drop or soften a claim, hedge, number or qualifier.
2. Tokens such as ⟦3⟧ stand for math, a line break or a control; pairs such as ⟦1⟧…⟦/1⟧ wrap formatted or linked words. Keep every token exactly once, wrapping the matching words; move tokens to fit natural word order. Never change a token.
3. {0}, {1}… stand for numbers. Keep each exactly once.
4. Keep exactly as written: Sīdus and SĪDUS, experiment and gate names (E0, E0-A, E0-B, E1–E6, A1–A4, B2, H1–H4), DOI and Zenodo, symbols and variable names (such as rᵥ, mᵥ, Δ, ℐ, Cᵥ, Sᵥ), the glyphs 司 量 道, the Latin motto PER ASPERA / AD ASTRA, people's names, numbers and decimal points.
5. Use the glossary consistently. Items of kind "a" are accessibility labels and "t" are page titles; keep interface labels short.
${style ? '6. ' + style + '\n' : ''}
Glossary:
${glossaryFor(l, batch)}

Return only a JSON object that maps each id to its translation, with no commentary.

Items:
${JSON.stringify(batch.map(it => ({ id: it.id, en: it.en, kind: it.kind, tag: it.tag, context: context(it.id) })), null, 1)}`;
}
function qaPrompt(l, batch, loc) {
  return `Below are passages in ${l.name}. You have not seen any source text. For each, give a literal English back-translation and flag anything a native reader would mark: grammar, unnatural phrasing, wrong register, ambiguity, or a term used inconsistently. Ignore tokens like ⟦1⟧ and {0}.
Return only a JSON object mapping each id to {"back": "...", "flags": "..."} (flags empty if none).

${JSON.stringify(batch.map(it => ({ id: it.id, text: loc.entries[it.id].t })), null, 1)}`;
}

// ---- backends ------------------------------------------------------------------------------
const have = cmd => spawnSync(process.platform === 'win32' ? 'where' : 'which', [cmd]).status === 0;
function pickBackend() {
  const b = opt('backend', 'auto');
  if (b !== 'auto') return b;
  if (have(cfg.translator.cli[0])) return 'claude';
  if (process.env.ANTHROPIC_API_KEY) return 'api';
  return 'packets';
}
async function ask(backend, text) {
  if (backend === 'claude') {
    const [cmd, ...rest] = cfg.translator.cli;
    const r = spawnSync(cmd, rest, { input: text, encoding: 'utf8', maxBuffer: 64 << 20, timeout: 15 * 60 * 1000 });
    if (r.status !== 0) throw new Error(`${cmd} exited ${r.status}: ${(r.stderr || '').slice(0, 400)}`);
    return r.stdout;
  }
  const res = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: { 'x-api-key': process.env.ANTHROPIC_API_KEY, 'anthropic-version': '2023-06-01', 'content-type': 'application/json' },
    body: JSON.stringify({ model: cfg.translator.apiModel, max_tokens: 32000, messages: [{ role: 'user', content: text }] })
  });
  if (!res.ok) throw new Error(`API ${res.status}: ${(await res.text()).slice(0, 400)}`);
  return (await res.json()).content.map(c => c.text || '').join('');
}
function parseJSON(out) {
  const a = out.indexOf('{'), b = out.lastIndexOf('}');
  if (a < 0 || b < a) throw new Error('no JSON object in the reply');
  return JSON.parse(out.slice(a, b + 1));
}
function batches(list) {
  const out = []; let cur = [], n = 0;
  for (const it of list) {
    const w = words(it.en) + 1;
    if (cur.length && n + w > cfg.translator.batchWords) { out.push(cur); cur = []; n = 0; }
    cur.push(it); n += w;
  }
  if (cur.length) out.push(cur);
  return out;
}

// ---- back-translation QA ----------------------------------------------------------------------
if (opt('qa')) {
  const backend = pickBackend();
  if (backend === 'packets') { console.error('QA needs a model: install the claude CLI or set ANTHROPIC_API_KEY.'); process.exit(1); }
  for (const l of langList) {
    const loc = locale(l.code), list = scope.filter(it => loc.entries[it.id]);
    let md = `# Cold back-translation: ${l.name} (${wave}, ${today})\n\nThe reviewing model saw only the ${l.name} text, never the English.\n\n`;
    for (const batch of batches(list)) {
      const res = parseJSON(await ask(backend, qaPrompt(l, batch, loc)));
      for (const it of batch) {
        const r = res[it.id] || {};
        md += `## ${it.id}\n\n- **English source:** ${it.en}\n- **${l.name}:** ${loc.entries[it.id].t}\n- **Back-translation:** ${r.back || '(missing)'}\n` + (r.flags ? `- **Flags:** ${r.flags}\n` : '') + '\n';
      }
    }
    fs.mkdirSync(rel('i18n/qa'), { recursive: true });
    fs.writeFileSync(rel(`i18n/qa/${l.code}-${today}.md`), md);
    console.log(`${l.code}: wrote i18n/qa/${l.code}-${today}.md`);
  }
  process.exit();
}

// ---- translate -------------------------------------------------------------------------------
const backend = pickBackend();
for (const l of langList) {
  const list = todo(l);
  if (!list.length) { console.log(`${l.code}: ${wave} is complete`); continue; }
  if (backend === 'packets') {
    writeJSON(`i18n/work/${l.code}.todo.json`, { lang: l.code, name: l.name, wave, instructions: prompt(l, []).split('\nItems:')[0],
      items: list.map(it => ({ id: it.id, en: it.en, kind: it.kind, context: context(it.id) })) });
    fs.writeFileSync(rel(`i18n/work/${l.code}.todo.tsv`), 'row\tid\tkind\tenglish\ttranslation\n' +
      list.map((it, i) => [i + 1, it.id, it.kind || '', it.en, ''].join('\t')).join('\n') + '\n');
    console.log(`${l.code}: ${list.length} items (${list.reduce((a, it) => a + words(it.en), 0)} words) → i18n/work/${l.code}.todo.json and .todo.tsv. Fill either and import with --import.`);
    continue;
  }
  let done = 0, failed = [];
  for (const batch of batches(list)) {
    let pending = batch;
    for (let attempt = 0; attempt < 2 && pending.length; attempt++) {
      let res;
      try { res = parseJSON(await ask(backend, prompt(l, pending))); }
      catch (e) { console.error(`${l.code}: batch failed (${e.message}); will retry`); continue; }
      const loc = locale(l.code), retry = [];
      for (const it of pending) {
        const t = res[it.id], problems = validate(it.en, t, it.kind === 'p');
        if (problems.length) { retry.push(it); continue; }
        loc.entries[it.id] = { s: it.en, t, st: 'draft', by: backend === 'claude' ? 'claude-cli' : cfg.translator.apiModel, at: today };
        done++;
      }
      saveLocale(l.code, loc);
      pending = retry;
    }
    failed.push(...pending.map(it => it.id));
    console.log(`${l.code}: ${done}/${list.length}`);
  }
  if (failed.length) console.log(`${l.code}: ${failed.length} items still need a translation (they stay in English): ${failed.slice(0, 8).join(', ')}${failed.length > 8 ? '…' : ''}`);
}
