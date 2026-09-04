# Sīdus: Towards Metarepresentational Ecology
## II. Research Programme: Local Laws, Experiments, and Falsification

**Working research programme - August 2026**  
**Status:** defeasible programme; falsifiable local models. This document does not assert that a metarepresentational ecology exists.

> **Truth, maximally sought. Ambition tempered by humility. Beauty tempered by goodness. Honesty above all else.**

---

## 0. Programme rule

The programme is not allowed to infer a global ecology from vocabulary.

It proceeds in the opposite direction:

\[
\boxed{
\begin{array}{c}
\text{define a construct}\;\rightarrow\;\text{build a discriminating experiment}\\[3pt]
\rightarrow\;\text{validate a local relation}\;\rightarrow\;\text{replicate/generalize}\\[3pt]
\rightarrow\;\text{only then infer larger organization}
\end{array}
}
\]

The central working hypothesis is deliberately weak:

> **Some internal monitoring systems may stand in structured, causally important relations to one another. Those relations can be tested one at a time. If sufficiently general regularities emerge, an ecology-level description may become warranted.**

Sīdus is the name of the programme while this is the most viable empirical direction. It is not a commitment to preserve any particular legacy construct, experiment, notation, or attention-centric hypothesis.

---

## 1. What is inherited from the earlier Sīdus package

### Retained

The previous package did several things well enough to keep:

1. **Local identifiability over global latent architecture.** The old unconstrained interaction matrix was correctly retired.
2. **Capacity-only claims.** No result about internal monitoring licenses a phenomenality claim.
3. **The information seam as an experimental scaffold.** Restricted access can create an identifiable communication problem without being asserted as literal neuroanatomy.
4. **Rate spent versus information delivered.** \(r_v\neq m_v\) remains a load-bearing distinction.
5. **Joint benefit surfaces.** Complementarity and substitution should be measured rather than assumed away.
6. **Causal use.** Decodability is insufficient.
7. **Optimization validity.** Posterior/channel collapse and training history can masquerade as scientific allocation preferences.
8. **Role/implementation separation.** Functional claims should survive implementation controls where technically feasible.
9. **Stage gates and kill criteria.** Expensive methods and broader claims are conditional on simpler pilots.

### Demoted or revised

1. **Attention privilege.** Attention becomes one candidate control process, not the privileged residual target of the programme.
2. **The old definition of metarepresentation.** A message about an internal controller is now called an *internal-state model* unless stricter representational criteria are independently satisfied.
3. **One global coordinator.** \(\Pi\) is a tractable experimental consumer, not a theory of cognitive headquarters.
4. **One global resource currency.** A single rate budget is a controlled experimental manipulation, not a claim about one biological pool.
5. **Astrocyte as default method.** Gaussian-process Bayesian optimization is optional infrastructure, not a prerequisite for the first experiment.
6. **Doerig as the programme's ontology.** Doerig-style adversarial pressure is retained; consciousness-specific inferential criteria are not imported where phenomenality is no longer the explanandum.

---

## 2. What would count as an ecology-level result?

A single second-order signal does not make an ecology. Neither do three modules drawn in a diagram.

An ecology-level result requires at least one **relational regularity** that predicts how one internal model changes the value, fidelity, use, or resource allocation of another across more than one condition.

Candidate relation classes are:

- **competition** - models trade off under a demonstrably shared constraint;
- **complementarity** - one model increases the marginal utility of another;
- **substitution** - one model reduces the marginal utility of another;
- **causal-topological dependence** - monitoring value tracks causal role/position rather than implementation identity;
- **recursive regulation** - a model of a control process changes subsequent control;
- **fidelity dependence** - downstream use scales with calibrated accuracy, not merely decodability;
- **temporal niche** - optimal/useful monitoring differs systematically with volatility, persistence, lag, or control horizon.

The programme does not assume all seven exist.

---


# PART 0 - POSITIONING AGAINST ADJACENT LITERATURES

**[R4 · correction, August 2026 review pass]**

Constraint C5 of Document I requires that no novelty claim survive an unsearched
prior-art row. That constraint was executed thoroughly on the
metacognition and consciousness-methodology side and **not** on the
information-theory, control, and reinforcement-learning side. Five literatures
substantially overlap E1, E3 and E4 and were absent from earlier drafts. Each is
given a paragraph here stating what it established and where this programme
actually differs. Where the difference is thin, that is said. A sixth family —
the nearest neurocomputational neighbours — was still missing after that pass
and is added as P6 in the second external review pass.

## P1. Emergent communication in multi-agent RL under bandwidth constraints

Learned communication protocols over limited channels are an established
subfield. DIAL and RIAL (Foerster et al. 2016) learn discrete and differentiable
protocols end to end; SchedNet (Kim et al. 2019) learns *which* agents may
transmit over a contested channel by learned importance weights; IMAC (Wang et
al. 2020) derives a mutual-information upper bound as an explicit bandwidth
constraint and learns low-entropy messages; VBC (Zhang et al. 2019) prunes
communication by variance. E1 — learned agents allocating a shared information
rate across sources, with messages tested for causal use — is structurally close
to this work, and the resemblance should be stated before a reviewer states it.
Three differences are defensible. The sources are **internal control states of a
single agent** rather than other agents' observations of external world state,
so encoder and consumer share a body and a reward. The **scientific object is the
allocation law measured against an empirically estimated benefit surface**,
rather than task return maximised by any protocol that works. And **causal-use
validation is a gate rather than a diagnostic**: a decodable but behaviourally
inert channel fails E0-A outright. Honesty about the first difference: a single
agent with private modules and a shared reward is formally close to a cooperative
multi-agent system, and the architectural distinction alone will not carry the
positioning. The scientific one will.

## P2. Information-theoretic bounded rationality

Ortega and Braun's free-energy formulation, and Genewein et al. (2015) on
hierarchical decision-making under an information-processing cost, establish the
trade-off between expected utility and rate as an optimality principle, with
antecedents in Tishby and Polani (2011) and in linearly-solvable control. The
\(r\) versus \(m\) distinction and the KL rate cost used throughout this package
live **inside** this tradition and are inherited from it, not derived here; they
should be cited accordingly. The difference is one of direction. That literature
specifies the trade-off normatively and derives optimal policies from it. E1
applies the constraint to self-monitoring specifically and **measures** the
benefit surface empirically rather than assuming a parametric form for it — which
is what permits interaction, non-concavity, and failure of separability to appear
as findings rather than as violated assumptions.

## P3. Rational inattention

Sims (2003) formalised capacity-constrained attention allocation under a Shannon
cost; Caplin and Dean (2015) supplied revealed-preference tests for costly
information acquisition. H1 is, in structure, a rational-inattention hypothesis
pointed inward, and this is the collision most likely to be recognised by a
cognitive scientist rather than only by a machine-learning reviewer. Two
differences. Rational inattention constrains the acquisition of **external**
state; here the constrained resource is applied to states the agent itself
generates, where the benefit accrues to control of control rather than to
decision accuracy. More importantly: rational inattention **assumes the optimum
is attained** and derives behaviour from that premise. This programme treats
attainment as the empirical question. The real content of H1 and H2 is not
whether a capacity-constrained optimum exists — it does — but whether a learning
system operating under realistic optimisation pathologies finds it, and what it
does instead when it does not.

## P4. Value-of-information sensor scheduling and networked control

"Which sensor's state is worth transmitting under a communication constraint"
has been formalised for decades. Imer and Başar (2005), Lipsa and Martins (2011),
and Gao, Akyol and Başar (2018) treat remote estimation in which communication is
limited or explicitly priced; Gao et al. directly distinguish soft transmission
costs from a hard limit on transmission opportunities. Sequential rate-distortion
work by Tanaka et al. (2017), and later finite-rate sequential source coding by
Stavrou, Skoglund and Tanaka (2022), formalises closely related rate--distortion
and encoder-design problems for dynamical systems. **Some E1 specialisations are
formally very close to this problem class**, and pretending otherwise would be
indefensible; the package does not claim a general isomorphism without an explicit
mapping of state, information pattern, objective and constraint. The differences
are that the intended sources are non-Gaussian and low-cardinality internal
control states, the distortion analogue is expected return rather than quadratic
estimation error, and the encoders are **learned rather than designed**. The right
posture toward this literature is not defensive. Per Document I §8.1, a deliberately
constructed solved linear-Gaussian case is not a competitor but a **validation
target**: a learned allocation that cannot recover a known optimum where one
exists has not earned interpretation where none does.

## P5. Rational metareasoning and value of computation

Russell and Wefald (1991) and Hay, Russell, Tolpin and Shimony (2012) price a
computation by its expected effect on the decision it informs. The hypothesis
that monitoring value tracks causal position and downstream reach --- **H2** in
this document, **H4** in the Master's scoping document --- overlaps conceptually
with value of computation, and the overlap must be stated. Graph position and
value of computation are not identical, but they are close enough that a
topology result could be a VOC result wearing different notation.

**[Revised after release-candidate review.]** An earlier version of this
paragraph described VOC as "myopic and per-item" and contrasted that with a
joint, constrained Sīdus problem. That characterisation was wrong. Rational
metareasoning is formulated as a **metalevel MDP**; the myopic or meta-greedy
policy is one *approximation* within that framework, not its definition, and Hay
et al. explicitly analyse the relation between myopic and optimal metalevel
policies. Exact metalevel policies are intractable in general, which is why
myopic approximations are used in practice --- a fact that applies symmetrically
to \(\mathbf r^*(C)\) and is already covered by anti-slop rule 5.

The honest differences are narrower. VOC prices **computations against a
decision**; the allocation problem prices **channels against each other** under a
binding shared budget, where sources may be complementary or substitutable.
Neither is tractable in general; both enter as benchmarks rather than as claims
about what any system computes. For the separable, non-interacting case they
converge, which is why a **specified myopic-VOC baseline** belongs in the
comparison set rather than in a related-work paragraph. If the joint resource
surface fails to improve out-of-sample prediction over myopic VOC, the experiment
provides **no incremental predictive evidence** for the interaction structure this
programme is built to detect beyond that simpler benchmark.

## P6. Precision weighting, attention-as-resource, and working-memory limits

**[Second external review pass — neuroscience-side C5.]** The nearest
neurocomputational neighbours are not source-coding problems at all, and they
constrain a different part of the programme. Expected-precision accounts of
attention (Feldman & Friston 2010) treat attention as the optimisation of
precision estimates that weight first-order sensory evidence — formally, E2's
consumer using \(M_v\) to weight first-order representations *is* precision
weighting, and any neuroscience-facing reading of E2 must say so.
Attention-as-resource (Kahneman 1973) is the classical ancestor of every
shared-budget intuition in this package. The working-memory
slots-versus-resources debate (Ma, Husain & Bays 2014) shows that even for the
best-studied candidate "shared pool" in cognition, the existence of a single
common currency is contested rather than established. None of this changes the
synthetic thesis, which makes no biological budget claim. It becomes
load-bearing at E6, where these literatures — not the source-coding apparatus —
set the standard of evidence for any human translation.

## What the six leave standing

Nothing in the formalism. The rate machinery, the shared-budget structure, the
utility-versus-rate trade-off, and the marginal-value logic are all inherited.
What survives is narrower and should be stated in exactly these terms:

> The application of an established rate-allocation apparatus to **internal
> monitoring targets specifically**, with **construct validity gated before**
> any allocation claim (E0), and with **causal use required rather than
> decodability**.

That is an application-level and methodological contribution. It is smaller than
"a new theory of bounded self-monitoring" and it is the size that the evidence
can currently carry.

---

# PART I - HYPOTHESIS FAMILIES

## 3. H1 - Scarcity and competition

### Hypothesis

When multiple internal targets are locally available but their models must pass through a genuinely binding shared communication constraint, learned systems will allocate unequal rate according to the marginal control value of exposing each target.

The safest empirical object is the joint benefit surface:

\[
\mathcal B(\mathbf r)=\mathbb E[J\mid\mathbf r]-\mathbb E[J\mid\mathbf 0],
\]

with normative benchmark

\[
\mathbf r^*(C)=
\arg\max_{\mathbf r\ge0,\;\sum_vr_v\le C}
\mathcal B(\mathbf r).
\]

This is not a claim that organisms compute the argmax. It is a benchmark against which learned allocation can be compared.

### Competing explanations

- source entropy alone;
- ordinary inferability from public information;
- fixed head/implementation bias;
- training-order/path dependence;
- no shared resource at all;
- a simpler architecture in which every source is transmitted independently.

### Falsifying / narrowing outcomes

H1 is weakened or rejected in a given architecture if:

- reducing nominal capacity does not create measurable cross-source trade-offs;
- allocation differences vanish after ordinary inferability is controlled;
- rates are dominated by head identity or initialization;
- learned allocations do not generalize to held-out task conditions better than simpler predictors;
- transmitted state information is behaviorally unused.

---

## 4. H2 - Causal topology predicts monitoring value

### Hypothesis

The value of monitoring an internal target depends partly on its causal position in the system. Holding obvious statistical properties as controlled as practical, states with greater downstream reach, bottleneck position, persistence, or influence over other computations should exhibit systematically different benefit-rate curves.

This reframes the old Sīdus topology model from a nuisance control into a candidate explanatory principle.

### Minimal test

Create matched modules from the same implementation family but vary one high-level causal property, such as how many downstream decisions depend on the state. Measure:

\[
B_v(r)=J(r_v=r)-J(r_v=0)
\]

and ask whether topology predicts the curve out of sample.

### Stronger test

If simple manipulations establish an effect, use causal-role permutation. Only then consider causal-abstraction/interchange validation to verify that a proposed high-level role is actually realized by the low-level module.

### Failure condition

If topology metrics add no predictive value beyond entropy, inferability, and direct control relevance, do not elevate topology into an organizing principle.

---

## 5. H3 - Recursive monitoring can improve control of control

### Hypothesis

Monitoring the *realized state* of a control or resource-allocation process can have future control value when commands are imperfect, the realized state persists or lags, and future actions can compensate.

Use two distinct resource levels:

\[
\sum_i a_{i,t}\le C_{\mathrm{base}}
\]

for first-order world-facing allocation, and

\[
\sum_v r_v + r_A\le C_{\mathrm{meta}}
\]

for internal-state modelling.

The recursion is temporal:

\[
\text{allocate}
\rightarrow
\text{observe realized allocation}
\rightarrow
\text{use the model}
\rightarrow
\text{allocate better later}.
\]

### Primary estimand

Let

\[
B_A^H(r)=J_H(r_A=r)-J_H(r_A=0)
\]

be finite-horizon benefit. Separate current interpretive value from future feedback value with a matched contrast:

\[
\Gamma_A^H(r)
=
B_A^{\mathrm{feedback},H}(r)
-
B_A^{\mathrm{frozen},H}(r).
\]

The frozen condition makes the same current allocator information available but prevents it from influencing future allocation commands.

### Predictions

\(\Gamma_A^H\) should increase when:

- command-to-realized allocation is noisy or lagged;
- the realized allocation changes downstream signal reliability;
- allocation has temporal persistence;
- the horizon permits corrective reallocation.

It should collapse when:

- realized allocation is directly observable without the special channel;
- commands determine allocation perfectly and immediately;
- allocation has no behavioral consequences;
- feedback is impossible;
- the horizon is too short.

### Prior-art discipline

This experiment lives next to meta-control, rational metareasoning, active information gathering, and oMCD. Its novelty is **open**, not presumed.

---

## 6. H4 - Faithful self-models are more than decodable echoes

### Hypothesis

A candidate internal model earns a functional claim only when its information is sufficiently calibrated for its consumer and selectively perturbing it changes the downstream computation predicted by its content.

A useful evidence sequence is:

\[
\begin{array}{c}
\text{decodable}\;<\;\text{conditionally specific}\;<\;\text{misrepresentable}\\[3pt]
<\;\text{causally target-dependent}\;<\;\text{causally used}.
\end{array}
\]

### Failure condition

If a candidate signal decodes the target but perturbing it leaves the putative consumer unchanged, call it redundant or unused under the tested conditions. Do not rescue the claim by redefining its function.

---

## 7. H5 - Complementarity and substitution

### Hypothesis

The value of one internal model depends on what other models are available.

For a smooth estimated benefit surface, local cross-curvature can be used as a *diagnostic*:

\[
\Gamma_{uv}(\mathbf r)
=
\frac{\partial^2\mathcal B(\mathbf r)}{\partial r_u\partial r_v}.
\]

Positive values suggest local complementarity; negative values suggest substitution. The derivative is not an ontological quantity and should not be interpreted without uncertainty.

### More robust empirical alternative

Use factorial allocation contrasts or held-out predictive comparisons between:

- additive model \(\sum_vB_v(r_v)\);
- pairwise-interaction model;
- full joint surface.

The simplest model that predicts held-out returns adequately wins.

---

## 8. H6 - Temporal niche

### Hypothesis

Monitoring policies depend systematically on the timescale of the target and the horizon over which its state matters.

Candidate parameters include:

- target volatility;
- temporal autocorrelation;
- command/actuator lag;
- persistence of errors;
- duration of downstream consequences;
- cost of delayed correction.

### Prediction

Fast, volatile targets should favor frequent low-latency updating when they remain control-relevant; slowly drifting but consequential targets may favor lower-frequency, higher-fidelity summaries. The exact pattern is an empirical question.

### Failure condition

If timescale manipulations do not improve predictions of monitoring policy beyond static control value, temporal niche remains unnecessary.

---

# PART II - EXPERIMENTAL PROGRAMME

## 9. E0 - Construct benchmark: what actually counts as meta?

This is the first new experiment required by the reframing. It prevents the programme from building an ecology out of an undefined construct.

### Goal

Create synthetic systems with known computational relationships and test whether proposed measurements distinguish:

1. **ordinary first-order transformation**;
2. **internal-state model**;
3. **content/property metarepresentation**;
4. **process metarepresentation**.

### Minimal architecture

Let an external latent state \(X_t\) generate observation \(O_t\). A first-order system produces

\[
R_t=F_{\eta_t}(O_t),
\]

where \(\eta_t\) controls a hidden property of the representational process: noise, bias, gain, source type, or mapping rule.

Create four candidate downstream systems:

**A. First-order echo**  
Receives \(R_t\) and transforms it for the task. It has no separate target representing a property of \(R_t\).

**B. Internal-state monitor**  
Receives a hidden controller/process state \(C_t\) and reports its value.

**C. Property metarepresentation candidate**  
Must infer \(\phi(R_t)\), such as the likely correctness, source, or reliability of the current first-order representation.

**D. Process metarepresentation candidate**  
Must infer \(\eta_t\) or a compact property of \(F_{\eta_t}\), and use that model to predict how first-order representations will change under controlled counterfactual inputs.

### Critical matched controls

- hold external \(X_t\) constant while changing \(\eta_t\);
- hold first-order choice/output constant while changing reliability;
- create cases where confidence/source/process inference is wrong;
- perturb the candidate meta-state while preserving first-order \(R_t\);
- compare against a shortcut model that predicts \(\eta_t\) from public context without reading the first-order process.

### Main question

Which evidence tiers from Foundations actually discriminate the four architectures?

### Success

E0 succeeds if at least one operational test distinguishes a genuine property/process-monitoring architecture from first-order and internal-state controls under held-out interventions.

### Failure

If proposed criteria cannot distinguish the architectures without appealing to their labels or implementation history, the programme does **not** yet possess an empirically useful construct of metarepresentation. Stop and refine the construct before scaling.

---

## 10. E1 - Scarcity terrarium: bounded internal-state monitoring

This is the direct descendant of the strongest old Sīdus experiment, but it no longer pretends all messages are strict metarepresentations.

### Question

> **When several private internal control/process states are useful to a coordinating agent but can only be exposed through a binding shared information-rate channel, what predicts the learned allocation of monitoring capacity?**

### Environment

Use a compact POMDP with at least three low-cardinality private internal states, for example:

- sensory-selection state;
- working-memory update state;
- action-routing/effector state.

The consumer receives ordinary public information \(\mathcal I_t\) but no direct read of these private states.

Each source has a symmetric encoder:

\[
C_{v,t}\rightarrow S_{v,t}\rightarrow U
\]

with a single rate constraint:

\[
\sum_v r_v\le C_{\mathrm{meta}}.
\]

### Required measures

For each source:

- conditional uncertainty \(H(C_v\mid\mathcal I)\);
- state entropy/cardinality;
- causal return sensitivity;
- isolated learnability;
- distortion-rate / benefit-rate curve;
- temporal persistence/update frequency;
- basic causal-topological measures;
- rate spent \(r_v\);
- incremental information delivered \(m_v\);
- targeted-channel causal-use effect.

### Required controls

- direct-read oracle;
- no-seam/full-read control;
- non-binding budget control;
- source/head permutation across seeds;
- warm-up before scarcity;
- gradual constrained scarcity ramp;
- selected from-scratch scarcity runs;
- held-out task conditions.


### Constraint implementation: Arm S core, alphabet arm optional

**[Design addition, August 2026 — demoted after release-candidate review]**

An earlier version of this section proposed a hard alphabet-cardinality budget as
a mandatory second arm and made **rank-order invariance across arms** a
confirmatory prediction. Both claims were too strong and are withdrawn. What
follows is the corrected position.

**Arm S is the core experiment.** Primal-dual or augmented-Lagrangian training
formulates \(\sum_v r_v\le C_{\mathrm{meta}}\) as a constrained optimisation
problem rather than merely attaching a fixed penalty coefficient. In a non-convex
learned system, however, **feasibility is an empirical property of the trained
solution**, not something the optimiser name guarantees. Realised constraint
violation must therefore be reported and preregistered feasibility tolerances met
before the run is interpreted as genuinely budget-constrained. The second
epistemic question is whether the variational surrogate corresponds tightly enough
to the intended information currency --- and correction R2 makes that looseness
measurable:

\[
r_v=m_v+\Delta_v^{\mathrm{prior}},
\qquad
\Delta_v^{\mathrm{prior}}=\mathbb E_{\mathcal I}\,D_{KL}\!\left(q(S_v\mid\mathcal I)\,\Vert\,p(S_v\mid\mathcal I)\right).
\]

Arm S therefore requires two things to be reported alongside every allocation:
realised constraint violation, and \(\Delta_v^{\mathrm{prior}}\) per source as a
tightness diagnostic. Those reports are what license the surrogate as a rate
meter; a second arm is not needed for that purpose.

**Why the invariance test does not work.** A KL budget and an alphabet budget are
different resource currencies:

\[
\mathbb E[D_{KL}]\;\neq\;\log_2|\mathcal Z|.
\]

One constrains expected informational departure from a prior; the other
constrains maximum representational capacity. A source may be granted a large
alphabet and use it sparsely; another may use a small alphabet efficiently.
Different allocation rankings can therefore arise **under perfect optimisation
and an unchanged task**. So

\[
\text{ranking}_S\neq\text{ranking}_H
\]

does not license the conclusion that the allocation law is
optimiser-dependent. The more likely reading is that allocation depends on
**which resource is scarce**, which is interesting and is not what an invariance
test claims to measure.

**The alphabet arm as optional robustness.** If a stable allocation phenomenon is
established in Arm S, a hard-capacity arm becomes worth running as a
**currency-sensitivity** experiment: does the ordering change when the scarce
resource is capacity rather than expected information cost? Run that way, a
divergence is a finding about currency dependence rather than a failed invariance
check.

If it is run, the construction matters. Per-source codebooks give each source its
own hard cap and abolish competition; a single shared codebook abolishes
source-factorisation and with it the per-source identifiability of \(r_v\),
\(m_v\) and targeted intervention, taking Gates A3 and A4 and H3 with it. The
construction that is hard, shared and factorised at once constrains **total
alphabet cardinality with a learned split**:

\[
\sum_{v}\log_2|\mathcal Z_v|\;\le\;C_{\mathrm{meta}},
\]

with per-source cardinality drawn from a shared slot pool by a differentiable
arbitration. That is the right way to build the arm. It is not a reason to build
it before the phenomenon exists --- anti-slop rule 8 applies to this proposal as
much as to any other.

### Confirmatory comparisons

At minimum compare:

1. uniform allocation;
2. entropy-only / inferability-only allocation;
3. isolated causal-value predictor;
4. **myopic value-of-computation prediction** (Russell \& Wefald 1991; Hay et
    al. 2012) — the closest competitor drawn from an established formalism;
    specified as one-step value, not VOC in general; see Document III, H2;
5. joint empirical resource model;
6. joint resource + topology features;
7. implementation/head identity.

Do **not** make attention residual \(\Delta_A\) the centre of the thesis. Estimate generic source residuals \(\Delta_v\) if useful.

### Publishable outcomes

- stable scarcity law;
- topology improves prediction;
- strong source interactions invalidate additive resource models;
- learning repeatedly fails to discover a known normative value;
- allocation is path-dependent rather than law-like;
- no genuine trade-off exists.

All are informative.

---

## 11. E2 - Strict metarepresentation under scarcity

E2 proceeds only if E0 yields a defensible operational distinction and E1 demonstrates a real shared monitoring constraint.

### Question

> **When first-order representations differ in reliability, source, or generative process, does a bounded system allocate scarce rate to models of those representational properties/processes, and does the allocation improve control beyond first-order shortcuts?**

### Example

Two perceptual experts produce first-order estimates:

\[
R_{1,t}=F_{1,\eta_{1,t}}(O_t),\qquad
R_{2,t}=F_{2,\eta_{2,t}}(O_t).
\]

Their hidden process regimes alter reliability. Candidate meta-generators produce:

\[
M_{v,t}=G_v(R_{v,\le t},\text{process evidence})
\]

about \(\eta_{v,t}\), source, or correctness probability.

The consumer uses \(M_v\) to weight first-order evidence.

### Key comparison

Compare against:

- direct reliability cue;
- public-context predictor;
- first-order network with matched parameter count;
- internal-state monitor that knows a controller setting but not the representational process;
- meta-process model.

E2 is where the phrase **metarepresentation under scarcity** becomes substantively earned rather than merely inherited.

---

## 12. E3 - Causal topology and role dependence

Proceed only if E1/E2 produce a robust phenomenon.

### Phase 1: cheap topology manipulation

Change downstream reach, bottleneck status, persistence, or branching while holding module implementation fixed where possible.

### Phase 2: simple role permutation

Swap functional interfaces across matched implementations. Measure whether monitoring benefit follows role or implementation.

### Phase 3: causal-abstraction validation, conditional

Only if the role claim is central and simpler validation is inadequate, construct a high-level causal model and test interchange-intervention faithfulness.

A failed abstraction alignment blocks a high-level role conclusion. It does not invite a more elaborate rescue model.

---

## 13. E4 - Recursive allocator monitoring

This retains the two-budget S1-R construction because it converts a tempting regress into a temporal causal question.

Crucial terminology:

- if \(A_t\) is merely the realized resource-allocation/control state, \(R_A\) is an **internal-state model**;
- call it a strict metarepresentation only if the target is explicitly a representational property/process of the allocator.

The primary test is feedback versus frozen feedback, not an unexplained allocator residual.

---

## 14. E5 - Two validated meta-systems in interaction

This is the first experiment that would genuinely deserve the phrase **metarepresentational ecology**.

Use two previously validated meta-systems, for example:

- a model of perceptual reliability/source;
- a model of memory reliability or control allocation.

Ask whether their joint utility is additive, complementary, substitutable, or mediated through a third control process.

### Minimal criterion for an ecology-level claim

At least one interaction must:

1. survive selective interventions on each component;
2. improve held-out prediction over independent-module models;
3. recur under a second task or architecture;
4. not reduce to shared external input or generic confidence bias.

Until then, use "candidate interaction" rather than "ecological law."

---

## 15. E6 - External translations

### Human metacognition

Plausible targets include perception-memory confidence, source monitoring, error monitoring, and meta-control. The literature already warns against assuming strong domain generality. Human work should therefore test specific interactions and trade-offs, not merely group differences or correlations.

### Artificial-system introspection

The same construct discipline can test whether a model's report about an internal state is causally faithful rather than semantically plausible. Define the internal target independently; intervene on target and report separately; vary semantic framing; preserve non-target information.

### Clinical translation

This remains post-construct-validity. Hypervigilance, interoception, alexithymia or dissociation should not be redescribed as "metarepresentational ecology" unless the framework predicts a distinctive within-person interaction or trade-off that competing accounts do not.

---

# PART III - WHAT CAN AND CANNOT BE COMPUTED

## 16. Computational tractability map

| Object/question | Can render now? | Notes |
|---|---:|---|
| private low-cardinality internal process state | Yes | direct simulator ground truth |
| internal-state model of that process | Yes | supervised or learned encoder |
| rate spent \(r_v\) | Yes | variational KL control surrogate |
| incremental target information \(m_v\) | Yes, with validation | low-cardinality targets + held-out calibrated log loss |
| causal use of message | Yes | selective message intervention, support checks |
| joint benefit surface | Yes for small \(K\) | grid/design first; surrogate only if needed |
| complementarity/substitution | Yes, locally | factorial contrasts or uncertain surface derivatives |
| hidden process/reliability regime | Yes | known by simulator |
| process metarepresentation | Yes in proof-of-concept form | must beat first-order/public-context controls |
| topology manipulations | Yes in synthetic systems | exact matching may be impossible |
| causal abstraction | Conditional | high overhead; only after robust role effect |
| recursive allocator feedback | Yes | requires two budgets and temporal dynamics |
| one universal cognitive resource currency | No | experimental single-budget model is not neural fact |
| spontaneous discovery of arbitrary internal ontology | Not currently identifiable without strong assumptions | separate long-horizon problem |
| complete brain metarepresentational ecology | No | no current measurement/identification route |
| phenomenal consciousness | No | explicitly outside the programme |

---

## 17. Astrocyte: optional methods module

Astrocyte remains valid **only when the empirical surface is expensive enough to justify it**.

The scientific target is still:

\[
\mathbf r^*(C)=\arg\max_{\mathbf r\in\mathcal S_C}\mathcal B(\mathbf r).
\]

Gaussian-process Bayesian optimization estimates that target; it does not define it.

### Escalation rule

Use, in order:

1. small factorial / simplex design;
2. interpolation / regression with uncertainty;
3. GP surrogate if surface smoothness is empirically defensible;
4. noise-aware BO only when each new training configuration is genuinely expensive and active search materially reduces cost.

Do not deploy GP curvature diagnostics or Bayesian optimization because they make the project look sophisticated.

---

# PART IV - FALSIFICATION AND STAGE DISCIPLINE

## 18. Questions that can actually be false

| Question | Evidence for | Evidence against |
|---|---|---|
| Does a shared monitoring budget create competition? | cross-source trade-offs appear only when budget binds | no displacement/trade-off under validated scarcity |
| Does dynamic value predict allocation? | held-out rates/returns better predicted than by entropy/identity baselines | no out-of-sample advantage |
| Does topology matter? | controlled causal-position changes shift benefit/allocation | topology adds no predictive value |
| Are messages causally used? | selective perturbation changes predicted behavior with first-order target intact | decodable message can be removed without relevant effect |
| Is a candidate state meta rather than first-order? | survives E0 conditional, decoupling and intervention controls | simple first-order/public-context model explains data |
| Does recursive monitoring help? | feedback-vs-frozen benefit appears where lag/noise/horizon predict it | no specific feedback benefit or benefit persists when feedback impossible |
| Are two meta-systems complementary/substitutable? | robust interaction improves held-out prediction | additive independent model suffices |
| Is there an ecology-level regularity? | same relational principle generalizes to second task/architecture | every effect is domain/task specific |

---

## 19. Global kill/narrow criteria

The programme should be narrowed or abandoned as an ecology-level project if repeated work shows that:

- strict metarepresentational constructs cannot be operationally distinguished from first-order/process-reflexive alternatives;
- apparent interactions vanish under conditional-information and common-cause controls;
- shared-resource hypotheses repeatedly fail to generate trade-offs;
- topological features do not generalize;
- candidate models are decodable but not causally used;
- results are dominated by optimization history or implementation identity;
- each domain requires an unrelated explanation and a common relational vocabulary adds no predictive compression.

In that case the correct conclusion is not "the ecology is more complicated."

It is:

> **There may be no useful ecology-level theory. Study the domain-specific mechanisms instead.**

---

## 20. Stage gates

### Gate 0 - Construct validity

**Proceed only if E0 distinguishes at least one candidate metarepresentational relation from simpler controls.**

### Gate 1 - Scarcity exists

**Proceed beyond E1 only if the shared budget produces measurable, stable trade-offs and messages are useful.**

### Gate 2 - Relation is not training artifact

**Proceed to topology/recursion only if rates and causal effects survive reasonable seed/schedule/implementation controls.**

### Gate 3 - Local law exists

**Use the word "principle" only after held-out prediction and intervention succeed.**

### Gate 4 - Ecology claim

**Use the word "ecology" as an empirical result only after at least two validated monitoring/meta-systems show a reproducible interaction across more than one task or architecture.**

---

## 21. Immediate sequence

The programme should generate code before another conceptual companion.

1. **Systematic construct/prior-art review**: Proust, Shea, Cleeremans/SOMA, Kanai et al., metacognition architectures, meta-control, resource-rationality, distributed communication.
2. **E0 notebook**: synthetic first-order vs internal-state vs property-meta vs process-meta benchmark.
3. **E1 minimal environment**: no GP, no causal abstraction, no attention residual as primary target.
4. **Pilot stage gate**: prove an information seam, a binding shared budget, stable informative messages, and causal use.
5. **Freeze the smallest successful model.** Preregister/replicate.
6. Only then select **one** extension: topology, strict-meta scarcity, or recursive control.

Not all three.

---

## 22. What success would look like

A successful first paper need not mention consciousness or claim a new cognitive architecture.

A strong result could be:

> **In a controlled modular agent, private internal process states competed for a binding information-rate channel. Learned allocation was predicted by the joint dynamic control benefit of monitoring those states, and transmitted information was causally used. A controlled change in causal position altered monitoring value in the predicted direction.**

A stronger later result could be:

> **A separately validated metarepresentation of a first-order representational process competed with other internal models under the same constraint, and its value depended on the process's uncertainty and causal role.**

An ecology-level result would require more:

> **The same relational principle predicts interactions among multiple validated meta-systems across tasks or architectures.**

The programme must earn each sentence separately.

---

# References

1. Fazekas, P., Cleeremans, A., & Overgaard, M. (2024). A construct-first approach to consciousness science. *Neuroscience & Biobehavioral Reviews, 156*, 105480. https://doi.org/10.1016/j.neubiorev.2023.105480
2. Proust, J. (2003). Does metacognition necessarily involve metarepresentation? *Behavioral and Brain Sciences, 26*(3), 352. https://doi.org/10.1017/S0140525X0336008X
3. Shea, N. (2014). Reward prediction error signals are meta-representational. *Noûs, 48*(2), 314-341. https://doi.org/10.1111/j.1468-0068.2012.00863.x
4. Cleeremans, A., et al. (2020). Learning to be conscious. *Trends in Cognitive Sciences, 24*(2), 112-123. https://doi.org/10.1016/j.tics.2019.11.011
5. Kanai, R., Takatsuki, R., & Fujisawa, I. (2025). Meta-representations as representations of processes. *Neuroscience of Consciousness, 2025*(1), niaf038. https://doi.org/10.1093/nc/niaf038
6. Fleming, S. M. (2024). Metacognition and confidence: A review and synthesis. *Annual Review of Psychology, 75*, 241-268. https://doi.org/10.1146/annurev-psych-022423-032425
7. Mazancieux, A., et al. (2023). Towards a common conceptual space for metacognition in perception and memory. *Nature Reviews Psychology, 2*, 751-766. https://doi.org/10.1038/s44159-023-00245-1
8. Baer, C., Ghetti, S., & Odic, D. (2026). Domain generality is an emergent, not inherent, property of metacognition. *Nature Human Behaviour, 10*, 1316-1326. https://doi.org/10.1038/s41562-026-02443-2
9. Eppinger, B., Goschke, T., & Musslick, S. (2021). Meta-control: From psychology to computational neuroscience. *Cognitive, Affective, & Behavioral Neuroscience, 21*, 447-452. https://doi.org/10.3758/s13415-021-00919-4
10. Bénon, J., et al. (2024). The online metacognitive control of decisions. *Communications Psychology, 2*, 23. https://doi.org/10.1038/s44271-024-00071-y
11. Lieder, F., & Griffiths, T. L. (2020). Resource-rational analysis: Understanding human cognition as the optimal use of limited computational resources. *Behavioral and Brain Sciences, 43*, e1. https://doi.org/10.1017/S0140525X1900061X
12. Shenhav, A., Botvinick, M. M., & Cohen, J. D. (2013). The expected value of control. *Neuron, 79*(2), 217-240. https://doi.org/10.1016/j.neuron.2013.07.007
13. Berger, T., Zhang, Z., & Viswanathan, H. (1996). The CEO problem. *IEEE Transactions on Information Theory, 42*(3), 887-902. https://doi.org/10.1109/18.490552
14. Goyal, A., et al. (2021). Coordination among neural modules through a shared global workspace. *ICLR 2022 / arXiv:2103.01197*. https://arxiv.org/abs/2103.01197
15. Geiger, A., et al. (2025). Causal abstraction: A theoretical foundation for mechanistic interpretability. *Journal of Machine Learning Research, 26*(83), 1-64. https://www.jmlr.org/papers/v26/23-0058.html
16. Guest, O., & Martin, A. E. (2021). How computational modeling can force theory building in psychological science. *Perspectives on Psychological Science, 16*(4), 789-802. https://doi.org/10.1177/1745691620970585
17. van Rooij, I., & Baggio, G. (2021). Theory before the test: How to build high-verisimilitude explanatory theories in psychological science. *Perspectives on Psychological Science, 16*(4), 682-697. https://doi.org/10.1177/1745691620970604

18. Foerster, J., Assael, I. A., de Freitas, N., & Whiteson, S. (2016). Learning to communicate with deep multi-agent reinforcement learning. *NeurIPS 29*. https://arxiv.org/abs/1605.06676
19. Kim, D., Moon, S., Hostallero, D., Kang, W. J., Lee, T., Son, K., & Yi, Y. (2019). Learning to schedule communication in multi-agent reinforcement learning. *ICLR 2019*. https://arxiv.org/abs/1902.01554
20. Wang, R., He, X., Yu, R., Qiu, W., An, B., & Rabinovich, Z. (2020). Learning efficient multi-agent communication: An information bottleneck approach. *ICML 2020*. https://arxiv.org/abs/1911.06992
21. Zhang, S. Q., Zhang, Q., & Lin, J. (2019). Efficient communication in multi-agent reinforcement learning via variance based control. *NeurIPS 32*. https://arxiv.org/abs/1909.02682
22. Ortega, P. A., & Braun, D. A. (2013). Thermodynamics as a theory of decision-making with information-processing costs. *Proceedings of the Royal Society A, 469*(2153). https://doi.org/10.1098/rspa.2012.0683
23. Genewein, T., Leibfried, F., Grau-Moya, J., & Braun, D. A. (2015). Bounded rationality, abstraction, and hierarchical decision-making: An information-theoretic optimality principle. *Frontiers in Robotics and AI, 2*, 27. https://doi.org/10.3389/frobt.2015.00027
24. Tishby, N., & Polani, D. (2011). Information theory of decisions and actions. In *Perception-Action Cycle*. Springer.
25. Sims, C. A. (2003). Implications of rational inattention. *Journal of Monetary Economics, 50*(3), 665-690. https://doi.org/10.1016/S0304-3932(03)00029-1
26. Caplin, A., & Dean, M. (2015). Revealed preference, rational inattention, and costly information acquisition. *American Economic Review, 105*(7), 2183-2203. https://doi.org/10.1257/aer.20140117
27. Imer, O. C., & Basar, T. (2005). Optimal estimation with limited measurements. *Proceedings of the 44th IEEE Conference on Decision and Control*, 1029-1034.
28. Lipsa, G. M., & Martins, N. C. (2011). Remote state estimation with communication costs for first-order LTI systems. *IEEE Transactions on Automatic Control, 56*(9), 2013-2025. https://doi.org/10.1109/TAC.2011.2139370
29. Russell, S., & Wefald, E. (1991). Principles of metareasoning. *Artificial Intelligence, 49*(1-3), 361-395. https://doi.org/10.1016/0004-3702(91)90015-C
30. Hay, N., Russell, S., Tolpin, D., & Shimony, S. E. (2012). Selecting computations: Theory and applications. *Proceedings of UAI 2012*, 346-355. https://arxiv.org/abs/1408.2048
31. Slepian, D., & Wolf, J. K. (1973). Noiseless coding of correlated information sources. *IEEE Transactions on Information Theory, 19*(4), 471-480. https://doi.org/10.1109/TIT.1973.1055037
32. Wyner, A. D., & Ziv, J. (1976). The rate-distortion function for source coding with side information at the decoder. *IEEE Transactions on Information Theory, 22*(1), 1-10. https://doi.org/10.1109/TIT.1976.1055508

33. Gao, X., Akyol, E., & Başar, T. (2018). Optimal communication scheduling and remote estimation over an additive noise channel. *Automatica, 88*, 57-69. https://doi.org/10.1016/j.automatica.2017.10.010
34. Tanaka, T., Kim, K.-K. K., Parrilo, P. A., & Mitter, S. K. (2017). Semidefinite programming approach to Gaussian sequential rate-distortion trade-offs. *IEEE Transactions on Automatic Control, 62*(4), 1896-1910. https://doi.org/10.1109/TAC.2016.2601148
35. Stavrou, P. A., Skoglund, M., & Tanaka, T. (2022). Sequential source coding for stochastic systems subject to finite rate constraints. *IEEE Transactions on Automatic Control, 67*(8), 3822-3835. https://doi.org/10.1109/TAC.2021.3110430
36. Feldman, H., & Friston, K. J. (2010). Attention, uncertainty, and free-energy. *Frontiers in Human Neuroscience, 4*, 215. https://doi.org/10.3389/fnhum.2010.00215
37. Kahneman, D. (1973). *Attention and Effort*. Prentice-Hall.
38. Ma, W. J., Husain, M., & Bays, P. M. (2014). Changing concepts of working memory. *Nature Neuroscience, 17*(3), 347-356. https://doi.org/10.1038/nn.3655
