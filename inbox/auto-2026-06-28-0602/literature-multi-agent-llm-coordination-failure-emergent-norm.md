# Literature Review — 2026-06-28
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
  - The Multi-Agent Emergent Behavior Evaluation (MAEBE) framework can systematically assess emergent risks in multi-agent AI ensembles.
  - Using MAEBE with the Greatest Good Benchmark and a novel double-inversion question technique reveals that LLM moral reasoning produces specific emergent behaviors relevant to AI safety.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR models auditing as a coordinated mission carried out by specialized agents including a Planning Agent, Execution Agent, and Repair Agent.
  - The Planning Agent prioritizes contracts using risk-aware heuristics.
  - The Execution Agent allocates tasks via the Contract Net protocol.

## Synthesis
# Research Synthesis

**1. Points of Agreement**

All three papers converge on the fundamental premise that multi-agent systems (MAS) exhibit emergent properties that cannot be adequately understood or predicted by examining individual agents in isolation. Paper 1 establishes this as the defining characteristic of emergent language research—where communication protocols and behaviors arise from agent interactions within reinforcement learning environments. Paper 2 operationalizes this concern by arguing that isolated LLM safety evaluations are insufficient precisely because multi-agent ensembles introduce novel emergent risks. Paper 3 demonstrates this principle constructively, showing how coordinating specialized agents in a smart contract auditing workflow produces capabilities exceeding what any single agent could achieve. The papers also implicitly agree that understanding and engineering these emergent dynamics is critical—both for harnessing their potential (Papers 1 and 3) and for mitigating their risks (Paper 2).

**2. Points of Disagreement**

The papers diverge significantly in their normative orientation and problem framing. Paper 1 treats emergence primarily as an object of scientific curiosity and capability, focusing on how and why communication protocols arise between agents. Paper 2 adopts a precautionary stance, framing emergent multi-agent behavior as a novel category of risk requiring dedicated safety frameworks like MAEBE. Paper 3 is explicitly engineering-oriented, treating emergence as a resource to be structured through established MAS design patterns (coordinator, monitor, worker roles) for practical deployment. There is also implicit disagreement about whether emergent multi-agent behavior should be approached through benchmark-driven empirical analysis (Paper 2), taxonomic and theoretical synthesis (Paper 1), or applied engineering case studies (Paper 3). Paper 2's focus on emergent risks in LLM ensembles contrasts sharply with Paper 3's optimistic framing of coordination as a solution to existing problems.

**3. Most Urgent Open Question**

The most pressing unresolved question across these works is: **How can we reliably distinguish beneficial emergence from harmful emergence in multi-agent AI systems?** Paper 1 shows emergence can yield novel communication and coordination; Paper 3 demonstrates emergence can
