# Sīdus E0-B: Publication Addendum

Author: Ben Amuwo · Release date: 8 October 2026 · Zenodo version DOI: [10.5281/zenodo.23252262](https://doi.org/10.5281/zenodo.23252262) · Mirror: https://sidus.quest/research/e0-b/

## 1. Scope

This addendum accompanies the public release of E0-B. It changes no experimental result, decision rule, threshold, or archived file. E0-B remains complete under its frozen stopping criterion (Closing Report, 8 October 2026). The addendum records provenance only. It is not an experimental ledger.

## 2. Released Artifacts and Their Relationship

| Artifact | Role | Status |
|---|---|---|
| `E0B_MB0-MB2_archive_v4.zip` | Canonical experimental record: code, ledgers D–G, frozen specification, seed-level results, adjudication | **Immutable.** SHA-256 `64f2221a1caf3a838f7ef78d00327f34ab04783842baad2da1edecb97131dd66`; its internal manifest of 115 entries is unchanged |
| `Sidus_E0B_Research_Paper.pdf` / `.md` | Final paper | Release version. PDF SHA-256 `fac9368b49cfdc4ec1b38e9c1457e9145276df28339d27466ff72189b6efa635`; Markdown SHA-256 `4c0037c5bcfc3288252e6e45c81a4ceae148b842c5eff9f55e2c9d965ce3df05`. It differs from the 8 October text only in the items listed in §5 |
| `E0B_Independent_Final_Validation.md`, displayed as *Post-confirmation computational validation (ChatGPT-assisted)* | Supplementary record | **Outside archive v4** by design, so the archive manifest stays immutable. SHA-256 `886bb51b40b46d2cf667b321b10e855ce0e80d38108820b9bb5bdd04af6aa8a3`. Its title uses "independent" to mean recomputed from the raw seed-level results; it is not independent of the project |
| This addendum | Provenance clarification | New at release |

The archive is the experimental record. The supplementary validation record and this addendum were written after the archive was closed. They do not belong to it, and the archive manifest does not cover them.

## 3. Provenance Terminology

These labels apply across the paper, website, and Zenodo record.

| Activity | Label used |
|---|---|
| Review outside the original implementation workflow | Separate AI-assisted methodological review |
| Recalculation of archived statistical bounds | Post-confirmation computational cross-check |
| Fresh execution of the complete experiment | Independent execution-level reproduction: **not yet established** |
| Audit by unaffiliated researchers | **Not claimed** |

The Closing Report uses the phrases "External Audit" (§1) and "external auditors" (§5). Read them as *separate AI-assisted review*, not as review by researchers unaffiliated with the project. The original wording is preserved unchanged in the archive.

## 4. Disposition of the Closing Report §5 Interpretation Note

The Closing Report left one question open: whether the conditional audit required further review of the frozen thresholds before confirmation. The author's reading is:

> The conditional audit authorized progression subject to documented corrections. It was not a separate approval of the final frozen thresholds. The project implemented those corrections, recorded a prospective internal freeze, and then executed confirmation on reserved seeds 1001–1020. The numerical decisions have since undergone a separate, ChatGPT-assisted post-confirmation recalculation. The historical execution sequence has not been externally authenticated. The confirmation remains classified as an internally frozen, prospective test of pilot-derived hypotheses.

## 5. Changes Between the 8 October Paper and the Release Version

The text changes are limited to these five:

1. Title page: a new line, "Version of record | doi:10.5281/zenodo.23252262".
2. §7.4: the validation record is identified as "published with this record as a supplementary file outside archive v4".
3. §7.4: "no public E0-B repository or DOI is asserted here" is replaced by the Zenodo deposit (doi:10.5281/zenodo.23252262) and its mirror at sidus.quest/research/e0-b.
4. Appendix C, Archive: "no public release location assigned" is replaced by the same deposit and mirror.
5. Appendix C, Provenance: the validation record's location is stated.

There is no change to results, numbers, thresholds, figures, references, or interpretation. The release PDF was typeset again from the same source. The two figures are the unmodified vector figures from the 8 October PDF. Line breaks on pages 1–3 differ slightly. Every table, figure and subsection is on the same page as before. Two section headings that sat alone at the foot of a page in the 8 October PDF, §4 (page 4) and §6 (page 6), now open the next page beside their text. The 8 October PDF (SHA-256 `6b10e20f38961b0cbaa7a162e62749e918a3b1fd39be10fe83ac654728121c3a`) and Markdown (SHA-256 `d6c3e5d6eefb7a83edc88cbb89d4324c65775691a500632c3e17215332da44dc`) are kept unchanged at https://sidus.quest/downloads/archive/Sidus_E0B_Research_Paper_2026-10-08.pdf and https://sidus.quest/downloads/archive/Sidus_E0B_Research_Paper_2026-10-08.md. The release is typeset from `paper/e0b/` in https://github.com/RavenSeldon/Sidus.

## 6. What Remains Not Established

- Independent execution-level reproduction of the training and confirmation run.
- External authentication of the commitment and freeze timestamps. Hash matching establishes file identity, not historical sequence.
- Audit by researchers unaffiliated with the project.

An independent rerun of `python3 e0b_confirm.py confirm` against the frozen specification remains the strongest available check. It was never a condition of E0-B's completion criterion.
