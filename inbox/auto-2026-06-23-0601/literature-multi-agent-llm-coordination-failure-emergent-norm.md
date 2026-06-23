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
  - [Could not extract]

## Synthesis
# Research Synthesis: Multi-Agent Emergent Behavior Papers

## 1. Points of Agreement

All three papers converge on the premise that multi-agent AI systems exhibit qualitatively distinct behaviors and risks that cannot be understood by studying individual agents in isolation. Each positions emergence—whether linguistic (Paper 1), behavioral (Paper 2), or coordinative (Paper 3)—as a phenomenon that arises specifically from agent interaction rather than from any single agent's capabilities. They also share an implicit acknowledgment that current evaluation methodologies are inadequate for these systems: Paper 1 highlights the need for better analysis of emergent communication protocols, Paper 2 argues that traditional single-LLM safety evaluations miss emergent ensemble risks, and Paper 3 frames smart contract auditing as fundamentally requiring multi-agent coordination to handle complexity that exceeds monolithic approaches. The works collectively suggest that multi-agent architectures are not merely a deployment convenience but introduce new dynamics demanding their own theoretical and engineering frameworks.

## 2. Points of Disagreement

The papers diverge significantly in their orientation and underlying assumptions. Paper 1 treats emergent language primarily as a research phenomenon to be observed and taxonomized—presenting emergence as something to understand scientifically. Paper 2, by contrast, treats emergence as fundamentally a *risk vector*, focusing on miscoordination, deception, and unsafe collective behaviors, reflecting an AI safety/safety engineering perspective. Paper 3 is more pragmatic and constructive, viewing multi-agent coordination as a solution rather than a problem—using established MAS coordination patterns (likely informed by classical multi-agent systems research) to achieve reliability in a concrete engineering domain. This creates a notable tension: Papers 1 and 2 emphasize emergence as unpredictable or hazardous, while Paper 3 assumes that established coordination patterns can reliably shape emergent behavior for beneficial ends. Additionally, Paper 2 appears grounded in contemporary frontier LLM ensembles, whereas Paper 1 spans broader multi-agent RL traditions, and Paper 3 likely draws more from classical distributed AI—suggesting these communities may not fully share vocabulary or assumptions.
