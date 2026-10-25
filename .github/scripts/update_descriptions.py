#!/usr/bin/env python3
"""Refresh the Description column of the README table from each org's GitHub About text.

- If the org has an About text, it replaces the description in the row.
- If the org has none, the description already in the row stays.
- A row whose description ends with <!-- keep --> is never touched.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request

README = "README.md"
KEEP = "<!-- keep -->"

ROW = re.compile(
    r'^(\| <img src="https://github\.com/([A-Za-z0-9-]+)\.png[^>]*> \| .*? \| )'
    r'(.*?)'
    r'( \| \[Visit Org\]\(https://github\.com/[A-Za-z0-9-]+\) \|)\s*$'
)


def about_text(login):
    req = urllib.request.Request(
        f"https://api.github.com/orgs/{login}",
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "update-descriptions",
            **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {}),
        },
    )
    try:
        with urllib.request.urlopen(req) as r:
            return (json.load(r).get("description") or "").strip()
    except urllib.error.HTTPError as e:
        print(f"  warning: {login}: GitHub returned {e.code}, keeping current text")
    except urllib.error.URLError as e:
        print(f"  warning: {login}: {e.reason}, keeping current text")
    return ""


def clean(text):
    """One line, capped, and safe to drop into a Markdown table cell."""
    text = " ".join(text.split())[:200]
    return re.sub(r"([\\`*_\[\]|<>&])", r"\\\1", text)


def main():
    with open(README, newline="", encoding="utf-8") as f:
        lines = f.readlines()

    changed = 0
    out = []
    for line in lines:
        body = line.rstrip("\r\n")
        ending = line[len(body):]
        m = ROW.match(body)
        if not m:
            out.append(line)
            continue

        head, login, current, tail = m.groups()
        if KEEP in current:
            out.append(line)
            continue

        new = clean(about_text(login))
        if new and new != current:
            print(f"  updated {login}: {new}")
            out.append(head + new + tail + ending)
            changed += 1
        else:
            out.append(line)

    if changed:
        with open(README, "w", newline="", encoding="utf-8") as f:
            f.writelines(out)
    print(f"{changed} description(s) updated")


if __name__ == "__main__":
    sys.exit(main())
