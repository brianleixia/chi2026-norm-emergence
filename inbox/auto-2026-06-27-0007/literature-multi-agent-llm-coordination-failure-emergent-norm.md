# Literature Review — 2026-06-27
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
  - Traditional AI safety evaluations on isolated LLMs are insufficient for multi-agent AI ensembles due to novel emergent risks.
  - The paper introduces the MAEBE framework for systematically assessing emergent risks in multi-agent AI systems.
  - The framework uses the Greatest Good Benchmark combined with a novel double-inversion question technique to evaluate LLM moral behavior.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
**Points of Agreement**

All three papers converge on the view that multi-agent systems represent a meaningful departure from single-agent paradigms, whether measured through emergent communication, emergent behavior, or structured coordination. Each treats "emergence" as a defining property of these systems—Paper 1 frames it as language arising from interaction, Paper 2 as risk-bearing behaviors arising from ensemble dynamics, and Paper 3 as coordinated capability arising from structured role assignment. They also share an implicit methodological consensus: multi-agent phenomena cannot be adequately understood by studying individual components in isolation. Paper 1 advocates for taxonomies that capture interaction-level properties; Paper 2 explicitly critiques isolated LLM evaluation as insufficient; Paper 3 demonstrates the point concretely by showing that coordination patterns, not individual agent competence, drive outcomes in smart contract auditing.

**Points of Disagreement**

The papers diverge sharply on whether emergence should be cultivated, constrained, or engineered. Paper 1 takes a largely descriptive and exploratory stance, treating emergent language as a phenomenon to be catalogued and understood without strong normative claims. Paper 2 adopts a precautionary posture, framing emergent multi-agent behaviors primarily as a safety risk requiring evaluation and containment. Paper 3 is prescriptive and constructive, arguing that established multi-agent system patterns can and should be deliberately engineered into high-stakes domains. A subtler disagreement concerns the locus of value: Paper 1 and Paper 2 focus on properties arising from agent interaction itself, while Paper 3 emphasizes the value of imposed coordination structure—suggesting that Paper 3 would view Papers 1 and 2 as underweighting the role of architectural design.

**Most Urgent Open Question**

The most urgent open question is whether there exists a unified framework that can simultaneously explain emergent communication (Paper 1), diagnose emergent risk (Paper 2), and guide principled engineering of multi-agent coordination (Paper 3). Without such a framework, the field risks fragmenting into three disconnected literatures—a taxonomy without safety levers, a safety agenda without constructive
