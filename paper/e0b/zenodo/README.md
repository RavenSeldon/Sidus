# Sīdus E0-B: research record

**What Does a Monitoring Signal Represent? Definition-indexed discrimination of correctness monitoring, action value, process representation, and redescription**
Ben Amuwo · version of record, 8 October 2026 · doi:10.5281/zenodo.23252262

E0-B was completed under its frozen stopping criterion on 8 October 2026. The findings concern one finite synthetic system and one registered learned architecture. No claim of strict metarepresentation, consciousness, or biological generality is made.

| File | What it is | SHA-256 |
|---|---|---|
| `Sidus_E0B_Research_Paper.pdf` | Paper, version of record | `fac9368b49cfdc4ec1b38e9c1457e9145276df28339d27466ff72189b6efa635` |
| `Sidus_E0B_Research_Paper.md` | Paper source (pandoc Markdown with LaTeX) | `4c0037c5bcfc3288252e6e45c81a4ceae148b842c5eff9f55e2c9d965ce3df05` |
| `E0B_MB0-MB2_archive_v4.zip` | Canonical experimental record: code, contract tables, ledgers D–G, frozen specification, seed-level results, adjudication. Unchanged; contains its own 115-entry SHA-256 manifest | `64f2221a1caf3a838f7ef78d00327f34ab04783842baad2da1edecb97131dd66` |
| `E0B_Independent_Final_Validation.md` | Post-confirmation computational validation (ChatGPT-assisted): manifest recheck, H1–H3 bounds recomputed from the seed-level results, sensitivity checks. Kept outside archive v4. Not an execution-level reproduction | `886bb51b40b46d2cf667b321b10e855ce0e80d38108820b9bb5bdd04af6aa8a3` |
| `E0B_Publication_Addendum.md` | How the files relate to one another, provenance terminology, the author's reading of the open Closing Report note, and the exact changes from the 8 October paper | see file |

**Reproduce:** unzip the archive, recreate the environment recorded in `ENVIRONMENT.txt`, and run `python3 e0b_confirm.py confirm`. Then compare `confirm_results.json` and `confirm_adjudication.json` with the archived copies. No independent execution-level reproduction or audit by unaffiliated researchers is claimed.

**Companion and mirror:** https://sidus.quest/research/e0-b/ · interactive companion https://sidus.quest/#/results/e0-b · paper build: `paper/e0b/` in https://github.com/RavenSeldon/Sidus
**Preceding study:** Sīdus E0-A, doi:10.5281/zenodo.22661563
