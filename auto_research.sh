#!/bin/bash
# AutoResearch Loop Runner for CHI 2026 Paper
# Runs every 6 hours to advance paper toward CHI quality

cd /workspace/chi2026-norm-emergence

REPORT=$(python3 paper/auto_research_loop.py 2>&1)
echo "[$(date -u)] AutoResearch: $REPORT"

# If iteration advanced, push to GitHub
if echo "$REPORT" | grep -q "iteration"; then
    git add -A > /dev/null 2>&1
    git commit -m "AutoResearch iteration: $(date -u '+%Y-%m-%d %H:%M UTC')" > /dev/null 2>&1
    GIT_HTTP_VERSION=HTTP/1.0 git push origin master > /dev/null 2>&1 &
fi
