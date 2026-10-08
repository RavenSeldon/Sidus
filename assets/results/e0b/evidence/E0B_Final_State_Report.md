# Sīdus E0-B — Final-State Report (MB0–MB2 executed)

**8 October 2026 · protocol v2.2 + Ledgers D, D-II + Completion Plan (approved) · exact-scope development results; nothing here is confirmatory**

## 0. Status in One Paragraph

MB0, MB1 and MB2 have been executed as far as they can be without decisions only Ben can make, and without learned-system confirmation runs.

| Index | Status at exact scope | Why |
|---|---|---|
| **Shea** | operational gate **met** (functional finding only) | the token-φ witness passes every clause; every registered rival fails for the named reason; the correctness / correctness-contingent-value identity stays an explicit interpretive ceiling |
| **Process** | operational gate **met**, with two caveats (§4.3) | the structured process model passes; the per-cell tracker and identity classifier fail |
| **RR** | operational gate **not met as written** | its procedure-coupling clause (RR1c) turned out **not identified**: whether a code passes depends on which of several equally admissible frozen consumers is used. This is a newly discovered defect, recorded with its original outcome; it needs Ben's definitional decision (§7, D2) |

E0-B is therefore **not COMPLETE** under the frozen stopping criterion. Criterion 1 fails for RR pending D2, and the confirmation phase has not run (it needs B, D2, D3 and learned systems). Everything needed to generate this report, and to resume, is archived (§8).

---

## 1. What Was Run

| Script | Purpose | Arithmetic |
|---|---|---|
| `e0b_mb0.py` | MB0: trace estimators, R2.4 channel tables, D11 eligibility | exact (estimator distributions float64 for k > 10) |
| `e0b_mb12.py` | MB1 audit, consumer ladder, optimization gaps; MB2 witness × predicate matrix | exact (training float64) |
| `e0b_mb2_diag.py` | X1 RR1c identification over admissible consumers; X2 P1b criterion check | exact + LP feasibility |
| `e0b_mb2_diag2.py` | X3 RR1d robustness; X4 P1b decoder-tie range; X5 strengthened optimization-gap training | exact + LP; float64 training |
| `e0b_mb1_lsq.py` | alternative (least-squares) consumer training rule | float64 |
| `e0b_power.py` | power as a function of block budget | float64 Monte Carlo moments + normal approximation, with a simulation check |

Earlier, still-valid scripts: `e0b_reference.py`, `e0b_contracts.py`, `e0b_shea_repair.py`, `e0b_r24.py`.

---

## 2. MB0 Results

### 2.1 Trace estimators — relay (M, R) value of the ideal φ code

| k per input | marginal-MAP bits | joint-MAP mapping | full posterior |
|---|---|---|---|
| 10 | 0.716503 | 0.714921 | 0.734616 |
| 20 | 0.750250 | 0.748248 | 0.762713 |
| 40 | 0.789530 | 0.788818 | 0.794698 |
| 80 | 0.816540 | 0.816450 | not computed |
| oracle | 0.825000 | 0.825000 | 0.825000 |

The joint-MAP mapping is slightly *worse* than marginal-MAP bits for a single-cell decision, as expected: the marginal MAP is Bayes-optimal per bit. Recommended registration: **marginal-MAP as the hard-MAP reference condition, full posterior as the upper reference**. Joint-MAP is used only where a globally consistent mapping is required (e.g. Process).

### 2.2 R2.4 channel-dependent references (relay observes M and R; κ's hidden)

| Access | ε | φ code | B1-accept bound | B1-invert bound | B1-action-vector bound | φ − vector |
|---|---|---|---|---|---|---|
| oracle | 0 | 0.825000 | 0.773828 | 0.773828 | 0.804052 | +0.020948 |
| oracle | 1/10 | 0.809300 | 0.756539 | 0.756539 | 0.781149 | +0.028151 |
| oracle | 1/3 | 0.772667 | 0.718331 | 0.718331 | 0.729936 | +0.042731 |
| k=40 marginal-MAP | 0 | 0.789530 | 0.740914 | 0.740914 | 0.763131 | +0.026399 |
| k=40 marginal-MAP | 1/10 | 0.777093 | 0.728253 | 0.728253 | 0.744938 | +0.032155 |
| k=40 marginal-MAP | 1/3 | 0.748074 | 0.705762 | 0.705762 | 0.710933 | +0.037141 |
| k=40 joint-MAP | 0 | 0.788818 | 0.740371 | 0.740371 | 0.762392 | +0.026426 |
| k=40 joint-MAP | 1/10 | 0.776447 | 0.727788 | 0.727788 | 0.744283 | +0.032164 |
| k=40 joint-MAP | 1/3 | 0.747581 | 0.705580 | 0.705580 | 0.710639 | +0.036941 |

By the dominance argument (Ledger D-II), each bound covers every code measurable with respect to that rival, under the registered marginal-replacement channel. The φ advantage stays positive at every ε and access condition tested.

### 2.3 D11 rule

Sampled caliper matching is impractical. The population probability that a random same-R pair is matched on the full action-value vector *and* differs in φ-optimal action is only 1.1×10⁻⁵ to 2.9×10⁻⁴ (oracle, δ = 0.01–0.05) and up to 6.2×10⁻⁴ (k = 40). Because κ is **experimenter-controlled**, D11 is registered as a **designed intervention**: for a trial pair with different φ-optimal actions, set \(\kappa_a' = \kappa_a + \varphi_1 - \varphi_2\) and \(\kappa_i' = \kappa_i + \varphi_2 - \varphi_1\), which matches the vector exactly. Sampled caliper matching is kept only as a fallback, with its eligibility mass reported. MB2 executed the designed version on 13,824 constructed pairs.

### 2.4 Still open in MB0

The numerical **B** (and so k), and the **margins**. See §6 and §7.

---

## 3. MB1 Results

**Contract audit.** All 11 witness codes are functions of their declared inputs only, across five contexts (κ shifts, θ rewiring, prior shift). A deliberately cheating negative control, which declares no mapping access but reads f, **is detected**, so the audit is sensitive.

**RR consumer ladder (exact, mapping-oracle subproblem).** Linear-argmax 0.806250 → one hidden threshold unit 0.825000 = unrestricted 0.825000 (104 hidden units enumerated). The accessibility gap vanishes at the first rung that can compute parity, as required.

**Optimization gaps (a substantive MB1 finding).**

| Training rule | Rung | Exact rung optimum | Trained (20 seeds) | Seeds reaching optimum |
|---|---|---|---|---|
| policy gradient, softmax | linear | 0.806250 | median 0.757812 (0.745–0.769) | 0/20 |
| policy gradient, softmax | one hidden unit | 0.825000 | median 0.759594 (0.747–0.772) | 0/20 |
| least-squares action values | linear, raw features | 0.806250 | 0.733000 | — |
| least-squares action values | linear, + parity feature | 0.825000 | 0.825000 | — |

Trained consumers fall well short of their exact rung optima, and the shortfall depends on the training rule. Under least squares, the *apparent* accessibility gain is 0.733 → 0.825 = 0.092, almost five times the exact rung gain of 0.019. **Learned RR gains must therefore be measured against exact rung optima, never against trained raw consumers.** Optimization failure can either hide or inflate the RR effect, which confirms the v2.1 ladder qualification empirically. Any confirmation run needs restart protocols and exact-reference checks.

---

## 4. MB2 — Witness × Predicate Matrix (exact scope)

Exact-scope criterion: a clause passes only when the witness attains the exact optimum or exact invariance the clause names. Margins for learned systems remain [FRZ].

### 4.1 Summary (observed, with the original prediction in brackets)

| Witness | Shea | RR | Process |
|---|---|---|---|
| W1 regime code (θ-coupled) | fail (fail) | **not identified** (pass) | fail (fail) |
| W2 input parity (fixed) | fail (fail) | fail, robust (fail) | fail (fail) |
| W3 process model | fail (fail) | fail (fail) | **pass** (pass) |
| W5 token-φ monitor | **pass** (pass) | **not identified** (fail) | fail (fail) |
| W6a per-cell tracker | fail (fail) | fail (fail) | fail (fail) |
| W6b identity classifier | fail (fail) | fail (fail) | fail (fail) |
| W7 bundle W1+W3+W5 | pass (pass) | **not identified** (pass) | pass (pass) |
| B1-scalar reliability \(q_T\) | fail (fail) | **not identified** (fail) | fail (fail) |
| B1-accept-value | fail (fail) | n/e (n/e) | fail by bound (fail) |
| B1-invert-value | fail (fail) | n/e (n/e) | fail by bound (fail) |
| B1-action-vector | fail (fail) | n/e (n/e) | fail by bound (fail) |

W4 (access-matched, learned end-to-end) and W8/W9 are not separate rows. W8 and W9 are Q-measurable, so the B1-action-vector bound covers them analytically. W4 requires learned training (§6).

### 4.2 Shea — clause evidence

The token-φ witness W5 meets every clause:
- calibration excess 0;
- tracking rate 1; nuisance (κ) change mass 0;
- directional substitution rate 1;
- token-transplant action change 0.5;
- held-out d' value equals the optimum at 0.45 and at 0.65;
- endogenous misrepresentation mass 0.5;
- relay value 0.825 > the vector bound 0.804052;
- D11: 13,824 of 13,824 constructed pairs separated.

How the rivals fail:
- **Regime codes (W1, q_T):** calibration excess 0.0821, tracking 0, transplant 0, value 0.700.
- **B1-accept / B1-invert:** calibration excess 0.0318, κ-nuisance change mass 1.0, value 0.7738, D11 0 of 13,824.
- **B1-action-vector:** passes substitution, transplant and misrepresentation, but fails calibration (0.0157), κ-nuisance (1.0), held-out d' (0.8041 / 0.8133 against 0.825), the value bound (0.804052, which equals the bound and is not strictly above it) and D11 (0 of 13,824).

The discrimination is carried by **calibration, κ-invariance and the designed D11 intervention**. Those are exactly the clauses the action-value reading predicts differently.

**Shea readiness:** `validated_operationalization` at exact scope, for the functional finding: *M carries the statistic sufficient for correctness-contingent consumers, invariant to independently varied payoff contexts it could see.* The identity in Ledger D-II §3 stands: the experiment cannot separate "correctness probability" from "value of a correctness-contingent action". The Shea attribution remains the recorded interpretation decision (§7, D5).

### 4.3 Process — clause evidence (k = 5 traces at 00, 01, 10; query f(11))

| Witness | P1a linear / unrestricted / Bayes | P1b held-out-identity accuracy (bound 0.596178) |
|---|---|---|
| W3 process model | 0.596178 / 0.596178 / 0.596178 | 0.596178 |
| W6a per-cell tracker | 0.591577 / 0.591577 / 0.596178 | 0.518517 |
| W5 token-φ | 0.517643 / 0.554250 / 0.596178 | 0.517643 |
| W6b identity classifier | 0.564549 / 0.564549 / 0.596178 | 0.463034 |
| W1, W2, q_T | 0.5 | 0.5 |

- P1d holds for W3. P1e works: with k = 0 traces the accuracy is 0.5, which is labelled `inconclusive(non_identified)`, not fail.
- P1b results are **robust to decoder ties**: every train-optimal decoder gives the same held-out accuracy (X4).
- **Caveat 1 — weak P1a separation.** A per-cell tracker with a fitted linear decoder comes within **0.0046** of the structured Bayes bound at k = 5. The decoder supplies most of the structure. The structural discrimination is carried by **P1b**, held-out identities, where the gap is 0.078.
- **Caveat 2 — criterion consistency.** The v2.1 P1b criterion (> 1/2) is weaker than every other exact-scope criterion. Under it, W5 and W6a would pass P1b. Under the uniform criterion ("attains the held-out bound") they fail. **No index verdict changes** (both fail P1a), but the uniform criterion is recorded as a correction for D4, alongside the original outcome.
- **Design conflict (D3).** P1a needs traces withheld at one input. That contradicts the approved *balanced four-input* allocation, so Process needs its own arm (balanced over three inputs, \(k_p = B_{\text{trace}}/3\)).

**Process readiness:** `validated_operationalization` at exact scope, subject to D3 and D4.

### 4.4 RR — clause evidence and the identification defect

- RR1b: W1 and q_T reach 0.80625 → 0.825 = the unrestricted optimum. W5's φ code also makes the regime decision-accessible (0.825).
- RR1d (substitution) is **robust**: every admissible optimal consumer uses M (X3).
- **RR1c is not identified (X1).** The frozen consumer is *any* weight vector that realizes a pre-rewiring optimal linear policy. For every θ-coupled code (W1, W5, W7, q_T), some admissible frozen consumers keep the post-rewiring optimum and others lose value. The matrix run's "W1 pass / W5 fail" was an artifact of which feasible weight vector the LP solver returned. Only W2's failure is robust: no admissible consumer keeps value.

**Original outcome recorded:** W1 pass, W5 fail (solver-specific). **Identified outcome:** RR1c `inconclusive(non_identified)` for all θ-coupled codes. The same class of defect as Ledger D's quantizer ties: an underdetermined comparator.

**Consequences of each candidate definition (for D2; none adopted here):**

| RR1c definition | W1 / q_T | W5 | W7 | W2 | RR gate |
|---|---|---|---|---|---|
| A. *some* admissible consumer keeps value | pass | pass | pass | fail | met; **W5 cross-passes RR**, so Shea-passers ⊂ RR-passers in this fixture |
| B. *every* admissible consumer keeps value | fail | fail | fail | fail | **not met**: no constructed system passes, so RR is non-discriminating under the strict reading |
| C. a canonical consumer (e.g. max-margin) | depends on canon | depends | depends | fail | arbitrary; not recommended |
| D. decoder-level coupling (pre-rewiring M→T decoder still recovers T′) | pass | pass | pass | fail | same pattern as A |

Any choice is now made with these consequences visible. The record must say so, which is legitimate pre-freeze, since diagnosing exactly this is MB2's purpose.

### 4.5 Dispositions of every discrepancy

| Discrepancy | Disposition |
|---|---|
| B1-scalar q_T predicted RR fail, observed RR not identified (pass under A/D) | **prediction error**: q_T is an invertible relabel of W1's regime code, so the RR clauses treat it identically. Prediction corrected; record kept |
| W1 / W5 / W7 RR verdicts depend on the LP solution | **genuine defect** (RR1c non-identification); D2 |
| B1 rivals Process predicted fail, first run n/e | resolved: by data processing their decoder accuracy is ≤ W5's 0.554 < 0.596, so **fail by bound** |
| P1b criterion inconsistent with other exact-scope clauses | consistency correction; no verdict change; D4 |
| P1a separation of W3 from W6a only 0.0046 | recorded as a limitation; P1b carries the structural discrimination |
| Process requires a held-out input, conflicting with balanced 4-input allocation | design conflict; D3 |
| Optimization gaps far exceed the RR effect | recorded; confirmation must use exact-reference checks (§3) |

---

## 5. Validation Gate per Index (v2.1 §6, revised gate)

| Gate requirement | Shea | Process | RR |
|---|---|---|---|
| (a) a constructed system passes; another fails for the named reason | ✔ W5 passes; regime codes fail calibration/transplant; B1 rivals fail calibration, κ-invariance and D11 | ✔ W3 passes; W6a fails P1a/P1b; W6b fails P1a/P1b | ✘ as written: no robust pass (RR1c not identified) |
| (b) every declared rival defeated or recorded as equivalent | ✔ B1-scalar/accept/invert/vector defeated; correctness-contingent-value equivalence recorded | ✔ per-cell tracker, identity classifier, scalar cue defeated | pending D2 |
| (c) executed matrix archived | ✔ | ✔ | ✔ |
| **readiness** | `validated_operationalization` (exact scope) | `validated_operationalization` (exact scope; D3, D4) | `proposal`, blocked on D2 |

None is `frozen_for_confirmation`: that requires B and margins.

---

## 6. Power as a Function of Block Budget (input to D1; no B chosen)

Reference contrasts use *ideal* systems, so these are lower bounds on what learned systems need. Normal approximation on block means: blocks needed for power 0.80, one-sided α = 0.05 (and α/3 as a conservative Holm bound).

| Index | k per input | Effect μ | B_score = 50: N at margin 0 | N at margin μ/2 | N at α/3, margin μ/2 |
|---|---|---|---|---|---|
| Shea S1h | 10 | 0.0102 | 98 | 390 | 556 |
| Shea S1h | 20 | 0.0220 | 49 | 195 | 278 |
| Shea S1h | 40 | 0.0264 | 14 | 56 | 80 |
| RR RR1b | 10 | 0.0014 | 4,072 | 16,288 | 23,234 |
| RR RR1b | 20 | 0.0073 | 134 | 536 | 764 |
| RR RR1b | 40 | 0.0185 | 14 | 55 | 79 |
| Process P1a (own arm) | k_p = 10 / 20 / 40 | 0.138 / 0.202 / 0.294 | 76 / 32 / 12 | 302 / 128 / 47 | 431 / 182 / 67 |

The full grid (B_score = 20, 50, 100, 200) is in `power_output.md`.

- Simulated means agree with the exact reference gaps to within Monte Carlo error at every k (e.g. Shea k = 40: exact 0.02640, simulated 0.02644).
- **The normal approximation is mildly optimistic at small N.** A direct simulation at the 13-block design point gave power 0.770, not 0.80. Add roughly 2–3 blocks, or use t-quantiles, when N < 30.
- **Reading:** below k ≈ 20 traces per input, RR needs thousands of blocks, and this is before learned-system optimization gaps (§3), which can easily exceed the 0.019 effect. The risk recorded in the Completion Plan stands, now quantified as prospective, not established.

---

## 7. What Remains — Decisions Only Ben Can Make

| # | Decision | Options and consequences |
|---|---|---|
| **D1** | Block budget: \(B_{\text{trace}}\) (so k), \(B_{\text{score}}\), number of blocks | §6 table. The choice should follow the intended experiment and resources, not the gap (Completion Plan §1.4) |
| **D2** | RR1c definition | §4.4: A/D validate RR and make Shea-passers RR-passers; B leaves RR non-discriminating; C is arbitrary |
| **D3** | Process arm | separate held-out-input arm, balanced over three inputs, \(k_p = B_{\text{trace}}/3\) |
| **D4** | P1b criterion | uniform exact-scope criterion ("attains held-out bound"); the original outcome is preserved; no verdict changes |
| **D5** | Shea interpretation | whether the validated functional finding warrants the Shea attribution, given the identity in Ledger D-II §3 |
| **D6** | Margins | require learned pilot runs; the power table uses 0 and μ/2 for illustration only |

## 8. What Could Not Be Completed Here, and Why

1. **Confirmation (Completion Plan package D)** has not run. It needs D1–D3, frozen margins (D6), and learned candidate, rival and W4 systems trained end-to-end. MB1 shows that learned consumers fall short of their exact optima, so a confirmation run without restart protocols and exact-reference checks would confound optimization with representation. Running it now would cut the corner this programme exists to avoid.
2. **The MB0 freeze** cannot be declared until D1 (B), D2 (RR1c) and D6 (margins) are decided.
3. **W4** (access-matched, learned end-to-end) is a learned witness and belongs to confirmation.

Once D1–D6 are made, the remaining path is mechanical: freeze MB0 under the amendment rule; run the learned panel under the frozen spec; adjudicate against the stopping criterion.

## 9. Provenance

All scripts and logs are archived together with SHA-256 hashes (`E0B_MB0-MB2_archive/MANIFEST.sha256`). Every number in this report appears in one of the archived logs. Exact rational arithmetic is used throughout, except where a section is marked float64.

---

*The objective was not to make E0-B incapable of failure, but to make its conclusions incapable of outrunning their evidence. On that standard: Shea and Process are operationally validated at exact scope; RR is honestly unresolved; and the representational ceiling is explicit.*
