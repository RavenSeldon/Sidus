# Project Log — Sīdus Translation Layer (i18n)

Branch `i18n-wave2` in `~/Root/Sidus` on Hel. Ben commits and pushes, to the `github` remote (`origin` is the read-only recovery mirror). Railway deploys only `main`.

**Source of truth:** `~/Root/Sidus` on Hel, from CP2 on. Claude's cloud working copy is scratch and may be stale or gone.

**Resume point:** Wave 2 is complete and verified in all seven required languages: 2,416/2,416 each, 0 stale and 0 invalid. The strict rendered translation check and all site checks pass; the frozen canon and both standalone HTML files are unchanged. Arabic and the final service-worker cache bump await Ben’s commit. Every translation remains labelled as a draft until native-speaker review (see `i18n/README.md` → Reviewing).

## How a CP3 language is done (resumable)
1. `node scripts/i18n/translate.mjs --backend packets` writes `i18n/work/<code>.todo.tsv` (row, id, kind, English). Wave 1 has 551 rows in reading order. The id order hash is `e0e959de…`, identical to the cloud copy's.
2. The translator writes `i18n/work/<code>.done.<part>.tsv`, one line per item: `row<TAB>translation`.
3. `node scripts/i18n/translate.mjs --import i18n/work/<code>.done.<part>.tsv --by "claude-opus-5.5 (draft)"` validates the tokens and placeholders and stores the item in `i18n/locales/<code>.json`. Rejected rows are listed; fix them and re-import. Imports are idempotent.
4. A language is checkpointed when `build.mjs` shows 100% of wave1 for it.

With the `claude` CLI logged in on Hel, steps 1–3 are replaced by `node scripts/i18n/translate.mjs --lang <code>` (automatic, saved after every batch).

## Checkpoints
- [x] CP0: branch created, this log written (2026-10-14 10:05)
- [x] CP1: runtime `assets/i18n/i18n.js` + `i18n.css`; extractor; translation memory format; translate/build/check/sync scripts; English catalog extracted (2026-10-14 10:35). Verified on Hel: `npm install`, Playwright Chromium installed, `extract.mjs` gives 2,405 units / 11 patterns, the same as the cloud copy.
- [x] CP2: `i18n/glossary.json` holds style notes for 7 languages and 68 terms. `translate.mjs` now also imports spreadsheet-style TSV (2026-10-14 10:45).
- [x] CP3: Wave 1 translations all 7 done: fr, es, pt, nl, zh-hans, ja, ar; 551/551 each, 0 rejected on import
- [x] CP4: bundles built. `check.mjs --render` covers 8 languages × 16 Wave 1 pages and passes: no page errors, no English left, frozen canon unchanged. `build_companion.mjs` bumped the sw CACHE to `sidus-dossier-v7-e0b-e7423b1ebb26`. check_companion, check_e0b and check_e0a all PASS, and `e0a.html` and the Standalone are byte-unchanged. The `check.mjs` false positive for translations identical to English is fixed (2026-10-14 13:40).
- [x] CP5: `i18n/README.md` (runbook and review guide). Review sheets are exported to `i18n/work/<code>.review.tsv` (`--export`, then `--import --reviewed`). `.gitignore` ignores `i18n/work/`. Screenshots are in `~/Root/Hel-Setup/i18n-shots/`. HEL-SETUP has a pointer. The transfer inbox is removed (2026-10-14 13:40).

## Wave 2 checkpoints
- [x] Français (`fr`): 2,416/2,416, 0 stale, 0 invalid (2026-10-14 15:09)
- [x] Español (`es`): 2,416/2,416, 0 stale, 0 invalid (2026-10-14 19:44)
- [x] Português (`pt`): 2,416/2,416, 0 stale, 0 invalid (2026-10-14 20:02)
- [x] Nederlands (`nl`): 2,416/2,416, 0 stale, 0 invalid (2026-10-14 20:28)
- [x] 中文（简体）(`zh-hans`): 2,416/2,416, 0 stale, 0 invalid (2026-10-15 00:59)
- [x] 日本語 (`ja`): 2,416/2,416, 0 stale, 0 invalid (2026-10-15 01:25)
- [x] العربية (`ar`): 2,416/2,416, 0 stale, 0 invalid (2026-10-15 06:04)

## Done (verified by)
- Runtime and pipeline. Marker test, 2026-10-14:
  - Every Wave 1 unit was replaced in French, with zero English left and no page errors across all 15 Wave 1 routes.
  - The Arabic layout test renders right to left.
  - Screenshots reviewed.
- Catalog: 2,405 units and 11 number patterns, 28,497 English words over 111 routes. Wave 1 is 551 items, 4,797 words (`node scripts/i18n/extract.mjs`).
- Wave 1 translations: 7 languages × 551 items, drafted by Claude (Opus 5.5) with the glossary and imported with 0 rejections. `check.mjs --render` passes in every language (2026-10-14 13:40).
- Wave 2 translations: 7 languages × 2,416 items, with all 1,865 new items per language imported with 0 rejections. Each language reports 0 stale and 0 invalid (2026-10-15 06:04).
- Wave 2 final validation: `check.mjs --render --strict --shots ~/Root/Hel-Setup/i18n-shots-w2` passes with no page errors or English fallbacks. `check_companion.mjs`, `check_e0b.mjs` and `check_e0a.py` all pass; `e0a.html` and `Sidus_Dossier_Standalone.html` are byte-unchanged. `build_companion.mjs` bumped the service-worker cache to `sidus-dossier-v7-e0b-77f3722a5e60` (2026-10-15 06:05).
- Push from `~/Root/Sidus` goes to GitHub (authenticated dry run, 2026-10-14 05:50; see Hel-Setup/HEL-SETUP.md).

## Remaining
**Code to write:** None for required Wave 2.
**Human actions:**
1. Review the Wave 1 and Wave 2 drafts with native speakers. Start with Arabic and the glossary choices; the steps are in `i18n/README.md` → Reviewing.
2. Commit and push the completed Arabic checkpoint. A push to the branch deploys nothing, because Railway deploys `main` only:
   ```sh
   cd ~/Root/Sidus
   git add assets/i18n/ar.js assets/i18n/i18n.js i18n/coverage.json i18n/locales/ar.json i18n/PROJECT-LOG.md sw.js
   git commit -m "i18n: complete Arabic Wave 2 draft"
   git push -u github i18n-wave2
   ```
3. Publish that checkpoint to `main` when ready; the other six Wave 2 languages are already live and every language is clearly labelled a draft.
4. Yoruba (Ogun State), whenever you are ready; see `i18n/README.md` → Adding a language.

## Decisions of record
- **Languages:** English (source) plus Français, Español, Português (Brasil), Nederlands, 中文 (简体), 日本語 and العربية (RTL). The Yoruba (Ogun State) slot is reserved for Ben. (Ben, 2026-10-14)
- **Build it once.** A runtime layer translates whatever the site renders, keyed by a hash of each text unit's English text. English edits and new sections propagate with no per-page code, and app.js, e0a.js, e0b.js and the frozen canon stay untouched.
- **Extraction** runs the real site in headless Chromium and collects units with the same code the runtime uses, so keys match by construction. New routes are found by following links.
- **Inline markup becomes tokens** (⟦1⟧…⟦/1⟧; atomic ⟦2⟧). Translators never see HTML. Math, code and form controls are moved live, never retyped, and the runtime never parses translated HTML.
- **Translation memory** lives in `i18n/locales/<lang>.json`, each entry marked draft or reviewed. The runtime bundles `assets/i18n/<lang>.js` are generated from it.
- **Translators are pluggable:** work packets (JSON or TSV, for any agent or person), the `claude` CLI on Hel, or the Anthropic API. One sync command runs extract → translate what is missing → build → check.
- **Glossary** in `i18n/glossary.json`; the translator receives the terms that occur in each batch. Notable choices:
  - "gate" → filtre / filtro / filtro / toets / 关卡 / ゲート / بوابة
  - "For Dummies" → each market's edition name (Pour les Nuls, para Dummies, Para Leigos, voor Dummies) and plain equivalents in zh / ja / ar
  - "research programme" → 研究纲领 in Chinese (Lakatos)
  - "Astrocyte" is a module name and is kept as is
- **Register:** fr vous; es usted (neutral Latin American); pt você (Brazil); nl je; ja desu/masu prose with plain headings; ar Modern Standard Arabic.
- **Wave 1:** chrome, home (including results panels), atlas, Sīdus for Dummies, research pages, and the opening section of each document. **Wave 2** (after Ben's review): full Documents I–IV and the E0-A and E0-B reports.
- **Stays English:** PDFs, Markdown sources, Zenodo records, evidence logs, `e0a.html` (script-free edition) and `Sidus_Dossier_Standalone.html`. Site search stays English-indexed in Wave 1.
- **Frozen canon** is never edited; a check proves it byte-identical.
- **Numbers and decimal marks** are kept exactly as in English (they are data).
- **Draft label:** every language is labelled a draft until a native speaker reviews it; English is authoritative.
- **Arabic mirrors arrows** (→ becomes ←, “back” ← becomes →) so “forward” points the reading direction; arrows between Latin codes such as E0 → E6 stay. Added to the Arabic style note in the glossary.
- **Typography:** French uses non-breaking spaces before : ; ? ! and inside « » (applied mechanically at import); citations, DOIs, hashes and file names stay as in English in every language.
- **Transfer to Hel:** Claude writes files to `~/PycharmProjects/.sidus-inbox/` and moves them into place, because `~/Root` isn't a folder this session can write to directly. The inbox is removed at CP5.
- **Screenshots are reviewed by Ben, not by Claude.** Reading an image back through the bridge costs tens of thousands of tokens. Claude relies on `check.mjs --render` (no page errors, no stray English) and looks at one screenshot only when a check points to a problem.
