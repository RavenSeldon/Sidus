# Sīdus: Towards Metarepresentational Ecology
## I. Foundations: Constructs, Boundaries, and Empirical Warrant

**Working research document - August 2026**  
**Status:** construct-first foundation. This document proposes no theory of consciousness and does not assert that a unified metarepresentational ecology exists.

> **Truth, maximally sought. Ambition tempered by humility. Beauty tempered by goodness. Honesty above all else.**

---

## 0. The claim in its strongest defensible form

Cognition contains multiple systems that **monitor, estimate, model, or regulate internal states and processes**. Metacognitive confidence, source monitoring, error monitoring, cognitive control, meta-control, and self-modeling are established research domains. Some internal models may satisfy stronger criteria for **metarepresentation**; others may not. Evidence from metacognition already suggests a mixture of domain-specific and shared organization rather than a single universal monitor. The existence of these mechanisms does **not** yet establish that they form one coherent ecology, share one resource pool, obey one allocation law, or have any constitutive relation to phenomenal consciousness.

The programme therefore asks a narrower question:

> **Do internal monitoring and metarepresentational systems exhibit reproducible relational principles - such as scarcity, causal-topological dependence, recursive control, fidelity constraints, complementarity or substitution - that generalize beyond a single task or architecture?**

The word **ecology** is a hypothesis about organization, not an accomplished result. It earns scientific content only if multiple locally validated mechanisms interact in regular ways that support prediction, intervention, and generalization.

---

## 1. Why move upstream from consciousness?

The immediate motivation is methodological, not metaphysical. Consciousness science has accumulated sophisticated theories but still faces difficult disputes about how behavioural and neural measurements license claims about phenomenality. Doerig, Schurger and Herzog proposed stringent empirical criteria partly to prevent theories from insulating themselves against functionally equivalent alternatives. Their criteria have themselves been criticized for placing too much weight on functional equivalence rather than mechanistic explanation. The useful lesson is therefore not that one checklist solves consciousness science, but that a scientific construct must expose the conditions under which it would lose to a simpler or mechanistically different account. [1,2]

A closely aligned methodological precedent is the **construct-first approach** of Fazekas, Cleeremans and Overgaard. Instead of beginning with entire theories of consciousness, they recommend decomposing theories into central constructs - including metarepresentation, recurrent processing and global workspace - and investigating their lower-level mechanisms, compatibility and combinations. [3]

This package takes that move further for one construct family. It deliberately suspends the question:

\[
\text{Which mechanism constitutes phenomenality?}
\]

and instead asks:

\[
\begin{array}{c}
\text{What internal models exist, what are they about,}\\[3pt]
\text{who generates them, who uses them, and how do they interact?}
\end{array}
\]

If the answers later constrain consciousness theories, that is downstream. The programme remains successful if phenomenality is never explained.

---

## 2. What the literature permits us to take seriously

### 2.1 Internal monitoring and metacognition are real empirical targets

Metacognition is routinely studied as the monitoring and control of cognitive processes. Computational and neurobiological work distinguishes first-order task performance from second-order evaluations such as confidence, and identifies both common and domain-specific neural contributions. [4-7]

This does **not** establish one metacognitive system. A major review of perception and memory found no evidence for the strongest form of domain-general metacognition, while still identifying common computational ingredients. [7] A 2026 developmental study found that confidence bias is shared across memory and perception while sensitivity and efficiency remain domain-specific; the ability to compare confidence across domains emerges developmentally. [8] That is exactly the kind of mixed architecture that makes an ecological hypothesis plausible without making it inevitable.

### 2.2 Monitoring need not equal metarepresentation

Proust's process-reflexive account is an important boundary condition. A task-specific system can monitor its own feedback using quantitative cues without representing those cues *as mental representations*. Metacognition therefore does not automatically entail metarepresentation. [9]

This means the programme must resist three invalid inferences:

\[
\text{internal signal} \not\Rightarrow \text{metarepresentation},
\]

\[
\text{monitoring} \not\Rightarrow \text{metarepresentation},
\]

\[
\text{second neural layer} \not\Rightarrow \text{metarepresentation}.
\]

### 2.3 There are serious, competing definitions of metarepresentation

The term is not settled enough to be used as if it named an obvious natural kind.

**Content-based criterion.** Shea argues that a metarepresentation must concern a *representational property* of another representation. Merely tracking the vehicle state of another neural population is insufficient; some property such as its content, correctness, truth condition, or likely error must figure in the meta-state's correctness conditions. Shea uses this criterion to argue that reward prediction error signals can have low-level, non-conceptual metarepresentational content. [10]

**Representational-redescription criterion.** Cleeremans' Radical Plasticity Thesis and later Self-Organizing Metarepresentational Account (SOMA) emphasize learning to redescribe first-order activity. Higher-order systems learn properties and relations of first-order representations and make knowledge that is merely *in* the system increasingly available *to* the system. [11-13]

**Process-representation criterion.** Kanai, Takatsuki and Fujisawa sharpen the computational problem in 2025. If every mapping \(x\to y\to z\) makes \(z\) a metarepresentation of \(y\), then metarepresentation becomes trivial and ubiquitous. They propose instead that a metarepresentation can represent the **process that transforms input into a first-order representation**, and demonstrate a proof-of-concept in artificial neural networks. [14]

These views overlap but are not equivalent. The programme therefore does **not** legislate one philosophical definition as fact. It uses a graded operational taxonomy and asks which definitions support reproducible causal and computational distinctions.

---

## 3. Construct lexicon

The programme begins with typed objects rather than one undifferentiated latent space.

| Symbol / term | Working meaning | What it is not |
|---|---|---|
| \(X_t\) | external or bodily state relevant to a system | not necessarily represented faithfully |
| \(R_t\) | first-order representation of some target \(X_t\) | not automatically conscious |
| \(C_t\) | internal control/process state, e.g. a gate, allocator, gain regime | not necessarily a representation |
| \(S_t\) | internal-state model: a state carrying information about \(C_t\) or another internal variable | not automatically a strict metarepresentation |
| \(F\) | a computational/representational process, e.g. mapping \(X\mapsto R\) | not a single activation state |
| \(M_t\) | candidate metarepresentation: a state about a representational property or process of \(R\) or \(F\) | not defined merely by being one layer downstream |
| \(G\) | generator/monitor that constructs \(S\) or \(M\) | not assumed to be one anatomical area |
| \(U\) | consumer that uses \(S\) or \(M\) for inference, control, report or learning | not necessarily a global workspace |
| \(T_v\) | generic target variable in the abstract rate formalism; may denote an internal control state or a representational property/process depending on the experiment | not a separate ontological category beyond the typed targets above |
| \(Z_v\) | generic transmitted code/message about \(T_v\) in the abstract rate formalism | not a commitment to a particular coding architecture or message alphabet |
| \(r\) | resource/rate spent transmitting or maintaining a model | not identical to information successfully conveyed |
| \(m\) | incremental information made available about the target | not identical to channel cost |

### 3.1 Internal-state model versus strict metarepresentation

The earlier Sīdus package called a compressed message about an attention, memory or action-routing controller a metarepresentation. That is defensible under a **minimal functional self-monitoring** usage, but too permissive for a programme that wants metarepresentation itself to carry explanatory weight.

We therefore separate:

\[
C_t \xrightarrow{G} S_t
\]

from:

\[
R_t \text{ or } F \xrightarrow{G} M_t.
\]

A message such as

> "the sensory-selection controller currently prioritizes the left"

is an **internal-state model** unless the target controller state is independently shown to be representational in the relevant sense.

A message such as

> "the current visual representation is likely to be unreliable"

or

> "the mapping currently generating this visual representation has a high-noise / biased transformation regime"

is a stronger candidate metarepresentation because its target is a representational property or representational process.

### 3.2 Metacognition

Metacognition is treated as a functional family involving evaluation or control of cognition. It may be implemented by strict metarepresentations, process-reflexive cues, domain-specific monitors, domain-general confidence metrics, or mixtures of these. The programme must not define metacognition and metarepresentation as synonyms.

### 3.3 Meta-control

Meta-control concerns monitoring and regulating control strategies or parameters themselves. Contemporary reviews define it as mechanisms that monitor controlled processing and adjust underlying control parameters in response to goals and constraints. [15] The online metacognitive control of decisions (oMCD) provides a concrete computational example in which confidence and effort are used to regulate further decision processing. [16]

Meta-control is therefore established neighbouring territory for any recursive Sīdus experiment.

---

## 4. A graded empirical membership test

Because the ontology is contested, this package uses **evidence tiers** rather than declaring a universal essence of metarepresentation.

### Tier 0 - correlation / decodability

A candidate signal \(Z\) covaries with an internal target \(T\), or a probe can decode \(T\) from \(Z\).

This is weak evidence only.

\[
I(Z;T)>0
\]

can arise because both variables share a common external cause.

### Tier 1 - conditional representational specificity

The candidate carries information about an internal representational property after relevant external and publicly available information is controlled:

\[
I(M;\phi(R)\mid X,\mathcal I)>0,
\]

where \(\phi(R)\) is a representational property such as source, accuracy, uncertainty, content relation, calibration, or process regime.

This is an informational specificity criterion, not a universal prerequisite for every redescription account. For a bounded-consumer RR operationalization, preregister accessibility and consumer-role tests separately from absolute information; do not demand new Shannon information beyond a deterministic redescription's complete inputs. See Document IV §7.

### Tier 2 - decoupling and misrepresentation

The candidate can be wrong about its target. A confidence estimate can be high when the first-order representation is wrong; a source monitor can misattribute memory as perception; a process model can infer the wrong transformation regime.

Misrepresentation matters because a signal that can never dissociate from its target may be a copy or common downstream consequence rather than a model.

### Tier 3 - causal dependence

Intervene on the target representational property or process while controlling competing causes:

\[
\operatorname{do}(\phi(R)=a) \Rightarrow M\text{ changes as predicted}.
\]

### Tier 4 - causal use

Intervene selectively on \(M\) while preserving the first-order representation and non-target signals. A downstream consumer should change behaviour in the direction predicted by the claimed meta-level content.

\[
\operatorname{do}(M=m') \Rightarrow U\text{ changes},
\]

while \(R\) remains approximately intact.

**Decodability is not use.** This principle is inherited from the strongest part of the earlier Sīdus package.

### Tier 5 - generalization / role dependence

The relation survives changes in superficial implementation, environment and task, or follows a validated causal role under controlled role permutation. This is the point at which the programme begins to earn a law-like claim rather than a task-specific circuit description.

---

## 5. What "ecology" means here

The term is useful only if it imposes burdens that "collection of mechanisms" would not.

A provisional ecological object is a **dynamic typed relational graph**:

\[
\mathcal E_t=(\mathcal N_t,\mathcal R_t,\mathbf C_t),
\]

where:

- \(\mathcal N_t\) contains typed targets, representations, internal-state models, metarepresentations, generators and consumers;
- \(\mathcal R_t\) contains empirically validated relation types;
- \(\mathbf C_t\) contains resource constraints that may limit communication, memory, computation, energy, time or plasticity.

The graph is **not written down in advance**. It is reconstructed only from locally validated edges.

Candidate relation types include:

| Relation | Meaning | Example empirical signature |
|---|---|---|
| represents / monitors | one state carries specific information about an internal target | conditional prediction + intervention |
| controls | a model alters a downstream policy or process | selective perturbation changes behaviour |
| predicts | one model forecasts another state/process | out-of-sample prediction |
| competes | two models draw on a shared limited resource | increasing one degrades the other under fixed capacity |
| complements | one model raises the marginal utility of another | positive interaction in joint benefit surface |
| substitutes | one model lowers the marginal utility of another | negative interaction in joint benefit surface |
| recursively regulates | a model of control changes future control | feedback condition outperforms matched frozen-feedback condition |
| persists / integrates across time | value depends on temporal horizon or lag | interaction with horizon, autocorrelation or delayed control |

An ecology is established only if some of these relations generalize beyond one engineered task.

---

## 6. Order, topology and geometry must remain separate

The earlier conversation repeatedly risked collapsing distinct mathematical ideas.

### Representational order

A representation may be first-order, second-order, or recursively higher-order in virtue of what it is about. This is a **logical/relational order**, not a quantity of consciousness.

### Graph topology

A model may occupy a causal bottleneck, have many downstream dependents, or connect otherwise separated subsystems. This is a property of a **network of causal relations**.

### Representational geometry

A population or latent representation may occupy a multidimensional embedding whose distances encode similarity or other structure. This is **state-space geometry**.

These concepts can interact, but they are not interchangeable.

This is fully compatible with Bayne, Hohwy and Owen's rejection of a single scalar "level of consciousness". Their argument targets global ordinal rankings of consciousness while allowing multidimensional profiles and ordering along particular dimensions. [17] Nothing in that argument prohibits relational order, graph topology, or representational geometry in a non-phenomenal theory.

The programme therefore rejects language such as "higher levels of the ecology" unless the order relation is explicitly defined.

---

## 7. First candidate organizing principles

These are **hypothesis families**, not laws.

### 7.1 Scarcity

Internal models can be costly to transmit, maintain or make globally usable. Resource-rational analysis already studies cognition as adaptation under limited computational resources, and Expected Value of Control formalizes allocation of control according to payoff and effort. [18,19] Information theory provides mature machinery for rate-distortion and distributed coding, including the CEO problem in which multiple encoders send compressed observations of a common source to a central estimator under rate constraints. [20]

The open question is not whether scarcity exists in cognition. It is whether **specific internal monitoring systems compete in reproducible ways for a shared resource**, and whether the allocation can be predicted from measurable properties of the monitored targets.

### 7.2 Causal topology

The value of monitoring a state may depend not only on uncertainty but on its causal position. A state that changes the interpretation or reliability of many downstream signals may be disproportionately worth monitoring. This predicts that downstream reach, bottleneck position, persistence and number of dependents can explain monitoring value.

Causal abstraction and interchange interventions provide tools for testing whether a low-level implementation really realizes a hypothesized high-level causal role. [21-23]

### 7.3 Recursive control

A system may benefit from modelling the state of a controller or allocator because knowledge of realized control can improve future commands. This overlaps strongly with meta-control, rational metareasoning and oMCD; novelty cannot be assumed. The tractable hypothesis is whether a *specific* monitoring relation adds future-control value once immediate interpretive value is controlled.

### 7.4 Fidelity and misrepresentation

A self-model is useful only to the extent that it tracks the relevant target at the resolution required by its consumer. High decodability does not guarantee calibrated, causally used or decision-relevant representation. Metacognitive research already documents systematic divergence between first-order performance and confidence. [4,5]

### 7.5 Complementarity and substitution

Two internal models may be jointly more useful than expected from their isolated effects, or one may make another redundant. This is why the earlier Sīdus shift from additive source curves to a joint benefit surface should be preserved.

### 7.6 Temporal niche

Targets with different update rates, persistence and future consequences may require different monitoring policies. Fast volatile processes may need high-frequency low-fidelity monitoring; slow persistent processes may justify lower-frequency richer summaries. This is a candidate law, not an established result.

---

## 8. The resource formalism retained from Sīdus

The old Sīdus experiment contributed a useful distinction that survives the reframing.

For source \(v\), define a variational rate cost:

\[
r_v=
\mathbb E\left[
D_{KL}\left(q(Z_v\mid T_v,\mathcal I)\Vert p(Z_v\mid\mathcal I)\right)
\right].
\]

When sources share a budget,

\[
\sum_v r_v\le C.
\]

Separately define incremental information delivered about the target:

\[
m_v=I(T_v;Z_v\mid\mathcal I).
\]

The key distinction remains:

\[
\boxed{r_v\neq m_v.}
\]

A system can spend substantial capacity while conveying little useful information. The KL quantity is a variational rate surrogate, not exact mutual information. The target \(T_v\) may be an internal control state in a self-monitoring experiment or a representational property/process in a stricter metarepresentational experiment.

A joint benefit surface remains the safest normative object:

\[
\mathcal B(\mathbf r)=\mathbb E[G\mid\mathbf r]-\mathbb E[G\mid\mathbf 0],
\]

with the experimental optimum

\[
\mathbf r^*(C)=\arg\max_{\mathbf r\ge0,\;\sum_vr_v\le C}\mathcal B(\mathbf r).
\]

This is an **experimenter's benchmark**, not a claim that biological agents solve a global optimization problem. Critiques of resource-rational analysis correctly warn against sliding from a normative modelling device to the substantive claim that humans are resource-optimal. [24]

---


### 8.1 Closest classical analogues, and which special cases are actually solved

**[R1 · correction, August 2026 — revised after release-candidate review]**

The rate formalism above was previously presented as generic bottleneck
machinery. It has older relatives, and naming them separates what is solved from
what is open. An earlier version of this section identified E1 *with* the CEO
problem in its Wyner--Ziv variant. That identification was wrong in two specific
ways, and the corrected version is stated here.

**Where E1 actually sits.** The consumer receives ordinary public information
\(\mathcal I_t\) before any monitoring message arrives, and the specified source
encoder is itself of the form \(q(S_v\mid C_v,\mathcal I)\). In the default E1
architecture, then, \(\mathcal I\) is **common side information available to both
encoder and consumer**, not decoder-only side information. Several encoders, each
with private access to one source in addition to that common information, transmit
under a shared sum-rate constraint to a single consumer. That places E1 in the
family

\[
\begin{array}{c}
\text{multiterminal / distributed lossy source coding with side information}\\[3pt]
+\;\text{networked estimation and control}
\end{array}
\]

with CEO-, Slepian--Wolf- and Wyner--Ziv-like *constructed special cases*, rather
than being identical to any one of them. Wyner--Ziv is relevant only when a
special case with side information unavailable to the encoder is deliberately
constructed.

**Why not the CEO problem.** The classical CEO problem is a **remote-source**
problem: several agents observe independently corrupted versions of one common
hidden source and transmit to a central estimator (Berger, Zhang \&
Viswanathan 1996). E1 begins with several potentially **distinct** controller
states \(C_1,\dots,C_K\), which need not be noisy views of a single latent
variable. Particular E1 configurations can be constructed to instantiate a CEO
structure; the general architecture does not.

**What \(u_v\) is, and what it is not.** In the **single-source lossless**
case, \(H(C_v\mid\mathcal I)\) is the natural conditional-entropy rate benchmark.
Slepian--Wolf supplies the corresponding distributed lossless benchmark when
correlated sources are separately encoded and jointly decoded (Slepian \& Wolf
1973). In a genuinely multiterminal lossless E1 special case, the relevant object
is the full Slepian--Wolf rate region (conditional on \(\mathcal I\) when that
information is shared), not a collection of independent per-source conditional
entropies. Under **lossy** coding the operative rate depends on the
distortion criterion, and the Wyner--Ziv rate-distortion function involves a
minimisation over an auxiliary variable subject to a distortion constraint when
side information is decoder-only (Wyner \& Ziv 1976). So

\[
u_v=\frac{H(C_v\mid\mathcal I)}{H(C_v)}
\]

is a well-motivated **dimensionless normalised residual-uncertainty measure**. In
the single-source lossless limit it can be interpreted as the minimum conditional
rate **normalised by \(H(C_v)\)**; it is not itself a coding rate. It is not "the
Wyner--Ziv rate," and the earlier claim that it was is withdrawn.

**How much is actually solved.** Less than the earlier version implied. The
general multiterminal lossy source-coding problem has been open for decades.
Solved cases relevant here are narrow and specific:

| Case | Status | Source |
|---|---|---|
| Distributed **lossless** coding of correlated sources | solved rate region | Slepian \& Wolf (1973) |
| Single-source **lossy** coding with correlated side information available only at the decoder | solved rate-distortion function | Wyner \& Ziv (1976) |
| Scalar quadratic-Gaussian CEO | solved | Oohama (1998); Prabhakaran, Tse \& Ramchandran (2004) |
| Two-encoder quadratic-Gaussian | solved | Wagner, Tavildar \& Viswanath (2008) |
| Vector Gaussian CEO, quadratic distortion | outer bound generally **not** tight | Ekrem \& Ulukus (2014) |
| General multiterminal lossy | **open** | --- |

**What this changes, and what it does not.** It removes a false comfort: E1 does
not inherit an analytic solution. It sits adjacent to an **open** problem class,
which is a more defensible position than the one previously claimed, and it makes
the calibration requirement sharper rather than weaker. The validation target
must be a **deliberately constructed solved special case** --- a scalar
quadratic-Gaussian configuration whose optimum is known --- used to check that the
learned allocation recovers a known answer where one exists. A pipeline that
cannot do that has not earned interpretation where no answer is known.

The surviving **candidate contribution [N?]** is narrow: allocation over
non-Gaussian, low-cardinality, agent-generated control states, with expected
return as the distortion measure, where the encoders are **learned rather than
designed**. Per C5 below, this remains a candidate contribution rather than a
novelty claim until its own prior-art row has been systematically searched.

## 9. Methodological constraints for the new programme

The strongest constraints from the old master are retained but rewritten around constructs rather than consciousness.

### C1 - Declare the construct and target

Every study states:

1. what is being represented or monitored;
2. whether the target is an ordinary internal state, a first-order representation, or a representational process;
3. which operational definition of metarepresentation is being tested;
4. what observable pattern would distinguish it from a simpler first-order transformation.

### C2 - Keep levels and timescales separate

Fast activation states, learned parameters, process descriptions, capacities, graph topology and representational geometry do not share one time index merely because they can all be written as vectors.

### C3 - Local models under identifiability

A study names at least one competing model that predicts a different intervention effect. If two models imply indistinguishable observations under the available interventions, the study does not adjudicate them.

### C4 - Causal use over decodability

A representation that is readable but behaviorally unused does not earn the claimed control function.

### C5 - Deposited novelty

No claim is called new because it was independently derived. Potential novelty remains **[N?]** until the relevant prior-art row is systematically searched.

### C6 - Method proportional to evidence

The methodological overhead cannot outrun the existence of the phenomenon. Simple pilots precede GP surrogate modelling, causal abstraction, large sweeps or human translation. A sophisticated estimator does not rescue a nonexistent effect.

---

## 10. Doerig retained as adversarial pressure, not ontology

The programme borrows the empirical spirit of Doerig's hard criteria without pretending that consciousness-specific problems remain unchanged after phenomenality is removed.

| Doerig-style pressure | Construct-first analogue |
|---|---|
| functionally equivalent alternatives | create matched systems where simple first-order transformations and genuine candidate meta-processes make different intervention predictions |
| unfolding / internal-organization concern | require internal topology to generate causally testable consequences, not merely different diagrams |
| small-network problem | prevent the definition of metarepresentation from becoming so permissive that every multilayer transformation qualifies |
| other-systems problem | state what should generalize across architectures, species or task domains before looking at results |
| falsifiability | preregister what would count against each local hypothesis |

Doerig is therefore an **empirical acid test**. It is not the metaphysical spine of the programme.

---

## 11. What is currently established, suggested, and open

### Established or strongly literature-supported

- Cognitive systems exhibit metacognitive monitoring and control.
- Confidence and uncertainty can be computationally and neurally dissociated from first-order performance.
- Metacognition shows mixtures of shared and domain-specific organization.
- Meta-control monitors and regulates lower-level control processes.
- Limited computational resources and resource allocation are established modelling problems.
- Distributed modules can communicate through restricted channels in engineered neural architectures.
- Rate-distortion and distributed source coding provide mature mathematical machinery.
- Causal abstraction offers formal methods for testing high-level role claims in artificial systems.

### Suggested but not established as one framework

- Internal monitoring systems may interact through shared constraints.
- Some relations may be better described as an ecology than as isolated modules.
- Causal topology may predict which internal processes are worth modelling.
- Cross-domain confidence may provide a common currency while retaining domain-specific sensitivity.
- Recursive monitoring of control may improve future control under specific conditions.

### Open

- Whether strict metarepresentations, under a defensible definition, are widespread in biological cognition.
- Whether there is any shared metarepresentational resource budget in brains.
- Whether one or several resource currencies govern internal monitoring.
- Whether ecology-level relational laws generalize across tasks and architectures.
- Whether higher-order representational order has any privileged relation to control or learning.
- Whether process metarepresentations have identifiable neural implementations.
- Whether this programme adds predictive value beyond existing metacognition, meta-control, resource-rational and modular-computation literatures.
- Any constitutive relationship to phenomenality.

---

## 11A. Correction register - external review pass, August 2026

This register lives inside Document I rather than in a separate file, because
the Tractable Horizon rule permits revision under external criticism but not the
proliferation of companion documents. Nothing here is a new idea; every entry is
a repair to something already written.

### Corrections adopted

Rows marked ⚑ were themselves corrected in the release-candidate pass. The
original wording is retained so the record shows what was claimed and when, but
no ⚑ row should be read as the package's current position without reading the
retraction section that follows.

| ID | Correction | Lands in | What it repairs |
|---|---|---|---|
| **R1** ⚑ | *Superseded in part — see "Corrections to the corrections" below.* As first written: the rate formalism is the **CEO problem with decoder side information** (Wyner--Ziv). \(u_v\) is the theoretically indicated quantity, not an ad hoc covariate; the Gaussian case supplies a derived benchmark independent of the training procedure. | Doc I §8.1 | An unnamed frame that concealed which parts of the problem are already solved |
| **R2** ⚑ | \(r_v=m_v+\Delta_v^{\mathrm{prior}}\) is an **identity**, not an assumption — *as first written the mismatch term lacked its expectation over \(\mathcal I\); corrected below.* The redundant-coding signature decomposes into prior mismatch plus excess rate, both estimable. | Doc IV §3.3a; Doc III §4.5 | An asserted inequality, and a diagnostic that could not be measured |
| **R3** ⚑ | Cross-source leakage must be measured **conditionally** on \(\mathcal I\). Unconditional \(I(S_u;S_v)\) flags correct architectures as cheating. The fault condition was first given as \(I(C_u;S_v\mid\mathcal I)\) — ⚑ *superseded; the correct diagnostic conditions on \(C_v\) as well, see below.* | Doc IV §5A | A preventive fix: the error is not yet in the protocol, and would have entered at implementation |
| **R4** | Five uncited adjacent literatures, each positioned in one paragraph: MARL communication, information-theoretic bounded rationality, rational inattention, VoI sensor scheduling, value of computation. | Doc II, Part 0 | Constraint C5 executed on the metacognition side and not on the information-theory side |

### Design additions

| Addition | Lands in | Why |
|---|---|---|
| **Dual-arm constraint implementation** — variational surrogate *and* total-alphabet-cardinality with a learned split, \(\sum_v\log_2\vert\mathcal Z_v\vert\le C_{\mathrm{meta}}\). First proposed with rank-order invariance across arms as a confirmatory prediction — ⚑ *superseded; the arms price different currencies, see below.* | Doc II §10 | A KL-surrogate budget is soft; a naive hard channel destroys the factorisation that makes \(r_v\), \(m_v\) and targeted intervention identifiable. The split-alphabet construction is hard, shared and factorised at once |
| **Value of computation added to the H2 baseline set.** | Doc III §5; Doc II §10 | Uniform allocation is the null; entropy-only, inferability-only and isolated-causal-value are simpler structured competitors. Myopic VOC is the closest comparator drawn from an established metareasoning formalism. |

### Corrections considered and declined

Recording rejected advice with reasons is part of the same discipline as
recording accepted advice.

**Declined: "the normative benchmark is trivially matched — optimizer matches
optimizer."** This was correct against the *earlier* Sīdus, whose confirmatory
estimand was the deviation of observed allocation from \(\arg\max\mathcal B\)
computed under the same training procedure — making the null the procedure's own
first-order condition. It is **stale against the present package**. H2 is now an
**out-of-sample predictive comparison** of a joint resource model against named
baselines on held-out environments, not an argmax-matching test. \(\mathbf
r^*(C)\) is retained only as a benchmark under anti-slop rule 5. The criticism
should not be re-imported.

**Declined as stated: "enforce the budget at the channel level instead of the
variational surrogate."** The diagnosis is right and the prescription is not.
Per-source codebooks give every source its own hard cap and abolish competition;
a single shared codebook abolishes source-factorisation and with it Gates A3 and
A4 and hypothesis H3. The **initial** repair was the split-alphabet construction;
the release-candidate review then demoted that arm to optional currency-sensitivity
work because KL rate and alphabet capacity price different resources. The current
core is Arm S with realised constraint-violation and surrogate-tightness
diagnostics. See Doc II §10.

**Noted, not adopted: letter-graded summary assessment.** Grades that do not
propagate from findings are decoration. The external review awarded high marks
for falsifiability in the same document in which it argued the primary comparison
might be tautological; the two cannot both stand. This package reports gates and
kill criteria instead, which either fire or do not.

### Corrections to the corrections - release-candidate review

The August 2026 additions were themselves reviewed against the prior package.
Six blocking issues were found and repaired. All six are recorded here. Three
were mathematical, and a register that only records what other people got wrong
is not a register.

| Issue | What was wrong | Repair |
|---|---|---|
| **R1 over-identified** | E1 was identified *with* the CEO problem in its Wyner--Ziv variant. CEO is a **remote-source** problem --- several encoders observing corrupted views of one common latent. E1 has distinct sources. Separately, \(H(C_v\mid\mathcal I)\) is the Slepian--Wolf lossless quantity, not the Wyner--Ziv rate, which minimises over an auxiliary variable under a distortion constraint. And the "known analytically" claim was too broad: the general multiterminal lossy problem is open. | Doc I §8.1 rewritten as *closest analogues and solved special cases*, with a status table. The \(u_v\) claim is withdrawn and restated as a dimensionless normalised residual-uncertainty measure; in the single-source lossless limit it equals the minimum conditional rate divided by \(H(C_v)\). The default E1 architecture is also corrected from decoder-only to common side information because \(q(S_v\mid C_v,\mathcal I)\) gives \(\mathcal I\) to the encoder. |
| **Missing expectation** | \(r_v=m_v+\Delta_v^{\mathrm{prior}}\) was written with a bare \(D_{KL}(q(S_v\mid\mathcal I)\Vert p(S_v\mid\mathcal I))\). That is a function of the random variable \(\mathcal I\), not a scalar. Stated as an identity, it must be exact. | \(\Delta_v^{\mathrm{prior}}:=\mathbb E_{\mathcal I}\,D_{KL}(\cdot)\) in Doc IV §3.3a and Doc III §4.5. |
| **Leakage criterion too strong** | \(I(C_u;S_v\mid\mathcal I)>0\) was named as the fault. But \(C_u\rightarrow C_v\rightarrow S_v\) is a legitimate chain: dependent sources make this positive under a *correct* factorised architecture. | Fault condition is \(I(C_u;S_v\mid C_v,\mathcal I)\), which vanishes exactly under the intended factorisation. \(I(C_u;C_v\mid\mathcal I)\) reported for scale. Doc IV §5A. |
| **VOC mischaracterised** | VOC was called "myopic and per-item." Rational metareasoning is a metalevel MDP; the myopic policy is one approximation within it. Exact metalevel policies are intractable in general --- which applies symmetrically to \(\mathbf r^*(C)\). | Baseline specified as **myopic VOC**. Contrast rewritten. Doc II P5, Doc III H2. |
| **Invariance claim unjustified** | Rank-order invariance across the variational and alphabet arms was made confirmatory. But \(\mathbb E[D_{KL}]\neq\log_2\vert\mathcal Z\vert\): they price different resources, so divergence may mean allocation depends on *which resource is scarce* rather than on the optimiser. | Arm S is core E1 with \(\Delta_v^{\mathrm{prior}}\) reported as the tightness diagnostic; the alphabet arm is demoted to an optional currency-sensitivity experiment after a phenomenon exists, per anti-slop rule 8. Doc II §10. |
| **Reference integrity** | Roughly eighteen works were cited in the new Part 0 and §8.1 without reference entries. | Entries added to Documents I, II and III. |

Two of these were errors introduced by the correction pass rather than inherited
from the original package. That is the expected failure mode of a fast repair
round, and it is the reason the gate exists.

### Second external review pass

Four repairs from a further external review. All land in Documents II and IV
unless noted; they are recorded here because the register, not a changelog, is
where repairs live.

| ID | Correction | Lands in |
|---|---|---|
| **R5** | E0-B is now **definition-indexed** (Shea / redescription / process); a split outcome across indices is a finding about construct unity, not a failure | Doc IV §7, §10 |
| **R6** | Neuroscience-side prior art still missing after R4: expected precision / precision weighting, attention-as-resource, and the slots-versus-resources debate | Doc II, P6 |
| **R7** | Gate A4 required preregistered thresholds with reported intervals; bare ratios of point estimates disallowed | Doc IV §5 |
| **R8** | Reference repair (Geiger et al. 2021 is NeurIPS 2021, not arXiv-only); the bits convention restated where the estimators live | Doc I refs; Doc IV §0 |

### Implementation-validity and portability review - September 2026

These bounded repairs implement the accepted audit and its qualifications; they do not reopen the programme's conceptual scope.

| ID | Correction | Lands in |
|---|---|---|
| **R9** | Decoder approximation error can manufacture A1 hiddenness and A2 transmission even with matched classes and nested features. Exact-reference estimator and full-evaluator validation precede pilot thresholds. This alone does not demonstrate a false pass of all E0-A gates. | Doc IV §§2-3, §6, §11; standing conventions |
| **R10** | Declining hiddenness is only a declining upper bound on message information. A4 requires a validated manipulation of task-relevant message information and an explicit matched-benefit estimand. Exact estimation alone does not repair the prediction. | Doc IV §5 |
| **R11** | Check intervention support conditional on fixed consumer inputs. Separate consumer dependence from achievable benefit. Retain full observability for information/performance; label unavailable alternative-state interventions not applicable. | Doc IV §§4-6 |
| **R12** | E0-B indices require distinct executable criteria before confirmation. RR accessibility is a bounded-consumer estimand, with redescription and feature-transformation controls, not additional Shannon information beyond complete inputs. | Doc I §4; Doc IV §§7, 10 |
| **R13** | Myopic VOC selects the greatest one-step net value, including cost and stopping; proportional allocation is a separate heuristic. E1 requires E0-A; strict-meta work requires the relevant E0-B index. Methods validation does not close C5 novelty review. | Doc II §§10, 20-21; Doc III §5 |
| **R14** | The tractable thesis is portable across relevant AI/cognitive-science programmes. Replace institution-specific admissions, curriculum, personnel and credit assumptions with skills, supervision and project-scope requirements. | Doc III; website companions |

### Standing conventions

- **Units.** All rates, entropies and informations are in **bits**
  (\(\log_2\)) throughout the package. Any code, threshold or figure reported in
  nats must be converted at the point of reporting, not at the point of reading.
- **Estimator classes.** Where an information quantity is estimated as a
  difference of two fitted log-losses, the two predictors must be of the **same
  class and nested feature sets**, and the plug-in bias reported. A difference of
  upper bounds is not itself a bound and can go negative. Matching classes and nested features is necessary for a controlled comparison but insufficient for information identification. Validate against a tractable exact reference before pilot threshold selection; quantify approximation and sampling uncertainty separately.

---

## 12. Anti-slop rules

1. **Ecology is not a synonym for complexity.** If the programme cannot identify interactions with predictive consequences, drop the word.
2. **Metarepresentation is not a synonym for internal information.** Every membership claim must name the representational property/process that is represented.
3. **No global graph by declaration.** Validate local edges first; reconstruct larger organization only afterward.
4. **No global resource pool by metaphor.** A shared budget exists only when experimentally manipulated or independently measured.
5. **No optimality inflation.** \(\mathbf r^*(C)\) is an experimental benchmark unless organisms are independently shown to approximate it.
6. **No attention privilege.** Attention is one candidate control process among others unless data make it exceptional.
7. **No phenomenality laundering.** "Higher-order," "self-model," "global," and "integrated" are not synonyms for conscious.
8. **No machinery before phenomenon.** Bayesian optimization, interchange interventions and complex hierarchical statistics are conditional tools.
9. **Negative results simplify the programme.** They do not demand another layer of explanation by default.
10. **A one-paper thesis that kills a grander idea is a successful scientific outcome.**

---

## 13. The four maxims as research conduct

### Truth, maximally sought

The programme is designed to lose claims. Prior art, simpler explanations, failed manipulation checks and null results reduce the ontology rather than provoke ad hoc rescue.

### Ambition tempered by humility

The long-range ambition is to understand how cognitive systems model their own organization. The near-term obligation is to establish one causal relation at a time.

### Beauty tempered by goodness

The project may use a coherent visual identity and memorable language, but formal submission defaults to standard notation. Elegance is valuable when it increases understanding; otherwise it yields to clarity and empirical utility.

### Honesty above all else

Every document distinguishes literature-supported premise, derived design choice, open hypothesis and unverified novelty. Every experiment reports manipulation failure, optimization path dependence and model non-identifiability as substantive outcomes.

---

## 14. Working conclusion

The first principle is not that cognition *is* a metarepresentational ecology.

It is weaker:

> **Cognition contains multiple internal monitoring and self-modeling processes. Some plausibly meet stricter criteria for metarepresentation. Their interactions are empirically understudied enough that scarcity, causal topology, recursive control, fidelity, complementarity and temporal structure can be tested as candidate organizing principles.**

If those principles fail to generalize, there may be no useful ecology-level theory. If they survive across distinct systems, an ecology may gradually be inferred rather than declared.

That is the standard this package adopts.

---

# References

1. Doerig, A., Schurger, A., & Herzog, M. H. (2020). Hard criteria for empirical theories of consciousness. *Cognitive Neuroscience*. https://doi.org/10.1080/17588928.2020.1772214
2. Fahrenfort, J. J., & van Gaal, S. (2020). Criteria for empirical theories of consciousness should focus on the explanatory power of mechanisms, not on functional equivalence. *Cognitive Neuroscience*. https://doi.org/10.1080/17588928.2020.1838470
3. Fazekas, P., Cleeremans, A., & Overgaard, M. (2024). A construct-first approach to consciousness science. *Neuroscience & Biobehavioral Reviews, 156*, 105480. https://doi.org/10.1016/j.neubiorev.2023.105480
4. Fleming, S. M., Dolan, R. J., & Frith, C. D. (2012). Metacognition: computation, biology and function. *Philosophical Transactions of the Royal Society B, 367*, 1280-1286. https://doi.org/10.1098/rstb.2012.0021
5. Fleming, S. M. (2024). Metacognition and confidence: A review and synthesis. *Annual Review of Psychology, 75*, 241-268. https://doi.org/10.1146/annurev-psych-022423-032425
6. Morales, J., Lau, H., & Fleming, S. M. (2018). Domain-general and domain-specific patterns of activity supporting metacognition in human prefrontal cortex. *Journal of Neuroscience, 38*, 3534-3546. https://doi.org/10.1523/JNEUROSCI.2360-17.2018
7. Mazancieux, A., Pereira, M., Faivre, N., Mamassian, P., Moulin, C. J. A., & Souchay, C. (2023). Towards a common conceptual space for metacognition in perception and memory. *Nature Reviews Psychology, 2*, 751-766. https://doi.org/10.1038/s44159-023-00245-1
8. Baer, C., Ghetti, S., & Odic, D. (2026). Domain generality is an emergent, not inherent, property of metacognition. *Nature Human Behaviour, 10*, 1316-1326. https://doi.org/10.1038/s41562-026-02443-2
9. Proust, J. (2003). Does metacognition necessarily involve metarepresentation? *Behavioral and Brain Sciences, 26*(3), 352. https://doi.org/10.1017/S0140525X0336008X
10. Shea, N. (2014). Reward prediction error signals are meta-representational. *Noûs, 48*(2), 314-341. https://doi.org/10.1111/j.1468-0068.2012.00863.x
11. Cleeremans, A. (2011). The Radical Plasticity Thesis: How the brain learns to be conscious. *Frontiers in Psychology, 2*, 86. https://doi.org/10.3389/fpsyg.2011.00086
12. Cleeremans, A., et al. (2020). Learning to be conscious. *Trends in Cognitive Sciences, 24*(2), 112-123. https://doi.org/10.1016/j.tics.2019.11.011
13. Cleeremans, A., Timmermans, B., & Pasquali, A. (2007). Consciousness and metarepresentation: A computational sketch. *Neural Networks, 20*, 1032-1039. PMID: 17904799.
14. Kanai, R., Takatsuki, R., & Fujisawa, I. (2025). Meta-representations as representations of processes. *Neuroscience of Consciousness, 2025*(1), niaf038. https://doi.org/10.1093/nc/niaf038
15. Eppinger, B., Goschke, T., & Musslick, S. (2021). Meta-control: From psychology to computational neuroscience. *Cognitive, Affective, & Behavioral Neuroscience, 21*, 447-452. https://doi.org/10.3758/s13415-021-00919-4
16. Bénon, J., et al. (2024). The online metacognitive control of decisions. *Communications Psychology, 2*, 23. https://doi.org/10.1038/s44271-024-00071-y
17. Bayne, T., Hohwy, J., & Owen, A. M. (2016). Are there levels of consciousness? *Trends in Cognitive Sciences, 20*(6), 405-413. https://doi.org/10.1016/j.tics.2016.03.009
18. Lieder, F., & Griffiths, T. L. (2020). Resource-rational analysis: Understanding human cognition as the optimal use of limited computational resources. *Behavioral and Brain Sciences, 43*, e1. https://doi.org/10.1017/S0140525X1900061X
19. Shenhav, A., Botvinick, M. M., & Cohen, J. D. (2013). The expected value of control: An integrative theory of anterior cingulate cortex function. *Neuron, 79*(2), 217-240. https://doi.org/10.1016/j.neuron.2013.07.007
20. Berger, T., Zhang, Z., & Viswanathan, H. (1996). The CEO problem [multiterminal source coding]. *IEEE Transactions on Information Theory, 42*(3), 887-902. https://doi.org/10.1109/18.490552
21. Geiger, A., Lu, H., Icard, T., & Potts, C. (2021). Causal abstractions of neural networks. *Advances in Neural Information Processing Systems, 34*, 9574-9586. arXiv:2106.02997.
22. Geiger, A., et al. (2022). Inducing causal structure for interpretable neural networks. *ICML 2022*. https://proceedings.mlr.press/v162/geiger22a.html
23. Geiger, A., et al. (2025). Causal abstraction: A theoretical foundation for mechanistic interpretability. *Journal of Machine Learning Research, 26*(83), 1-64. https://www.jmlr.org/papers/v26/23-0058.html
24. Rahnev, D. (2020). Resource-rational analysis versus resource-rational humans. *Behavioral and Brain Sciences, 43*, e19. https://doi.org/10.1017/S0140525X19001699

25. Slepian, D., & Wolf, J. K. (1973). Noiseless coding of correlated information sources. *IEEE Transactions on Information Theory, 19*(4), 471-480. https://doi.org/10.1109/TIT.1973.1055037
26. Wyner, A. D., & Ziv, J. (1976). The rate-distortion function for source coding with side information at the decoder. *IEEE Transactions on Information Theory, 22*(1), 1-10. https://doi.org/10.1109/TIT.1976.1055508
27. Oohama, Y. (1998). The rate-distortion function for the quadratic Gaussian CEO problem. *IEEE Transactions on Information Theory, 44*(3), 1057-1070. https://doi.org/10.1109/18.669162
28. Prabhakaran, V., Tse, D., & Ramchandran, K. (2004). Rate region of the quadratic Gaussian CEO problem. *Proceedings of the IEEE International Symposium on Information Theory (ISIT)*, 119.
29. Wagner, A. B., Tavildar, S., & Viswanath, P. (2008). Rate region of the quadratic Gaussian two-encoder source-coding problem. *IEEE Transactions on Information Theory, 54*(5), 1938-1961. https://doi.org/10.1109/TIT.2008.920343
30. Ekrem, E., & Ulukus, S. (2014). An outer bound for the vector Gaussian CEO problem. *IEEE Transactions on Information Theory, 60*(11), 6870-6887. https://doi.org/10.1109/TIT.2014.2353811
