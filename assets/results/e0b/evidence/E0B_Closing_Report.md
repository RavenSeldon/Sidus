# Sīdus E0-B — Closing Report (incorporating Ledger G)

**8 October 2026 · protocol v2.2 + Ledgers D–G · Completion Plan stopping criterion (frozen) · all earlier ledgers, reports and archives v1–v3 are preserved unchanged**

## 0. Outcome

**E0-B is COMPLETE under the frozen stopping criterion (§6).** Every index ends in a frozen, executed, auditable result or a justified determination of non-identification. No result was manufactured.

| Index | Final disposition |
|---|---|
| **Shea** | **Exact scope:** `validated_operationalization`, functional finding only. **Learned (prospective test of pilot-derived hypotheses, seeds 1001–1020):** H1, H2 and H3 all **confirmed** |
| **RR** | `inconclusive(non_identified)`: bounded accessibility gain demonstrated; matched transformations reproduce it; the coupling clause is non-identified |
| **Process** | `inconclusive(non_identified)` under U1: the fixture leaves no nonlinear structural distinction to identify |

**One-sentence finding.** Under the registered architecture and training procedure, explicit correctness supervision produces a code that meets the operational correctness-monitoring profile, while reward-only optimization produces an action-value-like code that does not; the profile is detectable, but in this setup it does not emerge from reward alone.

---

## 1. Ledger G — Corrections Executed After the External Audit of Ledger F

| Audit item | Action | Evidence |
|---|---|---|
| Process identity | Verified: every permitted map has f(00) + f(01) + f(10) + f(11) = 2, so **f(11) = 2 − f(00) − f(01) − f(10)**. A linear readout of per-cell values recovers the held-out value exactly | exact check; Ledger F `e0b_pilot_process_check.py` |
| Process disposition | **Closed as `inconclusive(non_identified)` under U1.** The 8-map probe is kept as exploratory only | audit decision |
| D11 did not match κ_d | **Repaired:** one shared κ_d per pair; κ_a and κ_i drawn uniformly on their feasible intervals; full three-action vector matched (asserted in code) | `e0b_confirm.py` |
| Thresholds needed a measurement floor | The exact φ_post code was run through the identical fitted pipeline on pilot evaluation sets; thresholds = floor + pre-stated tolerance | §2 |
| κ-sensitivity is coordinate-dependent | Added the decoder-based κ-retention R² from (M, φ_post, R); κ-sensitivity kept as a descriptive diagnostic for multi-dimensional codes | §2 |
| Failure must be established positively | Each hypothesis has confirm, disconfirm and inconclusive rules with one-sided t-bounds over seeds; Bonferroni for joint confirmation and for declaring clause failure | Confirmation Rules §4 |
| H3 overstated | Narrowed to "carries demonstrable correctness-relevant information while retaining payoff-context information" | Confirmation Rules §4 |
| 100k evaluation blocks is a new design choice | Labelled as a pilot-informed design choice, not an output of the original budget rule; the seed is the unit of inference | Frozen spec |

The repaired D11 changed the pilot-seed means modestly: C-end 0.048 → 0.026, B0-am 0.697 → 0.680 (medians 0.013 → 0.013 and 0.717 → 0.700). It did not change any qualitative pattern.

## 2. Governance Trail (in order)

| Step | Artifact | SHA-256 (prefix) | UTC |
|---|---|---|---|
| Pilot protocol committed before the pilot | `E0B_Pilot_Protocol_P0.md` | 25cb3989… | 12:37:37 |
| Confirmation rules committed **before** the pilot recheck | `E0B_Confirmation_Rules.md` | 67e4c680… | 13:21:30 |
| Pilot-seed recheck (exploratory) → mechanical thresholds | `recheck_thresholds.json` | in frozen spec | — |
| **Freeze** (thresholds + code hashes) | `E0B_Frozen_Confirmation_Spec.json` / `.md` | 910e39a9… / dc3d2775… | 13:35:26 |
| Confirmation run, seeds 1001–1020 | `confirm_results.json`, `confirm_adjudication.json` | archive v4 | after freeze |

- Confirmation seeds appear in no pilot or recheck file.
- All four frozen files were verified **unchanged** after the run.
- Timestamps are self-recorded and not independently authenticated, as the audit noted for the pilot commitment.

**Exploratory pilot-seed result recorded in the freeze document before confirmation:** H1 inconclusive (S1b κ-retention upper bound 0.026 against threshold 0.0184), H2 confirmed, H3 confirmed. The thresholds were not adjusted.

**Frozen thresholds:**

| Threshold | Value |
|---|---|
| calibration excess | ≤ 0.002341 |
| S1e gap at 0.75 / 0.80 | ≤ 0.002729 / 0.002384 |
| κ-retention R², invariant | ≤ 0.018406 |
| κ-retention R², retains | ≥ 0.098406 |
| D11 agreement | ≥ 0.816867 |
| relay advantage over best learned rival | > 0.01299 |

## 3. Confirmation Results (seeds 1001–1020; each seed evaluated on 100k + 100k fresh independent blocks)

### 3.1 System profiles (seed mean ± sd)

| System | Relay | Calibration excess | κ-sensitivity | κ-retention R² | D11 agreement | S1e gap 0.75 / 0.80 |
|---|---|---|---|---|---|---|
| ideal φ_post (pipeline floor) | 0.7944 | 0.0003 | 0 | −0.003 | 0.921 | 0.0005 / 0.0002 |
| **C-sup** (supervised) | 0.7943 ± 0.0009 | 0.0004 | 0.014 | 0.012 ± 0.012 | 0.945 ± 0.016 | 0.0006 / 0.0007 |
| **C-end** (reward-only scalar) | 0.7692 ± 0.0048 | 0.0174 | 0.548 | 0.327 | 0.050 ± 0.078 | 0.022 / 0.025 |
| **B0-am** (4-d, end-to-end) | 0.7878 ± 0.0090 | 0.0070 | 1.908 | 0.791 ± 0.063 | 0.716 ± 0.285 | 0.009 / 0.009 |
| R-vec (action-vector rival) | 0.7680 | 0.0201 | 1.216 | 0.660 | 0.013 | 0.027 / 0.033 |
| R-acc (accept-value rival) | 0.7470 | 0.0315 | 0.777 | 0.329 | 0.007 | 0.039 / 0.041 |

### 3.2 Adjudication (mechanical, under the frozen rules)

**H1 — C-sup passes every learned Shea clause: CONFIRMED.**

| Clause | Mean | One-sided bound | Threshold |
|---|---|---|---|
| calibration excess | 0.00044 | upper 0.00046 | ≤ 0.00234 |
| κ-retention R² | 0.0122 | upper **0.0166** | ≤ 0.0184 |
| S1e gap 0.75 / 0.80 | 0.00056 / 0.00067 | upper 0.00062 / 0.00078 | ≤ 0.00273 / 0.00238 |
| D11 agreement | 0.945 | lower 0.939 | ≥ 0.817 |
| relay advantage over best rival | 0.0263 | lower 0.0258 | > 0.0130 |

**H2 — C-end (reward-only) fails the profile in the predicted way: CONFIRMED.**
- D11 agreement 0.050, upper bound (α/2) 0.087 ≤ 0.20.
- κ-sensitivity 0.548, lower bound 0.537 ≥ 0.25.
- Descriptive κ-retention R² 0.327.

**H3 — B0-am carries correctness-relevant information while retaining payoff-context information: CONFIRMED.**
- D11 agreement 0.716, lower bound 0.583 ≥ 0.30.
- κ-retention R² 0.791, lower bound 0.761 ≥ 0.098.

### 3.3 What the means do not show (stated so the confirmations are not over-read)

- **H1 is a claim about the seed-level mean.** Only **14/20** C-sup seeds individually meet all six clauses; the binding clause is κ-retention, with per-seed R² up to 0.036. The supervised encoder sees κ as an input and does not learn to ignore it in every initialization. Its invariance holds on average, not uniformly. One-sided 95 % exact lower bound on per-seed reliability at 14/20 ≈ 0.49.
- **The H1 S1b margin is narrow.** The upper bound of 0.0166 sits against a threshold of 0.0184, and on pilot seeds (n = 10) the same clause was inconclusive. The confirmation is genuine under the frozen rule, but this clause is the most fragile result in E0-B.
- **H2 per seed:** 19/20 seeds meet both H2 conditions; one C-end seed exceeded D11 0.20.
- **H3 per seed:** 17/20 seeds; B0-am's D11 is highly variable across seeds (sd 0.285).
- **Pipeline artifact.** The ideal code's D11 agreement through the binned relay (0.921) is *below* C-sup's (0.945). That is a property of quantile binning near decision boundaries, not evidence that C-sup exceeds the ideal. The threshold rule (floor_0.05 − 0.10) absorbs it.

## 4. What E0-B Establishes and What It Does Not

**Establishes:**
1. A synthetic experiment can distinguish a correctness-monitoring code from registered first-order action-value rivals under explicit operational criteria. This is shown at exact scope with constructed witnesses (trace-compliant included) and with learned systems.
2. In the registered architecture and training procedure, **reward-only optimization did not produce** the operational correctness-monitoring profile. It produced an action-value-like code, while correctness supervision did produce the profile.
3. Two of the three operationalizations could not be identified in the registered fixtures, for documented mathematical reasons:
   - RR: the gain is reproduced by matched feature engineering, and the coupling clause depends on which admissible consumer is frozen;
   - Process: under U1, f(11) is a linear function of the observed values.

**Does not establish:**
- **Strict metarepresentation.** The correctness / correctness-contingent-value identity (Ledger D-II §3) caps interpretation at the functional finding.
- That reward-only learning *cannot* produce the profile. Only one architecture and training procedure were tested, so other rewards, curricula or architectures may differ.
- Anything about process or redescription representation outside U1.
- Ecology-level or biological claims.

## 5. Independent-Verification Status

- **Reproduced by the external auditors:**
  - exact Shea references, RR1e, the P1b contracts and the S1e vacuity;
  - the Process identity and per-cell readout;
  - archive integrity (v2: 33/33 manifest; v3: 101/101) and the pilot records.
- **Not yet independently reproduced:**
  - the full 43-assertion suite (it exceeded the auditor's execution window);
  - the confirmation run itself, which the same agent designed, froze, ran and adjudicated.

The stopping criterion does not require external reproduction. Still, an independent re-run of `e0b_confirm.py confirm` against the frozen spec is the strongest remaining check and is recommended. Training and evaluation are deterministic by seed, so it should reproduce the confirmation bit-for-bit.

**Interpretation note for Ben.** The audit's "CONDITIONAL GO" listed "freeze, run the reserved seeds, adjudicate" as the path once its conditions were met. I took the conditions as satisfied by the executed repairs (§1). If you or the auditor read the audit as requiring a further review of the frozen thresholds *before* the run, that reading should be recorded and the confirmation treated accordingly under the amendment rule. The record preserves the order of events, so either reading can be applied.

## 6. Stopping Criterion — Final Check

| Item | Status |
|---|---|
| 1. Every index has a frozen, executed, auditable test, or a justified non-identification | ✔ Shea (exact + learned confirmation); RR and Process (justified determinations) |
| 2. Conclusions survive registered rivals and uncertainty controls | ✔ exact rivals defeated; learned hypotheses adjudicated with seed-level bounds and multiplicity control |
| 3. All discrepancies and cross-passes have dispositions | ✔ Ledgers D–G, Report §4.5, this report §3.3 |
| 4. Empirical findings separated from representational interpretation | ✔ §4 |
| 5. No necessary experiment unfinished; reproduction artifacts archived | ✔ archive v4 |

**E0-B: COMPLETE.** Per the programme decision, E0-B was never a gate on E1. E1 (monitoring under genuine scarcity) is the natural next step, and the learned finding here (reward pressure produces action-value codes; correctness codes need targeted pressure or capacity) is directly relevant to its allocation questions.

## 7. Provenance — Archive v4

v3 contents plus:
- **Rules, freeze and commitments:** `E0B_Confirmation_Rules.md` and its commitment; `E0B_Frozen_Confirmation_Spec.json`/`.md` and the freeze commitment.
- **Code:** `e0b_confirm.py`.
- **Recheck:** `recheck_results.json`, `recheck_thresholds.json`, `recheck_output.md`, the exploratory recheck adjudication.
- **Confirmation:** `confirm_results.json`, `confirm_adjudication.json`, `confirm_output.md`.
- **This report.**

Archive v4 has a fresh SHA-256 manifest. Reproduce with:
- `python3 e0b_confirm.py recheck` (pilot seeds, exploratory)
- `python3 e0b_confirm.py confirm` (requires the frozen spec; seeds 1001–1020)
