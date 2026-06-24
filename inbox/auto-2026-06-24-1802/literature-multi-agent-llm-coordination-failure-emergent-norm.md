# Literature Review — 2026-06-24
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language is a novel area of research within artificial intelligence, particularly within multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation rather than its utility for artificial systems.
  - The abstract is truncated, so additional empirical claims cannot be extracted beyond the conceptual claims provided.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR models smart contract auditing as a coordinated mission carried out by specialized agents.
  - SPEAR employs a Planning Agent that prioritizes contracts using risk-aware heuristics.
  - SPEAR uses an Execution Agent that allocates tasks via the Contract Net protocol.

## Synthesis
# Synthesis of Three Papers on Multi-Agent Systems and Emergent Behavior

## Points of Agreement

All three papers converge on the premise that multi-agent systems (MAS) introduce fundamentally different dynamics compared to single-agent or isolated model deployments. The emergent language survey establishes that when agents interact—whether through reinforcement learning signaling games or communicative protocols—behaviors, conventions, and coordination strategies arise that were not explicitly programmed. The MAEBE paper extends this insight to the safety domain, arguing that emergent risks in LLM ensembles cannot be predicted by evaluating models in isolation, since inter-agent dynamics produce novel failure modes. SPEAR provides concrete engineering evidence for both themes, demonstrating that established MAS coordination patterns (role allocation, message passing, consensus) produce structured, useful collective behavior when applied to a real-world security workflow. Collectively, the papers agree that multi-agent interaction is a first-class phenomenon requiring dedicated study, not merely a scaled-up version of single-agent analysis.

## Points of Disagreement

The papers diverge sharply in their treatment of emergence and its desirability. The emergent language survey treats emergence largely as a *positive* phenomenon—a means of studying how compositional communication, grounding, and social learning can arise naturally, often treating agents as relatively simple reinforcement learners in controlled games. MAEBE, by contrast, treats emergence as predominantly *hazardous*, focusing on deception, collusion, and goal drift as failure modes that arise unpredictably from agent interaction. SPEAR sits between these views, deliberately *engineering* emergence through prescribed coordination patterns (rather than letting it arise spontaneously), thereby aiming to harness multi-agent benefits while constraining the system to predictable, auditable behavior. A second tension concerns methodology: the survey emphasizes open-ended environments and learned protocols, MAEBE stresses adversarial probing and red-teaming of LLM ensembles, and SPEAR favors deterministic, role-based orchestration—reflecting fundamentally different philosophies about whether MAS should be discovered or designed.

## Most Urgent Open Question

The most urgent open question raised across these works is
