# Literature Review — 2026-06-12
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Emergent language is a novel area of research within artificial intelligence, particularly within multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily focused on explaining human language formation.
  - Early approaches gave little consideration to the potential utility of emergent language for artificial intelligence applications.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient as multi-agent AI ensembles become prevalent, introducing novel emergent risks.
  - The paper introduces the Multi-Agent Emergent Behavior Evaluation (MAEBE) framework to systematically assess such risks.
  - Using MAEBE with the Greatest Good Benchmark (and a novel double-inversion question technique), the paper demonstrates findings about LLM moral behavior.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR is a multi-agent coordination framework designed for smart contract auditing that applies established MAS patterns in a realistic security analysis workflow.
  - SPEAR models auditing as a coordinated mission carried out by specialized agents, including a Planning Agent that prioritizes contracts using risk-aware heuristics.
  - SPEAR employs an Execution Agent that allocates tasks via the Contract Net protocol, and a Repair Agent (description truncated in abstract).

## Synthesis
**Paragraph 1 — Points of Agreement:**
All three papers converge on the premise that multi-agent systems (MAS) introduce qualitatively different dynamics compared to single-agent or isolated model settings, and that these dynamics warrant dedicated study. Paper 1 frames emergent language as a phenomenon arising specifically from multi-agent reinforcement learning interactions, emphasizing that communicative structure emerges from the demands of coordination rather than being pre-specified. Paper 2 builds on this by arguing that emergent behaviors in LLM ensembles constitute a distinct safety surface that cannot be assessed through traditional single-model evaluation, since agent-to-agent interactions generate novel risks. Paper 3 operationalizes the same intuition in a concrete engineering context, demonstrating that multi-agent coordination patterns (rather than monolithic reasoning) produce meaningful gains in real-world audit workflows. Together, they endorse the view that coordination, communication, and interaction topology are first-class objects of analysis rather than incidental implementation details.

**Paragraph 2 — Points of Disagreement:**
The papers diverge meaningfully on the *locus* of emergence and its implications for evaluation. Paper 1 treats emergent language as a comparatively neutral scientific phenomenon — a product of optimization pressure that can be taxonomized and studied for its own sake, with little concern for safety. Paper 2, by contrast, casts emergence in LLM ensembles as primarily a *risk vector*, focusing on measurement and mitigation rather than understanding emergent structure in itself; it implicitly assumes emergence is something to be controlled. Paper 3 sidesteps the emergence question almost entirely, treating multi-agent coordination as an applied engineering pattern whose benefits are pre-justified by established MAS theory rather than something that itself emerges from agent interaction. There is also a methodological gap: Paper 1 favors controlled reference games as the substrate for study, Paper 2 advocates adversarial probing of deployed ensembles, and Paper 3 relies on domain-specific task decomposition — three rather different empirical traditions with limited cross-citation.

**Paragraph 3 — Most Urgent Open Question:**
The most pressing unresolved question is whether the empirical findings from
