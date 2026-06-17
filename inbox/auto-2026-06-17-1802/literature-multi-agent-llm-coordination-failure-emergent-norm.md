# Literature Review — 2026-06-17
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language is a novel area of research within artificial intelligence, particularly within multi-agent reinforcement learning.
  - Studying language emergence is not a new concept, but early approaches were primarily concerned with explaining human language formation.
  - Early approaches to language emergence gave little consideration to its potential utility for artificial systems.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing multi-agent AI ensembles, which introduce novel emergent risks
  - The paper introduces the Multi-Agent Emergent Behavior Evaluation (MAEBE) framework to systematically assess emergent risks in multi-agent AI systems
  - The framework uses the Greatest Good Benchmark along with a novel double-inversion question technique to evaluate LLM moral reasoning in multi-agent settings

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR is a multi-agent coordination framework for smart contract auditing that applies established MAS patterns in a realistic security analysis workflow.
  - SPEAR models auditing as a coordinated mission carried out by specialized agents: a Planning Agent that prioritizes contracts using risk-aware heuristics, an Execution Agent that allocates tasks via the Contract Net protocol, and a Repair Agent.
  - SPEAR was developed and evaluated as an engineering case study of multi-agent coordination applied to smart contract auditing.

## Synthesis
# Research Synthesis: Emergent Language, MAEBE, and SPEAR

**1. Points of Agreement**

All three papers converge on a fundamental premise: as AI systems move from isolated, single-model deployments toward multi-agent configurations, novel and poorly understood dynamics emerge that cannot be analyzed through traditional single-agent evaluation frameworks. The Emergent Language survey grounds this claim in the multi-agent reinforcement learning literature, documenting how autonomous agents develop communication protocols and behavioral regularities that are not explicitly programmed. MAEBE operationalizes this concern for AI safety, arguing that ensembles of LLMs produce emergent risks that evade standard benchmarking. SPEAR provides the engineering counterpart, demonstrating through a smart contract auditing case study that established multi-agent system (MAS) coordination patterns can be productively harnessed in real-world workflows, implicitly validating the assumption that multi-agent dynamics are a meaningful unit of design and analysis. Together, the papers suggest that multi-agent interaction is a first-class phenomenon deserving dedicated theoretical, safety, and engineering treatment.

**2. Points of Disagreement**

The papers diverge sharply in their posture toward emergent multi-agent behavior. The Emergent Language survey treats emergent communication as a phenomenon to be *understood*, mapping it as a research curiosity and scientific question. MAEBE, by contrast, treats emergent multi-agent behavior primarily as a *risk vector* requiring adversarial evaluation and safety guardrails, framing the same underlying dynamics as hazards. SPEAR takes a third, more constructive position: it treats multi-agent coordination as an *engineering substrate*—deploying established MAS patterns to solve a concrete problem (smart contract auditing) without claiming novelty in emergent behavior itself. These three framings—scientific object, safety threat, and engineering tool—reflect unresolved tensions about whether emergent dynamics are something to be discovered, defended against, or designed with. Additionally, the papers differ on maturity: SPEAR is pragmatic and applied, MAEBE is evaluative and cautionary, and the survey is descriptive and taxonomic, suggesting the field has not yet
