"""Rewrites the "Recently pushed" block of README.md from the GitHub API."""
import json
import os
import re
import urllib.request

USER = "Ajay702"
req = urllib.request.Request(
    f"https://api.github.com/users/{USER}/repos?sort=pushed&per_page=30&type=owner",
    headers={"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}", "Accept": "application/vnd.github+json"},
)
repos = [r for r in json.load(urllib.request.urlopen(req))
         if not r["fork"] and not r["private"] and r["name"].lower() != USER.lower()][:5]

lines = [f"- [{r['name']}]({r['html_url']}) - {r['pushed_at'][:10]}" + (f" - {r['description']}" if r["description"] else "")
         for r in repos]

readme = open("README.md").read()
readme = re.sub(r"(<!-- recent:start -->\n).*?(<!-- recent:end -->)",
                lambda m: m.group(1) + "\n".join(lines) + "\n" + m.group(2), readme, flags=re.S)
open("README.md", "w").write(readme)
