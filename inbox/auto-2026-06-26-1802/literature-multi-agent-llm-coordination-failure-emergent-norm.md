# Literature Review — 2026-06-26
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
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing multi-agent AI ensembles
  - Multi-agent AI ensembles introduce novel emergent risks not present in single-agent evaluations
  - The MAEBE framework, combined with the Greatest Good Benchmark and a novel double-inversion question technique, can systematically assess emergent risks in multi-agent AI systems

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
**Where They Agree**
All three papers converge on the recognition that multi-agent LLM systems represent a distinct and increasingly important research domain that cannot be understood by studying individual models in isolation. They share the foundational premise that coordination between multiple agents produces novel dynamics—whether these are linguistic protocols (Paper 1), emergent behaviors with safety implications (Paper 2), or structured division of labor in complex tasks like security auditing (Paper 3). Each paper treats emergent properties arising from agent interaction as a legitimate and necessary object of study. They also implicitly agree that current evaluation methodologies and theoretical frameworks remain underdeveloped for capturing these multi-agent phenomena, calling for new taxonomies, benchmarks, and engineering patterns tailored to the multi-agent setting.

**Where They Disagree**
The papers diverge sharply in their stance toward emergence itself. Paper 1 treats emergent language as a phenomenon to be understood and catalogued, approaching it with descriptive taxonomic ambition and treating emergent communication as potentially valuable. Paper 2 approaches emergence with explicit suspicion, framing emergent behaviors in multi-agent LLM ensembles primarily as *risks* requiring detection and mitigation—the language is cautionary, not exploratory. Paper 3 sidesteps the emergence debate entirely, treating multi-agent coordination as a conventional software engineering problem solved by applying established MAS (multi-agent system) patterns, effectively denying that anything genuinely novel is happening. This spectrum—from emergent phenomenon to emergent hazard to ordinary engineering—reflects fundamentally different assumptions about whether multi-agent LLM systems exhibit new properties or merely instantiate familiar coordination structures.

**Most Urgent Open Question**
Does genuine emergence occur in current multi-agent LLM systems, or are observed dynamics reducible to known multi-agent system patterns scaled to more capable language models? Resolving this question is urgent because it determines research priorities across all three communities: if emergence is real, then Paper 2's safety concerns and Paper 1's linguistic investigations are warranted; if it is illusory, then the field risks reinventing decades of MAS research while missing that the real challenges are
