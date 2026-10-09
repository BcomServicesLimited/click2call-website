"""check_landing_overlap.py — how much wording each landing page shares with the others.

WHY: Google treats pages that differ only by a swapped city or industry name
as near-duplicates. The landing-page rebuild (Oct 2026 onwards) holds every
rebuilt page to a rule: no more than 25% of its wording may also appear on any
single other landing page.

HOW IT MEASURES: the visible body text of each page (header, navigation,
footer, scripts and styles removed) is cut into overlapping 5-word phrases.
For page A and page B, "shared" is the share of A's phrases that also appear
on B. A page's score is its highest share against any one other page.

Landing pages = every top-level folder starting with voip- plus call-centre,
so new pages (e.g. a North Queensland or aged-care page) are included as soon
as their folder exists.

USAGE
    python3 scripts/check_landing_overlap.py                  # report every landing page
    python3 scripts/check_landing_overlap.py voip-perth       # check one page; exit 1 if over 25%
    python3 scripts/check_landing_overlap.py --threshold 0.2 voip-perth

Standard library only.
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
K = 5
DEFAULT_THRESHOLD = 0.25


def landing_pages():
    names = sorted(p.name for p in ROOT.iterdir()
                   if p.is_dir() and (p.name.startswith("voip-") or p.name == "call-centre")
                   and (p / "index.html").is_file())
    return names


def body_text(name):
    s = (ROOT / name / "index.html").read_text(encoding="utf-8")
    s = re.sub(r"<head.*?</head>", " ", s, flags=re.S | re.I)
    for tag in ("script", "style", "svg", "header", "nav", "footer", "noscript"):
        s = re.sub(rf"<{tag}\b.*?</{tag}>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", s)).split())


def phrases(text):
    words = re.findall(r"[a-z0-9$']+", text.lower())
    return {" ".join(words[i:i + K]) for i in range(len(words) - K + 1)}


def main(argv):
    threshold = DEFAULT_THRESHOLD
    if "--threshold" in argv:
        i = argv.index("--threshold")
        threshold = float(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    pages = landing_pages()
    sets = {p: phrases(body_text(p)) for p in pages}
    targets = argv or pages
    unknown = [t for t in targets if t not in sets]
    if unknown:
        sys.exit(f"not a landing page folder: {', '.join(unknown)}")

    failed = []
    print(f"{'page':38s} {'words*':>7s}  {'max shared':>10s}  with")
    for a in targets:
        best, partner = 0.0, "-"
        for b in pages:
            if b == a or not sets[a]:
                continue
            share = len(sets[a] & sets[b]) / len(sets[a])
            if share > best:
                best, partner = share, b
        flag = "  OVER" if best > threshold else ""
        print(f"{a:38s} {len(sets[a]):7d}  {best:9.0%}   {partner}{flag}")
        if best > threshold:
            failed.append(a)
    print(f"\n* 5-word phrases counted. Rule: max shared <= {threshold:.0%}.")
    if argv and failed:
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
