# Confirmatory statistical plan — draft

The experimental unit is a seed, containing its entire registered sweep and eight controls. Conditions within a seed are not independent trials. Inference assumes the declared hash-derived PRNG initializations behave as independent draws across seeds; hashing and repeatability do not prove this assumption. The simulator is enumerated exactly within each frozen system, subject to stated numerical tolerance. It is not a sampled-data generalization experiment.

## Decisions

1. Recompute every outcome from verified checkpoint bytes, and replay the recorded R1 training. Reject a mismatched source, configuration, inventory or cache. Cached pass strings cannot grant acceptance.
2. Evaluate A1–A3 at the primary condition and A4 using that seed's own five-level sweep. Full-reveal A3 remains unavailable by design; it is not required to pass.
3. Preserve the all-registered-seed gate guard. Any valid failed required seed clause/control fails the corresponding finite-replication requirement. Missing/invalid evidence remains inconclusive unless another valid required failure is established. This is stricter than merely permitting a few failures under a population reliability target.
4. Additionally require a joint full-protocol success probability of at least .95, using an exact Clopper–Pearson interval. The interval is computed over seed-level joint outcomes; it cannot turn a failed finite-replication guard into a pass.
5. Additionally require simultaneous A4 population-mean lower bounds above the respective minimum declines. The three quantities are not substituted for one another.

## Family error allocation

Total alpha=.05. Allocate .025 to a two-sided exact binomial interval, and .025/3 to each of three two-sided Hoeffding mean intervals. The four intervals jointly cover with probability at least .95 under their assumptions by the union bound; independence between the four statistics is unnecessary. Each two-sided interval divides its allocation across two tails. This explains why its reliability bound differs from a standalone one-sided .05 calculation.

Pass an interval criterion when its lower endpoint reaches the threshold; fail when its upper endpoint is below the threshold; otherwise report inconclusive. Measurement comparisons additionally retain their numerical enclosure. Malformed inputs and observations outside a justified bound do not produce passing intervals.

## Justified A4 ranges

- Incremental-information decline is in [0,1]: at rho=1 C is completely public, and rho=0 has at most one bit.
- Class-benefit decline is in [0,.5]: no class benefit remains at full reveal; public Bayes reward at rho=0 is .5.
- Observed-benefit decline is in [−1.5,1.5]: at rho=0 any I-only comparator scores .5, so B_obs lies in [−.5,.5]; at full reveal the difference between two stochastic consumer rewards is in [−1,1]. Subtracting gives the stated range. This bound does not assume either trained consumer is optimal.

For range width W, the two-sided Hoeffding radius is W sqrt(log(2/alpha)/(2n)). The widest, observed-benefit bound dominates the current ideal sample-size calculation. With ideal mean decline .5 and threshold .25, at least 395 seeds are needed for its lower bound to exceed the threshold under this allocation. The draft contains 500 reserved confirmation seeds (10000–10499), none executed. This is a prospective ideal calculation, not guaranteed statistical power; the all-seed guard may fail, and non-ideal outcomes may be inconclusive. Goal 4 must review and freeze this plan before execution.

## Trust and chronology

A scientific license requires a frozen config, a receipt binding config and source, and an independently supplied trusted digest of that receipt. The supported runner writes an exclusive start record before training. The adjudicator verifies binding and temporal order, in addition to replaying all outcomes. A digest supplied by the same outcome bundle is not treated as independent trust. Local timestamps are not independently authenticated and cannot defeat deliberate external fabrication. Archive the trusted freeze record outside the outcome directory before the run.

Rehearsal results can exercise numerical decisions but never license E0-A or E1. E0-B always remains separate. No freeze receipt or scientific confirmation is created in Goals 1–3.
