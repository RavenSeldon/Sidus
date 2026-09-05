# Sīdus: Towards Metarepresentational Ecology
## III. Master's Research: The Tractable Horizon

**University-agnostic Master's scoping note - revised September 2026**

**Status:** a Master's-scale research plan, not the full Sīdus programme.

> **The Master's thesis should test one candidate organizing principle. It should not attempt to establish a metarepresentational ecology.**

---

## 0. Programme and supervision fit

This project can be proposed within an AI, cognitive science, computational neuroscience or related research programme that supports a substantial computational thesis. Its scientific premises do not depend on a university, named specialisation, admissions route or planned start year.

The implementation requires artificial agents, partial observability, learned representations, information constraints, causal interventions and probabilistic model comparison. Suitable supervision combines experience building such systems with scrutiny of construct validity, identifiability and competing explanations.

> **Implementation fit:** probabilistic machine learning, reinforcement learning and artificial cognitive systems.
>
> **Formal/adversarial fit:** computational cognitive science, information theory, control and scientific modelling.

These are selection criteria, not claims about any institution's offerings or supervision availability. Confirm local prerequisites, thesis scope, compute access and supervisory support before committing; the core experiment remains the same.

---

## 1. The Master's project

### Working title

**Internal-State Monitoring Under Scarcity: Causal and Information-Theoretic Tests of Learned Resource Allocation**

### One-sentence question

> **When several private internal control states are useful to a coordinating agent but can only be exposed through a genuinely binding shared information-rate channel, what predicts which states the agent learns to communicate, at what rate, and whether those messages are causally used?**

This is the **E1 Scarcity Terrarium** from the research programme.

It intentionally does **not** ask:

- whether the agent is conscious;
- whether all internal-state messages are strict metarepresentations;
- whether human cognition has one global self-monitoring budget;
- whether a metarepresentational ecology exists;
- whether attention is uniquely privileged.

It tests one possible organizing pressure - **scarcity** - in a substrate where ground truth and interventions are available.

---

## 2. Why this is the right tractable horizon

The full programme contains at least four difficult scientific problems:

1. defining genuine metarepresentation rather than generic internal monitoring;
2. discovering whether monitoring systems share resources;
3. identifying causal-topological relations among them;
4. determining whether any of these principles generalize to biological cognition.

A Master's cannot solve all four without becoming a manifesto rather than a thesis.

The chosen project has a better risk profile:

- **internal states are known by construction;**
- **privacy/access can be controlled;**
- **scarcity can be manipulated rather than inferred;**
- **rate and incremental information can be estimated;**
- **messages can be selectively perturbed;**
- **negative results remain interpretable;**
- **no phenomenality measurement problem is imported.**

The thesis is therefore useful even if the larger ecology hypothesis is wrong.

---

## 3. Thesis architecture

Use a compact partially observed control environment with at least three low-cardinality private states:

\[
C_{1,t},C_{2,t},C_{3,t}.
\]

Candidate functions can include:

- sensory selection / fidelity allocation;
- working-memory update/protection;
- action routing or effector selection.

Each state is generated within a local controller. A coordinating policy \(U\) receives ordinary information \(\mathcal I_t\) but cannot directly inspect the private states.

A source-specific encoder may send a compressed internal-state message:

\[
C_{v,t}\rightarrow S_{v,t}\rightarrow U.
\]

All sources share a total information-rate constraint:

\[
\sum_{v=1}^{K} r_v\le C_{\mathrm{meta}}.
\]

The experimenter supplies the candidate source set; the learned agent determines how much rate each source receives. This is **endogenous allocation**, not spontaneous ontology discovery.

---

## 4. Core quantities

### 4.1 Residual uncertainty

Before receiving the special message, how hidden is the state from ordinary coordinator information?

\[
u_v(t)=
\frac{H(C_{v,t}\mid\mathcal I_t)}{H(C_{v,t})},
\qquad H(C_{v,t})>0.
\]

If \(u_v\approx0\), the special message has little informational problem to solve.

### 4.2 Causal control relevance

For small valid state corruption probability \(\delta\):

\[
c_v(\delta)=
\frac{\mathbb E[J\mid p_v=0]-\mathbb E[J\mid p_v=\delta]}{\delta}.
\]

Use reachable/on-support alternative states rather than arbitrary invalid corruptions.

### 4.3 Learnability

Estimate how quickly the source can be learned under a dedicated, non-scarce channel. Keep this outside the competitive bottleneck so allocation does not contaminate the covariate used to explain allocation.

### 4.4 Compressibility

Estimate an empirical distortion-rate or benefit-rate curve for each source. Easy to learn and easy to compress are distinct.

### 4.5 Rate spent

\[
r_v=
\mathbb E\left[
D_{KL}\left(q(S_{v,t}\mid C_{v,t},\mathcal I_t)
\Vert
p(S_{v,t}\mid\mathcal I_t)\right)
\right].
\]

Treat this as a variational rate-control surrogate.


**[R2 · correction, revised]** The rate--information gap is an identity, not an
assumption: \(r_v=m_v+\Delta_v^{\mathrm{prior}}\), where the mismatch term is an
**expectation over the conditioning variable**,
\(\Delta_v^{\mathrm{prior}}=\mathbb E_{\mathcal I}\,D_{KL}(q(S_v\mid\mathcal I)\Vert p(S_v\mid\mathcal I))\ge0\).
Report \(\Delta_v^{\mathrm{prior}}\) as a measured quantity alongside \(r_v\) and
\(m_v\). See Document IV, §3.3a.

### 4.6 Information delivered

\[
m_v=I(C_{v,t};S_{v,t}\mid\mathcal I_t).
\]

The central distinction remains:

\[
\boxed{r_v\neq m_v.}
\]

### 4.7 Joint benefit surface

\[
\mathcal B(\mathbf r)
=
\mathbb E[J\mid\mathbf r]-\mathbb E[J\mid\mathbf 0].
\]

The normative experimental benchmark is:

\[
\mathbf r^*(C)
=
\arg\max_{\mathbf r\ge0,\;\sum_vr_v\le C}
\mathcal B(\mathbf r).
\]

Do not interpret this as a claim that the learned agent explicitly solves the argmax.

---

## 5. Confirmatory hypotheses

### H1 - Binding scarcity produces a real trade-off

As \(C_{\mathrm{meta}}\) is swept from non-binding to binding capacity, increasing rate to one source should reduce feasible rate available to others and alter performance in predictable ways.

**Against H1:** nominally lower capacity leaves every source fully informative, or no cross-source displacement occurs despite validated rate control.

### H2 - Dynamic control value predicts allocation better than trivial baselines

A joint resource model using measured benefit should predict held-out learned allocations better than:

- uniform allocation;
- source cardinality/entropy alone;
- ordinary inferability alone;
- isolated causal value alone;
- fixed source identity;
- encoder-head identity;
- **myopic value of computation (myopic VOC)** — define eligible increments of monitoring communication and select the increment with greatest **one-step expected net improvement** in downstream decision quality, accounting for communication cost and the option to stop. Specify increment size, information updates and budget feasibility. Rate proportional to gross one-step value is a separate heuristic, not the canonical meta-greedy policy (Russell \& Wefald 1991; Hay et al. 2012; Callaway et al. 2018).

**[Design addition, August 2026 — revised after release-candidate review]**
Uniform allocation is a null; entropy-only, inferability-only and
isolated-causal-value are **simpler structured models**, not nulls, and an
earlier version wrongly lumped all five together. Myopic VOC is added because it
is the closest competitor drawn from an established formalism, and because H4's
topology hypothesis **overlaps conceptually** with value of computation — graph
position is not identical to VOC, but the two are close enough that a topology
result could be a VOC result in different notation. The comparator is
specifically one-step value and is named as such: **myopic VOC**, one
approximation within the metalevel-MDP framework, not VOC in general.

**Against H2:** the richer resource model does not improve out-of-sample
prediction over these baselines. **If it fails specifically against myopic VOC**, the
honest reading is that a joint, budget-constrained resource surface adds nothing
beyond myopic per-source value of computation. That is a clean, publishable
negative result and it should be pre-registered as one.

### H3 - Messages are causally used

Selective corruption/replacement of \(S_v\) should impair the downstream behavior for which information about \(C_v\) is useful, while preserving non-target messages and remaining near trained support.

**Against H3:** \(C_v\) is decodable from \(S_v\) but removing/corrupting \(S_v\) has no relevant behavioral effect.

### H4 - Topology is a candidate secondary predictor

If technically feasible, vary or measure downstream reach/persistence and test whether these properties improve prediction beyond direct causal value and inferability.

This is secondary. It should not endanger completion of H1-H3.

---

## 6. The controls that are not optional

1. **Direct-read oracle.** Give the coordinator direct access to selected private states to estimate the ceiling and verify that hidden-state information can help.
2. **No-seam/full-read control.** Confirm that the communication problem is generated by restricted access rather than the task alone.
3. **Non-binding capacity condition.** All candidate heads must be capable of becoming informative before scarcity is imposed.
4. **Head permutation across seeds.** Source identity must not be confounded with a privileged encoder index.
5. **Scarcity ramp with a real constraint.** Avoid treating a fixed penalty coefficient as equivalent to a known shared budget.
6. **Allocation plateau.** Measure confirmatory rates only after budget, return and rate trajectories stabilize by a preregistered rule.
7. **From-scratch diagnostic for selected conditions.** If ramped and from-scratch training disagree, report optimization hysteresis.
8. **Held-out environments/contingencies.** The allocation model should predict more than the exact configurations used to fit it.

These controls are the scientific core. They are more important than decorative model complexity.

---

## 7. What is deliberately excluded from the core thesis

### No primary attention residual

The earlier Sīdus question asked whether attention received excess rate relative to a resource baseline. In the new programme, attention is one source among others. Generic residuals may be inspected, but the thesis does not depend on a special attention effect.

### No strict-metarepresentation claim

The messages in this experiment are **internal-state models**. That terminology avoids pretending the project has already solved the contested definition of metarepresentation.

### No causal abstraction by default

Interchange-intervention/causal-abstraction analysis is elegant but high overhead. Use it only if a robust role-dependent effect has already been established and the high-level role claim materially matters.

### No Gaussian-process Bayesian optimization by default

Start with a small factorial/simplex design. Escalate to Astrocyte only if training evaluations become sufficiently expensive that active surface estimation is justified.

### No human or clinical translation

A human study should not be added as a thesis appendix merely to make the work look neuroscientific. Biological translation becomes meaningful after construct validity and a reproducible computational phenomenon exist.

---

## 8. One optional extension - choose at most one

If H1-H3 are completed early and cleanly, choose **one** extension.

### Option A - strict metarepresentation benchmark

Add a source whose target is a representational property/process, such as a hidden reliability/source regime affecting a first-order perceptual representation. Test whether a meta-process model beats matched first-order/public-context alternatives.

**Why this option is attractive:** it ties the thesis more directly to the broader programme while preserving a clear computational manipulation.

### Option B - recursive allocator monitor

Add a first-order resource allocator with \(C_{\mathrm{base}}\) and a separate monitoring budget \(C_{\mathrm{meta}}\). Compare feedback-enabled and frozen-feedback conditions.

**Why this option is attractive:** it retains the strongest S1-R idea and connects to meta-control.

### Option C - causal topology

Manipulate downstream reach/persistence for one source and ask whether benefit/allocation follows causal position.

**Why this option is attractive:** it tests a candidate organizing principle directly.

**Rule:** completing the core thesis beats attempting two extensions.

---

## 9. Stage gates and adaptable research schedule

The schedule below illustrates an eight-to-nine-month research window. It is not a credit, degree-duration or institutional-timetable claim. Adapt the scope to the host programme's thesis allocation and supervision; for a shorter window, retain E0-A validation and core H1-H3 while dropping extensions.

| Stage | Illustrative project window | Deliverable | Stop/narrow decision |
|---|---:|---|---|
| Prior art + construct freeze | month 1 | concise literature/claim register; frozen core question | if E1 is already duplicated exactly, redesign before coding |
| Environment + baseline | months 1-2 | compact POMDP; working local controllers; direct-read baseline | if private states do not matter to performance, redesign task |
| Measurement and gate validation | month 2 | exact-reference \(r_v,m_v,u_v\) checks and complete-evaluator negative controls before pilot threshold selection | if quantities or gate decisions are unreliable, simplify the simulator |
| Non-binding communication | months 2-3 | all heads demonstrably informative | if heads cannot learn, do not impose scarcity |
| Scarcity pilot | months 2-3 | stable rate-control manipulation and preliminary trade-offs | **Gate:** if no real trade-off, narrow/stop scarcity claim |
| Freeze + preregister analysis | end of month 3 | fixed environment, manipulations, models and seed/precision plan | no confirmatory tuning afterward |
| Confirmatory E1 | months 4-6 | held-out allocation/return data across seeds | if results are path-dependent, report that rather than hiding it |
| Causal-use + topology secondary | months 6-7 | selective interventions; optional topology test | drop secondary analyses if core is not complete |
| Optional single extension | month 7 | E2 *or* recursive *or* topology extension | optional, never required for success |
| Replication + writing | months 8-9 | thesis, code, data, negative-result ledger | finish before expanding |

---

## 10. Curriculum and methods alignment

Evaluate a prospective programme by access to the methods the thesis needs, rather than course titles or a particular specialisation:

- **Probability, statistics and Bayesian modelling:** uncertainty, calibration and model comparison.
- **Machine learning and neural computation:** learned encoders, consumers and representation controls.
- **Reinforcement learning and decision processes:** partial observability, policies and task value.
- **Information theory and constrained optimisation:** conditional information, rate surrogates and feasibility.
- **Causal inference and computational modelling:** selective interventions, identifiability and competing explanations.

Coursework, supervised reading or prior experience can supply these foundations. Information theory and experimental design must be explicitly covered even if absent from the formal curriculum. Neuromorphic systems, BCI and biological implementation are optional directions, not prerequisites for the synthetic core.

---

## 11. Preparation and prerequisite gaps

Assess preparation individually, whether entry is direct or involves a bridging programme. Relevant foundations are programming, calculus, linear algebra, probability and statistics, followed by machine learning, reinforcement learning and computational cognition.

The dependency sequence is:

\[
\begin{array}{c}
\text{probability and programming}\rightarrow\text{information theory and optimisation}\\[3pt]
\rightarrow\text{RL/POMDPs and probabilistic modelling}\rightarrow\text{causal experimental design}.
\end{array}
\]

Use small implementations to identify gaps before expanding the research environment. A particular admissions pathway or named preparatory course is not a scientific assumption of the thesis.

---

## 12. Research-group and supervisor fit

### Implementation support

Look for experience with learned agents, probabilistic models, representation learning or computational neuroscience, plus sufficient compute and time for independent runs and intervention checks. Complete simulator access is essential during the synthetic phase; a biological dataset is not required.

### Formal and adversarial support

Look for supervision that can challenge the construct, assess identifiability and computational tractability, and demand comparisons with established communication, control and metareasoning models. Computational modelling should force theoretical commitments to become testable; relevant methodological precedents include Guest & Martin and van Rooij & Baggio. [1,2]

One supervisor or a complementary supervisory team may provide this combination. Confirm actual interest and availability rather than inferring them from a lab label. The project fits a host through its methods and question, not through an institutional affiliation.

---

## 13. What to bring to a prospective supervisor

Bring a **two-page study**, not the whole Sīdus history.

The supervisor-facing package should contain:

1. one paragraph of prior art;
2. one computational question;
3. one architecture diagram;
4. H1-H3;
5. the direct-read/no-seam/scarcity controls;
6. the estimands \(r_v,m_v,\mathcal B(\mathbf r)\);
7. the primary comparison models;
8. one paragraph of kill criteria;
9. a compute pilot plan.

Questions worth asking:

- Is the shared-rate competition experiment already present in a literature we have missed?
- Is the proposed information seam a useful abstraction for this lab, or does it bake in too much modularity?
- What simpler baseline would you demand before accepting the joint resource model?
- Would you consider the artificial-agent result cognitively explanatory, or only an engineering demonstration?
- Which part should be removed to fit a Master's timeline?
- Which lab infrastructure or existing environment could make the test cheaper and more biologically meaningful?

---

## 14. What not to say in a Master's proposal

Do not say:

- "I am developing a theory of metarepresentational ecology."
- "The brain has a global metarepresentational budget."
- "This model explains consciousness."
- "Attention is uniquely worth monitoring."
- "The model discovers its own self."
- "The glyphs represent deep computational principles."

Say:

> **I want to test whether a binding information-rate constraint produces predictable competition among models of private internal control states in a modular learning agent, and whether the resulting messages are causally used. This is one candidate mechanism that could later inform a broader construct-first account of internal monitoring.**

That is enough.

---

## 15. Success conditions

The Master's is successful if any one of the following is established cleanly:

- a real shared rate constraint produces stable, reproducible allocation trade-offs;
- a joint benefit model predicts learned allocation out of sample;
- a simpler model explains everything and the larger allocation story is unnecessary;
- rate allocation is strongly path-dependent, showing that the apparent "law" is an optimization history;
- transmitted internal-state information is decodable but behaviorally unused;
- the information seam proves unnecessary in the tested task;
- a controlled topology manipulation changes monitoring value;
- the experiment falsifies a central assumption and thereby prevents the larger programme from building on it.

The worst outcome is not a null result.

The worst outcome is an ambiguous system with too many moving parts to know what failed.

---

## 16. The tractable horizon

The Master's should end with one of two conclusions.

### Positive

> **Under controlled partial access and a binding information-rate constraint, learned internal-state monitoring exhibits a reproducible allocation principle that survives simpler baselines and causal-use tests. This justifies testing whether the same principle applies to stricter metarepresentations or other architectures.**

### Negative

> **The tested scarcity formulation does not produce a stable/generalizable allocation principle, or its effects reduce to simpler inferability, implementation or optimization factors. The broader programme should not treat scarcity as an organizing law without a different empirical basis.**

Both conclusions move the programme forward.

A one-paper thesis that kills a grander idea remains a successful scientific outcome.

---

# References

1. Guest, O., & Martin, A. E. (2021). How computational modeling can force theory building in psychological science. *Perspectives on Psychological Science, 16*(4), 789-802. https://doi.org/10.1177/1745691620970585
2. van Rooij, I., & Baggio, G. (2021). Theory before the test: How to build high-verisimilitude explanatory theories in psychological science. *Perspectives on Psychological Science, 16*(4), 682-697. https://doi.org/10.1177/1745691620970604
3. Russell, S., & Wefald, E. (1991). Principles of metareasoning. *Artificial Intelligence, 49*(1-3), 361-395. https://doi.org/10.1016/0004-3702(91)90015-C
4. Hay, N., Russell, S., Tolpin, D., & Shimony, S. E. (2012). Selecting computations: Theory and applications. *Proceedings of UAI 2012*, 346-355. https://arxiv.org/abs/1408.2048
5. Callaway, F., Gul, S., Krueger, P., Griffiths, T. L., & Lieder, F. (2018). Learning to select computations. *Proceedings of UAI 2018*. https://auai.org/uai2018/proceedings/papers/269.pdf
