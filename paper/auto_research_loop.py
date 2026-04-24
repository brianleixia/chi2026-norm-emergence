#!/usr/bin/env python3
"""
auto_research_loop.py — Research Pipeline v4
=============================================
Enhanced with AutoClaudeCodeResearchInSleep logic:
- Sleep/Wake cycle management (cron-based scheduling)
- Topic-driven research (topics.json)
- Wake time calculator
- Structured Git commits with research notes
- Citation tracking + novelty scoring

Usage:
  python3 auto_research_loop.py --update           # Morning research update
  python3 auto_research_loop.py --sleep           # Enter sleep mode
  python3 auto_research_loop.py --status           # Show sleep schedule + stats
  python3 auto_research_loop.py --literature "query"   # Run literature review
  python3 auto_research_loop.py --review "url"         # Paper peer review
  python3 auto_research_loop.py --cite-check "url"      # Citation distortion check
  python3 auto_research_loop.py --plan              # Show research plan for today
"""
import os, sys, json, time, subprocess, re, urllib.parse, datetime, threading, sched
from pathlib import Path
from collections import defaultdict

# ── Paths ───────────────────────────────────────────────────────────────────
BASE      = Path("/workspace/chi2026-norm-emergence")
INBOX_DIR  = Path("/workspace/chi2026-norm-emergence/inbox")
JOURNAL    = Path("/workspace/chi2026-norm-emergence/journal/index.md")
PAPER_DIR  = BASE / "paper"
SLEEP_CFG  = Path("/workspace/chi2026-norm-emergence/sleep_config.json")
TOPICS_F  = Path("/workspace/chi2026-norm-emergence/topics.json")
OUT_DIR   = INBOX_DIR / f"auto-{datetime.datetime.now().strftime('%Y-%m-%d-%H%M')}"

# ── Sleep Configuration ─────────────────────────────────────────────────────
DEFAULT_CRON = "0 9 * * 1-5"  # Weekdays at 9am UTC

def load_sleep_config():
    if SLEEP_CFG.exists():
        with open(SLEEP_CFG) as f:
            return json.load(f)
    return {
        "cron": DEFAULT_CRON,
        "sleep_duration_hours": 8,
        "active_topics": [],
        "last_wake": None,
        "last_update": None,
        "total_runs": 0,
    }

def save_sleep_config(cfg):
    SLEEP_CFG.parent.mkdir(parents=True, exist_ok=True)
    with open(SLEEP_CFG, "w") as f:
        json.dump(cfg, f, indent=2)

def parse_cron_next(cron_expr):
    """Parse cron expression and return next wake datetime (UTC)."""
    parts = cron_expr.strip().split()
    if len(parts) != 5:
        return None
    minute, hour, day_of_month, month, day_of_week = parts
    now = datetime.datetime.now(datetime.timezone.utc)
    # Simple: find next matching time today or tomorrow
    for day_offset in range(14):
        candidate = now.replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=day_offset)
        try:
            if hour != "*":
                h = int(hour)
                if day_offset == 0 and h <= now.hour:
                    continue
                candidate = candidate.replace(hour=h)
            if minute != "*":
                candidate = candidate.replace(minute=int(minute))
            if day_of_week != "*":
                dow = int(day_of_week)
                if candidate.weekday() + 1 != dow:  # Python weekday: Mon=0
                    continue
            return candidate
        except (ValueError, TypeError):
            continue
    return None + datetime.timedelta(days=1)

def time_until_next_wake(cron_expr):
    """Return human-readable time until next wake."""
    next_wake = parse_cron_next(cron_expr)
    if not next_wake:
        return "not scheduled"
    now = datetime.datetime.now(datetime.timezone.utc)
    delta = next_wake - now
    if delta.total_seconds() < 0:
        return "wake time passed today"
    hours, rem = divmod(int(delta.total_seconds()), 3600)
    mins = rem // 60
    if hours > 24:
        days = hours // 24
        return f"in {days}d {hours%24}h"
    return f"in {hours}h {mins}m"

def sleep_until_next_wake(cron_expr):
    """Block until next wake time (for cron-triggered use)."""
    next_wake = parse_cron_next(cron_expr)
    if not next_wake:
        print("[Sleep] No valid cron schedule, skipping sleep")
        return
    now = datetime.datetime.now(datetime.timezone.utc)
    wait_secs = max(1, int((next_wake - now).total_seconds()))
    print(f"[Sleep] Sleeping until {next_wake.strftime('%Y-%m-%d %H:%M UTC')} ({wait_secs}s)...")
    time.sleep(min(wait_secs, 3600))  # Max 1hr per sleep cycle

# ── Topics Management ────────────────────────────────────────────────────────
DEFAULT_TOPICS = [
    "LLM multi-agent social norms emergence",
    "AI agent citation distortion scientific literature",
    "LLM theory of mind strategic reasoning Keynesian Beauty Contest",
    "human-AI collective behavior social influence",
    "multi-agent LLM coordination failure security",
]

def load_topics():
    if TOPICS_F.exists():
        with open(TOPICS_F) as f:
            data = json.load(f)
            return data.get("topics", DEFAULT_TOPICS)
    return DEFAULT_TOPICS

def save_topics(topics):
    TOPICS_F.parent.mkdir(parents=True, exist_ok=True)
    with open(TOPICS_F, "w") as f:
        json.dump({"topics": topics, "updated": datetime.datetime.now(datetime.timezone.utc).isoformat()}, f, indent=2)

def add_topic(topic):
    topics = load_topics()
    if topic not in topics:
        topics.append(topic)
        save_topics(topics)
        print(f"[Topics] Added: {topic}")
    else:
        print(f"[Topics] Already tracked: {topic}")

# ── GitHub Push ──────────────────────────────────────────────────────────────
def push_with_note(message, files=None, repo=None):
    """Git add + commit + push with structured commit message."""
    if not repo:
        repo = "/workspace/chi2026-norm-emergence"
    if not os.path.exists(os.path.join(repo, ".git")):
        print(f"[GitHub] Not a git repo: {repo}")
        return False
    try:
        if files:
            for f in files:
                subprocess.run(["git", "-C", repo, "add", f], check=True, capture_output=True)
        else:
            subprocess.run(["git", "-C", repo, "add", "-A"], check=True, capture_output=True)
        result = subprocess.run(
            ["git", "-C", repo, "commit", "-m", message],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            if "nothing to commit" in result.stderr.lower():
                print("[GitHub] Nothing to commit")
                return True
            print(f"[GitHub] Commit failed: {result.stderr}")
            return False
        push = subprocess.run(
            ["git", "-C", repo, "push", "origin", "master"],
            capture_output=True, timeout=30
        )
        if push.returncode == 0:
            print(f"[GitHub] ✓ {message[:60]}")
            return True
        else:
            print(f"[GitHub] Push failed: {push.stderr[:200]}")
            return False
    except Exception as e:
        print(f"[GitHub] Error: {e}")
        return False

# ── Research Pipeline ─────────────────────────────────────────────────────────
def run_literature_review(query, max_results=8):
    """Five-step evidence synthesis: search → screen → extract → synthesize → write."""
    print(f"\n[LitReview] Query: {query}")
    
    results = openalex_search(query, limit=max_results)
    if not results:
        results = arxiv_search(query, limit=max_results)
    
    if not results:
        return {"status": "no_results", "query": query}
    
    # Screen by novelty
    screened = [r for r in results if novelty_score(r) >= 2][:6]
    
    # Extract claims
    for r in screened:
        r["claims"] = extract_claims(r)
    
    # Synthesize
    synthesis = synthesize_findings(screened)
    
    # Write inbox file
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = OUT_DIR / f"literature-{slugify(query)}.md"
    content = format_literature_md(query, screened, synthesis)
    out_file.write_text(content)
    print(f"[LitReview] Written: {out_file}")
    
    return {
        "status": "success", "query": query,
        "n_results": len(results), "n_screened": len(screened),
        "output": str(out_file), "papers": screened
    }

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower())[:50]

def novelty_score(paper):
    score = 0
    t = (paper.get("title","") + paper.get("abstract","")).lower()
    for kw in ["fail","break","wrong","distort","bias","collapse","crisis","vulnerability"]:
        if kw in t: score += 1
    for kw in ["AI agent","multi-agent","emergent","collective","norm","coordination"]:
        if kw in t: score += 1
    if paper.get("citation_count",0) > 50: score += 1
    return max(0, min(5, score))

def extract_claims(paper):
    prompt = (
        f"From this paper abstract, extract exactly 3 specific empirical claims as a JSON list:\n"
        f"Title: {paper.get('title','?')}\n"
        f"Abstract: {paper.get('abstract','?')[:400]}\n\n"
        f'Output format: ["claim 1", "claim 2", "claim 3"]'
    )
    result = call_llm(prompt, max_tokens=200)
    try:
        m = re.search(r'\[.*\]', result, re.DOTALL)
        if m: return json.loads(m.group())
    except: pass
    return ["[Could not extract]"]

def synthesize_findings(papers):
    prompt = (
        f"You are a research synthesizer. Given {len(papers)} papers, produce 3 paragraphs:\n"
        f"1. What do they agree on?\n2. Where do they disagree?\n3. Most urgent open question?\n\n"
        + "\n\n".join([f"{i+1}. {p.get('title','?')[:80]}\n{p.get('abstract','?')[:200]}" for i,p in enumerate(papers)])
    )
    return call_llm(prompt, max_tokens=400)

def format_literature_md(query, papers, synthesis):
    lines = [
        f"# Literature Review — {datetime.date.today()}",
        f"**Query:** {query}",
        f"**Papers reviewed:** {len(papers)}",
        "",
    ]
    for i, p in enumerate(papers):
        stars = "⭐" * novelty_score(p)
        lines += [
            f"## {i+1}. {p.get('title','')}",
            f"- Authors: {p.get('authors','?')} | Year: {p.get('year','?')} | Venue: {p.get('venue','?')}",
            f"- Novelty: {stars}",
            f"- Claims:",
        ]
        for c in p.get("claims", []):
            lines.append(f"  - {c}")
        lines.append("")
    lines += ["## Synthesis", synthesis, ""]
    return "\n".join(lines)

def run_paper_review(paper_ident):
    """Three-perspective peer review."""
    print(f"\n[PaperReview] {paper_ident[:80]}")
    content = fetch_paper_content(paper_ident)
    if len(content) < 100:
        print(f"[PaperReview] Could not fetch content")
        return {"status": "fetch_failed"}
    
    reviews = {
        "reviewer": generate_review(content, "reviewer"),
        "methodologist": generate_review(content, "methodologist"),
        "practitioner": generate_review(content, "practitioner"),
    }
    
    overall = call_llm(
        f"Summarize 3 peer reviews and give recommendation (accept/reject/revise):\n"
        f"R: {reviews['reviewer'][:200]}\nM: {reviews['methodologist'][:200]}\nP: {reviews['practitioner'][:200]}",
        max_tokens=150
    )
    
    result = {"status": "success", "reviews": reviews, "overall": overall,
              "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = OUT_DIR / f"review-{slugify(paper_ident[:40])}.md"
    out_file.write_text(json.dumps(result, indent=2))
    print(f"[PaperReview] Written: {out_file}")
    return result

REVIEW_PROMPTS = {
    "reviewer": "Critical reviewer: (1) Is the research question well-motivated? (2) Are claims supported? (3) What would you reject this for?",
    "methodologist": "Methodologist: (1) Is design appropriate? (2) Are statistics correct? (3) Would it reproduce?",
    "practitioner": "Practitioner: (1) Works in real deployment? (2) Ethical concerns? (3) What would you change?",
}

def generate_review(content, role):
    prompt = f"{REVIEW_PROMPTS[role]}\n\nPaper:\n{content[:2000]}\n\n3-bullet structured review."
    return call_llm(prompt, max_tokens=300)

def check_citation_distortion(paper_ident):
    """SourceCheckup-style citation audit."""
    print(f"\n[CiteCheck] {paper_ident[:80]}")
    content = fetch_paper_content(paper_ident)
    prompt = (
        "You are a citation auditor. For each claim + citation pair:\n"
        "Is the citation SUPPORTED / CONTRADICTED / NOT ADDRESSED?\n"
        "Rate overall accuracy: HIGH / MEDIUM / LOW\n\n"
        f"Paper: {content[:3000]}"
    )
    result = call_llm(prompt, max_tokens=400)
    low = result.count("LOW") + result.count("contradicted") + result.count("not support")
    level = "HIGH" if low >= 3 else "MEDIUM" if low >= 1 else "LOW"
    
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = OUT_DIR / "cite-check.json"
    json.dump({"paper": paper_ident, "analysis": result, "level": level, "n_issues": low}, open(out_file,"w"), indent=2)
    print(f"[CiteCheck] {level} ({low} issues) → {out_file}")
    return {"level": level, "n_issues": low, "output": str(out_file)}

# ── Full Research Update ──────────────────────────────────────────────────────
def full_research_update():
    """Morning research update: run literature review for all active topics."""
    cfg = load_sleep_config()
    topics = cfg.get("active_topics") or load_topics()
    
    print(f"\n{'='*50}")
    print(f"Research Update — {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"Topics: {len(topics)}")
    print(f"{'='*50}")
    
    all_results = []
    for topic in topics:
        result = run_literature_review(topic)
        all_results.append(result)
        time.sleep(2)  # rate limit
    
    # Update journal
    journal_entry = f"- **{datetime.date.today()}**: {len(all_results)} topics reviewed — " + \
                   ", ".join([r["query"] for r in all_results if r["status"] == "success"])
    if JOURNAL.exists():
        JOURNAL.write_text(JOURNAL.read_text() + "\n" + journal_entry)
    else:
        JOURNAL.parent.mkdir(parents=True, exist_ok=True)
        JOURNAL.write_text(f"# Journal Index\n\n{journal_entry}\n")
    
    # Update config
    cfg["last_update"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    cfg["total_runs"] = cfg.get("total_runs", 0) + 1
    save_sleep_config(cfg)
    
    # Push
    push_with_note(f"AutoResearch update {datetime.date.today()}")
    
    return all_results

# ── Search APIs ─────────────────────────────────────────────────────────────
def openalex_search(query, limit=8):
    url = (f"https://api.openalex.org/works?search={urllib.parse.quote(query)}"
           f"&filter=is_oa:true&sort=relevance_score&per_page={limit}"
           f"&select=title,authorships,abstract_inverted_index,publication_year,"
           f"concepts,cited_by_count,primary_location,doi")
    try:
        import requests
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        return [_parse_openalex(w) for w in data.get("results",[])]
    except Exception as e:
        print(f"  OpenAlex error: {e}")
        return []

def _parse_openalex(w):
    abs_text = ""
    idx = w.get("abstract_inverted_index", {})
    if idx:
        words = {}
        for word, positions in idx.items():
            for pos in positions: words[pos] = word
        abs_text = " ".join(words[w] for w in sorted(words))
    authors = [a["author"]["display_name"] for a in w.get("authorships",[])[:3]]
    venue = w.get("primary_location",{}).get("source",{}).get("display_name","unknown")
    return {
        "title": w.get("title",""),
        "authors": ", ".join(authors),
        "abstract": abs_text[:500],
        "year": w.get("publication_year",""),
        "venue": venue,
        "citation_count": w.get("cited_by_count",0),
        "url": w.get("doi",""),
    }

def arxiv_search(query, limit=8):
    import urllib.request, ssl
    ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
    q = urllib.parse.quote(query[:50])
    url = f"http://export.arxiv.org/api/query?search_query=all:{q}&max_results={limit}&sortBy=relevance"
    try:
        req = urllib.request.Request(url, headers={"Accept":"application/xml"})
        r = urllib.request.urlopen(req, context=ctx, timeout=12)
        content = r.read().decode("utf-8", errors="replace")
        entries = re.findall(r"<entry>(.*?)</entry>", content, re.DOTALL)
        results = []
        for e in entries:
            tm = re.search(r"<title>(.*?)</title>", e, re.DOTALL)
            am = re.findall(r"<name>(.*?)</name>", e)
            sm = re.search(r"<summary>(.*?)</summary>", e, re.DOTALL)
            im = re.search(r"<id>(.*?)</id>", e, re.DOTALL)
            results.append({
                "title": tm.group(1).strip().replace("\n"," ") if tm else "",
                "authors": ", ".join(am[:3]),
                "abstract": sm.group(1).strip()[:500] if sm else "",
                "year": datetime.datetime.now().year,
                "venue": "arXiv",
                "citation_count": 0,
                "url": im.group(1) if im else "",
            })
        return results
    except Exception as e:
        print(f"  arXiv error: {e}")
        return []

def fetch_paper_content(paper_ident):
    if "arxiv.org" in str(paper_ident):
        import urllib.request, ssl
        ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
        aid = paper_ident.split("arxiv.org/")[-1].strip().split("/")[0].split("?")[0]
        url = f"http://export.arxiv.org/api/query?id_list={aid}"
        req = urllib.request.Request(url, headers={"Accept":"application/xml"})
        r = urllib.request.urlopen(req, context=ctx, timeout=15)
        sm = re.search(r"<summary>(.*?)</summary>", r.read().decode("utf-8",errors="replace"), re.DOTALL)
        return sm.group(1).strip() if sm else ""
    return str(paper_ident)

# ── LLM Call ────────────────────────────────────────────────────────────────
def call_llm(prompt, max_tokens=300):
    import urllib.request, ssl, os
    API_KEY = os.environ.get("MINIMAX_API_KEY","sk-cp-78BJu2Lhi7FGVnV1xvzDnj0J3b9AdDojkIQMAuDc03OSn5gI3pHTlxntB1inbwU4M0lCtAoSbc8vxbjoJjlKyg3dQDg7ZdAQXWrZtMMZcA0wWxZYe23-fv0")
    API_BASE = "https://api.minimaxi.com/anthropic/v1"
    ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
    req = urllib.request.Request(
        f"{API_BASE}/messages",
        data=json.dumps({"model":"MiniMax-M2-Highspeed","max_tokens":max_tokens,
                         "messages":[{"role":"user","content":prompt}]}).encode(),
        headers={"Authorization":f"Bearer {API_KEY}","Content-Type":"application/json","x-api-key":API_KEY},
        method="POST"
    )
    try:
        r = urllib.request.urlopen(req, context=ctx, timeout=30)
        resp = json.loads(r.read())
        for b in resp.get("content",[]):
            if b.get("type")=="text": return b["text"].strip()
        return ""
    except Exception as e:
        return f"[LLM error: {e}]"

# ── CLI ─────────────────────────────────────────────────────────────────────
HELP = """
auto_research_loop.py v4 — Research Pipeline

Commands:
  --update           Full morning research update (all topics)
  --sleep            Enter sleep mode until next cron wake
  --status           Show sleep schedule and run statistics
  --literature Q     Run literature review on query Q
  --review URL       Run three-perspective peer review on paper
  --cite-check URL   Run citation distortion check on paper
  --plan             Show today's research plan
  --topics            List active research topics
  --add-topic T      Add topic T to tracking list
"""

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or "--help" in args:
        print(HELP)
    elif "--status" in args:
        cfg = load_sleep_config()
        print(f"Cron: {cfg['cron']}")
        print(f"Next wake: {time_until_next_wake(cfg['cron'])}")
        print(f"Last wake: {cfg.get('last_wake','never')}")
        print(f"Last update: {cfg.get('last_update','never')}")
        print(f"Total runs: {cfg.get('total_runs',0)}")
        print(f"Active topics: {len(cfg.get('active_topics', load_topics()))}")
    elif "--sleep" in args:
        cfg = load_sleep_config()
        sleep_until_next_wake(cfg["cron"])
        print("[Wake] Good morning! Running research update...")
        full_research_update()
    elif "--update" in args:
        results = full_research_update()
        print(f"\nDone. {len(results)} topics processed.")
    elif "--literature" in args:
        idx = args.index("--literature") + 1
        q = args[idx] if idx < len(args) else ""
        run_literature_review(q)
    elif "--review" in args:
        idx = args.index("--review") + 1
        p = args[idx] if idx < len(args) else ""
        run_paper_review(p)
    elif "--cite-check" in args:
        idx = args.index("--cite-check") + 1
        p = args[idx] if idx < len(args) else ""
        check_citation_distortion(p)
    elif "--topics" in args:
        for t in load_topics(): print(f"  - {t}")
    elif "--add-topic" in args:
        idx = args.index("--add-topic") + 1
        t = args[idx] if idx < len(args) else ""
        add_topic(t)
    elif "--plan" in args:
        cfg = load_sleep_config()
        print(f"Next wake: {time_until_next_wake(cfg['cron'])}")
        print("Active topics:")
        for t in load_topics(): print(f"  • {t}")
    else:
        print(HELP)