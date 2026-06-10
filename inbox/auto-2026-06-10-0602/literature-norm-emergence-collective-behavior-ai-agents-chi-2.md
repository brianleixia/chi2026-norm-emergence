# Literature Review — 2026-06-10
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 2

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## 2. Integrated Design and Governance of Agentic AI Systems through Adaptive Information Modulation
- Authors: Qiliang Chen, Sepehr Ilami, Nunzio Lorè | Year: 2024 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
**Where they agree:**
Both papers recognize that the convergence of multiple interacting AI agents represents a fundamental shift beyond traditional single-agent AI safety and cybersecurity paradigms. They converge on the view that agentic AI systems create novel, emergent risks that cannot be adequately addressed by existing frameworks, whether those risks emerge from adversarial exploitation (Paper 1) or from inadequate governance structures in complex sociotechnical systems (Paper 2). Both implicitly endorse the need for systemic, multi-layered defenses rather than point solutions, and both acknowledge that humans remain critical actors who must be integrated into the control and oversight loop rather than removed from it.

**Where they disagree:**
The papers diverge in their primary locus of concern and methodological orientation. Paper 1 adopts a more adversarial, threat-centric posture, treating inter-agent interaction as a new attack surface populated by deception, collusion, prompt injection, and emergent adversarial dynamics among autonomous agents. Paper 2, by contrast, frames the problem as one of adaptive governance and information alignment, emphasizing the epistemic and coordination challenges of ensuring that distributed agents (human and artificial) share accurate, relevant information under uncertainty. Where Paper 1 asks "how do we prevent agents from harming each other or their users?", Paper 2 asks "how do we design systems so that the right information flows to the right agents at the right time, including the humans in the loop?" The first foregrounds security against malicious behavior; the second foregrounds reliability and coordination among nominally cooperative actors.

**Most urgent open question:**
How can we design multi-agent systems that simultaneously resist adversarial manipulation and maintain coherent shared situational awareness when the number, identity, and trustworthiness of participating agents are not known in advance and may shift dynamically? In other words, can security guarantees and information-governance guarantees be unified into a single principled framework, or are these objectives fundamentally in tension in open, internet-scale agentic environments? Answering this is prerequisite to either paper's recommendations being operationally deployable.
