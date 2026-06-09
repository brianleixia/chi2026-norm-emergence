# Literature Review — 2026-06-09
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language is a novel area of research within artificial intelligence, particularly in multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily focused on explaining human language formation.
  - Early approaches gave little consideration to the potential utility of emergent language for artificial applications.

## 2. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR models auditing as a coordinated mission with a Planning Agent, Execution Agent, and Repair Agent
  - SPEAR applies established MAS (multi-agent system) patterns to smart contract auditing
  - The Planning Agent prioritizes contracts using risk-aware heuristics

## 3. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing multi-agent AI ensembles because they introduce novel emergent risks.
  - The paper introduces the Multi-Agent Emergent Behavior Evaluation (MAEBE) framework to systematically assess emergent risks in multi-agent AI systems.
  - Using MAEBE with the Greatest Good Benchmark and a novel double-inversion question technique, the authors demonstrate effects related to LLM moral reasoning (specific claim incomplete in abstract).

## Synthesis
Based on the three abstracts provided, here is a synthesis:

**1. Points of Agreement**

All three papers share a foundational concern with multi-agent systems (MAS) and their increasing complexity. Each recognizes that multi-agent configurations—whether in emergent communication research, smart contract auditing, or AI safety evaluation—introduce dynamics that cannot be understood by examining individual agents in isolation. They agree that coordination, communication, and interaction patterns among agents are central to the behavior of these systems, and that traditional single-agent analysis methods are insufficient. Furthermore, all three implicitly acknowledge that multi-agent systems are becoming more prevalent in real-world applications, necessitating dedicated frameworks and methodologies to study them.

**2. Points of Disagreement**

The papers diverge significantly in their orientation toward emergent properties. Papers 1 and 3 treat emergence as a phenomenon to be studied, characterized, or evaluated—Paper 1 taxonomizes emergent language as a research object, while Paper 3 frames emergent behaviors as "risks" requiring safety evaluation. Paper 2, by contrast, takes a pragmatic engineering stance, treating multi-agent coordination not as something emergent to be observed but as a structured pattern to be *applied* deliberately to solve a concrete problem (smart contract auditing). There is also a tension in their evaluation of multi-agent complexity: Paper 3 views emergent behaviors as dangers to be controlled, Paper 1 views them as phenomena of scientific interest, and Paper 2 treats the coordination as a beneficial tool.

**3. Most Urgent Open Question**

Given the limited abstracts, the most pressing open question appears to be: *How can we reliably distinguish beneficial emergent coordination from harmful emergent behavior in multi-agent systems?* Paper 2 demonstrates that structured multi-agent coordination can produce useful outcomes in security-critical domains, while Paper 3 warns that the same multi-agent ensembles can produce novel emergent risks. Paper 1's taxonomy of emergent language suggests we lack shared vocabulary to even describe these phenomena consistently. The field urgently needs unified theoretical frameworks and empirical benchmarks
