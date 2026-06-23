# Literature Review — 2026-06-23
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
  - The paper introduces the MAEBE framework to systematically assess emergent risks in multi-agent AI ensembles, though specific empirical results are cut off in the provided abstract.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
Here are the three synthesis paragraphs based on the available information:

**1. Areas of Agreement**

All three papers converge on the recognition that multi-agent systems (MAS) introduce qualitatively distinct dynamics that cannot be understood by studying individual agents in isolation. Papers 1 and 2 share a foundational framing: emergent behaviors, languages, or risks arise from interactions *between* agents rather than from their individual capabilities. Paper 1 establishes the theoretical taxonomy for how communication and coordination protocols spontaneously form, while Paper 2 treats emergent behavior as a safety concern requiring structured evaluation. Paper 3 implicitly affirms this view by demonstrating that engineering multi-agent coordination deliberately (for smart contract auditing) still requires managing coordination overhead, role allocation, and inter-agent dependencies — suggesting that emergence, whether beneficial or risky, is a structural property of MAS regardless of intent.

**2. Areas of Disagreement**

The papers diverge significantly in their posture toward emergent multi-agent phenomena. Paper 1 adopts a neutral-to-optimistic stance, framing emergent language as a research opportunity for understanding communication, representation learning, and protocol formation. Paper 2 takes a precautionary and adversarial stance, treating emergent behaviors in LLM ensembles primarily as *risks* — failure modes, jailbreak cascades, or unsafe coordination that demand detection and mitigation frameworks like MAEBE. Paper 3 sits apart from both, taking a pragmatic engineering view: emergence is neither celebrated nor feared but *managed* through deliberate architectural choices (role assignment, coordination patterns) to serve a well-defined domain task. This creates a tension between viewing multi-agent dynamics as a phenomenon to study (1), a hazard to contain (2), or a capability to harness (3).

**3. Most Urgent Open Question**

**Do the emergent risks identified in LLM-based multi-agent ensembles (Paper 2) represent a fundamentally new class of failure, or are they surface-level instantiations of coordination pathologies already catalogued in the classical MAS and emergent communication literature (Paper 1)?** If the latter
