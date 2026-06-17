# Literature Review — 2026-06-17
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Emergent language is a novel area of research within artificial intelligence, particularly within multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation.
  - Early approaches gave little consideration to the potential utility of language emergence for artificial intelligence.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing multi-agent AI ensembles because such ensembles introduce novel emergent risks.
  - The MAEBE framework, combined with the Greatest Good Benchmark and a novel double-inversion question technique, can systematically assess emergent risks in multi-agent AI systems.
  - Multi-agent LLM ensembles exhibit emergent moral reasoning behaviors that cannot be predicted from isolated LLM evaluations.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR models auditing as a coordinated mission carried out by specialized agents.
  - A Planning Agent prioritizes contracts using risk-aware heuristics.
  - An Execution Agent allocates tasks via the Contract Net protocol.

## Synthesis
Based on the fragments provided, here is a synthesis of the three papers:

**1. Points of Agreement:**
All three papers recognize that multi-agent AI systems introduce fundamentally new dynamics that are not present in single-agent architectures, and that these dynamics warrant dedicated study. Paper 1 frames this around emergent language in multi-agent reinforcement learning, while Paper 2 extends the concern to emergent behaviors in LLM ensembles, and Paper 3 grounds it in coordinated security analysis workflows. Together, they share an assumption that the interactions between agents—whether linguistic, behavioral, or task-coordinated—produce properties that must be understood, evaluated, or engineered rather than left as black-box outputs.

**2. Points of Disagreement:**
The papers diverge sharply on whether multi-agent emergent properties are primarily an *opportunity* or a *risk*. Paper 1 treats emergent language as a phenomenon to be characterized and taxonomized for scientific understanding, implicitly neutral or optimistic. Paper 2 explicitly frames emergent multi-agent behavior as a novel *safety risk* requiring new evaluation frameworks. Paper 3 takes a pragmatic engineering stance, treating multi-agent coordination as a structured pattern to be *applied* for utility (smart contract auditing), without engaging the safety or unpredictability concerns raised in Paper 2. This reflects an unresolved tension in the field between emergentism-as-discovery and emergence-as-hazard.

**3. Most Urgent Open Question:**
Do the beneficial coordination patterns demonstrated in engineered systems like SPEAR generalize to—or accidentally suppress—the unmanaged emergent behaviors and risks that MAEBE seeks to evaluate? In other words, can structured multi-agent frameworks reliably contain emergent risk, or do they merely shift where emergence occurs? Answering this is critical before multi-agent systems are deployed at scale in high-stakes domains.
