# E0-A recorded robustness development batch

Complete package: unchanged adapter 0.4 and runbook 1.1, plus development extension 0.5. No scientific license is issued.

| Arm | Collapses below full reveal | Primary engineering passes | Mean primary joint gap | Controls | Execution failures |
|---|---|---|---|---|---|
| baseline | 0/20 | [100, 101, 102, 103, 104] | 0.0 | 35/35 | 0 |
| R1 | 0/20 | [100, 101, 102, 103, 104] | 0.0 | 35/35 | 0 |
| R2 | 0/20 | [100, 101, 102, 103, 104] | 0.0 | 35/35 | 0 |
| R3 | 0/20 | [100, 101, 102, 103, 104] | 0.0 | 35/35 | 0 |

Frozen selection: **R1**. Development robustness criterion met: **True**.

Selection and reliability assessment use the same five development seeds. No independent success-rate inference follows.

## Historical diagnosis

All 25 historical learned checkpoints and archived reward/encoder trajectories must reproduce. Consumer trajectories below are reconstructed, not present in the original logs.
- Seed 0, rho 0.75: constant boundary at step 10; erased-context action gap first zero at None; final projected update 0.0; raw encoder gradient [-0.2309285083629418, -0.08783145690526643].
- Seed 3, rho 0.5: constant boundary at step 5; erased-context action gap first zero at None; final projected update 0.0; raw encoder gradient [-0.1417361321138388, -0.09691274276140131].
- Seed 4, rho 0.75: constant boundary at step 7; erased-context action gap first zero at None; final projected update 0.0; raw encoder gradient [0.25332382897721484, 0.1957490840531703].

## Reward and nuisance evidence

Every erasure run records atom-level paired reward drops, no-op mass, changed-only contrast, signed fractions, sham and non-target controls. These are additional engineering diagnostics, not silently added protocol gate clauses.
No-op subsets can be empty and remain unavailable. Context mismatch is non-discriminating because the encoder reads C only. The independent non-target scaffold makes selectivity controls easy; they do not establish recurrent or arbitrary-code preservation.
A reward drop is signed; TV is unsigned. They need not coincide even in a one-step task.

## Grid scope

The grid uses a public-optimal consumer slice. Its fractions describe only finite grid points; they are not collapse probabilities under the seeded continuous initialization.

## What remains

Review failure paths and candidate selection; then use a new recorded development batch if justified, or retain a bounded procedural claim. Threshold calibration, a real confirmatory adjudicator, and independent confirmation remain outstanding. Do not license E1 from this batch.
