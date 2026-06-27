# Literature Review — 2026-06-27
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Unable to extract 3 specific empirical claims: the provided abstract excerpt is truncated and contains only introductory/background statements with no empirical findings.

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
**1. Points of Agreement:**
All three papers converge on the premise that multi-agent AI systems produce fundamentally different dynamics than isolated models, requiring dedicated study rather than extrapolation from single-agent behavior. Papers 1 and 2 both treat emergence as a central phenomenon—Paper 1 catalogs it as a research area in its own right within multi-agent RL, while Paper 2 frames emergent multi-agent behavior as a novel safety risk class that single-agent evaluations cannot capture. Paper 3 implicitly endorses this view by demonstrating that multi-agent coordination patterns yield real engineering value (smarter contract audits) precisely because agents decompose and recombine work in ways monolithic systems do not. The papers also share an implicit methodological agreement: emergence and coordination are best understood through structured frameworks—whether taxonomies (Paper 1), evaluation harnesses (Paper 2), or reusable coordination patterns (Paper 3).

**2. Points of Disagreement:**
The papers diverge sharply on whether multi-agent dynamics are primarily an *opportunity* or a *threat*. Paper 1 takes a neutral, exploratory stance, treating emergent language as a phenomenon to be understood and catalogued. Paper 3 is overtly constructive, framing coordination as an engineering asset to be designed into systems for concrete tasks. Paper 2, by contrast, is predominantly adversarial in framing—emergent behavior is treated as a safety hazard requiring red-teaming and containment. A subtler disagreement concerns *causality*: Paper 1 and Paper 2 treat emergence as something that arises spontaneously from agent interaction (often unpredictably), whereas Paper 3 treats coordination as something deliberately engineered through established MAS patterns, implying emergence can be designed rather than merely observed.

**3. Most Urgent Open Question:**
How can we reliably distinguish *beneficial* emergent coordination (the kind Paper 3 exploits for auditing) from *harmful* emergent behavior (the kind Paper 2 seeks to detect) before deployment—and can this distinction be made *a priori* from a system's architecture, or
