# Literature Review — 2026-06-17
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
  - Modern engineered systems increasingly involve complex sociotechnical environments where multiple agents must navigate social dilemmas that pit individual interests against collective welfare.
  - As engineered systems evolve toward multi-agent architectures with autonomous LLM-based agents, traditional governance approaches become insufficient.
  - Agentic AI systems powered by large language models represent an emerging paradigm that must be integrated into both the design and governance of engineered systems.

## Synthesis
# Research Synthesis: Multi-Agent AI Security & Agentic AI Governance

**Points of Agreement.** Both papers converge on the recognition that multi-agent and agentic AI systems introduce fundamentally novel safety and security challenges that exceed the scope of traditional cybersecurity or single-agent AI alignment frameworks. Each frames the core problem as emergent: risks arise not from any individual agent but from the interactions, communication channels, and coordination dynamics among heterogeneous agents operating across organizational and digital boundaries. Both works also implicitly or explicitly endorse an interdisciplinary design philosophy—one combining computer science, social science, and governance perspectives—arguing that technical controls alone are insufficient. They share a forward-looking posture, treating agentic AI not as a hypothetical but as an emerging reality requiring urgent conceptual and methodological investment before deployment scales further.

**Points of Disagreement or Divergent Emphasis.** The papers diverge notably in their analytic scope and methodological orientation. The Open Challenges paper adopts a threat-centric framing, focusing on adversarial dynamics, vulnerabilities in inter-agent communication, and the absence of mature defensive primitives (e.g., authentication, trust negotiation) for AI-to-AI interaction. Its concern is principally *external*—how malicious actors can exploit agent ecosystems. The Integrated Design paper, by contrast, emphasizes *internal* coordination and institutional governance, foregrounding how adaptive information-passing interfaces can harmonize heterogeneous agents (human, algorithmic, institutional) within shared regulatory and operational contexts. Where the first paper asks "how do we prevent misuse?", the second asks "how do we design coherent collective behavior?" This produces differing prescriptions: the former leans toward security primitives, sandboxing, and adversarial robustness; the latter toward socio-technical design patterns, interface design, and governance integration.

**Most Urgent Open Question.** How can security guarantees and governance frameworks be jointly designed for open multi-agent AI systems *before* deployment lock-in occurs? Specifically, there is a critical need for primitives that simultaneously (a) provide verifiable trust and authentication between autonomous agents operating across trust boundaries, and (b) embed
