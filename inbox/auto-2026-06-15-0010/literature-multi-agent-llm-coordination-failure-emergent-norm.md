# Literature Review — 2026-06-15
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language is a novel area of research within artificial intelligence, particularly within multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation.
  - Early approaches gave little consideration to the potential utility of emergent language for artificial applications.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR is a multi-agent coordination framework for smart contract auditing
  - SPEAR consists of a Planning Agent, an Execution Agent, and a Repair Agent
  - The Planning Agent prioritizes contracts using risk-aware heuristics while the Execution Agent allocates tasks via the Contract Net protocol

## Synthesis
Based on the three papers provided, I can only see brief excerpts/abstracts for two of them, and partial information for the third. I'll synthesize based on what's visible, noting where information is incomplete.

## 1. Points of Agreement

All three papers converge on the recognition that **multi-agent systems (MAS) introduce emergent dynamics that cannot be fully understood by analyzing individual agents in isolation**. The emergent language survey establishes that when multiple agents interact, novel communication patterns and behaviors arise that exceed the sum of their parts. MAEBE explicitly builds on this premise, arguing that isolated LLM evaluations are insufficient precisely because ensemble interactions produce novel emergent risks. SPEAR reinforces this implicitly by treating auditing as a coordination problem requiring structured multi-agent interaction rather than monolithic reasoning. There is also shared agreement that **established MAS patterns and frameworks provide legitimate, valuable foundations for engineering reliable multi-agent behavior**, rather than treating emergence as purely uncontrollable—the three papers collectively treat emergence as both a phenomenon to study (paper 1), a risk to evaluate (paper 2), and a capability to harness (paper 3).

## 2. Points of Disagreement

A clear tension exists between **MAEBE's risk-focused framing and SPEAR's opportunity-focused framing** of the same underlying phenomenon. MAEBE positions emergent multi-agent behavior primarily as a *safety concern*, treating emergent dynamics as a source of novel risks that traditional evaluations cannot capture. SPEAR, by contrast, positions the same multi-agent coordination as a *constructive engineering tool*, leveraging MAS patterns to produce better security outcomes than single-agent approaches would allow. This reflects a deeper disagreement about whether emergence should be treated as a phenomenon to *constrain* or one to *cultivate*. Additionally, there appears to be a gap between the **theoretical/taxonomic orientation of paper 1** and the **applied/engineering orientation of papers 2 and 3**—paper 1 surveys emergent language as a research phenomenon to characterize, while the others
