# Literature Review — 2026-06-09
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 2

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - AI agents are beginning to interact with each other directly across internet platforms and physical environments
  - Free-form protocols enable new threats like secret collusion and coordinated swarm attacks
  - Network effects can rapidly spread privacy breaches

## 2. Integrated Design and Governance of Agentic AI Systems through Adaptive Information Modulation
- Authors: Qiliang Chen, Sepehr Ilami, Nunzio Lorè | Year: 2024 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐⭐
- Claims:
  - Modern engineered systems increasingly involve complex sociotechnical environments where multiple agents must navigate social dilemmas that pit individual interests against collective welfare.
  - As engineered systems evolve toward multi-agent architectures with autonomous LLM-based agents, traditional governance approaches become inadequate.
  - Agentic AI systems, powered by large language models, represent an emerging paradigm that requires integrated design and governance through adaptive information modulation to address collective action problems.

## Synthesis
# Research Synthesis: Multi-Agent Security & Adaptive Agentic AI Governance

**Points of Agreement**
Both papers converge on the recognition that we are entering an era of complex multi-agent sociotechnical systems where AI agents must interact with humans and other AI systems in open, dynamic environments. They share a concern that traditional cybersecurity and AI safety frameworks are insufficient for these emerging configurations. The first paper, focused on multi-agent security, emphasizes that interacting AI agents introduce novel attack surfaces (such as adversarial inter-agent communication, emergent collusion, and cross-platform trust failures) that cannot be addressed by analyzing individual agents in isolation. The second paper, on adaptive information governance for agentic AI, similarly argues that governance must move beyond static, rule-based oversight to accommodate agents that learn, negotiate, and make autonomous decisions. Both implicitly endorse a systems-level perspective: security and governance are properties of interactions, not just individual components, and both call for new technical and theoretical foundations to manage these properties at scale.

**Points of Disagreement**
The two papers differ notably in their primary framing of the problem and the locus of intervention. The multi-agent security paper centers on *adversarial dynamics*—treating other agents, messages, and environments as potentially hostile, and asking how to defend against attacks such as prompt injection across agent boundaries, emergent harmful coordination, and identity spoofing. Its implicit worldview is closer to classical security: a defender must anticipate and resist a malicious counterpart. The adaptive governance paper, by contrast, frames the challenge in terms of *coordination and legitimacy*—how to design governance mechanisms (norms, protocols, information flows) that allow agents with different objectives to align their behavior productively, often under conditions of incomplete information and shifting context. Where the security paper asks "how do we prevent harm from adversarial interactions?", the governance paper asks "how do we design interactions so that beneficial coordination emerges?" These framings imply different priorities: one privileges robustness and containment, the other adaptability and alignment through information design.
