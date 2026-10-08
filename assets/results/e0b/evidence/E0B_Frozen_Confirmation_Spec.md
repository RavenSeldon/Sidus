# E0-B Frozen Confirmation Specification 1.0

**Frozen 2026-10-08T13:35:26Z · implements E0B_Confirmation_Rules.md (commitment 67e4c680bdbb3a775cc04f5a6802e4595c3ce24f4701a0a7724fa36119d4b475) · seeds 1001–1020 have not been run before this freeze**

## Numeric thresholds (filled mechanically from the pilot-seed recheck, ideal pipeline only)

| threshold | value |
|---|---|
| thr_cal | 0.002341 |
| thr_s1e_0.75 | 0.002729 |
| thr_s1e_0.8 | 0.002384 |
| thr_inv | 0.018406 |
| thr_ret | 0.098406 |
| thr_d11 | 0.816867 |
| relay_margin | 0.012990 |

## Code identity

| file | SHA-256 |
|---|---|
| e0b_pilot.py | `5acbf25ce3ee5064778f78f605d67e7aec0c06b0eafacd582a5b4a2d5acddab9` |
| e0b_confirm.py | `31701eaa44772f5d6de8861cd732ddb54175457cea428a64f33e6dabd4610820` |
| E0B_Confirmation_Rules.md | `67e4c680bdbb3a775cc04f5a6802e4595c3ce24f4701a0a7724fa36119d4b475` |
| recheck_thresholds.json | `52f9b4e37d5d08d880e94435fafa44b3449b645ea8cc301e349aa4bd96ff3b36` |

## Exploratory note recorded before confirmation

On pilot seeds (n = 10) the decision algebra returned H1 inconclusive (S1b κ-retention: mean R² 0.017, upper bound 0.026 vs threshold 0.0184), H2 confirmed, H3 confirmed. The thresholds were NOT adjusted in response; they follow the committed rules.
