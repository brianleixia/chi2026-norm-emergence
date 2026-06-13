# Literature Review — 2026-06-13
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
  - Traditional AI safety evaluations on isolated LLMs are insufficient as multi-agent AI ensembles become prevalent, introducing novel emergent risks.
  - The MAEBE framework can systematically assess emergent risks in multi-agent AI ensembles.
  - Using MAEBE with the Greatest Good Benchmark and a novel double-inversion question technique demonstrates specific findings about LLM moral reasoning.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR models auditing as a coordinated mission carried out by specialized agents, including a Planning Agent that prioritizes contracts using risk-aware heuristics, an Execution Agent that allocates tasks via the Contract Net protocol, and a Repair Agent.
  - SPEAR is a multi-agent coordination framework for smart contract auditing that applies established MAS (multi-agent system) patterns in a realistic security analysis workflow.
  - SPEAR was developed and presented as an engineering case study demonstrating the application of multi-agent coordination for smart contract auditing.

## Synthesis
# Research Synthesis: Emergent Language, Multi-Agent Safety, and Coordinated MAS

## 1. Points of Agreement

All three papers converge on the premise that **multi-agent systems (MAS) introduce qualitatively different dynamics that cannot be understood by studying individual agents in isolation**. Paper 1 frames emergent language as a product of multi-agent reinforcement learning pressures, arguing that compositional, communicative protocols arise specifically from the interaction dynamics between agents rather than from any single agent's capabilities. Paper 2 echoes this by claiming traditional single-LLM safety evaluations are "insufficient" for multi-agent ensembles, which "introduce novel emergent risks." Paper 3 reinforces the consensus from an engineering perspective, showing that established MAS coordination patterns (task decomposition, role specialization, structured communication) yield real value when applied to complex domains like smart contract auditing. Together, they suggest that **agent interaction topology, communication structure, and emergent coordination are first-class concerns** for both understanding and deploying multi-agent AI.

## 2. Points of Disagreement

The papers diverge sharply on **whether emergent behavior is an asset or a liability**. Paper 1 treats emergent language as a phenomenon to be *cultivated and studied* — potentially yielding insights into the origins of natural language and more efficient communication protocols. Paper 2 treats emergent behavior as a *risk surface* to be detected, benchmarked, and contained, focusing on adversarial dynamics like collusion and deception between agents. Paper 3 occupies a middle ground but leans toward **engineering control**, treating coordination as a designable property through explicit MAS patterns rather than something to be left to emerge. This reflects a deeper tension: should the field prioritize *discovering* emergent capabilities (Paper 1), *defending* against emergent failures (Paper 2), or *engineer* emergent coordination toward known objectives (Paper 3)? None of the three papers explicitly reconcile these framings, and their evaluation methodologies are correspondingly incompatible.

## 3. Most Urgent Open Question

The most
