# E0-B Confirmation Rules (written and hash-committed BEFORE the pilot-seed recheck)

**8 October 2026 · implements the external audit of Ledger F ("CONDITIONAL GO") · thresholds are defined here as rules; their numeric values are filled in mechanically from the pilot-seed recheck and then frozen**

## 1. Scope and Dispositions Already Final

| Index | Final disposition |
|---|---|
| RR | `inconclusive(non_identified)` (Ledgers E, F; D2) |
| Process | `inconclusive(non_identified)` under U1 (audit, Ledger G). Every permitted mapping inverts exactly two of four inputs, so f(11) = 2 − f(00) − f(01) − f(10): a linear readout of per-cell values recovers the held-out value, and no nonlinear structural distinction remains to identify. The 8-map probe is kept as exploratory only |
| Shea exact scope | `validated_operationalization`, functional finding only |
| Shea learned | **prospective test of pilot-derived hypotheses** H1–H3 on untouched seeds 1001–1020; one registered architecture family. Conclusions are limited to that architecture and training procedure |

## 2. Repaired Measurement Pipeline (`e0b_confirm.py`)

1. **D11, full action-value matching.** For each pair (same R, different φ_post-optimal relay action):
   - one shared κ_d is drawn and given to both members;
   - κ_a⁽¹⁾ is drawn uniformly on [max(0, φ₂−φ₁), min(1, 1+φ₂−φ₁)], and κ_a⁽²⁾ = κ_a⁽¹⁾ + φ₁ − φ₂;
   - κ_i⁽¹⁾ is drawn uniformly on [max(0, φ₁−φ₂), min(1, 1+φ₁−φ₂)], and κ_i⁽²⁾ = κ_i⁽¹⁾ + φ₂ − φ₁.

   All three action values then coincide across the pair.
2. **Ideal-pipeline floor.** The exact φ_post code is run through the identical fitted pipeline (binned relay, binned regressor, D11, S1e, κ-retention). This measures the error the evaluation method itself introduces.
3. **Decoder-based κ-retention.** An MLP regresses (κ_a, κ_i, κ_d) on (M, φ_post, R), fit on the fit split and evaluated on the test split:
   - R²_κ = 1 − MSE / Var(κ), averaged over the three components;
   - the counterfactual κ-sensitivity score is kept as a descriptive diagnostic only (it is coordinate-dependent for d > 1).
4. All other measures are unchanged from the pilot (E1 relay, E2 calibration excess, E5 S1e gaps at 0.75 and 0.80).

## 3. Threshold Rules (numeric values set from pilot seeds 1–10, ideal pipeline only)

Write floor_q for the q-quantile, over the 10 pilot evaluation sets, of the ideal code's value through the same pipeline.

| Quantity | Threshold rule |
|---|---|
| calibration excess (S1a) | thr_cal = floor_0.95 + 0.002 |
| S1e gap at each d′ | thr_s1e = floor_0.95 + 0.002 |
| κ-retention: invariant (S1b) | R²_κ ≤ thr_inv = floor_0.95 + 0.02 |
| κ-retention: retains (H3) | R²_κ ≥ thr_ret = floor_0.95 + 0.10 |
| D11 correctness-tracking (H1) | agreement ≥ thr_d11 = floor_0.05 − 0.10 |
| relay advantage over best learned rival (H1) | > 0.01299 (the pilot rule's half-P10 for C-sup, Ledger F §3.2) |

## 4. Hypotheses and Decision Rules (seed = unit of inference, n = 20)

For each measure, compute the seed-level mean and one-sided 95 % t-bounds (df = 19).

**H1 (engineering positive control): C-sup passes every learned Shea clause.**
- Clauses: S1a ≤ thr_cal; S1b R²_κ ≤ thr_inv; S1e gap ≤ thr_s1e at both d′; D11 ≥ thr_d11; relay advantage > 0.01299.
- A clause **passes** when its bound lies on the passing side at α = 0.05; by the intersection–union test the conjunction needs no further correction.
- A clause **fails** when the opposite bound lies on the failing side, with Holm control over the six clauses.
- Otherwise the clause is inconclusive.
- **H1 confirmed** iff all six pass.

**H2 (scientific, directional): C-end (reward-only scalar) fails the Shea profile in the pre-specified way.**
- (a) D11 agreement upper bound ≤ 0.20;
- (b) κ-sensitivity lower bound ≥ 0.25 (scalar code, so the measure is meaningful).
- **H2 confirmed** iff both (a) and (b) hold, each at α = 0.05/2 (Bonferroni, since confirmation is conjunctive and joint).
- **Disconfirmed** iff the D11 lower bound > 0.20 or the κ-sensitivity upper bound < 0.25 (Holm).
- Otherwise inconclusive.
- R²_κ is reported descriptively.

**H3 (narrowed per the audit): B0-am carries demonstrable correctness-relevant information while retaining payoff-context information.**
- (a) D11 agreement lower bound ≥ 0.30;
- (b) R²_κ lower bound ≥ thr_ret.
- Confirmation, disconfirmation and inconclusive outcomes follow the same algebra as H2.

**Required rivals.** R-vec and R-acc are trained on the same confirmation seeds and enter H1's relay advantage. The rivals' own clause outcomes are reported descriptively.

## 5. Freeze Procedure

1. Run the pilot-seed recheck (seeds 1–10) with the repaired pipeline. Report it as exploratory.
2. Fill the numeric thresholds by the rules above.
3. Write `E0B_Frozen_Confirmation_Spec.md` with those thresholds and the SHA-256 of every code file used, and commit its hash.
4. Run seeds 1001–1020 for C-sup, C-end, B0-am, R-vec and R-acc.
5. Adjudicate mechanically. Any later change follows the amendment rule and cannot turn an outcome into a pass.
