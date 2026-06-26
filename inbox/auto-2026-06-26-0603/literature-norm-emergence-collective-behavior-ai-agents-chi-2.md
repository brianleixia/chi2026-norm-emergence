# Literature Review — 2026-06-26
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
  - [Could not extract]

## Synthesis
# Research Synthesis: Multi-Agent Security & Agentic AI Governance

## Points of Agreement

Both papers converge on the recognition that the proliferation of autonomous AI agents—especially those powered by large language models operating in open environments—fundamentally outpaces existing security and governance frameworks. They share a core premise that current approaches, built around isolated models or single-agent oversight, are inadequate for systems where multiple agents (human or artificial) interact, negotiate, and influence one another in real time. Both works acknowledge that agentic AI introduces emergent risks that cannot be decomposed into the sum of individual agent behaviors, and both call for architectures that embed safety, alignment, and governance as first-class design concerns rather than post-hoc additions. Additionally, they implicitly agree that the boundary between technical security (e.g., adversarial robustness, protocol integrity) and broader governance concerns (e.g., accountability, coordination norms) is dissolving, demanding integrated solutions.

## Points of Disagreement

The papers diverge in their primary framing of the problem. The first adopts a **threat-centric, security-oriented lens**, emphasizing adversarial scenarios, protocol-level vulnerabilities, and the concrete attack surfaces that emerge when agents interact across internet and physical platforms—framing the challenge as one of defending systems against misuse and exploitation. The second paper takes a **systems-engineering and governance lens**, focusing on adaptive information architectures, sociotechnical coordination, and the design principles that enable trustworthy collaboration among heterogeneous agents. Consequently, they propose different remedies: the first leans toward defensive mechanisms, verification protocols, and threat modeling, while the second advocates for governance structures and adaptive frameworks that manage the behavior of agent populations holistically. A subtler tension concerns the locus of risk—whether the principal danger lies in *external adversaries exploiting multi-agent dynamics* or in *the intrinsic coordination failures and value misalignments of the agent collective itself*.

## Most Urgent Open Question

The most pressing unresolved question is: **How can we develop theoretically grounded yet practically deployable mechanisms that simultaneously secure multi-agent AI systems
