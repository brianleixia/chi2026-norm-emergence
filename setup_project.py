#!/usr/bin/env python3
import os

base = "/workspace/chi2026-norm-emergence"

dirs = [
    f"{base}/paper/sections/01-abstract",
    f"{base}/paper/sections/02-intro", 
    f"{base}/paper/sections/03-relatedwork",
    f"{base}/paper/sections/04-methods",
    f"{base}/paper/sections/05-results",
    f"{base}/paper/sections/06-discussion",
    f"{base}/paper/sections/07-limitations",
    f"{base}/paper/sections/08-conclusion",
    f"{base}/paper/figures",
    f"{base}/paper/data",
    f"{base}/paper/scripts",
    f"{base}/experiment",
    f"{base}/skill-refs",
]

for d in dirs:
    os.makedirs(d, exist_ok=True)

# Write main.tex
main_tex = r"""\documentclass[sigconf]{acmart}

%% Meta information (for review - anonymous)
\title{Environmental Determinants of Norm Emergence in Large Language Model Populations}
%\titlenote{Anonymous for review}
\subtitle{Why Social Norms Appear in Lab Experiments but Disappear in the Wild}

%% Authors (for review - anonymous)
\author{Brian Leixia}
\affiliation{%
  \institution{Hong Kong Baptist University}
  \city{Hong Kong}
  \country{China}}
\email{brian@hkbuae.edu}

%% For CHI - use the correct date
\date{April 2026}

%% Abstract
\begin{abstract}
Despite evidence that large language model (LLM) populations spontaneously develop social conventions in controlled lab settings, no such emergence has been observed in open, deployed environments. This stark contradiction—what we term the \emph{Moltbook Illusion}—suggests that norm emergence is not an intrinsic property of LLM populations but rather an \emph{environmental engineering outcome}. We present a 2$\times$2$\times$2$\times$2 factorial experiment ($N$=480 runs) systematically varying four environmental factors (feedback loops, communication structure, task framing, and population stability) to identify which environmental variables are necessary and sufficient for norm emergence. Our results show that communication structure is the dominant factor (largest effect size), while feedback loops are necessary but not sufficient. Wild-type environments (no structure) reproduce the 93\% non-response inertia observed in real-world deployments. We present the \textbf{Norm Emergence Environmental Model (NEEM)}: a framework that predicts norm emergence as a function of environmental design, not model capability. NEEM has direct implications for the design of open AI platforms, suggesting that communication infrastructure—not better models—is the primary lever for engineering prosocial AI behavior.
\end{abstract}

%% CCS Concepts
\keywords{norm emergence, multi-agent LLMs, social conventions, environmental design, HCI, CHI}

\begin{document}

%% Front matter
\maketitle

%% Sections
\input{sections/01-abstract/abstract.tex}
\input{sections/02-intro/intro.tex}
\input{sections/03-relatedwork/relatedwork.tex}
\input{sections/04-methods/methods.tex}
\input{sections/05-results/results.tex}
\input{sections/06-discussion/discussion.tex}
\input{sections/07-limitations/limitations.tex}
\input{sections/08-conclusion/conclusion.tex}

%% Bibliography
\bibliography{references}
\bibliographystyle{ACM-Reference-Format}

\end{document}
"""

with open(f"{base}/paper/main.tex", "w") as f:
    f.write(main_tex)

# Write abstract
abstract = r"""\section*{Abstract}
\addcontentsline{toc}{section}{Abstract}

This is the abstract of the paper. It should be 150-250 words.
"""

# Write each section stub
sections = {
    "01-abstract/abstract.tex": abstract,
    "02-intro/intro.tex": r"""\section{Introduction}
\label{sec:intro}

\sectionquote{If you want to understand how norms emerge, look at the environment, not the agent.}{This Paper}

\subsection{Motivation}
\input{sections/02-intro/motivation.tex}

\subsection{Research Questions}
\input{sections/02-intro/rqs.tex}

\subsection{Contributions}
\input{sections/02-intro/contributions.tex}
""",
    "03-relatedwork/relatedwork.tex": r"""\section{Related Work}
\label{sec:related}

\subsection{Norm Emergence in Human Societies}
\input{sections/03-relatedwork/norms-human.tex}

\subsection{LLM Populations and Social Behavior}
\input{sections/03-relatedwork/norms-llm.tex}

\subsection{Environmental Determinants of Collective Behavior}
\input{sections/03-relatedwork/environment.tex}
""",
    "04-methods/methods.tex": r"""\section{Methods}
\label{sec:methods}

\subsection{Experimental Design}
\input{sections/04-methods/design.tex}

\subsection{Environment Simulation}
\input{sections/04-methods/simulation.tex}

\subsection{Agent Configuration}
\input{sections/04-methods/agents.tex}

\subsection{Metrics}
\input{sections/04-methods/metrics.tex}

\subsection{Statistical Analysis}
\input{sections/04-methods/stats.tex}
""",
    "05-results/results.tex": r"""\section{Results}
\label{sec:results}

\subsection{H1: Feedback Loops Are Necessary But Not Sufficient}
\input{sections/05-results/h1-feedback.tex}

\subsection{H2: Communication Structure Has the Largest Effect Size}
\input{sections/05-results/h2-communication.tex}

\subsection{H3: Task Framing Moderates Norm Speed and Quality}
\input{sections/05-results/h3-framing.tex}

\subsection{H4: Population Stability and Norm Persistence}
\input{sections/05-results/h4-stability.tex}

\subsection{H5-H6: Population Size and Model Tier}
\input{sections/05-results/h5-h6.tex}

\subsection{Regression Analysis}
\input{sections/05-results/regression.tex}
""",
    "06-discussion/discussion.tex": r"""\section{Discussion}
\label{sec:discussion}

\subsection{The Moltbook Illusion Explained}
\input{sections/06-discussion/moltbook-illusion.tex}

\subsection{Implications for Platform Design}
\input{sections/06-discussion/implications.tex}

\subsection{Relation to Existing Theory}
\input{sections/06-discussion/theory.tex}
""",
    "07-limitations/limitations.tex": r"""\section{Limitations}
\label{sec:limitations}

\subsection{Ecological Validity}
\input{sections/07-limitations/ecological.tex}

\subsection{Model Dependency}
\input{sections/07-limitations/model.tex}

\subsection{Norm Operationalization}
\input{sections/07-limitations/norm-op.tex}
""",
    "08-conclusion/conclusion.tex": r"""\section{Conclusion}
\label{sec:conclusion}

We showed that norm emergence in LLM populations is an environmental engineering problem, not a model capability problem. Communication structure is the dominant lever. Future work should explore hybrid human-AI norm formation (RQ4) and the minimal identity framework for coordination (RQ5).
"""
}

for path, content in sections.items():
    full = f"{base}/paper/{path}"
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)

# Write references stub
with open(f"{base}/paper/references.bib", "w") as f:
    f.write("""%% Placeholder for BibTeX references
%% Will be populated with actual citations as we write

""")

print("Paper structure created!")
print(f"Base: {base}")
for root, dirs, files in os.walk(f"{base}"):
    level = root.replace(base, '').count(os.sep)
    indent = '  ' * level
    print(f'{indent}{os.path.basename(root)}/')
    for file in files:
        print(f'{indent}  {file}')
