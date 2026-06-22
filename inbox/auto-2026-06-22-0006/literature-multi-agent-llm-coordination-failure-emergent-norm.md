# Literature Review — 2026-06-22
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Emergent language is a novel area of research within multi-agent reinforcement learning
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation
  - Early approaches gave little consideration to the potential utility of emergent language for artificial systems

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - MAEBE uses the Greatest Good Benchmark and a novel double-inversion question technique to evaluate multi-agent emergent behavior
  - LLM moral [statement cut off]
  - Multi-agent AI ensembles introduce novel emergent risks not captured by traditional isolated LLM safety evaluations

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
# Research Synthesis

**Points of Agreement:** All three papers converge on the recognition that multi-agent systems (MAS) exhibit emergent properties that cannot be fully understood by examining individual agents in isolation. Paper 1 frames emergence as a defining research challenge for understanding agent communication, Paper 2 operationalizes this concern by arguing that safety risks emerge from ensemble interactions rather than from single LLM failures, and Paper 3 demonstrates that coordination patterns themselves (rather than individual auditor capabilities) drive effective outcomes in smart contract analysis. The papers collectively endorse a shift away from single-agent evaluation paradigms toward frameworks that explicitly model interaction dynamics, shared protocols, and the gap between individual competence and collective behavior. They also implicitly agree that principled engineering of multi-agent coordination—whether through emergent communication (Paper 1), structured behavioral frameworks (Paper 2), or established MAS coordination patterns (Paper 3)—is a prerequisite for deploying these systems reliably.

**Points of Disagreement:** The papers diverge most sharply on whether emergence should be *cultivated* or *constrained*. Paper 1 treats emergent language as a phenomenon to be studied and taxonomized, implicitly treating it as valuable for understanding artificial communication. Paper 2 takes the opposite normative stance, framing emergence in multi-agent LLMs as a *risk surface* requiring detection, measurement, and mitigation—essentially treating the same phenomenon as a safety liability. Paper 3 sidesteps this tension by deliberately engineering away from emergence, opting for established, predictable coordination patterns over learned or emergent protocols. A second axis of disagreement concerns evaluation methodology: Paper 1 advocates for descriptive taxonomies of emergent behaviors, Paper 2 pushes for quantitative benchmarking of unsafe emergent behavior, and Paper 3 relies on domain-specific case-study validation. These reflect fundamentally different epistemologies about how multi-agent phenomena should be characterized and validated.

**Most Urgent Open Question:** How can the field develop unified evaluation criteria that distinguish *beneficial* emergence (productive coordination, novel problem-solving) from *harmful* emergence (de
