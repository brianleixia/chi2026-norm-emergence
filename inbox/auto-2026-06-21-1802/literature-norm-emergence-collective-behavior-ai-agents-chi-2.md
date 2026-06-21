# Literature Review — 2026-06-21
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 2

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - AI agents are beginning to interact with each other directly and across internet platforms and physical environments, creating security challenges beyond traditional cybersecurity and AI safety frameworks.
  - Free-form protocols are essential for AI's task generalization but enable new threats like secret collusion and coordinated swarm attacks.
  - Network effects can rapidly spread privacy breaches across multi-agent systems.

## 2. Integrated Design and Governance of Agentic AI Systems through Adaptive Information Modulation
- Authors: Qiliang Chen, Sepehr Ilami, Nunzio Lorè | Year: 2024 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐⭐
- Claims:
  - Modern engineered systems increasingly involve complex sociotechnical environments where multiple agents, including humans and agentic AI powered by large language models, must navigate social dilemmas that pit individual interests against collective welfare.
  - Traditional governance approaches are insufficient for multi-agent architectures with autonomous LLM-based agents.
  - Agentic AI systems are powered by large language models.

## Synthesis
# Research Synthesis: Multi-Agent AI Security and Agentic AI Governance

## 1. Points of Agreement

Both papers converge on the recognition that **agentic AI systems introduce fundamentally novel risks** that cannot be adequately addressed by extending existing cybersecurity or AI safety paradigms. They agree that as AI agents gain the ability to autonomously interact with each other, with humans, and with physical/digital infrastructure, the resulting systems exhibit emergent security and governance challenges stemming from inter-agent dynamics rather than isolated model behavior. Both works emphasize the need for **holistic, system-level frameworks**—spanning technical safeguards, policy mechanisms, and design principles—rather than piecemeal bolt-on solutions. They further share a commitment to **proactive, anticipatory governance**, arguing that governance and security considerations must be embedded into system design from the outset rather than retrofitted after deployment.

## 2. Points of Disagreement

The papers diverge in their **primary framing and locus of concern**. The first paper (Open Challenges in Multi-Agent Security) adopts a **threat-centric posture**, foregrounding adversarial risks, inter-agent manipulation, emergent collusion, and attack surfaces that arise when autonomous agents transact, negotiate, or coordinate without human intermediation. Its vocabulary is closer to cybersecurity and adversarial ML. The second paper (Integrated Design and Governance of Agentic AI Systems) takes a more **constructive, sociotechnical orientation**, emphasizing adaptive information governance, human-AI teaming, and the institutional conditions for trustworthy deployment. It treats security as one concern among many (alongside accountability, transparency, and alignment with human values), whereas the first paper treats adversarial interaction as the *defining* problem. There is also a subtle methodological tension: the first leans toward identifying *open problems* for the research community, while the second proposes a more *integrated prescriptive framework* combining design and governance.

## 3. Most Urgent Open Question

**How can we design inter-agent interaction protocols that are simultaneously provably secure against adversarial behavior *
