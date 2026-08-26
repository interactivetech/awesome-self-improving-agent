#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "data" / "projects.yml"
PAPERS = ROOT / "data" / "papers.yml"
WATCHLIST = ROOT / "data" / "watchlist.yml"

def fail(msg):
    print(f"ERROR: {msg}")
    return 1

def main():
    errors = 0
    p = PROJECTS.read_text(encoding="utf-8")
    papers = PAPERS.read_text(encoding="utf-8")
    w = WATCHLIST.read_text(encoding="utf-8")

    names = re.findall(r'^\s+- name:\s+"([^"]+)"', p, flags=re.M)
    repos = re.findall(r'^\s+repo:\s+"([^"]+)"', p, flags=re.M)
    statuses = re.findall(r'^\s+status:\s+"([^"]+)"', p, flags=re.M)

    if not names:
        errors += fail("No projects found")
    if len(names) != len(set(n.lower() for n in names)):
        errors += fail("Duplicate project name")
    if len(repos) != len(set(r.lower() for r in repos)):
        errors += fail("Duplicate repository URL")

    allowed = {"official", "reference", "third-party", "official-borderline"}
    bad = sorted(set(statuses) - allowed)
    if bad:
        errors += fail(f"Unknown project status values: {bad}")

    for repo in repos:
        if not repo.startswith("https://github.com/"):
            errors += fail(f"Repository is not a GitHub URL: {repo}")

    methods = re.findall(r'^\s+- method:\s+"([^"]+)"', papers, flags=re.M)
    paper_urls = re.findall(r'^\s+paper:\s+"([^"]*)"', papers, flags=re.M)
    code_statuses = re.findall(r'^\s+code_status:\s+"([^"]+)"', papers, flags=re.M)

    if not methods:
        errors += fail("No papers found")
    if len(methods) != len(set(m.lower() for m in methods)):
        errors += fail("Duplicate paper method")

    allowed_paper_status = allowed | {"paper-only", "preview"}
    bad_paper = sorted(set(code_statuses) - allowed_paper_status)
    if bad_paper:
        errors += fail(f"Unknown paper code_status values: {bad_paper}")

    for url in paper_urls:
        if url and not url.startswith("https://"):
            errors += fail(f"Paper URL is not HTTPS: {url}")

    watch_names = re.findall(r'^\s+- name:\s+"([^"]+)"', w, flags=re.M)
    if not watch_names:
        errors += fail("No watchlist items found")

    if errors:
        return 1

    print(f"OK: {len(names)} projects, {len(methods)} papers, {len(watch_names)} watchlist items")
    return 0

if __name__ == "__main__":
    sys.exit(main())
