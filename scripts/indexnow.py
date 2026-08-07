"""indexnow.py — submit changed URLs to IndexNow so search engines recrawl
within hours instead of waiting for their own schedule.

WHY A SCRIPT: submissions used to be done by hand with a GET query string:

    https://yandex.com/indexnow?url=<url>&key=<key>

That endpoint started returning 422 in August 2026. The JSON POST form still
returns 202. This script uses the POST form and keeps the key in one place so
the next format change is a one-line fix rather than a silent no-op.

USAGE
    python3 scripts/indexnow.py https://www.click2call.com.au/support/ ...
    python3 scripts/indexnow.py --changed        # URLs from the last commit
    python3 scripts/indexnow.py --changed --dry-run

Bing is submitted alongside Yandex but will 403 until the domain is verified
in Bing Webmaster Tools. That is expected and is reported, not treated as a
failure — Yandex succeeding is enough to trigger a recrawl.

Standard library only.
"""
import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

HOST = "www.click2call.com.au"
BASE = f"https://{HOST}"
KEY = "c545b40a993f47dc8e19d97473df5270fb62e2f6"
KEY_LOCATION = f"{BASE}/{KEY}.txt"

ENDPOINTS = [
    ("Yandex", "https://yandex.com/indexnow"),
    ("Bing", "https://www.bing.com/indexnow"),
]

# IndexNow accepts at most 10,000 URLs per submission; nowhere near a concern
# for this site, but chunk anyway so a future bulk run cannot silently fail.
MAX_URLS = 10000


def url_for(path: str) -> str:
    """Public URL for a repo-relative .html file.

    Prefers the page's own rel="canonical", which is authoritative and avoids
    guessing wrong about trailing slashes: directory pages canonicalise WITH a
    trailing slash while standalone .html pages (the blog posts) canonicalise
    WITHOUT one. Guessing produced URLs that 308-redirected to the real thing,
    which wastes the submission.
    """
    try:
        head = Path(path).read_text(errors="replace")[:8000]
        m = (re.search(r'rel="canonical"[^>]*href="([^"]+)"', head)
             or re.search(r'href="([^"]+)"[^>]*rel="canonical"', head))
        if m and m.group(1).startswith(BASE):
            return m.group(1)
    except OSError:
        pass
    if path.endswith("index.html"):
        stem = path[: -len("index.html")].rstrip("/")
        return f"{BASE}/{stem}/" if stem else f"{BASE}/"
    return f"{BASE}/{path[: -len('.html')]}"


def changed_urls() -> list:
    """Map files touched by the last commit to their public URLs."""
    out = subprocess.run(
        ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"],
        capture_output=True, text=True, check=True).stdout.split()
    return sorted({url_for(f) for f in out if f.endswith(".html")})


def submit(name: str, endpoint: str, urls: list) -> bool:
    payload = json.dumps({
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }).encode("utf-8")
    req = urllib.request.Request(
        endpoint, data=payload, method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"  {name:8s} HTTP {resp.status} — accepted")
            return True
    except urllib.error.HTTPError as e:
        note = ""
        if name == "Bing" and e.code == 403:
            note = "  (expected until the domain is verified in Bing Webmaster Tools)"
        print(f"  {name:8s} HTTP {e.code}{note}")
        return False
    except urllib.error.URLError as e:
        print(f"  {name:8s} unreachable: {e.reason}")
        return False


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("urls", nargs="*", help="Full URLs to submit")
    ap.add_argument("--changed", action="store_true",
                    help="Derive URLs from the .html files in the last commit")
    ap.add_argument("--dry-run", action="store_true",
                    help="Show what would be submitted, submit nothing")
    args = ap.parse_args()

    urls = list(args.urls)
    if args.changed:
        urls += changed_urls()
    urls = sorted(set(urls))

    if not urls:
        print("No URLs to submit.")
        return 0
    if len(urls) > MAX_URLS:
        print(f"Refusing to submit {len(urls)} URLs (limit {MAX_URLS}).")
        return 1

    print(f"{len(urls)} URL(s):")
    for u in urls:
        print(f"  {u}")
    if args.dry_run:
        print("\nDRY RUN — nothing submitted.")
        return 0

    print()
    results = [submit(name, ep, urls) for name, ep in ENDPOINTS]
    # Yandex alone is enough to trigger a recrawl, so succeed if any endpoint
    # accepted. Exiting non-zero only when every endpoint rejected keeps this
    # usable in a chain without Bing's expected 403 breaking the build.
    return 0 if any(results) else 1


if __name__ == "__main__":
    sys.exit(main())
