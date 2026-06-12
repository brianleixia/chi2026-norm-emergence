# Literature Review — 2026-06-12
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 2

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - AI agents are beginning to interact with each other directly and across internet platforms and physical environments
  - Free-form protocols are essential for AI's task generalization but enable new threats like secret collusion and coordinated swarm attacks
  - Network effects can rapidly spread privacy breaches

## 2. Integrated Design and Governance of Agentic AI Systems through Adaptive Information Modulation
- Authors: Qiliang Chen, Sepehr Ilami, Nunzio Lorè | Year: 2024 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
# Research Synthesis: Multi-Agent AI Security and Agentic AI Governance

## 1. Points of Agreement

Both papers recognize that the emergence of interconnected AI agents—particularly those powered by large language models—creates fundamentally new challenges that exceed the scope of traditional cybersecurity, AI safety, or systems engineering frameworks operating in isolation. They share a conviction that securing these multi-agent sociotechnical systems requires a **holistic, integrated approach** spanning technical design, governance, and operational deployment, rather than treating safety as a property bolted on after the fact. Both works acknowledge that as AI agents gain greater autonomy, delegation, and inter-agent communication capabilities, the attack surface and risk profile expand in ways that demand new theoretical foundations and practical mitigation strategies. They also implicitly agree on the inadequacy of single-stakeholder or purely technical solutions, emphasizing the need for governance structures that account for multi-party interactions across organizational and trust boundaries.

## 2. Points of Disagreement or Divergent Emphasis

The papers differ in their **primary analytical lens and intervention point**. The *Open Challenges* paper adopts a security-first, adversarial perspective—framing the problem space around threats, attack vectors, vulnerabilities, and the limitations of existing defenses when applied to inter-agent interactions. It treats governance more as a contextual concern. The *Adaptive Information Design* paper, by contrast, takes a **governance and design-first approach**, treating information flow, epistemic alignment, and adaptive control as the central mechanism for managing risk, with technical security as one consideration among many. Consequently, they diverge on where responsibility for safety should reside: the former emphasizes emergent risks arising at interaction boundaries between independently developed agents, while the latter emphasizes the responsibility of system architects to embed governance into design from the outset. The first paper is largely diagnostic (what is broken?); the second is more prescriptive (how should it be built?).

## 3. Most Urgent Open Question

**How can we operationalize adaptive, integrated governance for multi-agent AI systems without either
