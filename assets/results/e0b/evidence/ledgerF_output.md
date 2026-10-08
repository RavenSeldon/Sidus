# E0-B Ledger F execution log

## F1 S1e binding-payoff grid (relay value: phi code vs policy-bit W10)

| context | d' | phi code | W10 policy bit | phi advantage |
|---|---|---|---|---|
| oracle | 0.70 | 0.825000 | 0.825000 | +0.000000 |
| oracle | 0.75 | 0.850000 | 0.825000 | +0.025000 |
| oracle | 0.80 | 0.875000 | 0.825000 | +0.050000 |
| oracle | 0.85 | 0.900000 | 0.856500 | +0.043500 |
| oracle | 0.90 | 0.926500 | 0.900000 | +0.026500 |
| k=10 trace | 0.70 | 0.747253 | 0.747253 | +0.000000 |
| k=10 trace | 0.75 | 0.782503 | 0.757503 | +0.025000 |
| k=10 trace | 0.80 | 0.817752 | 0.800000 | +0.017752 |
| k=10 trace | 0.85 | 0.853002 | 0.850000 | +0.003002 |
| k=10 trace | 0.90 | 0.900000 | 0.900000 | +0.000000 |
| k=40 trace | 0.70 | 0.789530 | 0.789530 | +0.000000 |
| k=40 trace | 0.75 | 0.814530 | 0.789530 | +0.025000 |
| k=40 trace | 0.80 | 0.847021 | 0.800000 | +0.047021 |
| k=40 trace | 0.85 | 0.880731 | 0.850000 | +0.030731 |
| k=40 trace | 0.90 | 0.914440 | 0.900000 | +0.014440 |

## F2 Trace-compliant Shea matrix, k = 10, S1e at d' = 0.75 / 0.80

### W5t token-phi (trace-compliant): PASS
- S1a calibration excess (contract target): 0.0 -> ok
- S1b tracking rate: 1.0 -> ok
- S1b nuisance change mass: 0.0 -> ok
- S1c directional substitution rate: 1.0 -> ok
- S1d transplant action-change mass: 1.0 -> ok
- S1e binding d' (value, contract optimum): [(0.75, 0.7825025271155056, 0.7825025271155056), (0.8, 0.8177524007597303, 0.8177524007597303)] -> ok
- S1f endogenous misrepresentation mass: 0.24499522655960043 -> ok
- S1h relay value vs trace bound: (0.7165030325386068, 0.7067311789387465) -> ok
- S1h D11 separation: 55296/55296 -> ok

### W10 policy bit act(phi) at d=0.55: fail
- S1a calibration excess (contract target): 0.004760232460000705 -> NOT MET
- S1b tracking rate: 0.4549974728844943 -> NOT MET
- S1b nuisance change mass: 0.0 -> ok
- S1c directional substitution rate: 1.0 -> ok
- S1d transplant action-change mass: 1.0 -> ok
- S1e binding d' (value, contract optimum): [(0.75, 0.7575025271155057, 0.7825025271155056), (0.8, 0.8, 0.8177524007597303)] -> NOT MET
- S1f endogenous misrepresentation mass: 0.24499522655960043 -> ok
- S1h relay value vs trace bound: (0.7165030325386068, 0.7067311789387465) -> ok
- S1h D11 separation: 55296/55296 -> ok

### W1 regime code: fail
- S1a calibration excess (contract target): 0.018460699939896994 -> NOT MET
- S1b tracking rate: 0.0 -> NOT MET
- S1b nuisance change mass: 0.0 -> ok
- S1c directional substitution rate: 0.5 -> NOT MET
- S1d transplant action-change mass: 0.0 -> NOT MET
- S1e binding d' (value, contract optimum): [(0.75, 0.75, 0.7825025271155056), (0.8, 0.8, 0.8177524007597303)] -> NOT MET
- S1f endogenous misrepresentation mass: 0.16 -> ok
- S1h relay value vs trace bound: (0.7, 0.7067311789387465) -> NOT MET
- S1h D11 separation: 36864/55296 -> NOT MET

### B1t-accept-value: fail
- S1a calibration excess (contract target): 0.013583044951118945 -> NOT MET
- S1b tracking rate: 0.5 -> NOT MET
- S1b nuisance change mass: 1.0 -> NOT MET
- S1c directional substitution rate: 0.75 -> NOT MET
- S1d transplant action-change mass: 1.0 -> ok
- S1e binding d' (value, contract optimum): [(0.75, 0.7569355204324634, 0.7825025271155056), (0.8, 0.8028435283235875, 0.8177524007597303)] -> NOT MET
- S1f endogenous misrepresentation mass: 0.2024976132798002 -> ok
- S1h relay value vs trace bound: (0.7038040082484892, 0.7067311789387465) -> NOT MET
- S1h D11 separation: 0/55296 -> NOT MET

### B1t-invert-value: fail
- S1a calibration excess (contract target): 0.013583044951118945 -> NOT MET
- S1b tracking rate: 0.5 -> NOT MET
- S1b nuisance change mass: 1.0 -> NOT MET
- S1c directional substitution rate: 0.75 -> NOT MET
- S1d transplant action-change mass: 1.0 -> ok
- S1e binding d' (value, contract optimum): [(0.75, 0.7569355204324634, 0.7825025271155056), (0.8, 0.8028435283235875, 0.8177524007597303)] -> NOT MET
- S1f endogenous misrepresentation mass: 0.2024976132798002 -> ok
- S1h relay value vs trace bound: (0.7038040082484892, 0.7067311789387465) -> NOT MET
- S1h D11 separation: 0/55296 -> NOT MET

### B1t-action-vector: fail
- S1a calibration excess (contract target): 0.010150031366989496 -> NOT MET
- S1b tracking rate: 0.5 -> NOT MET
- S1b nuisance change mass: 1.0 -> NOT MET
- S1c directional substitution rate: 1.0 -> ok
- S1d transplant action-change mass: 1.0 -> ok
- S1e binding d' (value, contract optimum): [(0.75, 0.7620845018544313, 0.7825025271155056), (0.8, 0.8052315884861934, 0.8177524007597303)] -> NOT MET
- S1f endogenous misrepresentation mass: 0.24499522655960043 -> ok
- S1h relay value vs trace bound: (0.7067311789387465, 0.7067311789387465) -> NOT MET
- S1h D11 separation: 0/55296 -> NOT MET


## F2 Trace-compliant Shea matrix, k = 40, S1e at d' = 0.75 / 0.80

### W5t token-phi (trace-compliant): PASS
- S1a calibration excess (contract target): 0.0 -> ok
- S1b tracking rate: 1.0 -> ok
- S1b nuisance change mass: 0.0 -> ok
- S1c directional substitution rate: 1.0 -> ok
- S1d transplant action-change mass: 0.5 -> ok
- S1e binding d' (value, contract optimum): [(0.75, 0.8145296376142193, 0.8145296376142193), (0.8, 0.8470212622934034, 0.8470212622934034)] -> ok
- S1f endogenous misrepresentation mass: 0.03941151376197865 -> ok
- S1h relay value vs trace bound: (0.7895296376142192, 0.763131056981738) -> ok
- S1h D11 separation: 55296/55296 -> ok

### W10 policy bit act(phi) at d=0.55: fail
- S1a calibration excess (contract target): 0.011775377907680351 -> NOT MET
- S1b tracking rate: 0.42418814495431234 -> NOT MET
- S1b nuisance change mass: 0.0 -> ok
- S1c directional substitution rate: 1.0 -> ok
- S1d transplant action-change mass: 0.5 -> ok
- S1e binding d' (value, contract optimum): [(0.75, 0.7895296376142192, 0.8145296376142193), (0.8, 0.8, 0.8470212622934034)] -> NOT MET
- S1f endogenous misrepresentation mass: 0.03941151376197865 -> ok
- S1h relay value vs trace bound: (0.7895296376142192, 0.763131056981738) -> ok
- S1h D11 separation: 55296/55296 -> ok

### W1 regime code: fail
- S1a calibration excess (contract target): 0.055826110762911475 -> NOT MET
- S1b tracking rate: 0.0 -> NOT MET
- S1b nuisance change mass: 0.0 -> ok
- S1c directional substitution rate: 0.5 -> NOT MET
- S1d transplant action-change mass: 0.0 -> NOT MET
- S1e binding d' (value, contract optimum): [(0.75, 0.75, 0.8145296376142193), (0.8, 0.8, 0.8470212622934034)] -> NOT MET
- S1f endogenous misrepresentation mass: 0.16 -> ok
- S1h relay value vs trace bound: (0.7, 0.763131056981738) -> NOT MET
- S1h D11 separation: 36864/55296 -> NOT MET

### B1t-accept-value: fail
- S1a calibration excess (contract target): 0.028647338308162427 -> NOT MET
- S1b tracking rate: 1.0 -> ok
- S1b nuisance change mass: 1.0 -> NOT MET
- S1c directional substitution rate: 0.7499999999999777 -> NOT MET
- S1d transplant action-change mass: 0.5 -> ok
- S1e binding d' (value, contract optimum): [(0.75, 0.7835330671256633, 0.8145296376142193), (0.8, 0.8114882485678139, 0.8470212622934034)] -> NOT MET
- S1f endogenous misrepresentation mass: 0.09970575688098578 -> ok
- S1h relay value vs trace bound: (0.740914255711412, 0.763131056981738) -> NOT MET
- S1h D11 separation: 0/55296 -> NOT MET

### B1t-invert-value: fail
- S1a calibration excess (contract target): 0.028647338308162427 -> NOT MET
- S1b tracking rate: 1.0 -> ok
- S1b nuisance change mass: 1.0 -> NOT MET
- S1c directional substitution rate: 0.7500000000000223 -> NOT MET
- S1d transplant action-change mass: 0.5 -> ok
- S1e binding d' (value, contract optimum): [(0.75, 0.7835330671256633, 0.8145296376142193), (0.8, 0.8114882485678139, 0.8470212622934034)] -> NOT MET
- S1f endogenous misrepresentation mass: 0.09970575688099287 -> ok
- S1h relay value vs trace bound: (0.740914255711412, 0.763131056981738) -> NOT MET
- S1h D11 separation: 0/55296 -> NOT MET

### B1t-action-vector: fail
- S1a calibration excess (contract target): 0.016202357454833526 -> NOT MET
- S1b tracking rate: 1.0 -> ok
- S1b nuisance change mass: 1.0 -> NOT MET
- S1c directional substitution rate: 1.0 -> ok
- S1d transplant action-change mass: 0.5 -> ok
- S1e binding d' (value, contract optimum): [(0.75, 0.7964762828632274, 0.8145296376142193), (0.8, 0.8201696848826442, 0.8470212622934034)] -> NOT MET
- S1f endogenous misrepresentation mass: 0.03941151376197865 -> ok
- S1h relay value vs trace bound: (0.763131056981738, 0.763131056981738) -> NOT MET
- S1h D11 separation: 0/55296 -> NOT MET

## F3 Process P1c specificity arm (k = 5; matched anchor f(00), matched reliability, different f(11))

| witness | eligible ordered pairs | specificity |
|---|---|---|
| W1 regime code (theta-coupled) | 8 | +0.000000 |
| W2 input parity (fixed) | 8 | +0.000000 |
| W3 process model (truth table) | 8 | +0.192356 |
| W5 token-phi monitor | 8 | +0.035285 |
| W6a per-cell tracker | 8 | +0.183155 |
| W6b identity classifier | 8 | +0.101957 |
| W7 bundle W1+W3+W5 | 8 | +0.192356 |
| B1-scalar reliability q_T | 8 | +0.000000 |
