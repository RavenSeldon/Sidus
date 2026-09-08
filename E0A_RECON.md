# E0-A reconnaissance · 7 September 2026

- Router: hash segments, synchronous render; results must explicitly dispatch before home fallback. Scene anchors use #/results/e0-a/scene-N; bare hashes currently fall back to home.
- Atlas: lightbox copies the heading, first paragraph and SVG outerHTML. New evidence plates will be static, with links outside clickable plates.
- Service worker: sidus-dossier-v5; cache-first; install precaches, skipWaiting, activate deletes older sidus caches. Bump version and include matching new lightweight assets, exclude downloads and raw evidence.
- Search: generated at query time from SIDUS_DATA.docs sections and SIDUS_DATA.dummies. Add independent results search entries, keeping frozen payload untouched.
- Navigation: desktop topnav, four-item mobile bottom bar, rail opened by menu. Put Results in every contextual rail to keep it reachable on mobile without crowding the bottom bar.
- Document IV: index 3, #/document/3/frontpiece. Place related result in reader metadata, outside article.
- Static assets, no minification/package manager. scripts/rebuild.py regenerates canonical readers/PDFs and replaces inline standalone scripts. Do not run it on frozen documents. Add a dedicated companion-only build to generate evidence and synchronize standalone shell without changing SIDUS_DATA.
- Local git working tree was clean. Work is prepared in a staging copy, then applied to the provided repository after preservation checks. No commit, push or deployment.
- Use this site's Document IV surface. Host supplied complete ZIP adjacent to report as explicit download.
- Intermediate human review gates are replaced by automated checks under user's best-judgement authorization; final human comprehension/provenance drill remains a clearly labelled handover check.
