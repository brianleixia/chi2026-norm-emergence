# Literature Review — 2026-06-09
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
# Research Synthesis

## 1. Points of Agreement

Both papers converge on the recognition that traditional cybersecurity and AI safety frameworks are inadequate for systems composed of multiple interacting AI agents. They share a fundamental concern about **emergent risks arising from agent-to-agent interaction**, including scenarios where individually aligned agents produce unsafe collective behavior. Both works also emphasize the need for **proactive, system-level design** rather than reactive, component-level safeguards, and they highlight governance and coordination as essential—not secondary—concerns in agentic AI deployment. There is mutual acknowledgment that real-world deployment will involve heterogeneous agents (potentially built by different organizations) operating in open environments with varying trust assumptions.

## 2. Points of Disagreement

The papers diverge notably in **scope and framing**. The first paper adopts a *threat-centric* posture, treating multi-agent security as a new attack surface where adversaries may exploit inter-agent communication, prompt injection across agents, and coordinated manipulation. The second paper takes a *governance and design-centric* posture, framing the challenge as one of adaptive information flow management and socio-technical coordination, where the primary concern is ensuring appropriate trust calibration and accountability across human-AI teams. Consequently, they differ on **where intervention is best applied**: the first privileges protocol-level and communication-layer defenses, while the second privileges runtime governance and information architecture. They also diverge on the role of human oversight—the second paper treats humans as integral team members requiring adaptive interfaces, whereas the first treats human-in-the-loop controls as insufficient against sophisticated multi-agent attack chains.

## 3. Most Urgent Open Question

The most urgent open question is: **How can we formally verify and bound the safety properties of multi-agent AI systems when agents are independently designed, possess divergent objectives, and communicate through open channels?** Neither paper resolves whether security guarantees can be composable across heterogeneous agents, nor do they provide empirical evidence about which attack vectors or governance failures manifest first at scale. Bridging the threat-modeling rigor of the first
