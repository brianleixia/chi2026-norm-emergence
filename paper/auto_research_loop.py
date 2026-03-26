#!/usr/bin/env python3
"""
AutoResearch Loop for CHI 2026 Paper
Target: chi2026-norm-emergence paper
Goal: Iterate until paper is CHI-quality

每个 iteration:
1. 分析当前 paper 状态
2. 识别最关键的 gap（内容/结构/论证）
3. 制定下一个改进任务
4. 执行改进
5. 自我评审
6. 记录进度
"""

import os
import json
from datetime import datetime

PAPER_DIR = "/workspace/chi2026-norm-emergence/paper"
REPORTS_DIR = "/workspace/chi2026-norm-emergence/loop_reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

ITERATION_FILE = f"{REPORTS_DIR}/iteration_state.json"

def load_state():
    if os.path.exists(ITERATION_FILE):
        with open(ITERATION_FILE) as f:
            return json.load(f)
    return {
        "iteration": 0,
        "last_update": None,
        "current_phase": "writing_draft",
        "sections_complete": [],
        "sections_incomplete": ["abstract", "intro", "relatedwork", "methods", "results", "discussion", "limitations", "conclusion"],
        "chi_score": 0,
        "chi_threshold": 7,
        "notes": []
    }

def save_state(state):
    state["last_update"] = datetime.utcnow().isoformat()
    with open(ITERATION_FILE, "w") as f:
        json.dump(state, f, indent=2)

def check_sections():
    """检查每个 section 的完成度"""
    sections = {
        "abstract": f"{PAPER_DIR}/sections/01-abstract/abstract.tex",
        "intro": f"{PAPER_DIR}/sections/02-intro/intro.tex",
        "relatedwork": f"{PAPER_DIR}/sections/03-relatedwork/relatedwork.tex",
        "methods": f"{PAPER_DIR}/sections/04-methods/methods.tex",
        "results": f"{PAPER_DIR}/sections/05-results/results.tex",
        "discussion": f"{PAPER_DIR}/sections/06-discussion/discussion.tex",
        "limitations": f"{PAPER_DIR}/sections/07-limitations/limitations.tex",
        "conclusion": f"{PAPER_DIR}/sections/08-conclusion/conclusion.tex",
    }
    
    status = {}
    for name, path in sections.items():
        if not os.path.exists(path):
            status[name] = {"exists": False, "size": 0, "complete": False}
        else:
            size = os.path.getsize(path)
            with open(path) as f:
                content = f.read()
            # 粗略判断完成度：内容>200字 = 有实质内容
            has_content = len(content.strip()) > 200
            has_citations = ("\\cite{" in content or "\\bibliography" in content
                            or "\\citeA{" in content or "\\citep{" in content)
            status[name] = {
                "exists": True,
                "size": size,
                "has_content": has_content,
                "has_citations": has_citations,
                "complete": has_content and has_citations
            }
    return status

def next_task(state, section_status):
    """根据当前状态决定下一步任务"""
    # 优先完成没有内容的 section
    for name in ["results", "discussion", "limitations", "conclusion"]:
        if name in state["sections_incomplete"]:
            if not section_status.get(name, {}).get("has_content", False):
                return f"write_{name}", f"写 {name} 完整内容"
    
    # 其次添加 citation
    for name in state["sections_incomplete"]:
        if section_status.get(name, {}).get("has_content", False) and not section_status.get(name, {}).get("has_citations", False):
            return f"add_citations_{name}", f"为 {name} 添加引文"
    
    # 如果所有 section 都有内容，进阶优化
    return "polish", "进入精修阶段：优化论证逻辑和 CHI 风格"

def run_iteration():
    state = load_state()
    section_status = check_sections()
    task, desc = next_task(state, section_status)
    
    state["iteration"] += 1
    state["current_task"] = task
    state["current_task_desc"] = desc
    state["section_status"] = section_status
    
    report = {
        "iteration": state["iteration"],
        "timestamp": datetime.utcnow().isoformat(),
        "current_phase": state["current_phase"],
        "task": task,
        "task_desc": desc,
        "sections": {k: {kk: vv for kk, vv in v.items() if kk != "exists"} 
                      for k, v in section_status.items()},
        "chi_score": state["chi_score"],
        "target": state["chi_threshold"]
    }
    
    report_path = f"{REPORTS_DIR}/iteration_{state['iteration']:03d}.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
    
    save_state(state)
    
    print(f"[Iteration {state['iteration']}] {task}: {desc}")
    print(f"Sections: {json.dumps({k: v['complete'] for k, v in section_status.items()}, indent=2)}")
    print(f"Report: {report_path}")
    return report

if __name__ == "__main__":
    run_iteration()
