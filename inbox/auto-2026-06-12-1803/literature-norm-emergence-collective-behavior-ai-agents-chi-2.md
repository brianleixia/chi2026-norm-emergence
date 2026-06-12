# Literature Review — 2026-06-12
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
  - As engineered systems evolve toward multi-agent architectures with autonomous LLM-based agents, traditional governance approaches face new challenges requiring integrated design and governance solutions.
  - Agentic AI systems powered by large language models represent an emerging paradigm that necessitates adaptive information modulation for effective coordination in multi-agent architectures.

## Synthesis
# Research Synthesis: Multi-Agent AI Security

## 1. Points of Agreement

Both papers recognize that the emergence of AI agents capable of autonomous action and direct interaction—particularly with other agents across networks—represents a fundamental shift that exceeds the explanatory power of existing frameworks. They agree that traditional cybersecurity, designed around static perimeters and human operators, is insufficient for systems where agents negotiate, delegate, and transact independently. Each paper emphasizes that the security challenge is not merely technical but emerges from the interaction itself: emergent behaviors, misaligned incentive structures, and the unpredictability of multi-agent coordination. Both also implicitly endorse a governance-forward stance, treating safety and security as design-time concerns rather than post-hoc patches, and both call for frameworks that can scale with the growing autonomy and connectivity of agentic systems.

## 2. Points of Disagreement

The papers diverge meaningfully in scope and threat model. The first adopts a more adversarial framing, foregrounding offensive risks such as prompt injection across agent-to-agent channels, deceptive coordination, and the weaponization of multi-agent dynamics by malicious actors. Its concerns are largely external: what happens when agents are attacked or compromised by outside parties. The second paper, by contrast, centers on internal coordination challenges—how legitimate agents, including humans and LLM-powered systems, can be integrated through adaptive information architectures and governance protocols. Where the first treats the agentic ecosystem as a threat surface to be defended, the second treats it as a sociotechnical system to be designed. This leads to different remedies: the first pushes for adversarial robustness and protocol-level defenses, while the second advocates for adaptive governance, information flow design, and co-adaptation between humans and AI.

## 3. Most Urgent Open Question

The most pressing unresolved question is whether **secure multi-agent systems can be designed without first resolving the alignment problem at the individual agent level**. Both papers implicitly assume that individual agents are competent and roughly trustworthy, yet if a single agent's objectives can drift, be jailbroken
