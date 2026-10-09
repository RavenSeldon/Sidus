# Sīdus E0-B — Independent Final Validation Addendum

**Date:** 8 October 2026  
**Source:** `E0B_Closing_Report.md` and `E0B_MB0-MB2_archive_v4.zip`  
**Disposition:** **E0-B COMPLETE under its frozen, bounded stopping criterion; ready for formal report drafting.** This is not a claim of strict metarepresentation or an independent full-scale replication of the learning experiment.

## Independent checks

1. **Integrity.** Independently recomputed every one of the **115/115** SHA-256 manifest entries in archive v4; all match. The separately supplied closing report is byte-identical to the archived report. The frozen specification (`910e39a9…`) and associated rules, script hashes, and recheck-threshold file match their recorded commitments.
2. **Statistical adjudication.** Independently recomputed from `confirm_results.json`, rather than trusting `confirm_adjudication.json`, all six seed-level H1 bounds and the two bounds for each of H2 and H3. **H1, H2 and H3 all meet their predeclared numerical confirmation criteria** on seeds 1001–1020. Counts of individual seeds meeting each conjunctive profile reproduce: H1 **14/20**, H2 **19/20**, H3 **17/20**.
3. **Sensitivity.** H1's binding nuisance-retention mean is 0.012160; the registered one-sided upper t-bound is 0.016598 against threshold 0.018406. A 200,000-resample descriptive bootstrap yielded an upper 95th percentile of approximately 0.01637. A conservative three-hypothesis Bonferroni sensitivity check gives H1 an upper t-bound of approximately 0.01805, still beneath its threshold. H2 and H3 also retain their predicted directions under that adjustment. The preregistered decision rule, not these post-hoc sensitivity checks, determines the original verdict.
4. **Source implementation.** Reviewed the evaluation and adjudication code, including trace/block sampling, the repaired full three-action-value D11 pair matching, the ideal-pipeline thresholds, and the learned rival comparisons. The SHA-256 of each frozen source file agrees with the archived freeze.
5. **Scope.** The RR and Process non-identification dispositions are supported by the earlier documented fixture limitations. Neither is a positive metarepresentation finding. The Shea finding is restricted to the registered operational, functional criterion and tested architecture/training procedure.

## Precision qualifications for the formal report

- **Name the correct comparator.** H1's 0.026328 mean relay advantage is over the better of the **two registered learned action-value rivals** (`R-vec`, `R-acc`) on each seed. This is **not** an advantage of 0.026328 over *every* learned model. If `C-end` and the four-dimensional `B0-am` are also included, the mean advantage falls to approximately **0.006176**; that comparison was **not** the frozen H1 clause and must not be substituted after seeing the results.
- **Distinguish the seed-level mean from deployment reliability.** H1 confirmation concerns a population mean over initialization seeds; just **14 of 20** supervised seeds individually satisfy all six clauses. The binding κ-retention result is close to the threshold. The experiment does not establish uniformly reliable success across random initializations.
- **Report the provenance limitation precisely.** Artifact contents and source hashes match the recorded freeze; the self-recorded timestamps and historical separation of the recheck and confirmation runs cannot be independently authenticated from the archive alone. An attempted fresh training-and-evaluation rerun exceeded the available execution limit and did **not** yield an independent replicate. Therefore do not state that the full learning confirmation was independently rerun or bitwise reproduced.
- **Retain the interpretation ceiling.** Functional correctness-monitoring discrimination does not distinguish correctness probability from a correctness-contingent action-value interpretation under the mathematical identity recorded in Ledger D-II. The results do not establish strict metarepresentation, consciousness, biological generality, or architecture-general failure of reward-only learning.

## Sign-off decision

**Approved for the next stage: formal scientific report writing using the user's forthcoming sample/template.** The closing report can be treated as the completed *internal E0-B research record* under the agreed stopping criterion. Keep archive v4 and the original closing report unchanged; append this validation note rather than retroactively changing the frozen results. Full independent execution-level reproduction remains a desirable separate follow-up, but was not a condition of the preapproved E0-B completion rule.
