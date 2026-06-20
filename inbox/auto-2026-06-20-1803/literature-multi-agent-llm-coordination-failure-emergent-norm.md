# Literature Review — 2026-06-20
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Emergent language is a novel area of research within multi-agent reinforcement learning in AI.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation.
  - Early approaches gave little consideration to the potential utility of language emergence for artificial systems.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing multi-agent AI ensembles because such ensembles introduce novel emergent risks.
  - The MAEBE framework, combined with the Greatest Good Benchmark and a novel double-inversion question technique, can systematically assess emergent risks in multi-agent AI systems.
  - LLM moral judgments exhibit specific failures or vulnerabilities when evaluated using MAEBE with the Greatest Good Benchmark and double-inversion questions.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR is a multi-agent coordination framework that applies established MAS patterns to smart contract auditing workflows.
  - SPEAR employs a Planning Agent that prioritizes contracts using risk-aware heuristics.
  - SPEAR uses an Execution Agent that allocates tasks via the Contract Net protocol.

## Synthesis
## Where They Agree

All three papers situate multi-agent systems (MAS) as a qualitatively distinct paradigm from single-agent AI, emphasizing that coordination among agents produces capabilities—or risks—that cannot be understood by examining individual agents in isolation. They share a common vocabulary around "emergence": Paper 1 frames emergent language as the novel communicative protocols that arise when agents must coordinate under reinforcement learning pressures; Paper 2 treats emergent *behaviors* in LLM ensembles as the locus of new safety failures; Paper 3 takes the more pragmatic position that deliberately engineered MAS patterns (role assignment, negotiation, structured handoffs) can be harnessed for high-stakes domains like smart contract auditing. Across all three, there is consensus that multi-agent interaction introduces irreducible complexity—whether that complexity is interpreted as linguistic opportunity (Paper 1), safety hazard (Paper 2), or engineering substrate (Paper 3).

## Where They Disagree

The papers diverge sharply on whether emergent multi-agent dynamics are an asset to cultivate or a liability to govern. Paper 1 is fundamentally *optimistic and exploratory*, treating emergent language as a phenomenon worth studying for what it reveals about communication and representation learning. Paper 2 is *defensive and adversarial*, arguing that the same emergent dynamics that produce useful coordination also produce novel attack surfaces (collusion, stealth, coordinated jailbreaks) that single-model evaluations cannot detect. Paper 3 takes a third stance—*engineered and instrumental*—asserting that with the right architectural scaffolding, multi-agent coordination is already deployment-ready for critical infrastructure, implicitly pushing back against Paper 2's precautionary framing. There is also a methodological split: Paper 1 advocates studying emergence in controlled game-theoretic environments, Paper 2 demands red-teaming of black-box LLM ensembles, and Paper 3 argues for domain-specific engineering rather than abstract study.

## Most Urgent Open Question

**Can we rigorously measure and bound the safety properties of emergent multi-agent behavior *before* such systems are deployed
