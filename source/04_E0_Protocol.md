# Sīdus: Towards Metarepresentational Ecology
## IV. E0 Construct-Validity Protocol
### Two-stage mock-up for validating internal-state monitoring before testing strict metarepresentation

**Working methods companion - August 2026**  
**Status:** pre-experimental protocol. E0-A is specified strongly enough to guide implementation. E0-B is deliberately provisional and should be refined against the metarepresentation literature before confirmatory use.

> **Purpose:** establish construct validity before introducing shared bottlenecks, multi-source competition, causal-topology claims, recursive allocator monitoring, or any ecology-level inference.

---

## 0. Scope and decision rule

E0 is split into two independent stages because **internal-state monitoring is not automatically metarepresentation**.


a) **E0-A - Monitoring substrate validity** asks whether a private internal state is genuinely hidden, incrementally represented, and causally used.

b) **E0-B - Metarepresentational discrimination** asks whether a candidate higher-order signal represents a property or process of a first-order representation rather than merely tracking an internal state, public context, or another feedforward transformation.

The stages license different claims:

| Stage passed | Claim licensed | Claim not licensed |
|---|---|---|
| E0-A | a causally used internal-state monitoring channel exists | the signal is a strict metarepresentation |
| E0-B | the tested architecture satisfies the selected operational criterion for property/process metarepresentation | metarepresentation is a natural kind, domain-general, conscious, or ecologically organized |

**E1 scarcity requires E0-A.** Strict-metarepresentation experiments require E0-B. The broader programme should not infer metarepresentational ecology from E0-A alone.

**Units.** All rates, entropies and information quantities in this protocol are in **bits** (\(\log_2\)), per the standing conventions of Document I, §11A. Any implementation quantity produced in nats is converted at the point of reporting, not at the point of reading.

---

# PART I - E0-A: MONITORING SUBSTRATE VALIDITY

## 1. Core architecture

Let the coordinator have ordinary public information

\[
\mathcal I_t = \{o_{\le t}, a_{<t}, h^{U}_{t-1}\},
\]

where \(o_{\le t}\) is observation history, \(a_{<t}\) is action history, and \(h^{U}_{t-1}\) is the coordinator's recurrent state before the special monitoring message arrives.

A specialist process has a private internal state

\[
C_{v,t}\in\mathcal C_v.
\]

A source-specific encoder produces an internal-state message

\[
S_{v,t}=E_v(C_{v,t},\mathcal I_t).
\]

The coordinator/consumer \(U\) receives \(S_{v,t}\) in addition to \(\mathcal I_t\).

The intended causal chain is:

\[
\mathcal I_t \quad\Vert\quad C_{v,t} \rightarrow S_{v,t} \rightarrow U.
\]

E0-A asks three distinct questions:

\[
\boxed{\text{hiddenness} \neq \text{informativeness} \neq \text{causal use}.}
\]

---

## 2. Gate A1 - Residual hiddenness and potential value

### 2.1 Residual hiddenness

Define residual uncertainty:

\[
u_v=
\frac{H(C_{v,t}\mid\mathcal I_t)}{H(C_{v,t})},
\qquad H(C_{v,t})>0.
\]

The purpose is not to require independence between \(C_v\) and public history. It is to verify that a non-trivial informational problem remains after ordinary public information is used.

### 2.2 Practical estimator

The true conditional entropy is generally unavailable. Fit a calibrated held-out predictor \(\hat p_0(c\mid\mathcal I_t)\) and estimate predictive cross-entropy:

\[
\widehat{CE}_0
=
\mathbb E_{\mathrm{test}}
[-\log_2 \hat p_0(C_{v,t}\mid\mathcal I_t)].
\]

Because held-out cross-entropy upper-bounds the true conditional entropy by the predictor's approximation error, it should be treated as an **estimator/proxy**, not as exact entropy unless the decoder is demonstrably close to Bayes-optimal.

### 2.3 Direct-read headroom

Residual hiddenness alone is insufficient. Give the coordinator direct access to \(C_{v,t}\) in an oracle condition and measure the gain over public information alone:

\[
\Delta J_{\mathrm{oracle},v}
=
J(\mathcal I_t,C_{v,t})-J(\mathcal I_t).
\]

A source can be hidden yet irrelevant. E0-A therefore requires both:

\[
H(C_v\mid\mathcal I)>0
\]

and a preregistered minimally meaningful oracle benefit.

### 2.4 Gate A1

Pass only if:

1. residual hiddenness is reliably non-zero under the intended high-privacy condition;
2. the direct-read oracle shows that information about \(C_v\) can matter to the task;
3. public shortcut performance is quantified, not assumed absent.

**Thresholds such as \(u_v\ge0.25\) should not be fixed by aesthetics.** Calibrate pilot thresholds from task headroom and freeze them before confirmatory runs.

---

## 3. Gate A2 - Incremental transmission

### 3.1 Target quantity

Define the incremental information delivered by the monitoring message:

\[
m_v
=
I(C_{v,t};S_{v,t}\mid\mathcal I_t).
\]

Equivalently,

\[
m_v
=
H(C_{v,t}\mid\mathcal I_t)
-
H(C_{v,t}\mid\mathcal I_t,S_{v,t}).
\]

### 3.2 Practical log-loss estimator

Fit two matched auxiliary predictors on held-out data:

\[
\hat p_0(c\mid\mathcal I_t),
\qquad
\hat p_1(c\mid\mathcal I_t,S_{v,t}).
\]

Then estimate:

\[
\hat m_v
=
\widehat{CE}_0-
\widehat{CE}_1.
\]

This is an empirical conditional-information estimate under the chosen decoder class. Report cross-validation uncertainty and calibration diagnostics.

### 3.3 Rate spent

For a variational channel,

\[
r_v=
\mathbb E
\left[
D_{KL}
\left(
q(S_v\mid C_v,\mathcal I)
\Vert
p(S_v\mid\mathcal I)
\right)
\right].
\]

Under the intended variational construction,

\[
I(C_v;S_v\mid\mathcal I)\le r_v,
\]

but finite-sample estimates need not obey the inequality exactly.

The central distinction remains:

\[
\boxed{r_v\neq m_v.}
\]

A channel may consume rate while adding little useful information.


### 3.3a Decomposition of the rate--information gap

**[R2 · correction, August 2026 review pass]**

The inequality \(m_v\le r_v\) was previously asserted as a property of "the
intended variational construction." It is in fact an identity plus a
non-negative term, and writing it out converts a qualitative diagnostic into
two estimable numbers.

For any \(q\) and \(p\),

\[
\begin{aligned}
\mathbb E_q\!\left[D_{KL}\!\left(q(S_v\mid C_v,\mathcal I)\,\Vert\,p(S_v\mid\mathcal I)\right)\right]
&=\underbrace{I(C_v;S_v\mid\mathcal I)}_{m_v}\\[0.5em]
&\quad+\underbrace{\mathbb E_{\mathcal I}\,D_{KL}\!\left(q(S_v\mid\mathcal I)\,\Vert\,p(S_v\mid\mathcal I)\right)}_{\Delta_v^{\mathrm{prior}}\;\ge\;0}.
\end{aligned}
\]

So

\[
\boxed{\,r_v=m_v+\Delta_v^{\mathrm{prior}},\qquad
\Delta_v^{\mathrm{prior}}:=\mathbb E_{\mathcal I}\,D_{KL}\!\left(q(S_v\mid\mathcal I)\,\Vert\,p(S_v\mid\mathcal I)\right)\ge0.\,}
\]

**[Revised after release-candidate review.]** The mismatch term is an expectation
over \(\mathcal I\), not a bare divergence. \(D_{KL}(q(S_v\mid\mathcal I)\Vert
p(S_v\mid\mathcal I))\) is a function of the random variable \(\mathcal I\);
only its expectation is the scalar that completes the identity. Because this is
stated as an identity it has to be exact, and an implementation that omits the
average would compute a per-timestep quantity and mis-report it.

Three things follow.

1. **\(r_v\ge m_v\) is robust, not an assumption.** It holds for any prior,
   learned or fixed. Finite-sample estimates may still violate it; the
   population statement does not depend on the encoder having been trained well.
2. **The Gate A4 signature decomposes exactly.** The pattern
   \(m_v\approx0,\;r_v>0\) — recorded there as "possible redundant coding,
   inefficient optimization, or target-metric mismatch" — separates cleanly:
   the rate is spent on \(\Delta_v^{\mathrm{prior}}\), i.e. mismatch between the
   aggregate posterior \(q(S_v\mid\mathcal I)\) and the prior, rather than on
   information about \(C_v\). Estimate \(\Delta_v^{\mathrm{prior}}\) directly and
   report it; do not infer it by subtraction alone.
3. **It answers the "soft penalty with extra steps" objection.** With a *learned*
   prior fitted to the aggregate posterior, \(\Delta_v^{\mathrm{prior}}\)
   shrinks and the variational surrogate tightens toward the true conditional
   information. The surrogate's looseness is therefore a measurable quantity
   rather than an unknown, which is what licenses using it as a rate meter at
   all. It does **not**, on its own, establish that a trained run satisfies the
   shared constraint — see Arm S's realised-violation feasibility diagnostic in
   Document II, §10. The alphabet arm there is optional currency-sensitivity work,
   not a requirement for E1.

### 3.4 Gate A2

Pass only if, under a non-binding communication condition:

1. \(\hat m_v\) is meaningfully above zero with uncertainty reported;
2. \(r_v>0\) and the encoder has not collapsed;
3. performance approaches the direct-read ceiling enough to show that the channel can solve the intended information problem.

---

## 4. Gate A3 - Selective causal use

Decodability is not use.

### 4.1 On-support counterfactual scrambling

Replace the actual message with a valid message associated with an alternative reachable controller state:

\[
S_{v,t}
\leftarrow
S'_{v,t}
\sim
q(S_v\mid C'_{v,t},\mathcal I_t),
\qquad
C'_{v,t}\neq C_{v,t}.
\]

The intervention should remain near trained support. Avoid arbitrary zeroing unless zero is itself a trained message state.

### 4.2 Primary outcome

Measure the **proximal decision or policy variable** predicted to depend on \(C_v\), not only total episode return.

Examples:

\[
\Delta \pi_v,
\qquad
\Delta P(a_t\mid\cdot),
\qquad
\Delta J_v.
\]

Total return \(J\) is secondary when downstream compensation could mask a genuine local causal effect.

### 4.3 Non-target preservation

At the intervention time or within a preregistered proximal window, verify that non-target quantities remain approximately intact:

\[
C_u,
\quad
S_u,
\quad
m_u,
\qquad u\neq v.
\]

Later downstream changes caused by the intervention are legitimate causal consequences and should not be misclassified as intervention leakage.

### 4.4 Gate A3

Pass only if:

1. the on-support message intervention causes the predicted local downstream change;
2. the effect exceeds a preregistered minimally meaningful threshold, not merely a significance threshold;
3. first-order/private target execution is preserved at intervention time;
4. non-target channels are preserved over the specified proximal window.

---

## 5. Gate A4 - Shortcut sensitivity

E0-A should demonstrate that the special monitoring channel is valuable **because information is missing**, not merely because the architecture has learned to use an arbitrary extra input.

Construct legitimate environment conditions that vary the public inferability of \(C_v\):

\[
H(C_v\mid\mathcal I)_{\mathrm{high\ privacy}}
>
H(C_v\mid\mathcal I)_{\mathrm{low\ privacy}}.
\]

As public observability increases, predict:

\[
H(C_v\mid\mathcal I)\downarrow
\Rightarrow
m_v\downarrow
\]

and

\[
\text{causal benefit}(S_v)\downarrow.
\]

Do **not** require \(r_v\to0\) in the absence of a channel cost. Redundant coding can persist even when incremental information vanishes.

If an explicit message cost is imposed, then efficient learning additionally predicts:

\[
r_v\downarrow.
\]

The pattern

\[
m_v\approx0,\qquad r_v>0
\]

should be recorded as possible redundant coding, inefficient optimization, or target-metric mismatch rather than defined away.

### Gate A4

Pass only if the informational and causal value of \(S_v\) changes in the predicted direction as public observability is manipulated within the task distribution. **[Second external review pass.]** The manipulation check is a confirmatory test, not an impression of direction: decline thresholds — including any ratio-of-decline criterion — are preregistered before confirmatory runs, and the comparison is made with reported confidence intervals on \(\hat m_v\) and on the causal-benefit estimate, never with bare ratios of point estimates.

---


## 5A. Non-gating diagnostic - cross-source leakage must be measured conditionally

**[R3 · correction, August 2026 review pass — preventive]**

No cross-source independence check appears in the protocol above. Earlier
working sketches used an unconditional mutual information
\(I(S_u;S_v)\) as a "cheating" diagnostic, and any future implementation is
likely to reach for the same quantity. It is the wrong one, and the error is
silent.

Sources that share public context will exhibit \(I(S_u;S_v)>0\) **legitimately**,
because both messages are conditioned on \(\mathcal I_t\). An unconditional test
therefore flags correct architectures as leaking. The right quantity conditions
on the public information the consumer already holds:

\[
I(S_u;S_v\mid\mathcal I_t),
\]

and for \(K>2\) sources, the total correlation given \(\mathcal I\):

\[
TC(S_1,\dots,S_K\mid\mathcal I)
=
\sum_{v}H(S_v\mid\mathcal I)-H(S_1,\dots,S_K\mid\mathcal I).
\]

Non-zero conditional dependence is still not automatically a fault: encoders may
legitimately coordinate under a shared budget.

**[Revised after release-candidate review.]** An earlier version named the fault
condition as \(I(C_u;S_v\mid\mathcal I)>0\). That is still too strong. If the
sources are conditionally dependent,

\[
C_u\not\perp C_v\mid\mathcal I,
\]

then \(C_u\rightarrow C_v\rightarrow S_v\) forms a chain given \(\mathcal I\), so
\(S_v\) carries information about \(C_u\) **indirectly and legitimately**, even
though encoder \(v\) never saw \(C_u\). By data processing,
\(I(C_u;S_v\mid\mathcal I)\le I(C_u;C_v\mid\mathcal I)\), which is positive
whenever the sources are dependent. Flagging that as leakage would condemn a
correct architecture.

The diagnostic that isolates unauthorised access conditions on the source the
encoder is entitled to see:

\[
\boxed{\,I(C_u;S_v\mid C_v,\mathcal I),\qquad u\neq v.\,}
\]

Under the intended factorised architecture \(S_v\sim q_v(S_v\mid C_v,\mathcal I)\),
this quantity vanishes exactly, absent shared private randomness or another
forbidden path. Non-zero values indicate that encoder \(v\) has access it should
not have --- which is the quantity that would break the per-source attribution on
which Gate A3, Gate A4 and hypothesis H3 all depend.

Report \(I(C_u;C_v\mid\mathcal I)\) alongside it. Source dependence sets how much
legitimate cross-decodability to expect, and without it the conditional test has
no reference scale.

Finally, prefer architecture to inference. The access restriction should be
**enforced in code** --- encoder \(v\) is wired to receive only \(C_v\) and
\(\mathcal I\) --- and these information quantities used as **manipulation checks
on that wiring**, not as a method for inferring architecture from mutual
information alone.

## 6. E0-A pass/fail rule

E0-A licenses E1 scarcity only when all four gates pass across independent seeds. The cross-source leakage diagnostic in §5A is recommended and reportable when relevant, but it does **not** constitute a fifth gate:

| Gate | Required evidence |
|---|---|
| **A1 - Residual hiddenness + headroom** | public information leaves non-trivial uncertainty and direct-read information can improve relevant behavior |
| **A2 - Incremental transmission** | non-binding channel transmits additional target information and avoids collapse |
| **A3 - Selective causal use** | on-support message intervention produces the predicted local downstream effect with proximal non-target preservation |
| **A4 - Shortcut sensitivity** | increasing legitimate public observability reduces incremental message information and its causal value |

If a gate fails, do not proceed to multi-source scarcity as if the construct were intact. Re-engineer the task, simplify the channel, or revise the claim.

---

# PART II - E0-B: PROVISIONAL METAREPRESENTATIONAL DISCRIMINATION

## 7. Scope of E0-B

E0-B is deliberately less mature than E0-A.

Its purpose is not to settle the philosophy of metarepresentation. It asks whether a synthetic experiment can distinguish a candidate **property/process metarepresentation** from simpler alternatives under explicitly stated operational criteria.

**[Second external review pass — design commitment executed.]** E0-B is not run under a single chosen definition. The three criteria of Document I §2.3 disagree in principle, so the protocol is **definition-indexed**:

\[
E0\text{-}B^{\mathrm{Shea}}, \qquad E0\text{-}B^{\mathrm{RR}}, \qquad E0\text{-}B^{\mathrm{Process}},
\]

run over the same architectures, preregistered manipulations and evidence tiers. A system may satisfy one operationalization and fail another. That outcome is not experimental failure. If the criteria repeatedly carve systems differently, the warranted conclusion is that **"metarepresentation" does not yet behave as one empirically unified construct**, and the programme should then speak specifically of representational-property monitoring, process representation, or representational redescription — whichever actually survived — rather than of metarepresentation simpliciter.

E0-B should be refined against Proust, Shea, Cleeremans/SOMA, and process-metarepresentation work before confirmatory use.

---

## 8. Minimal architecture

Let an external latent state \(X_t\) generate observation \(O_t\). A first-order system produces:

\[
R_t=F_{\eta_t}(O_t),
\]

where \(\eta_t\) controls a hidden property of the representational process, for example:

- noise/reliability regime;
- systematic bias;
- source type;
- gain/transformation rule;
- mapping family.

Construct at least three comparison systems:

### B0 - First-order/public shortcut

Predicts the task target or \(\eta_t\) from public context, observation, or ordinary downstream activity without an explicit model of a representational property/process.

### B1 - Internal-state monitor

Represents a private controller/process state \(C_t\), but is not required to represent a property of \(R_t\) or the process \(F_{\eta_t}\).

### B2 - Candidate property/process metarepresentation

Produces a state \(M_t\) whose task-relevant target is explicitly:

\[
\phi(R_t)
\]

or

\[
\eta_t,
\]

where \(\phi(R_t)\) may be reliability, source, correctness probability, or another preregistered representational property.

---

## 9. Minimum discriminators

E0-B should not pass merely because \(M_t\) decodes \(\eta_t\).

At minimum, the design should include matched conditions that:

1. hold external target \(X_t\) fixed while \(\eta_t\) changes;
2. hold first-order choice/output fixed while reliability/source/process regime changes where feasible;
3. include cases in which \(M_t\) can misrepresent its target;
4. compare against a public-context shortcut with matched capacity;
5. perturb the target property/process and test whether \(M_t\) changes as predicted;
6. perturb \(M_t\) while preserving the first-order representation and test whether its intended consumer changes appropriately.

A provisional evidence hierarchy is:

\[
\begin{array}{c}
\text{decodable}\;<\;\text{conditionally specific}\;<\;\text{misrepresentable}\\[3pt]
<\;\text{target-dependent}\;<\;\text{causally used}.
\end{array}
\]

---

## 10. Provisional E0-B pass criterion

E0-B passes **for the selected operational definition only** if the candidate B2 architecture:

1. carries held-out information about the preregistered representational property/process after public and first-order shortcut predictors are controlled;
2. can dissociate from the first-order output and can misrepresent its meta-target;
3. responds selectively to intervention on the target representational property/process;
4. causally affects the intended downstream consumer when manipulated while first-order representation is preserved;
5. outperforms simpler B0/B1 explanations under held-out interventions, not merely under in-distribution decoding.

Outcomes are reported **per definition-index** as a vector of pass/fail results across the three operationalizations, not collapsed into a single verdict; a split outcome is a substantive finding about the construct, per §7.

If these conditions cannot be met under any index, the programme should not use the phrase **strict metarepresentation** for that system.

E0-B does **not** establish that this operationalization exhausts the concept of metarepresentation.

---

# PART III - ASSUMPTIONS AND LIMITATIONS

## 11. Assumptions

1. **Ground truth is available by construction.** The synthetic environment gives the experimenter access to \(C_t\), \(R_t\), \(\eta_t\), and intervention targets that biological work would not provide directly.
2. **Candidate variables are supplied by the experimenter.** E0 tests representation and use of known targets; it does not test spontaneous discovery of an internal ontology.
3. **Auxiliary decoders are adequate enough to support conditional-information estimates.** Their limitations must be measured through held-out calibration and capacity checks.
4. **On-support interventions can be designed without destroying unrelated computations.** This must be empirically verified rather than assumed.
5. **Task value is a legitimate local criterion.** Causal use is defined relative to the tested task and consumer; absence of use in one task does not prove universal absence of function.
6. **Representational properties/processes are operationally specified before data inspection.** E0-B cannot infer a meta-target after the fact from whichever latent dimension decodes best.

---

## 12. Limitations

### 12.1 E0-A validates monitoring, not metarepresentation

A perfectly successful E0-A system may still be only a sophisticated internal telemetry channel.

### 12.2 E0-B is definition-relative

Metarepresentation is contested. E0-B can validate one operational criterion against specified alternatives; it cannot settle all philosophical or cognitive-scientific definitions.

### 12.3 Conditional-information estimation is model-dependent

Cross-validated log-loss differences approximate conditional information only relative to the decoder class and data regime. Poor auxiliary predictors can create misleading residual uncertainty or information estimates.

### 12.4 Synthetic modularity is an experimental scaffold

Clean private states, encoders, and intervention points are engineered conveniences. They should not be read as claims about anatomical modules or a literal neural information seam.

### 12.5 Causal use is consumer-relative

A message may be unused by the tested coordinator yet useful elsewhere. E0 establishes only the causal relation explicitly tested.

### 12.6 Redundant coding is possible

\(m_v\to0\) does not imply \(r_v\to0\). Efficient rate reduction requires an actual cost or opportunity pressure.

### 12.7 Local validity does not establish ecology

Even successful E0-A and E0-B experiments validate only local constructs. Ecology-level claims require reproducible interactions among multiple independently validated systems across tasks or architectures.

---

## 13. Pipeline after E0

\[
\boxed{
\begin{array}{c}
\text{E0-A: monitoring substrate valid}
\\[4pt]
\Downarrow
\\[4pt]
\text{E1: multi-source scarcity / competition}
\end{array}}
\]

and separately:

\[
\boxed{
\begin{array}{c}
\text{E0-B: strict-meta discriminator valid}
\\[4pt]
\Downarrow
\\[4pt]
\text{E2: metarepresentation under scarcity}
\end{array}}
\]

Passing E0-A does not imply E0-B. Passing either does not imply ecology.

---

> **E0 exists to prevent later sophistication from compensating for a bad construct. If the substrate cannot survive these tests, stop before building the ecology around it.**


---

## References

1. Proust, J. (2003). Does metacognition necessarily involve metarepresentation? *Behavioral and Brain Sciences, 26*(3), 352. https://doi.org/10.1017/S0140525X0336008X
2. Shea, N. (2014). Reward prediction error signals are meta-representational. *Noûs, 48*(2), 314-341. https://doi.org/10.1111/j.1468-0068.2012.00863.x
3. Cleeremans, A. (2011). The Radical Plasticity Thesis: How the brain learns to be conscious. *Frontiers in Psychology, 2*, 86. https://doi.org/10.3389/fpsyg.2011.00086
4. Cleeremans, A., et al. (2020). Learning to be conscious. *Trends in Cognitive Sciences, 24*(2), 112-123. https://doi.org/10.1016/j.tics.2019.11.011
5. Cleeremans, A., Timmermans, B., & Pasquali, A. (2007). Consciousness and metarepresentation: A computational sketch. *Neural Networks, 20*, 1032-1039. PMID: 17904799.
6. Kanai, R., Takatsuki, R., & Fujisawa, I. (2025). Meta-representations as representations of processes. *Neuroscience of Consciousness, 2025*(1), niaf038. https://doi.org/10.1093/nc/niaf038
