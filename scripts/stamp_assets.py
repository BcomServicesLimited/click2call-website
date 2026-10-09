"""stamp_assets.py — add a content version to every local CSS and JS link.

WHY: /assets/css/*.css and /assets/js/*.js are served with
Cache-Control: max-age=14400 (4 hours). Without a version in the URL, a
returning visitor keeps the old file for up to 4 hours after a change and sees
new markup with old styles (it happened on 9 Oct 2026, when home-v2.css changed
between the homepage and Switch page launches).

The version is the first 10 hex characters of the file's SHA-256, so it changes
only when the file's content changes:

    href="/assets/css/tailwind.css"            -> href="/assets/css/tailwind.css?v=3f2a9c0d1e"
    href="/assets/css/tailwind.css?v=old"      -> href="/assets/css/tailwind.css?v=<new hash>"

Runs over every tracked .html file plus _header.html and _footer.html. Safe to
run any number of times; prints only the files it changed. Part of
`npm run prepush` (build -> sync -> stamp), so it runs after Tailwind is rebuilt
and the partials are synced.

    python3 scripts/stamp_assets.py
    python3 scripts/stamp_assets.py --check   # exit 1 if anything is stale

Standard library only.
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r'((?:href|src)=")(/assets/(?:css|js)/[^"?#]+\.(?:css|js))(?:\?v=[^"#]*)?(")')


def version(asset, cache={}):
    if asset not in cache:
        path = ROOT / asset.lstrip("/")
        cache[asset] = hashlib.sha256(path.read_bytes()).hexdigest()[:10] if path.is_file() else None
    return cache[asset]


def stamp(text):
    def sub(m):
        v = version(m.group(2))
        return m.group(0) if v is None else f"{m.group(1)}{m.group(2)}?v={v}{m.group(3)}"
    return LINK.sub(sub, text)


def main():
    check = "--check" in sys.argv
    tracked = subprocess.check_output(["git", "ls-files", "*.html"], cwd=ROOT, text=True).split()
    files = sorted(set(tracked) | {"_header.html", "_footer.html"})
    changed = []
    for name in files:
        path = ROOT / name
        if not path.is_file():
            continue
        old = path.read_text(encoding="utf-8")
        new = stamp(old)
        if new != old:
            changed.append(name)
            if not check:
                path.write_text(new, encoding="utf-8")
    missing = sorted(a for a, v in version.__defaults__[0].items() if v is None)
    for a in missing:
        print(f"warning: {a} is linked but not found; left unversioned")
    if check:
        print(f"{len(changed)} file(s) need stamping" + (": " + ", ".join(changed[:10]) if changed else ""))
        sys.exit(1 if changed else 0)
    print(f"stamped {len(changed)} file(s)")


if __name__ == "__main__":
    main()
