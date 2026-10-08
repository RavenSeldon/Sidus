# E0-B Ledger E execution log

## E1 RR1e matched transformations (mapping-oracle subproblem; linear-argmax consumer)

same-target feature learner (Bayes predictor of T from raw Z1,Z2): {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 0}  (= parity)

| code | linear without M | linear with M | gain |
|---|---|---|---|
| W1 regime code (theta-coupled) | 0.806250 | 0.825000 | +0.018750 |
| same-target feature learner | 0.806250 | 0.825000 | +0.018750 |
| W2 fixed parity | 0.806250 | 0.825000 | +0.018750 |
| shuffled parity (matched support) | 0.806250 | 0.806250 | +0.000000 |

## E2 Process P1c relabelling intervention and P1d controlled substitution (k = 5)

- W6b permutations (of 24) changing any f(11) prediction: 0
- W3 permutations (of 24) changing any f(11) prediction: 0
- W6b worst-case prediction-change mass under relabelling: 0.0

| witness | prediction follows SOURCE label | follows HOST label | own accuracy |
|---|---|---|---|
| W1 regime code (theta-coupled) | 0.500000 | 0.500000 | 0.500000 |
| W2 input parity (fixed) | 0.500000 | 0.500000 | 0.500000 |
| W3 process model (truth table) | 0.596178 | 0.500000 | 0.596178 |
| W5 token-phi monitor | 0.517643 | 0.500000 | 0.517643 |
| W6a per-cell tracker | 0.591577 | 0.500000 | 0.591577 |
| W6b identity classifier | 0.564549 | 0.500000 | 0.564549 |
| W7 bundle W1+W3+W5 | 0.596178 | 0.500000 | 0.596178 |
| B1-scalar reliability q_T | 0.500000 | 0.500000 | 0.500000 |

## E3 P1b information contract (k = 5, held-out identities)

- (a) decoder not told the held-out population (full structured prior): 0.596178
- (b) decoder told the held-out population [((1, 1), 0), ((0, 1), 0)]: 0.665140

## E5 Access audit

- W1 regime code (theta-coupled): trace-compliant [none (theta access only)]
- W2 input parity (fixed): trace-compliant [none]
- W3 process model (truth table): oracle feasibility only [ORACLE (wb)]
- W5 token-phi monitor: oracle feasibility only [ORACLE (f)]
- W6a per-cell tracker: oracle feasibility only [ORACLE (wb)]
- W6b identity classifier: oracle feasibility only [ORACLE (wb)]
- W7 bundle W1+W3+W5: oracle feasibility only [ORACLE (f, wb)]
- B1-scalar reliability q_T: trace-compliant [none]
- B1-accept-value: oracle feasibility only [ORACLE (f)]
- B1-invert-value: oracle feasibility only [ORACLE (f)]
- B1-action-vector: oracle feasibility only [ORACLE (f)]

## E4 Trace-compliant Shea witnesses, k = 10 (marginal-MAP traces; contract-relative targets)

### W5t token-phi (trace-compliant): PASS
- S1a calibration excess vs contract target: 0.0 -> ok
- S1b tracking rate: 1.0 -> ok
- S1b nuisance change mass: 0.0 -> ok
- S1c directional substitution rate: 1.0 -> ok
- S1d transplant action-change mass: 1.0 -> ok
- S1e held-out d (value, contract optimum): [(0.7125063177887642, 0.7125063177887642), (0.7370027798270562, 0.7370027798270562)] -> ok
- S1f endogenous misrepresentation mass (vs oracle phi): 0.24499522655960043 -> ok
- S1h relay value (trace bound 0.706731): 0.7165030325386068 -> ok
- S1h D11 separation: 55296/55296 -> ok

### W1 regime code: fail
- S1a calibration excess vs contract target: 0.018460699939896994 -> NOT MET
- S1b tracking rate: 0.0 -> NOT MET
- S1b nuisance change mass: 0.0 -> ok
- S1c directional substitution rate: 0.5 -> NOT MET
- S1d transplant action-change mass: 0.0 -> NOT MET
- S1e held-out d (value, contract optimum): [(0.7, 0.7125063177887642), (0.7, 0.7370027798270562)] -> NOT MET
- S1f endogenous misrepresentation mass (vs oracle phi): 0.16 -> ok
- S1h relay value (trace bound 0.706731): 0.7 -> NOT MET
- S1h D11 separation: 36864/55296 -> NOT MET

### B1t-accept-value: fail
- S1a calibration excess vs contract target: 0.013583044951118945 -> NOT MET
- S1b tracking rate: 0.5 -> NOT MET
- S1b nuisance change mass: 1.0 -> NOT MET
- S1c directional substitution rate: 0.75 -> NOT MET
- S1d transplant action-change mass: 1.0 -> ok
- S1e held-out d (value, contract optimum): [(0.7028827511498503, 0.7125063177887642), (0.710451844230539, 0.7370027798270562)] -> NOT MET
- S1f endogenous misrepresentation mass (vs oracle phi): 0.2024976132798002 -> ok
- S1h relay value (trace bound 0.706731): 0.7038040082484892 -> NOT MET
- S1h D11 separation: 0/55296 -> NOT MET

### B1t-invert-value: fail
- S1a calibration excess vs contract target: 0.013583044951118945 -> NOT MET
- S1b tracking rate: 0.5 -> NOT MET
- S1b nuisance change mass: 1.0 -> NOT MET
- S1c directional substitution rate: 0.75 -> NOT MET
- S1d transplant action-change mass: 1.0 -> ok
- S1e held-out d (value, contract optimum): [(0.7028827511498503, 0.7125063177887642), (0.710451844230539, 0.7370027798270562)] -> NOT MET
- S1f endogenous misrepresentation mass (vs oracle phi): 0.2024976132798002 -> ok
- S1h relay value (trace bound 0.706731): 0.7038040082484892 -> NOT MET
- S1h D11 separation: 0/55296 -> NOT MET

### B1t-action-vector: fail
- S1a calibration excess vs contract target: 0.010150031366989496 -> NOT MET
- S1b tracking rate: 0.5 -> NOT MET
- S1b nuisance change mass: 1.0 -> NOT MET
- S1c directional substitution rate: 1.0 -> ok
- S1d transplant action-change mass: 1.0 -> ok
- S1e held-out d (value, contract optimum): [(0.705101017810155, 0.7125063177887642), (0.7177433895924775, 0.7370027798270562)] -> NOT MET
- S1f endogenous misrepresentation mass (vs oracle phi): 0.24499522655960043 -> ok
- S1h relay value (trace bound 0.706731): 0.7067311789387465 -> NOT MET
- S1h D11 separation: 0/55296 -> NOT MET


## E4 Trace-compliant Shea witnesses, k = 40 (marginal-MAP traces; contract-relative targets)

### W5t token-phi (trace-compliant): PASS
- S1a calibration excess vs contract target: 0.0 -> ok
- S1b tracking rate: 1.0 -> ok
- S1b nuisance change mass: 0.0 -> ok
- S1c directional substitution rate: 1.0 -> ok
- S1d transplant action-change mass: 0.5 -> ok
- S1e held-out d (value, contract optimum): [(0.7895296376142192, 0.7895296376142192), (0.7895296376142192, 0.7895296376142192)] -> ok
- S1f endogenous misrepresentation mass (vs oracle phi): 0.03941151376197865 -> ok
- S1h relay value (trace bound 0.763131): 0.7895296376142192 -> ok
- S1h D11 separation: 55296/55296 -> ok

### W1 regime code: fail
- S1a calibration excess vs contract target: 0.055826110762911475 -> NOT MET
- S1b tracking rate: 0.0 -> NOT MET
- S1b nuisance change mass: 0.0 -> ok
- S1c directional substitution rate: 0.5 -> NOT MET
- S1d transplant action-change mass: 0.0 -> NOT MET
- S1e held-out d (value, contract optimum): [(0.7, 0.7895296376142192), (0.7, 0.7895296376142192)] -> NOT MET
- S1f endogenous misrepresentation mass (vs oracle phi): 0.16 -> ok
- S1h relay value (trace bound 0.763131): 0.7 -> NOT MET
- S1h D11 separation: 36864/55296 -> NOT MET

### B1t-accept-value: fail
- S1a calibration excess vs contract target: 0.028647338308162427 -> NOT MET
- S1b tracking rate: 1.0 -> ok
- S1b nuisance change mass: 1.0 -> NOT MET
- S1c directional substitution rate: 0.7499999999999777 -> NOT MET
- S1d transplant action-change mass: 0.5 -> ok
- S1e held-out d (value, contract optimum): [(0.740914255711412, 0.7895296376142192), (0.7521268568126818, 0.7895296376142192)] -> NOT MET
- S1f endogenous misrepresentation mass (vs oracle phi): 0.09970575688098578 -> ok
- S1h relay value (trace bound 0.763131): 0.740914255711412 -> NOT MET
- S1h D11 separation: 0/55296 -> NOT MET

### B1t-invert-value: fail
- S1a calibration excess vs contract target: 0.028647338308162427 -> NOT MET
- S1b tracking rate: 1.0 -> ok
- S1b nuisance change mass: 1.0 -> NOT MET
- S1c directional substitution rate: 0.7500000000000223 -> NOT MET
- S1d transplant action-change mass: 0.5 -> ok
- S1e held-out d (value, contract optimum): [(0.740914255711412, 0.7895296376142192), (0.7521268568126818, 0.7895296376142192)] -> NOT MET
- S1f endogenous misrepresentation mass (vs oracle phi): 0.09970575688099287 -> ok
- S1h relay value (trace bound 0.763131): 0.740914255711412 -> NOT MET
- S1h D11 separation: 0/55296 -> NOT MET

### B1t-action-vector: fail
- S1a calibration excess vs contract target: 0.016202357454833526 -> NOT MET
- S1b tracking rate: 1.0 -> ok
- S1b nuisance change mass: 1.0 -> NOT MET
- S1c directional substitution rate: 1.0 -> ok
- S1d transplant action-change mass: 0.5 -> ok
- S1e held-out d (value, contract optimum): [(0.763131056981738, 0.7895296376142192), (0.7725686733409871, 0.7895296376142192)] -> NOT MET
- S1f endogenous misrepresentation mass (vs oracle phi): 0.03941151376197865 -> ok
- S1h relay value (trace bound 0.763131): 0.763131056981738 -> NOT MET
- S1h D11 separation: 0/55296 -> NOT MET

