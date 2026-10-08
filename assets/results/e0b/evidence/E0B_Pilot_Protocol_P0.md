# E0-B Learned Pilot P0 — Protocol (written before any pilot run)

**8 October 2026 · decisions in force: D2–D6 approved by Ben (Ledger F); finish path "learned pilot, then pause" · pilot only: nothing here is confirmatory**

## Purpose

Estimate what *trained* systems achieve on the validated operationalizations (Shea at k = 40 traces per input; Process held-out-identity arm). The pilot then yields (i) proposed statistical margins, (ii) a proposed block budget B, and (iii) optimization-reliability figures. All three feed a **draft** MB0 freeze, which is submitted for external audit before any confirmatory run. RR is not piloted: D2 records it as `inconclusive(non_identified)`.

## Seeds

- **Pilot seeds:** 1–10, per system.
- **Confirmation seeds:** 1001 onward, reserved and **never touched** during the pilot.
- Every evaluation draws fresh blocks from an evaluation RNG (seed 9000 + training seed), disjoint from training draws.

## Shea arm (R2.4 contract, k = 40, balanced four-input traces)

- **Encoder inputs** (trace-compliant): one-hot input o, report R, regime T (θ access), the posterior marginal \(m_1(o) = P(f(o)=1 \mid \text{trace counts})\), and the payoff contexts \(\kappa_a, \kappa_i, \kappa_d\). The encoder never reads f or the mapping parameters.
- **Architectures:** one-hidden-layer tanh MLP, 32 units, Adam, minibatch 1024, 4,000 steps, data drawn online.

| System | Output | Training objective |
|---|---|---|
| C-end (B2 candidate, T-end arm) | scalar M | end-to-end through an acceptance consumer (MLP over M, R, κ's) maximizing expected acceptance payoff |
| C-sup (B2 candidate, T-sup arm) | scalar M | binary cross-entropy on correctness L |
| R-vec (B1-action-vector) | 2-d M | MSE to (L + κa, (1 − L) + κi) |
| R-acc (B1-accept-value) | scalar M | MSE to L + κa |
| B0-am (access-matched, unconstrained) | 4-d M | end-to-end as C-end; scored as a candidate |

- **Ideal reference:** the exact posterior correctness probability \(\varphi_{\text{post}}\), computed in closed form per sample.

## Measures (per trained system; evaluation fit split / test split, 100k trials each)

| Measure | Definition |
|---|---|
| E1 relay value | relay consumer observes (M, R); its policy is fit on the fit split by binning (scalar M: 40 quantile bins × R; 2-d: 20×20 bins × R; 4-d: an MLP relay with 3 restarts, best on the fit split), then evaluated on the test split |
| E2 calibration excess | mean (\(\hat\varphi\) − \(\varphi_{\text{post}}\))², where \(\hat\varphi\) = binned E[L ∣ M, R] (MLP regressor for 4-d) |
| E3 κ-sensitivity | mean ‖M(s, κ) − M(s, κ′)‖ / sd(M) under an independent κ′ redraw |
| E4 D11 agreement | designed pairs (same R, different φ_post-optimal relay actions, κ's set to match the vector Q exactly): fraction of pairs where the fitted relay chooses each member's φ_post-optimal action |
| E5 S1e gap | ideal value at d′ minus the relay value refit at d′ ∈ {0.75, 0.80} with M frozen |

## Process arm (k_p = 20, three observed inputs; f(11) held out)

| System | Inputs | Model |
|---|---|---|
| P-struct | the 3 normalized trace counts | MLP |
| P-cell-lin | per-cell MAP bits | logistic readout |
| P-cell-mlp | per-cell MAP bits | MLP readout |

- **Training:** BCE on f(11), training identities only.
- **Evaluation:** held-out identities. Reference: Monte Carlo identity-blind Bayes bound under the full structured prior (contract (a), Ledger E §E3).

## Pre-specified derivation rules (fixed now, before results)

1. **Margin per measure:** half the pilot 10th-percentile effect across the 10 seeds of the T-end candidate (direction-adjusted).
   - If the 10th-percentile effect is ≤ 0, no positive margin is defensible. That clause is reported as *not reliably achieved by learned systems at pilot scale*, and is not quietly dropped.
2. **Block budget:** B_trace = 160 (k = 40 × 4 inputs). The smallest B_score ∈ {20, 50, 100, 200} and number of blocks N such that a one-sided test on block means has power ≥ 0.90 at α = 0.05/3 (Holm-conservative) for the primary Shea contrast (E1: candidate minus best rival).
   - Pilot per-trial and between-block variances are used, with N inflated by 3 when N < 30 (t-correction, Report §6).
3. **Optimization reliability:** report seeds reaching ≥ 95 % of the ideal relay value. Under the amendment rule, no seed is excluded after the fact.
