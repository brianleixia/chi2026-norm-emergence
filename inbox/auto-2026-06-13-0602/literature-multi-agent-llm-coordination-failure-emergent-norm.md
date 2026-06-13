# Literature Review — 2026-06-13
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Emergent language is a novel area of research within artificial intelligence, particularly in multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation.
  - Early approaches gave little consideration to the potential utility of emergent language for artificial applications.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing risks in multi-agent AI ensembles.
  - The MAEBE framework can systematically assess novel emergent risks arising from multi-agent AI ensembles.
  - Using the Greatest Good Benchmark with a novel double-inversion question technique, MAEBE demonstrates emergent behaviors in LLM moral reasoning (specific result truncated in abstract).

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR is a multi-agent coordination framework for smart contract auditing that applies established MAS (Multi-Agent System) patterns in a realistic security analysis workflow.
  - SPEAR models auditing as a coordinated mission carried out by specialized agents, including a Planning Agent that prioritizes contracts using risk-aware heuristics.
  - SPEAR uses a Contract Net protocol for task allocation, where the Execution Agent allocates tasks across the multi-agent system.

## Synthesis
**1. Areas of Agreement**

All three papers converge on the premise that multi-agent systems (MAS) introduce qualitatively distinct dynamics that single-agent analyses cannot capture, and that structured interaction between agents produces behaviors warranting dedicated study. Each treats emergent phenomena as a central object of inquiry—whether framed as emergent language in cooperative signaling games (Paper 1), emergent behavioral risks in LLM ensembles (Paper 2), or emergent coordination patterns in domain-specific agent workflows (Paper 3). They also implicitly agree that rigorous evaluation requires moving beyond anecdotal observation toward systematic frameworks: Paper 1 calls for taxonomies, Paper 2 proposes an empirical benchmark suite, and Paper 3 applies established MAS patterns to validate coordination in a concrete engineering context. Together, they position multi-agent interaction as a legitimate and necessary layer of AI research, distinct from—and complementary to—single-agent capability evaluation.

**2. Areas of Disagreement**

The papers diverge sharply in their assessment of *whether* emergent multi-agent dynamics are primarily a benefit or a risk, and consequently what role evaluation should play. Paper 1 treats emergence as a largely neutral-to-positive phenomenon—a research opportunity to understand how communication protocols arise naturally under cooperative pressure. Paper 2 takes the opposite stance, framing emergent behavior in LLM ensembles as a novel *safety* concern requiring adversarial evaluation, treating it as a failure mode to detect rather than a capability to cultivate. Paper 3 occupies a middle ground, treating emergence as neither intrinsically good nor bad but as an engineering property to be *controlled* through deliberate architectural choices. This disagreement reflects deeper unresolved tension in the field: emergence is simultaneously a goal in language-grounding research, a hazard in safety research, and a design parameter in applied systems—without a shared vocabulary for distinguishing productive emergence from problematic emergence.

**3. Most Urgent Open Question**

The most pressing open question is: **Under what formal conditions does emergent multi-agent behavior transition from functional coordination to systemic risk, and can this boundary be detected *before*
