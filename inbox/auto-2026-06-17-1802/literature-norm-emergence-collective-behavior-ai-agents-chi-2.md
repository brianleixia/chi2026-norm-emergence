# Literature Review — 2026-06-17
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
  - Modern engineered systems increasingly involve complex sociotechnical environments where multiple agents, including humans and LLM-based agentic AI, must navigate social dilemmas that pit individual interests against collective welfare.
  - As engineered systems evolve toward multi-agent architectures with autonomous LLM-based agents, traditional governance approaches become insufficient.
  - The paper proposes an integrated design and governance approach for agentic AI systems through adaptive information modulation.

## Synthesis
## Points of Agreement

Both papers recognize that the rise of autonomous, interacting AI agents—particularly those powered by large language models—fundamentally reshapes the security and governance landscape beyond what traditional cybersecurity and AI safety frameworks were designed to handle. They share a core premise that as agents begin to communicate, negotiate, and act on behalf of humans across both digital and physical environments, the attack surface expands dramatically: vulnerabilities no longer reside only in individual systems but emerge from the *interactions* between agents. Both works treat multi-agent coordination as a sociotechnical problem, acknowledging that human actors, AI agents, and institutional structures must be designed as a coupled system rather than optimized in isolation. They also implicitly agree on the insufficiency of bolt-on safety mechanisms, arguing instead for security and governance to be treated as first-class design considerations from the outset.

## Points of Disagreement

The papers diverge meaningfully in framing and emphasis. The first adopts a **threat-centric posture**, treating security as the primary lens and cataloging concrete adversarial risks—prompt injection across agent boundaries, protocol manipulation, emergent collusion, and the difficulty of attribution when agents act on behalf of users. Its agenda is largely diagnostic: identifying what could go wrong. The second takes an **affirmative-design posture**, focusing on how to *build* agentic systems responsibly through adaptive information governance, stakeholder alignment, and integrated design processes. Where the first paper treats governance as one concern among many threat categories, the second elevates governance to the central organizing principle—suggesting that technical security measures are downstream of well-designed institutional and informational architectures. There is also an implicit tension over agency: the security paper tends to assume agents as potential adversaries or compromised components, while the governance paper treats them as collaborators in a well-structured sociotechnical workflow.

## Most Urgent Open Question

The most pressing unresolved question is: **How can we verify that a system of interacting agents—spanning multiple organizations, model providers, and human principals—actually behaves according to its stated
