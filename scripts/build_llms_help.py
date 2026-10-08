"""build_llms_help.py — keep the help centre visible to AI systems.

Does three things, all from the HELP_ARTICLES registry in assets/js/articles.js:

1. Rewrites the "## Help Centre" section of llms.txt and llms-full.md so every
   published guide is listed under its category. Lines that already exist for a
   URL are kept as written (many carry hand-tuned descriptions); new guides get
   the registry description.
2. Writes llms-help.md: the full text of every help guide as Markdown, one
   section per guide, so an AI crawler can read the whole help centre in a
   single fetch.
3. Prints any registry URL with no matching help/*.html file.

Run after adding or editing help pages:
    python3 scripts/build_llms_help.py

Standard library only.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://www.click2call.com.au"
CATS = [
    ("getting-started", "Getting Started"),
    ("phone-numbers", "Phone Numbers"),
    ("extensions", "Extensions & Users"),
    ("devices", "Phones & Devices"),
    ("call-flows", "Call Flows"),
    ("billing", "Billing & Account"),
    ("ai", "AI Features"),
]


def registry():
    js = (ROOT / "assets/js/articles.js").read_text(encoding="utf-8")
    body = js[js.index("var HELP_ARTICLES"):]
    out = []
    for block in re.findall(r"\{(.*?)\}", body, re.S):
        def field(name):
            m = re.search(name + r':\s*"((?:[^"\\]|\\.)*)"', block)
            return json.loads('"' + m.group(1) + '"') if m else ""
        url = field("url")
        if url.startswith("/help/"):
            out.append({"url": url, "title": field("title"), "desc": field("desc"),
                        "cat": field("category")})
    seen, uniq = set(), []
    for a in out:
        if a["url"] not in seen:
            seen.add(a["url"]); uniq.append(a)
    return uniq


def page_markdown(path):
    s = path.read_text(encoding="utf-8")
    m = re.search(r"<main[^>]*>(.*?)</main>", s, re.S)
    s = m.group(1) if m else s
    # drop the related-guides block, CTA and scripts/svg
    s = re.split(r'<h2[^>]*>\s*Related Guides', s)[0]
    s = re.split(r'<h2[^>]*>\s*Still need help', s)[0]
    s = re.sub(r"<(script|style|svg|nav)[^>]*>.*?</\1>", "", s, flags=re.S)
    s = re.sub(r"<pre[^>]*>(.*?)</pre>", lambda m: "\n```\n" + re.sub(r"<[^>]+>", "", m.group(1)).strip() + "\n```\n", s, flags=re.S)
    for n in range(1, 5):
        s = re.sub(rf"<h{n}[^>]*>(.*?)</h{n}>", lambda m, n=n: "\n" + "#" * (n + 1) + " " + re.sub(r"<[^>]+>", "", m.group(1)).strip() + "\n", s, flags=re.S)
    s = re.sub(r"<tr[^>]*>(.*?)</tr>", lambda m: "| " + " | ".join(re.sub(r"<[^>]+>", "", c).strip() for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", m.group(1), re.S)) + " |\n", s, flags=re.S)
    s = re.sub(r"<li[^>]*>", "\n- ", s)
    s = re.sub(r'<a [^>]*href="(/[^"]*)"[^>]*>(.*?)</a>', lambda m: f"[{re.sub('<[^>]+>', '', m.group(2)).strip()}]({BASE}{m.group(1)})", s, flags=re.S)
    s = re.sub(r"<(strong|b)>(.*?)</\1>", r"**\2**", s, flags=re.S)
    s = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", s, flags=re.S)
    s = re.sub(r"</(p|div|ul|ol|table)>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = "\n".join(l.strip() for l in s.splitlines())
    s = re.sub(r"\n{3,}", "\n\n", s).strip()
    return s


def help_section(arts, existing):
    lines = ["## Help Centre", "",
             f"The Click2Call Help Centre has {len(arts)} step-by-step guides for setting up and running a Click2Call phone system. "
             f"The full text of every guide is in one file: {BASE}/llms-help.md", "",
             f"- **Help Centre Index**: [{BASE}/help]({BASE}/help) — Browse all how-to guides by category.",
             f"- **Full text of all help guides**: [{BASE}/llms-help.md]({BASE}/llms-help.md)", ""]
    for key, label in CATS:
        group = [a for a in arts if a["cat"] == key]
        if not group:
            continue
        lines.append(f"### {label}")
        for a in group:
            url = BASE + a["url"]
            keep = existing.get(a["url"])
            lines.append(keep or f"- **{a['title']}**: [{url}]({url}) — {a['desc']}")
        lines.append("")
    return "\n".join(lines) + "\n"


def rewrite(path, arts):
    s = path.read_text(encoding="utf-8")
    start = s.index("## Help Centre")
    m = re.search(r"\n## (?!Help Centre)", s[start + 5:])
    end = start + 5 + m.start() + 1
    old = s[start:end]
    existing = {}
    for line in old.splitlines():
        u = re.search(r"click2call\.com\.au(/help/[a-z0-9-]+)", line)
        if u and line.lstrip().startswith("- ") and u.group(1) not in existing:
            existing[u.group(1)] = line.replace("https://click2call.com.au", BASE)
    # keep the external-AI-provider subsection (it has its own intro) as is
    ext = ""
    i = old.find("### Connecting External AI Voice Providers")
    if i >= 0:
        ext = old[i:].rstrip() + "\n\n"
        ext_urls = set(re.findall(r"click2call\.com\.au(/help/[a-z0-9-]+)", ext))
        arts = [a for a in arts if a["url"] not in ext_urls]
    path.write_text(s[:start] + help_section(arts, existing) + ext + s[end:], encoding="utf-8")


def main():
    arts = [a for a in registry() if (ROOT / (a["url"].lstrip("/") + ".html")).exists()]
    for a in registry():
        if not (ROOT / (a["url"].lstrip("/") + ".html")).exists():
            print("missing page:", a["url"])
    for name in ("llms.txt", "llms-full.md"):
        rewrite(ROOT / name, arts)
    parts = ["# Click2Call Help Centre — full text of every guide", "",
             "Click2Call is an Australian Cloud PBX, VoIP and AI voice provider (Bcom Services Pty Ltd, ABN 92 636 893 108). "
             "This file contains the complete text of every guide in the Click2Call Help Centre, for AI assistants and search engines. "
             f"Each section links to the live page. Index: {BASE}/help/ · Site summary: {BASE}/llms.txt", ""]
    for key, label in CATS:
        group = [a for a in arts if a["cat"] == key]
        if not group:
            continue
        parts.append(f"# {label}\n")
        for a in group:
            body = page_markdown(ROOT / (a["url"].lstrip("/") + ".html"))
            i = body.find("## " + a["title"])
            if i >= 0:  # drop the category label / read time / H1 above the intro
                body = body[i + len(a["title"]) + 3:].lstrip()
            parts.append(f"## {a['title']}\n\nSource: {BASE}{a['url']}\n\n{body}\n")
    (ROOT / "llms-help.md").write_text("\n".join(parts), encoding="utf-8")
    print(f"{len(arts)} guides → llms.txt, llms-full.md help sections; llms-help.md written")


if __name__ == "__main__":
    main()
