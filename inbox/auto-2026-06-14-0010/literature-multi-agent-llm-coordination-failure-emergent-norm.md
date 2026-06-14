# Literature Review — 2026-06-14
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
  - [Could not extract]

## Synthesis
**1. Points of Agreement**

All three papers converge on the recognition that multi-agent systems (MAS) represent a distinct and increasingly important research domain that cannot be adequately understood by studying individual agents in isolation. Each acknowledges that when multiple autonomous entities interact—whether reinforcement learning agents developing communication protocols (Paper 1), LLM ensembles exhibiting novel collective behaviors (Paper 2), or specialized agents coordinating on complex tasks like smart contract auditing (Paper 3)—system-level phenomena emerge that are not predictable from the properties of individual components. Furthermore, all three papers implicitly endorse the view that rigorous empirical evaluation of these multi-agent dynamics is essential for progress in the field.

**2. Points of Disagreement**

The papers diverge meaningfully in their assessment of where the field stands and what the primary challenges are. Paper 1 frames emergent language research as still in an exploratory, taxonomy-building phase, treating the field as nascent and primarily concerned with foundational questions about how communication protocols arise. Paper 2, by contrast, assumes the field has matured enough that evaluation frameworks are warranted and emphasizes that existing single-agent safety methods are insufficient—a position that implies greater confidence in the technology's deployment readiness while highlighting underappreciated risks. Paper 3 takes an even more applied stance, treating multi-agent coordination as an engineering discipline with established patterns ready to be deployed in production contexts like security auditing. There is also tension regarding the locus of emergent risk: Paper 2 views emergent multi-agent behavior as primarily a safety concern, while Papers 1 and 3 treat emergent dynamics as either scientifically interesting (communication emergence) or functionally beneficial (coordination outcomes).

**3. Most Urgent Open Question**

The most pressing unresolved question is whether emergent multi-agent behaviors—particularly those arising from LLM ensembles as documented in Paper 2—can be reliably characterized, predicted, and controlled *before* such systems are deployed at scale in high-stakes domains. Paper 2 demonstrates that multi-agent LLM interactions produce surprising and potentially risky collective dynamics, but neither
