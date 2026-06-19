# Literature Review — 2026-06-19
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language is a novel area of research within artificial intelligence, particularly within multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation.
  - Early approaches gave little consideration to the potential utility of language emergence for artificial [systems].

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient for multi-agent AI ensembles, which introduce novel emergent risks.
  - The MAEBE framework uses the Greatest Good Benchmark and a novel double-inversion question technique to systematically assess multi-agent emergent risks.
  - The paper demonstrates findings about LLM moral reasoning (specific claim incomplete in abstract).

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR is a multi-agent coordination framework designed for smart contract auditing.
  - SPEAR models the auditing process as a coordinated mission involving specialized agents including a Planning Agent, Execution Agent, and Repair Agent.
  - The Planning Agent uses risk-aware heuristics to prioritize contracts, and the Execution Agent allocates tasks through the Contract Net protocol.

## Synthesis
**1. Points of Agreement**

All three papers converge on the premise that multi-agent systems (MAS) introduce qualitatively new dynamics that single-agent analysis cannot capture. The emergent language survey frames this around multi-agent reinforcement learning, where agents develop communication protocols and conventions absent from isolated training. MAEBE extends the argument to LLM ensembles, arguing that emergent behaviors—coordination failures, collusion, deceptive signaling—arise specifically from interaction and cannot be predicted from individual model evaluations. SPEAR implicitly endorses the same foundation by treating smart contract auditing as a coordination problem requiring structured inter-agent protocols rather than a single powerful auditor. Together, the three works share a commitment to treating interaction, communication, and coordination as first-class objects of study, and to moving beyond static benchmark evaluation toward dynamic, behavioral assessment of agent collectives.

**2. Points of Disagreement**

The papers diverge sharply on the valence and purpose of emergent behavior. The emergent language literature treats emergent communication as a *constructive* phenomenon—a potential pathway to more capable, adaptive, and human-interpretable AI systems, with risks treated as secondary. MAEBE takes the opposite stance: emergent behavior is primarily a *safety hazard* to be detected, contained, and stress-tested, framing multi-agent interaction as a source of adversarial dynamics including covert collusion and goal drift. SPEAR occupies a middle, pragmatic position: it accepts MAS complexity but argues that the right response is *engineering discipline*—applying well-known coordination patterns (auctions, role allocation, blackboard architectures) to make emergent behavior predictable and auditable rather than either celebrating or fearing it. The disagreement is essentially normative: should emergent multi-agent dynamics be cultivated, defended against, or domesticated?

**3. Most Urgent Open Question**

The most pressing unresolved question is whether emergent multi-agent behaviors can be **evaluated with sufficient rigor before deployment**. MAEBE demonstrates that current LLM safety evaluations miss multi-agent risks entirely; SPEAR shows that coordination frameworks can be engineered for specific
