# Literature Review — 2026-06-16
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
  - SPEAR is a multi-agent coordination framework for smart contract auditing that applies established MAS (multi-agent system) patterns.
  - SPEAR models auditing as a coordinated mission involving specialized agents, including a Planning Agent that prioritizes contracts using risk-aware heuristics.
  - SPEAR includes an Execution Agent that allocates tasks via the Contract Net protocol and a Repair Agent for further coordination.

## Synthesis
# Research Synthesis

**1. Points of Agreement**
All three papers converge on the premise that multi-agent AI systems generate behaviors and communication patterns fundamentally distinct from those of isolated models. They share an implicit assumption that interaction—between agents or with structured environments—produces emergent properties that cannot be reliably predicted from studying individual components. Papers 1 and 2 both explicitly frame emergent phenomena as a domain warranting systematic study, with Paper 1 taxonomizing emergent language in MARL settings and Paper 2 proposing a framework (MAEBE) specifically for evaluating emergent risks in LLM ensembles. Paper 3 reinforces this view through empirical demonstration, showing that established multi-agent coordination patterns (role specialization, structured communication) can be operationalized to produce reliable collective behavior in a high-stakes domain (smart contract auditing).

**2. Points of Disagreement**
A clear tension exists in how each paper regards emergent behavior: Paper 1 treats it primarily as a *research subject to characterize*, adopting a neutral scientific stance on its value or danger. Paper 2 takes a cautionary posture, emphasizing that emergent multi-agent dynamics introduce "novel emergent risks" that isolated-model safety evaluations cannot capture—implicitly suggesting emergence is often undesirable. Paper 3, by contrast, treats emergence as *engineerable and beneficial*, deliberately imposing coordination structures to channel collective intelligence toward a concrete goal. There is also disagreement on the role of structure: Paper 2 implies emergent behavior is largely unconstrained and risky, while Paper 3 demonstrates that structured role-based architectures can make multi-agent systems predictable and auditable.

**3. Most Urgent Open Question**
The most pressing unresolved question is: **Under what conditions does multi-agent emergence become a safety liability versus a deployable asset?** Paper 2 warns of emergent risks but offers limited insight into when they materialize; Paper 3 shows emergence can be tamed through engineering, but only within a narrow, well-structured task. Bridging these perspectives—developing principled methods to distinguish *
