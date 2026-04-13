#!/usr/bin/env python3
"""
apply_footer.py
Replaces the <footer>...</footer> block in ALL HTML files across the
Click2Call website with the canonical footer from _footer.html.

Usage:
    python3 scripts/apply_footer.py

The script skips cloud-pbx/index.html (the source of the template)
and skips template/partial files.
"""

import os
import re
import glob

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOOTER_TEMPLATE_PATH = os.path.join(REPO_ROOT, "_footer.html")
SKIP_FILE = os.path.join(REPO_ROOT, "cloud-pbx", "index.html")
# Also skip template/partial files
SKIP_BASENAMES = [
    "_footer.html", "_header.html", "template.html",
    "article-template.html", "email-signature-support.html",
    "primary-knowledge-base.html"
]

# Read the canonical footer template
with open(FOOTER_TEMPLATE_PATH, "r", encoding="utf-8") as f:
    footer_template = f.read().rstrip("\n")

# Find ALL html files recursively
html_files = sorted(glob.glob(os.path.join(REPO_ROOT, "**", "*.html"), recursive=True))
# Also include root-level html files
html_files += sorted(glob.glob(os.path.join(REPO_ROOT, "*.html")))
html_files = sorted(set(html_files))

changed = []
skipped_no_footer = []
skipped_source = []
skipped_pattern = []

for filepath in html_files:
    # Skip the source file
    if os.path.abspath(filepath) == os.path.abspath(SKIP_FILE):
        skipped_source.append(filepath)
        continue

    # Skip template/partial files
    basename = os.path.basename(filepath)
    if basename in SKIP_BASENAMES:
        skipped_pattern.append(filepath)
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Match everything from <footer to </footer> (inclusive, non-greedy across newlines)
    pattern = re.compile(r'<footer[\s\S]*?</footer>', re.DOTALL)
    match = pattern.search(content)

    if not match:
        skipped_no_footer.append(filepath)
        continue

    new_content = pattern.sub(footer_template, content, count=1)

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        rel_path = os.path.relpath(filepath, REPO_ROOT)
        changed.append(rel_path)
    else:
        # Footer was already identical
        rel_path = os.path.relpath(filepath, REPO_ROOT)
        changed.append(f"{rel_path} (already identical)")

print(f"\n{'='*60}")
print(f"Footer replacement complete")
print(f"{'='*60}")
print(f"\nFiles updated ({len(changed)}):")
for f in changed:
    print(f"  ✓ {f}")

if skipped_no_footer:
    print(f"\nFiles with no <footer> tag ({len(skipped_no_footer)}):")
    for f in skipped_no_footer:
        print(f"  ✗ {os.path.relpath(f, REPO_ROOT)}")

if skipped_pattern:
    print(f"\nFiles skipped (templates/partials) ({len(skipped_pattern)}):")
    for f in skipped_pattern:
        print(f"  - {os.path.relpath(f, REPO_ROOT)}")

print(f"\nSource file skipped (template origin):")
for f in skipped_source:
    print(f"  - {os.path.relpath(f, REPO_ROOT)}")

print(f"\nDone.\n")
