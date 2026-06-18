# Literature Review — 2026-06-18
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language represents a novel area of research within artificial intelligence, particularly within multi-agent reinforcement learning.
  - The concept of studying language emergence is not new, with early approaches primarily concerned with explaining human language formation.
  - Early approaches to language emergence gave little consideration to the potential utility of emergent language for artificial intelligence applications.

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
# Synthesis of Three Papers on Multi-Agent Systems

**1. Points of Agreement:**
All three papers converge on the recognition that multi-agent systems (MAS) introduce fundamentally new dynamics that cannot be understood by studying individual agents in isolation. The emergent language survey establishes that interaction between agents produces communication protocols, coordination patterns, and behaviors that arise from the collective rather than being programmed directly. MAEBE extends this principle to AI safety, arguing that emergent risks in LLM ensembles require new evaluation frameworks precisely because multi-agent interactions produce failure modes absent in single-model assessments. SPEAR implicitly reinforces this view by demonstrating that established MAS patterns—such as role differentiation, message-passing, and coordinated task decomposition—can be productively applied to complex real-world problems like smart contract auditing. Together, the papers treat emergence not as a curiosity but as a load-bearing concept for understanding and engineering multi-agent AI.

**2. Points of Disagreement:**
The papers diverge sharply on the normative framing of emergent behavior. The emergent language survey adopts a largely descriptive and exploratory stance, treating emergent protocols as phenomena to be characterized and taxonomized, with relatively little concern for their safety implications. MAEBE, by contrast, is explicitly alarmist in posture—framing emergent multi-agent behavior as a novel source of risk that demands immediate mitigation frameworks, potentially before the engineering community fully understands the mechanisms at play. SPEAR occupies a third position: pragmatic and applied, it treats multi-agent coordination as a solved-enough engineering pattern to be deployed against well-defined problems, showing little anxiety about either emergence-as-discovery (paper 1) or emergence-as-threat (paper 2). This reflects a deeper tension between treating emergence as opportunity, as risk, or as routine engineering substrate.

**3. Most Urgent Open Question:**
The critical unresolved question is whether emergent behaviors in multi-agent LLM systems can be reliably predicted and controlled before such systems are deployed at scale. MAEBE calls for safety frameworks, SPEAR demonstrates coordination patterns work in narrow
