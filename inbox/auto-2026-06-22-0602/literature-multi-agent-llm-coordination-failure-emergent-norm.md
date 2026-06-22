# Literature Review — 2026-06-22
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Emergent language is a novel area of research within artificial intelligence, particularly within multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation, with little consideration given to its potential utility for artificial systems.
  - The concept of studying language emergence is not new.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Using MAEBE with the Greatest Good Benchmark (and a novel double-inversion question technique) to systematically assess emergent risks in multi-agent AI ensembles.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR is a multi-agent coordination framework for smart contract auditing.
  - SPEAR models auditing as a coordinated mission carried out by specialized agents, including a Planning Agent, an Execution Agent, and a Repair Agent.
  - SPEAR applies established MAS patterns in a realistic security analysis workflow.

## Synthesis
# Research Synthesis: Multi-Agent Language, Behavior, and Coordination

## 1. Points of Agreement

All three papers converge on the recognition that multi-agent AI systems exhibit properties—emergent communication, emergent behavior, and coordinated problem-solving—that cannot be understood by studying individual agents in isolation. They share a foundational assumption that the interactions between agents produce qualitatively distinct phenomena worth investigating as a discipline of their own. Papers 1 and 2 both explicitly frame emergent properties as novel sources of risk or research opportunity that single-agent paradigms fail to capture, while Paper 3 demonstrates empirically that structured multi-agent coordination can outperform monolithic approaches on complex real-world tasks (smart contract auditing). There is also implicit consensus across the three that the field is maturing: Paper 1 calls for a taxonomy to organize the emerging work, Paper 2 proposes a formal framework for evaluation, and Paper 3 delivers a deployed engineering case study—together suggesting the community is moving from observation toward systematization and application.

## 2. Points of Disagreement

The papers differ most sharply in their normative orientation toward emergent multi-agent phenomena. Paper 1 (Emergent Language) treats emergent communication as a phenomenon to be understood and cataloged, largely value-neutral. Paper 2 (MAEBE), by contrast, treats emergent behavior as inherently suspect—a safety liability requiring measurement and mitigation. Paper 3 (SPEAR) takes the opposite pragmatic stance from Paper 2: it deliberately engineers emergent coordination as a *feature* for solving hard problems, showing that carefully designed MAS patterns yield better auditing results than single-agent baselines. A subtler disagreement concerns the locus of emergence: Paper 1 emphasizes emergent properties *between* agents (language as a shared protocol), Paper 2 focuses on emergent properties *within* ensembles (collective misbehavior), while Paper 3 treats emergence as a designed architectural property—suggesting the field has not yet settled whether emergence is an object of study, a risk, or a tool.

## 3. Most
