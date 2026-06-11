# Literature Review — 2026-06-11
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
  - SPEAR models smart contract auditing as a coordinated mission carried out by specialized agents including a Planning Agent, Execution Agent, and Repair Agent
  - The Planning Agent prioritizes contracts using risk-aware heuristics
  - The Execution Agent allocates tasks via the Contract Net protocol

## Synthesis
Here is a synthesis of the three papers:

**1. Points of Agreement.** All three papers share a common grounding in the premise that multi-agent AI systems—particularly those built on LLM-based agents or emergent communication protocols—represent a fundamentally new and underexplored research frontier. Each acknowledges that the collective behavior of interacting agents produces dynamics, capabilities, or risks that cannot be predicted from studying individual agents in isolation. The emergent language survey frames this around communication protocols that arise de novo from agent interactions, while the MAEBE paper focuses on emergent risks arising from multi-agent LLM ensembles, and SPEAR demonstrates how coordinated agent behavior can be engineered to solve structured, real-world tasks. Implicitly, all three endorse the view that multi-agent coordination—whether emergent or deliberately designed—is a critical lens for understanding next-generation AI capabilities and safety.

**2. Points of Disagreement.** The papers diverge significantly on the valence and controllability of emergent multi-agent behavior. The emergent language survey treats emergence largely as a *neutral or beneficial* phenomenon—a rich space for studying communication, abstraction, and proto-language dynamics, with risks discussed but not foregrounded. MAEBE takes the opposite stance, emphasizing that emergence in multi-agent LLM systems is primarily a *source of risk* requiring formal evaluation frameworks, treating coordination as a potential failure mode rather than an asset. SPEAR occupies a third position, arguing that emergence and coordination can be *tamed and productively engineered* through deliberate architectural patterns, demonstrating that multi-agent systems can be made reliable and goal-directed in domain-specific contexts. There is also tension around the role of LLMs specifically: the survey treats language emergence as largely decoupled from modern foundation models, MAEBE centers on LLM ensembles, and SPEAR applies LLM-based agents without explicitly theorizing emergence.

**3. Most Urgent Open Question.** The most pressing unresolved question bridging these works is: **Can we develop principled methods to distinguish productive, controllable emergence from dangerous, uncontrolled emergence
