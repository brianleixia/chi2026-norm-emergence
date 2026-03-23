# CHI 2026: Environmental Determinants of Norm Emergence in LLM Populations

**Target Conference**: ACM CHI 2026 (Barcelona)
**Submission Deadline**: September 11, 2025 (Abstract: September 4)
**Status**: In Progress

## The Moltbook Illusion

Why do LLM populations develop social norms in lab experiments but not in the wild?

This paper investigates the environmental determinants of norm emergence in multi-agent LLM systems through a $2\times2\times2\times2$ factorial experiment.

## Repository Structure

```
paper/
├── main.tex           # CHI 2026 main paper (acmart sigconf)
├── references.bib     # BibTeX
├── sections/          # Paper sections
│   ├── 01-abstract/
│   ├── 02-intro/
│   ├── 03-relatedwork/
│   ├── 04-methods/
│   ├── 05-results/
│   ├── 06-discussion/
│   ├── 07-limitations/
│   └── 08-conclusion/
├── figures/          # Figures
└── data/             # Data

experiment/
├── RQ1-protocol.md    # Full experiment protocol
└── results/          # Experimental results

skill-refs/           # Writing and research skills
```

## Key Findings (Preliminary)

1. Communication structure is the dominant factor (largest $\eta^2$)
2. Feedback loops are necessary but not sufficient
3. Wild settings reproduce Tsinghua 93% non-response baseline

## Team

- Brian Leixia, Hong Kong Baptist University

## AutoResearch Loop

See `paper/auto_research_loop.py` for iteration tracking.

## Citation

```bibtex
@article{leixia2026normemergence,
  title={Environmental Determinants of Norm Emergence in Large Language Model Populations},
  author={Leixia, Brian},
  journal={ACM CHI},
  year={2026}
}
```
