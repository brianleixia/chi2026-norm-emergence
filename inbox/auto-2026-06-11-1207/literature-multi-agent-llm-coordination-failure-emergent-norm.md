# Literature Review — 2026-06-11
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language is a novel area of research within AI, particularly in multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation.
  - Early approaches gave little consideration to the potential utility of emergent language for artificial systems.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Using MAEBE with the Greatest Good Benchmark and a novel double-inversion question technique, the authors demonstrate results regarding LLM moral reasoning (claim incomplete in the provided abstract)

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
# Synthesis of Three Papers on Multi-Agent Systems

## Points of Agreement

All three papers converge on the foundational premise that multi-agent systems (MAS) represent a distinct and increasingly important paradigm in AI research, one that cannot be adequately understood by extrapolating from single-agent or isolated model behavior. They share a commitment to studying how interactions between agents—whether artificial agents in language emergence games, LLM ensembles, or specialized auditing bots—produce properties, dynamics, and outcomes that are genuinely emergent rather than merely additive. Each work also implicitly recognizes that coordination, communication, and interaction protocols are central to making multi-agent arrangements tractable and analyzable, whether the goal is inducing compositional communication, surfacing safety-relevant behaviors, or distributing complex cognitive work like security analysis.

## Points of Disagreement

The papers diverge sharply in scope, stakes, and orientation. The *Emergent Language Survey* treats emergent communication primarily as a scientific phenomenon—a way to study the foundations of language and representation under controlled conditions—framing it as a fascinating but largely theoretical pursuit. *MAEBE*, by contrast, treats multi-agent interaction as an urgent *safety problem*, arguing that emergent behaviors in LLM ensembles constitute novel risks that demand adversarial evaluation frameworks rather than scientific curiosity. *SPEAR* stakes out a third position, treating multi-agent coordination as a practical *engineering tool* whose value lies in decomposing real-world tasks (smart contract auditing) into roles and protocols, without foregrounding either foundational questions or safety risks. There is also an implicit tension in how each paper views the agent: Paper 1 studies agents as abstractions that converge on protocols; Paper 2 views them as opaque systems whose interactions may produce harm; Paper 3 treats them as engineered components whose coordination is a design choice.

## Most Urgent Open Question

The most pressing open question, drawn from the intersection of these works, is: **Can we develop principled methods to predict, characterize, and govern the emergent behaviors of multi-agent LLM systems before
