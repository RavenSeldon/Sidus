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

### 2.2 Exact reference and practical estimator

**Exact reference first.** The initial E0-A simulator must permit exact enumeration or exact filtering of the joint distribution, including the coordinator's pre-message information state. Observing realized ground-truth states does not by itself make their conditional distributions tractable. Compute \(H(C_v\mid\mathcal I)\) and the Bayes public-only/direct-read task values exactly in this reference environment. These quantities anchor A1; gains over a bounded public-only consumer are reported separately as computational accessibility, not evidence of hidden information.

For later environments where exact conditionals are unavailable, validate the measurement procedure against the exact reference before using it to support gates. Fit a calibrated held-out predictor \(\hat p_0(c\mid\mathcal I_t)\) and estimate predictive cross-entropy:

\[
\widehat{CE}_0
=
\mathbb E_{\mathrm{test}}
[-\log_2 \hat p_0(C_{v,t}\mid\mathcal I_t)].
\]

Population cross-entropy equals conditional entropy plus non-negative decoder approximation error; a finite held-out average is itself uncertain. Positive cross-entropy therefore supplies no lower bound proving hiddenness. Report approximation and sampling error separately. If these cannot be bounded adequately for the gate decision, report **inconclusive** rather than pass.

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

**Thresholds such as \(u_v\ge0.25\) should not be fixed by aesthetics.** First validate the estimators and complete gate evaluator against exact ground truth, including negative controls; only then calibrate pilot thresholds from task headroom and freeze them before independent confirmatory runs. A pilot with an inadequate decoder can bake its bias into the threshold; freezing does not remove that bias.

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

Use exact \(m_v\) as the initial simulator's reference. The log-loss difference is a decoder-dependent proxy, not automatically conditional mutual information. At population level,

\[
CE_0-CE_1=m_v+\epsilon_0-\epsilon_1,
\]

where \(\epsilon_i\ge0\) is decoder \(i\)'s expected conditional KL approximation error. Matching classes and nested features does not equalize those errors. For public fair bits \(A,B\), target \(C=A\oplus B\), and message \(S=C\), exact hiddenness and incremental information are zero, yet linear logistic decoders can report nearly one apparent bit because the added message makes XOR linearly readable. This can falsely support both A1 and A2; it does not establish a false pass of all four gates, since a correct A3 support check rejects the alternative-state construction.

Validate the proxy against exact values across known-positive, public-shortcut and collapsed-channel controls, and report approximation error, calibration and cross-validation uncertainty before threshold selection. The complete evaluator must also reject informative-but-unused and forbidden-access controls and distinguish redundant consumer reliance from informational benefit.

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

1. exact \(m_v\), or a validated estimate with approximation and sampling uncertainty accounted for, is meaningfully above zero;
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

Require \(C'_v\) to be reachable conditional on the same \(\mathcal I_t\), and verify replacement-message support conditional on all other inputs held fixed at the consumer, including non-target messages. Marginal familiarity of a message is insufficient. Record the eligible intervention population and use paired draws or replay with non-target state and randomness held fixed where appropriate. If no eligible alternative exists, report **not applicable** for that intervention; do not substitute a zero effect or count it as a pass. Avoid arbitrary zeroing unless zero is a trained, conditionally supported message state.

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

Total return \(J\) is secondary when downstream compensation could mask a genuine local causal effect. This intervention estimates the existing consumer's dependence on its message. It is distinct from the achievable task-value difference between matched consumers with and without the channel, and from exact Bayes informational headroom. Report these estimands separately: a consumer can rely on redundant information.

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

The manipulation must reveal the task-relevant information supplied by the message, not merely an unrelated component of \(C_v\). Reduced hiddenness alone gives only the bound

\[
0\le m_v\le H(C_v\mid\mathcal I),
\]

not a general monotonicity law for message information or benefit. For independent fair bits \(C=(A,B)\), message \(S=A\), and a task requiring \(A\), revealing \(B\) reduces hiddenness from two bits to one while message information stays at one bit and optimal accuracy gain stays at 50 percentage points. Exact estimation exposes this counterexample; it does not repair the prediction.

Preregister a task-specific observability manipulation and establish its predicted effect using the exact reference before testing the learned system. Name three separate estimands: incremental information \(m_v\); matched achievable message benefit (with exact Bayes headroom reported separately); and the existing consumer's proximal dependence under A3. Do not use corruption sensitivity as a substitute for informational benefit.

Full observability remains a valid endpoint for exact information and public-only performance. The alternative-state intervention stops where its conditional-support requirement fails; mark that endpoint **not applicable** for the intervention rather than failed or zero. Define the eligible range before confirmatory evaluation and report how the eligible population changes across the sweep.

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

Pass only if incremental information and matched achievable message benefit decline by the preregistered meaningful amounts under the validated task-relevant observability manipulation. Report confidence intervals and approximation uncertainty; any ratio criterion must be preregistered and never evaluated using bare ratios of point estimates. Report A3 consumer dependence separately over its eligible support range. Failed support or unresolved measurement uncertainty cannot be silently converted into a passing result.

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
| **A4 - Shortcut sensitivity** | a validated task-relevant observability manipulation reduces incremental information and matched achievable message benefit; consumer dependence and support eligibility are reported separately |

Report **pass, fail, or inconclusive** for each gate under a preregistered seed/precision rule. **Not applicable** labels a particular unsupported intervention, not successful gate evidence. E1 is licensed only when A1-A4 pass; a false positive on A1/A2 alone is not a demonstrated false pass of E0-A. If a gate fails or remains inconclusive, do not proceed as if the construct were intact. Re-engineer the task, simplify the channel, or revise the claim.

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

Before confirmatory use, each index requires a distinct executable predicate, named counterexamples and controls showing which architectures can satisfy one index while failing another. The shared discriminators below are necessary design scaffolding, not three completed definitions.

For **Shea**, specify the representational property entering the candidate's correctness conditions and a consumer that uses it as such. For **RR**, test a preregistered gain in accessibility to a bounded consumer, with explicit first-order redescription, consumer-role and matched feature-transformation controls; accessibility gain alone is ordinary feature engineering as well. For **Process**, require evidence about the generating mapping beyond a scalar reliability cue, using held-out process interventions and matched simpler process-state monitors. These are operational commitments to refine against Proust, Shea, Cleeremans/SOMA and process-metarepresentation work, not claims to exhaust those accounts.

Specify exactly which inputs, history, parameters, training data and computational capacity B0/B1 receive. A bounded shortcut predictor is not equivalent to conditioning on complete first-order activity. If \(M\) is a deterministic redescription of that activity, it adds no Shannon information beyond its complete inputs; it may nevertheless improve bounded-consumer accessibility. Report that accessibility separately from absolute conditional information.

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

1. satisfies the preregistered index-specific specificity or bounded-accessibility predicate, with explicit B0/B1 inputs and capacity controls; information and accessibility are reported as different estimands;
2. can dissociate from the first-order output and can misrepresent its meta-target;
3. responds selectively to intervention on the target representational property/process;
4. causally affects the intended downstream consumer when manipulated while first-order representation is preserved;
5. outperforms simpler B0/B1 explanations under held-out interventions, not merely under in-distribution decoding.

After index-specific rules are fixed and validated, report a vector of pass/fail/inconclusive results rather than a single verdict. An unspecified or unvalidated index is not confirmatory-ready; do not manufacture a verdict from the shared checklist. A reproducible split outcome is a substantive finding about the selected operationalizations, per §7.

If these conditions cannot be met under any index, the programme should not use the phrase **strict metarepresentation** for that system.

E0-B does **not** establish that this operationalization exhausts the concept of metarepresentation.

---

# PART III - ASSUMPTIONS AND LIMITATIONS

## 11. Assumptions

1. **Ground truth is available by construction.** The synthetic environment exposes \(C_t\), \(R_t\), \(\eta_t\), and intervention targets. The initial reference must additionally support tractable exact conditional probabilities; access to realized states alone does not provide this.
2. **Candidate variables are supplied by the experimenter.** E0 tests representation and use of known targets; it does not test spontaneous discovery of an internal ontology.
3. **Measurement validation precedes calibration.** Exact-reference estimator and complete-evaluator checks precede pilot threshold selection, which precedes independent confirmation. Held-out calibration and matched decoder classes alone are insufficient.
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
