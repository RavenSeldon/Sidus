# Sīdus E0-A expansion · 7 September 2026

Built as dated companion material. No commit, push or deployment was performed.

## Reader experience

- Results index: `#/results`; full six-scene field report: `#/results/e0-a`.
- Scene deep links use `#/results/e0-a/scene-1` through `scene-6`.
- Gate highlighting, five discrete public-reveal stops, eight-family control cabinet, development comparisons, seed matrix with keyboard navigation, exact interval table/plot, commitment records, and sample-size explanation.
- `e0a.html` is a genuinely script-free reading edition with the same narrative, tables and source links. The existing standalone reader also includes the expansion.
- Dossier panel, For Dummies entry, separate Atlas evidence group, and related-result link outside Document IV's article.
- Desktop Results navigation, Results in the mobile contextual menu, and report search entries.
- Supplied results and freeze ZIPs are explicit downloads; neither is precached.

## Evidence and scope

The builder reads the supplied ZIPs and the experiment ZIP nested inside the freeze. It never loads ATTEMPTS.jsonl, EVIDENCE.json or checkpoints into the browser or the agent context. No experiment was rerun and no new observations were created.

The disputed grid denominator is resolved by `history/stress_examples/SUMMARY.json → summary.arms.<arm>.panels.grid.runs`: 1,458 configurations per arm. It remains a controlled slice, not a population failure rate.

Provenance uses 190 executable, field/subtree recipes. Every one of the 4,918 emitted leaf values is covered by a source selector and checked against its source; subtree recipes append the displayed row/field. Records are lazy-loaded and individually linked from every table. Four compact data files plus the provenance index make up the browser data bundle (about 105 KB uncompressed). Raw source excerpts remain separately downloadable.

Controls expose the actual archived metric profiles, collapse counts and expected-diagnostic counts. The compact final CSV does not contain per-control A1–A4 verdicts; the report explicitly says those verdicts are unavailable rather than inventing them or promoting provisional journal gates. Seed-level A1–A4 outcomes come from the final adjudication/seed CSV.

## Preservation

SHA-256 and byte comparisons passed for all eight canonical Markdown/PDF files, `assets/content.js`, `assets/atlas.js`, and `SOURCE_SHA256.txt`. The original document payload embedded in `Sidus_Dossier_Standalone.html` is byte-for-byte unchanged. `E0A_PRESERVATION.json` records those hashes. The supplied ZIPs are copied without alteration.

## Validation completed

- All 6,500 attempt rows, 2,500 learned rows, 4,000 control rows and 500 final seed records match the archive inventory.
- Seed identities and final gates agree with the configuration/adjudication.
- Per-seed endpoint declines match adjudication; registered Hoeffding radii reproduce within the specified tolerance; ideal-outcome minimum recomputed from the frozen plan.
- 4,918 emitted leaf values checked against archived selectors; 4,245 rendered values checked against emitted data/formatting.
- Static-page links, raw evidence links and packaged downloads resolve on disk.
- Browser checks: Results search, direct scene entry and refresh, Back, Document IV companion link, Atlas evidence group, standalone route, and script-free edition.
- Keyboard gate selection and matrix arrow navigation; full reveal and public-shortcut interventions display “unavailable”.
- Mobile Results menu exercised at 390 px; no page overflow at 390 or 320 px. Diagram regions scroll internally where needed. Reduced-motion styling disables scrolling animation.

**Human acceptance still to perform:** the brief's unannounced five-number provenance drill and new-reader comprehension test require a human participant. They have not been represented as completed. The site is prepared for that review, with no publishing action taken.

## Files changed

Existing files: `assets/app.js` (integration only), `index.html` (navigation/assets), `Sidus_Dossier_Standalone.html` (companion styles/scripts/navigation), `sw.js` (matching cache generation), `scripts/rebuild.py` (companion synchronization hook), and `README.txt` (build instructions).

New files: `assets/results/` (renderer, stylesheet, generated data, provenance and selected unmodified sources), `downloads/` (the supplied ZIPs), `e0a.html`, `scripts/build_e0a.py`, `scripts/build_companion.mjs`, `scripts/check_e0a.py`, `scripts/check_companion.mjs`, and E0-A recon/preservation/handover notes.

## Rebuilding only the companion

From the Sidus directory:

```sh
python3 scripts/build_e0a.py --results /path/to/Sidus_E0_F1_Complete_Results.zip --freeze /path/to/Sidus_E0_Frozen_v0.7_F1.zip
node scripts/build_companion.mjs
python3 scripts/check_e0a.py
node scripts/check_companion.mjs
```

Python and Node standard libraries only; no package installation required. Do not run the canonical document/PDF regeneration command for this companion change. If a future authorized corpus rebuild is run, its existing pipeline now also synchronizes the companion.

The companion builder derives the new service-worker cache suffix from the app/report assets. Returning visitors install a matching cache set; existing v5 caches are removed on activation. Already open pages may need one reload to show the new navigation. Evidence excerpts/ZIPs remain on-demand downloads, so they are not promised offline.
