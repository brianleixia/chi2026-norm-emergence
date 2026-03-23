#!/usr/bin/env python3
import urllib.request, json, base64, os

os.makedirs('/workspace/chi2026-norm-emergence/skill-refs', exist_ok=True)

repos = [
    ("amplify-paper-writing", "EvoClaw", "amplify", "skills/paper-writing/SKILL.md"),
    ("scientific-writing", "christophacham", "agent-skills-library", "skills/writing/scientific-writing/SKILL.md"),
]

for slug, owner, repo, path in repos:
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/vnd.github.v3+json", "User-Agent": "Mozilla/5.0"})
        r = urllib.request.urlopen(req, timeout=10)
        data = json.loads(r.read())
        content = base64.b64decode(data['content']).decode('utf-8', errors='replace')
        outdir = f"/workspace/chi2026-norm-emergence/skill-refs/{slug}"
        os.makedirs(outdir, exist_ok=True)
        with open(f"{outdir}/SKILL.md", 'w') as f:
            f.write(content)
        print(f"Downloaded {slug}: {len(content)} chars")
    except Exception as e:
        print(f"Failed {slug}: {e}")
