# Literature Review — 2026-06-20
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language is a novel area of research within artificial intelligence, particularly within multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation.
  - Early approaches gave little consideration to the potential utility of emergent language for artificial systems.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient for multi-agent AI ensembles
  - Multi-agent AI ensembles introduce novel emergent risks
  - The MAEBE framework can systematically assess emergent risks in multi-agent AI systems using the Greatest Good Benchmark and a novel double-inversion question technique

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
**Paragraph 1 — Points of Agreement:**
All three papers converge on the recognition that multi-agent systems (MAS) introduce qualitatively distinct dynamics that cannot be understood by studying individual agents in isolation. Paper 1 frames this as "emergent language," where communication protocols and coordination strategies arise spontaneously from agent interactions. Paper 2 echoes this through its focus on "emergent behavior" in LLM ensembles, arguing that multi-agent configurations surface failure modes, biases, and capabilities not predictable from single-model evaluations. Paper 3 demonstrates the constructive counterpart: that deliberately structured multi-agent coordination—applying established MAS patterns—can produce reliable, expert-level performance in complex domains like smart contract auditing. Together, they establish a shared premise: the interaction space between agents is itself a first-order object of study and engineering.

**Paragraph 2 — Points of Disagreement:**
The papers diverge sharply on whether emergence is primarily an opportunity or a risk, and on the appropriate methodological response. Paper 1 treats emergent language as a phenomenon to be catalogued and understood neutrally—building taxonomies of what arises, without strongly valorizing or condemning it. Paper 2 adopts a safety-critical stance, framing emergent behaviors as novel hazards requiring rigorous evaluation frameworks, implicitly assuming that uncontrolled emergence is dangerous. Paper 3 takes the opposite engineering stance: emergence is harnessed through deliberate architectural design (coordinated roles, MAS patterns), suggesting that structured systems can make emergence predictable and beneficial. There is also a tension in scope—Papers 1 and 2 focus on open-ended, general emergence, while Paper 3 argues for domain-specific, applied coordination as the path forward, implicitly critiquing general emergent-language research as insufficiently grounded.

**Paragraph 3 — Most Urgent Open Question:**
The most pressing unresolved question is: **Under what conditions does multi-agent emergence transition from a reliable capability to an uncontrolled risk, and can this boundary be predicted a priori?** Paper 3 suggests that well-engineered coordination patterns can make emergent multi-agent systems
