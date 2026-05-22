#!/usr/bin/env python3
"""
sync_partials.py — Sync the canonical header and footer from _header.html
and _footer.html into every HTML page on the site.

Usage:
    python3 scripts/sync_partials.py            # sync header + footer
    python3 scripts/sync_partials.py --header   # sync only header
    python3 scripts/sync_partials.py --footer   # sync only footer
    python3 scripts/sync_partials.py --dry-run  # report changes without writing

Match strategy (per page, per partial):
    1. If the page contains the marker comments (e.g. "===== HEADER ====="
       and "=== END HEADER ==="), replace the content between them inclusive.
    2. Otherwise fall back to a DOM-tag match: first <header ... id="site-header">
       to its matching </header> (for the header partial), or the first
       <footer ...> to its matching </footer> (for the footer partial).
    3. After a successful replacement, the page will contain the marker
       comments — making future syncs marker-based and unambiguous.

The script is idempotent: running it twice produces the same result.
"""

import argparse
import os
import re
import sys
import glob

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Files we never modify
SKIP_BASENAMES = {
    "_header.html", "_footer.html",
    "template.html", "article-template.html",
    "email-signature-support.html",
    "primary-knowledge-base.html",
}
# Source-of-truth page — extracted partials came from here, leave it alone
SKIP_RELPATHS = {"index.html"}


def load_partial(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().rstrip("\n")


def find_partial_region(content, marker_start_re, marker_end_re, fallback_re):
    """Locate the partial region in `content`. The region is anchored by the
    fallback tag (e.g. <header ... id="site-header">...</header>) and then
    expanded outward to absorb any adjacent START/END marker comments — so
    that running the sync repeatedly does not pile up duplicate markers,
    and so that orphan markers from prior partial syncs are cleaned up.

    Returns (start_idx, end_idx) covering the full region to be replaced,
    or (None, None) if the fallback tag isn't found."""
    fb = fallback_re.search(content)
    if not fb:
        return None, None

    region_start, region_end = fb.start(), fb.end()

    # Expand backward to absorb a START marker if it sits immediately before
    # the tag (only whitespace allowed between marker and tag opening).
    head = content[:region_start]
    last_start_match = None
    for m in marker_start_re.finditer(head):
        last_start_match = m
    if last_start_match and head[last_start_match.end():].strip() == "":
        region_start = last_start_match.start()

    # Expand forward to absorb an END marker if it sits immediately after
    # the tag (only whitespace allowed between tag close and marker).
    tail = content[region_end:]
    end_match = marker_end_re.search(tail)
    if end_match and tail[:end_match.start()].strip() == "":
        region_end = region_end + end_match.end()

    return region_start, region_end


def replace_partial(content, partial_text, marker_start_re, marker_end_re, fallback_re):
    """Replace the partial. Returns (new_content, mode) where mode is
    "replaced" or None (not found)."""
    s, e = find_partial_region(content, marker_start_re, marker_end_re, fallback_re)
    if s is None:
        return content, None
    return content[:s] + partial_text + content[e:], "replaced"


# Marker regexes — match the homepage's existing comment style, tolerant of
# minor whitespace/punctuation variations.
HEADER_START_RE = re.compile(r"<!--\s*=+\s*HEADER\s*=+\s*-->", re.IGNORECASE)
HEADER_END_RE   = re.compile(r"<!--\s*=+\s*END\s+HEADER\s*=+\s*-->", re.IGNORECASE)
FOOTER_START_RE = re.compile(r"<!--\s*=+\s*FOOTER\s*=+\s*-->", re.IGNORECASE)
FOOTER_END_RE   = re.compile(r"<!--\s*=+\s*END\s+FOOTER\s*=+\s*-->", re.IGNORECASE)

# Fallback regexes — used only when markers are absent.
# Header: first <header ...id="site-header"...>...</header>
HEADER_FALLBACK_RE = re.compile(
    r'<header\b[^>]*\bid="site-header"[^>]*>[\s\S]*?</header>',
    re.IGNORECASE,
)
# Also accept the reverse attribute order (id before class)
HEADER_FALLBACK_RE_ALT = re.compile(
    r'<header\b[^>]*>[\s\S]*?</header>',
    re.IGNORECASE,
)
# Footer: first <footer ...>...</footer> on the page (site footer)
FOOTER_FALLBACK_RE = re.compile(
    r'<footer\b[^>]*>[\s\S]*?</footer>',
    re.IGNORECASE,
)

# Match any HTML comment <!-- ... --> non-greedily.
HTML_COMMENT_RE = re.compile(r"<!--[\s\S]*?-->", re.DOTALL)

# Inside a comment, this string identifies the legacy "Shared Header/Footer
# Snippet" instruction blocks that were copy-pasted into many pages.
LEGACY_COMMENT_MARKER_RE = re.compile(
    r"Shared\s+(?:Header|Footer)\s+Snippet",
    re.IGNORECASE,
)


def strip_legacy_comments(content):
    """Remove legacy 'Click2Call — Shared Header/Footer Snippet' instruction
    comments. Implemented as: iterate HTML comments, drop any whose body
    matches LEGACY_COMMENT_MARKER_RE. Idempotent.

    These comments must be removed before the fallback partial regex runs,
    because they contain literal <footer ...> text fragments that would
    otherwise confuse the regex into matching across the comment + the real
    site footer."""
    def _drop_if_legacy(m):
        return "" if LEGACY_COMMENT_MARKER_RE.search(m.group(0)) else m.group(0)
    new = HTML_COMMENT_RE.sub(_drop_if_legacy, content)
    # Collapse any blank lines left where the comment used to be.
    new = re.sub(r"\n[ \t]*\n[ \t]*\n+", "\n\n", new)
    return new


def iter_html_files():
    pattern_root = os.path.join(REPO_ROOT, "*.html")
    pattern_nested = os.path.join(REPO_ROOT, "**", "*.html")
    files = set(glob.glob(pattern_root)) | set(glob.glob(pattern_nested, recursive=True))
    return sorted(files)


def should_skip(filepath):
    basename = os.path.basename(filepath)
    if basename in SKIP_BASENAMES:
        return "partial/template"
    rel = os.path.relpath(filepath, REPO_ROOT)
    if rel in SKIP_RELPATHS:
        return "source-of-truth"
    return None


def sync_one(filepath, *, do_header, do_footer, header_text, footer_text, dry_run):
    with open(filepath, "r", encoding="utf-8") as f:
        original = f.read()
    content = strip_legacy_comments(original)
    modes = {}

    if do_header:
        new_content, mode = replace_partial(
            content, header_text, HEADER_START_RE, HEADER_END_RE, HEADER_FALLBACK_RE
        )
        if mode is None:
            # Try the more permissive fallback (any <header>)
            new_content, mode = replace_partial(
                content, header_text, HEADER_START_RE, HEADER_END_RE, HEADER_FALLBACK_RE_ALT
            )
        modes["header"] = mode
        content = new_content

    if do_footer:
        new_content, mode = replace_partial(
            content, footer_text, FOOTER_START_RE, FOOTER_END_RE, FOOTER_FALLBACK_RE
        )
        modes["footer"] = mode
        content = new_content

    if content == original:
        return "unchanged", modes
    if not dry_run:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    return "updated", modes


def main():
    parser = argparse.ArgumentParser(description="Sync canonical header/footer into every HTML page.")
    parser.add_argument("--header", action="store_true", help="Sync header only")
    parser.add_argument("--footer", action="store_true", help="Sync footer only")
    parser.add_argument("--dry-run", action="store_true", help="Do not write files; just report")
    args = parser.parse_args()

    do_header = args.header or not args.footer  # default: both
    do_footer = args.footer or not args.header

    header_text = load_partial(os.path.join(REPO_ROOT, "_header.html")) if do_header else ""
    footer_text = load_partial(os.path.join(REPO_ROOT, "_footer.html")) if do_footer else ""

    updated, unchanged, skipped, not_found = [], [], [], []

    for filepath in iter_html_files():
        skip_reason = should_skip(filepath)
        if skip_reason:
            skipped.append((filepath, skip_reason))
            continue

        status, modes = sync_one(
            filepath,
            do_header=do_header,
            do_footer=do_footer,
            header_text=header_text,
            footer_text=footer_text,
            dry_run=args.dry_run,
        )
        rel = os.path.relpath(filepath, REPO_ROOT)
        if status == "updated":
            updated.append((rel, modes))
        else:
            unchanged.append((rel, modes))

        # Report files that didn't match either marker or fallback for a requested partial
        for partial, mode in modes.items():
            if mode is None:
                not_found.append((rel, partial))

    print()
    print(f"{'DRY RUN: ' if args.dry_run else ''}sync_partials complete")
    print(f"  updated   : {len(updated)}")
    print(f"  unchanged : {len(unchanged)}")
    print(f"  skipped   : {len(skipped)}")
    if not_found:
        print(f"  not found : {len(not_found)} (partial missing on page)")
        for rel, partial in not_found[:20]:
            print(f"    ! {rel}: no {partial} block matched")
        if len(not_found) > 20:
            print(f"    ... and {len(not_found) - 20} more")

    if updated:
        print("\nUpdated files (first 30):")
        for rel, modes in updated[:30]:
            tag = ",".join(f"{k}:{v}" for k, v in modes.items() if v)
            print(f"  ✓ {rel}  [{tag}]")
        if len(updated) > 30:
            print(f"  ... and {len(updated) - 30} more")


if __name__ == "__main__":
    main()
