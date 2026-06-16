# Literature Review — 2026-06-16
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 2

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - AI agents are beginning to interact with each other directly and across internet platforms and physical environments
  - Free-form protocols are essential for AI's task generalization but enable new threats like secret collusion and coordinated swarm attacks
  - Network effects can rapidly spread privacy breaches across multi-agent systems

## 2. Integrated Design and Governance of Agentic AI Systems through Adaptive Information Modulation
- Authors: Qiliang Chen, Sepehr Ilami, Nunzio Lorè | Year: 2024 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐⭐
- Claims:
  - Modern engineered systems increasingly involve complex sociotechnical environments where multiple agents, including humans and agentic AI powered by large language models, must navigate social dilemmas that pit individual interests against collective welfare.
  - As engineered systems evolve toward multi-agent architectures with autonomous LLM-based agents, traditional governance approaches become insufficient for managing the resulting complex interactions.
  - The paper proposes an integrated design and governance framework using adaptive information modulation to address collective action problems in systems containing both human and LLM-based autonomous agents.

## Synthesis
Based on the partial excerpts provided for both papers, I can offer a synthesis, though the incomplete nature of the texts limits depth. Here is my best attempt:

**1. Points of Agreement**

Both papers recognize that the convergence of AI agents into multi-agent sociotechnical systems creates fundamentally new governance and security challenges that exceed what traditional frameworks can address. They share a concern that as agents—whether autonomous AI systems, humans, or both—interact at scale across digital and physical environments, the resulting emergent behaviors introduce risks (security vulnerabilities in one, governance and coordination failures in the other) that cannot be decomposed into the safety of any single agent. Both implicitly call for integrated, system-level approaches rather than purely component-level analysis, and both situate their work at the intersection of classical engineering/cybersecurity concerns and the novel capabilities introduced by LLM-powered agentic AI.

**2. Points of Disagreement**

The clearest divergence is in framing and primary concern. The first paper (focused on multi-agent security) treats security as the central problem and emphasizes adversarial dynamics, attack surfaces, and the vulnerabilities that arise specifically when agents interact *with each other* across open platforms. The second paper (focused on integrated design and governance) takes a broader sociotechnical view, treating governance, information flow, and adaptive coordination among humans and AI agents as the primary design problem—with security being only one consideration among many. In short, one asks "how do we keep these systems safe from attack?" while the other asks "how do we design and govern these systems coherently?" They likely also differ on the role of formal methods: the governance paper hints at structured information architectures, whereas the security paper likely emphasizes threat modeling.

**3. Most Urgent Open Question**

Given the partial texts, the most pressing open question bridging both works is: **How can we design governance and security mechanisms for multi-agent AI systems that remain robust under open-world conditions, where agents are heterogeneous, partially adversarial, and operating without a
