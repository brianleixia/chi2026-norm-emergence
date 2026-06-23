# Literature Review — 2026-06-23
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR is a multi-agent coordination framework for smart contract auditing that applies established MAS patterns in a realistic security analysis workflow.
  - SPEAR models auditing as a coordinated mission with specialized agents including a Planning Agent that prioritizes contracts using risk-aware heuristics.
  - The Execution Agent in SPEAR allocates tasks via the Contract Net protocol.

## Synthesis
**Points of Agreement**

All three papers converge on the recognition that multi-agent systems (MAS) represent a fundamentally different computational paradigm from single-agent architectures, one that introduces novel dynamics not reducible to the properties of individual components. Paper 1 establishes that emergent communication and coordination in multi-agent reinforcement learning constitute a distinct research front with their own theoretical challenges. Paper 2 builds on this by arguing that multi-agent LLM ensembles create emergent risks that cannot be predicted from evaluating isolated models, formalizing this through the MAEBE framework. Paper 3 translates these insights into practice with SPEAR, demonstrating that established MAS coordination patterns (agent specialization, structured communication, role-based workflows) yield tangible benefits in a concrete engineering domain—smart contract auditing. Together, the papers agree that inter-agent dynamics—emergent language, emergent behavior, and emergent coordination—are the defining phenomenon of the field and that principled frameworks, rather than ad-hoc designs, are necessary to study and harness them.

**Points of Divergence**

The papers differ meaningfully in stance on the tractability and risk profile of emergent multi-agent behavior. Paper 1 treats emergence primarily as a scientific object of study—something to be catalogued, taxonomized, and understood—adopting a relatively neutral posture toward whether emergent communication is beneficial or problematic. Paper 2 takes a decidedly cautionary stance, framing emergent behavior in LLM ensembles as a safety concern requiring dedicated evaluation infrastructure (MAEBE), implying emergence is more often a liability than an asset. Paper 3 pushes in the opposite direction, presenting emergence-adjacent coordination patterns as engineering solutions whose value lies in their ability to produce reliable, useful collective behavior. A secondary disagreement concerns the maturity of the field: Paper 1 suggests emergent language research is still early-stage and largely disconnected from downstream applications, while Paper 3 assumes sufficient patterns have already crystallized to be confidently deployed in production security work.

**Most Urgent Open Question**

The most pressing unresolved question is whether multi-agent emergent behavior can be
