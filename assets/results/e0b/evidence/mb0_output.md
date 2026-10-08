## M1 Trace estimators — relay (M,R) value of the ideal phi code, R2.4 kappa-free

| k | marginal-MAP bits | joint-MAP mapping | full posterior (Ledger D, D7) |
|---|---|---|---|
| 10 | 0.716503 | 0.714921 | 0.734616 |
| 20 | 0.750250 | 0.748248 | 0.762713 |
| 40 | 0.789530 | 0.788818 | 0.794698 |
| 80 | 0.816540 | 0.816450 | not computed |
| oracle | 0.825000 | 0.825000 | 0.825000 |

## M2 R2.4 channel-dependent references — relay observes (M, R)

| access | eps | phi code | B1-accept bound | B1-invert bound | B1-action-vector bound | phi minus vector |
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

## M3 D11 caliper eligibility (population probability that a random same-R pair is caliper-matched on the rival code AND phi-optimal relay actions differ)

| access | delta | accept-rival caliper | vector-rival caliper |
|---|---|---|---|
| oracle | 1/100 | 0.001596 | 0.000011 |
| oracle | 1/50 | 0.003192 | 0.000046 |
| oracle | 1/20 | 0.007980 | 0.000287 |
| k=40 joint-MAP | 1/100 | 0.002589 | 0.000025 |
| k=40 joint-MAP | 1/50 | 0.005178 | 0.000100 |
| k=40 joint-MAP | 1/20 | 0.012946 | 0.000623 |
