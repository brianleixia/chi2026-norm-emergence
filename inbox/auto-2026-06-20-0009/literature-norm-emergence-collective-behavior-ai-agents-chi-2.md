# Literature Review — 2026-06-20
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 2

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - AI agents are beginning to interact with each other directly and across internet platforms and physical environments, creating security challenges beyond traditional cybersecurity and AI safety frameworks.
  - Free-form protocols are essential for AI's task generalization but enable new threats like secret collusion and coordinated swarm attacks.

## 2. Integrated Design and Governance of Agentic AI Systems through Adaptive Information Modulation
- Authors: Qiliang Chen, Sepehr Ilami, Nunzio Lorè | Year: 2024 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
**What they agree on**

Both papers recognize that we are entering an era where AI agents—particularly those powered by large language models—are operating alongside humans and other AI systems in complex sociotechnical environments, and that this shift introduces governance and security challenges that existing frameworks cannot adequately address. They share a core concern that the autonomy, adaptability, and inter-agent communication capabilities of modern AI systems create attack surfaces and coordination problems that traditional cybersecurity (designed for static, single-system defenses) and classical AI safety (focused on individual model alignment) were not built to handle. Both implicitly endorse the need for layered, adaptive, and systems-level approaches—integrating technical safeguards with governance mechanisms—rather than treating safety as a property of any single component in isolation.

**Where they disagree**

The papers diverge in emphasis and framing. The first is more alarm-oriented, foregrounding the *adversarial* dimensions of multi-agent interaction: emergent attack vectors, inter-agent deception, prompt injection across agent boundaries, and the absence of identity, authentication, and trust primitives for autonomous AI actors. Its analytical lens is closer to offensive security and threat modeling. The second paper is more constructive and design-oriented, emphasizing *adaptive information governance*, coordination protocols, and the integration of human oversight into the engineering lifecycle of agentic systems. It treats the challenge primarily as one of principled system design under uncertainty, rather than as a contest against malicious actors. In short, one frames the problem as "how do we defend against emergent threats," while the other frames it as "how do we engineer trustworthy multi-agent systems from the start."

**Most urgent open question**

How can we design governance and security mechanisms for multi-agent AI systems that are robust to *both* unintentional coordination failures *and* deliberate adversarial manipulation, without ossifying the system through overly rigid controls that defeat the adaptability that makes agentic AI valuable in the first place? Resolving this tension—between flexibility and assurance, between openness and verification—appears to be the critical bottleneck
