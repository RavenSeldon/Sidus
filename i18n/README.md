# Sīdus in other languages

English is the source. Visitors choose another language with the 文A switcher, and the choice is remembered. Any page can also be linked in a language with `?lang=`, e.g. `https://sidus.quest/?lang=fr#/home` or `/research/?lang=ja`. Anything not translated yet stays in English, and the page says so.

Languages: Français, Español, Português (Brasil), Nederlands, 简体中文, 日本語, العربية (right to left). Yoruba (Ogun State) is reserved; see *Adding a language*.

## How it works

- **Runtime.** `assets/i18n/i18n.js` runs on every page.
  - It splits what the page renders into text units and hashes each unit's English text.
  - It swaps in the translation from `assets/i18n/<code>.js` when one exists.
  - Inline formatting, links, math and form controls are kept as they are. Translators see them as tokens: `⟦1⟧…⟦/1⟧` around words, `⟦2⟧` for an element that stays put.
- **Translation memory.** `i18n/locales/<code>.json` is where every translation lives.
  - Each entry records the English it was made from (`s`), the translation (`t`), its status (`st`: `draft` or `reviewed`), who made it (`by`) and when (`at`).
  - When the English changes, the old translation becomes *stale* and the page shows English until the unit is translated again.
- **Generated files** (never edit by hand):
  - `i18n/source.json`: the English catalog.
  - `assets/i18n/<code>.js`: the bundles the site loads.
  - `i18n/coverage.json`.
- **Settings.**
  - `i18n/config.json` holds the languages, the crawl entry points, the waves and the translator settings.
  - `i18n/glossary.json` holds the style note per language and the shared terms. The translator is given both.

## After changing the English, or adding an experiment or section

```sh
cd ~/Root/Sidus
npm run i18n            # extract → translate what is missing or stale → build → check
node scripts/build_companion.mjs   # existing rule on every deploy: bumps the service-worker cache
```

The extractor runs the real site in a headless browser and follows links, so new routes are found without configuration. Only pages in the current wave are translated (`currentWave` in `i18n/config.json`). Each wave is a list of route patterns, so a new route outside them stays English until a wave includes it. `wave2` matches everything.

First time on a machine: `npm install && npx playwright install chromium`.

## Translators

`npm run i18n` picks the first one available:

1. **The `claude` CLI**, using your Claude login. On Hel, run `claude /login` once; it currently answers "Invalid API key".
2. **The Anthropic API**, if `ANTHROPIC_API_KEY` is set.
3. **Work packets**, if neither is available:
   - `node scripts/i18n/translate.mjs --backend packets` writes `i18n/work/<code>.todo.tsv` (and `.json`) for a person or any agent to fill.
   - Import the filled file with `node scripts/i18n/translate.mjs --import i18n/work/<code>.<name>.tsv --by "Name"`.

Every import is validated: each token and `{n}` placeholder must appear exactly once, and pairs must nest. Rejected rows are listed and stay in English. Progress is saved after every batch, so an interrupted run resumes where it stopped.

## Reviewing a language (Wave 1 now)

All seven languages are machine drafts made with the glossary. Each page shows a draft notice linking to the English.

1. **Read the pages.**
   - Wave 1 routes: `#/home`, `#/primer` and its sub-pages (begin-here, doc-i … doc-iv, equations), `#/atlas`, `#/document/0…3/frontpiece`, `/research/`, `/research/e0-b/`, `/research/archive/`.
   - Locally: `python3 -m http.server 8000`, then open `http://localhost:8000/?lang=fr#/home`.
   - Screenshots of five key pages per language are in `~/Root/Hel-Setup/i18n-shots/`. Look at Arabic first, since it runs right to left.
2. **Correct in a spreadsheet.**
   - `node scripts/i18n/translate.mjs --export --lang fr` writes `i18n/work/fr.review.tsv`, with columns row, id, kind, English, translation. These sheets have already been exported for all seven languages.
   - Fix the last column. Keep the tokens. Delete any rows you did not review.
3. **Bring it back.**
   - `node scripts/i18n/translate.mjs --import i18n/work/fr.review.tsv --reviewed --by "Your name"`, then `npm run i18n:build`.
   - Without `--reviewed`, only changed rows are imported, and they stay drafts.
4. **Second opinion without a speaker.** `node scripts/i18n/translate.mjs --qa --lang fr` (needs the CLI or the API) writes a cold back-translation report to `i18n/qa/`. The reviewing model never sees the English.
5. **When a language has been reviewed by a native speaker,** set its `"status": "reviewed"` in `i18n/config.json` and run `npm run i18n:build`. The draft notice disappears for that language.

Worth checking first:

- **Glossary choices** (the "Decisions of record" in `PROJECT-LOG.md`):
  - "gate" → filtre / filtro / toets / 关卡 / ゲート / بوابة
  - "For Dummies" → Pour les Nuls, para Dummies, Para Leigos, voor Dummies, 通俗版, やさしい解説, للمبتدئين
  - "research programme" → 研究纲领 in Chinese
- **Register:** vous, usted, você, je; desu/masu in Japanese; Modern Standard Arabic.
- **Arabic arrows** are mirrored, so "forward" points left.
- **Hero title:** each language breaks it over three lines.

To start Wave 2 once you are happy with Wave 1: set `"currentWave": "wave2"` in `i18n/config.json` and run `npm run i18n`.

## Adding a language (Yoruba, Ogun State)

The `yo` entry already exists in `i18n/config.json`, with `"enabled": false`. While a language is disabled, visitors don't see it, but you can still translate into it by naming it with `--lang yo`.

1. In `i18n/glossary.json`:
   - Add a `"yo"` style note, e.g. which orthography and tone marking to use and the Ogun State usage you want.
   - Add a `"yo"` value to the terms you want fixed.
2. Translate:
   - Have a draft made with `node scripts/i18n/translate.mjs --lang yo`.
   - Or translate it yourself: run `node scripts/i18n/translate.mjs --backend packets --lang yo`, fill `i18n/work/yo.todo.tsv`, and import it with `--import … --by "Ben Amuwo"`.
3. When you are ready for visitors to see it, set `"enabled": true` and run `npm run i18n:build`.
   - The switcher lists every enabled language after a build.
   - Untranslated passages show in English, with a notice.
   - Keep `"status": "draft"` until the language has been reviewed.

## Checks

`npm run i18n:check` verifies four things:

- The frozen canon is byte-identical (`SOURCE_SHA256.txt`, plus a `git diff` of protected paths).
- The translation memory is valid.
- The bundles match the memory.
- Wave coverage.

Add `--render` to load every page of the wave in every language. That fails on page errors and warns about any English left over. Add `--shots <dir>` to save screenshots, and `--strict` to turn gaps into failures. The site's own checks still apply: `node scripts/check_companion.mjs`, `node scripts/check_e0b.mjs`, `python3 scripts/check_e0a.py`.

## What stays English

PDFs, Markdown sources, Zenodo records and citations, evidence logs and hashes, `e0a.html` (the script-free edition), `Sidus_Dossier_Standalone.html`, and site search (indexed in English).

## Files to commit

`assets/i18n/`, `i18n/` (except `i18n/work/`, which is ignored), `scripts/i18n/`, `package.json`, `package-lock.json`, the four edited HTML pages, and `sw.js`. Never commit `node_modules/`.
