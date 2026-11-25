#!/usr/bin/env python3
"""Add or refresh the 'Reviewed by Royce Clark, Director · Updated <Month YYYY>' line
on every help guide, and point the guide's main JSON-LD author at the Person entity
defined on /about/ (#royce-clark), with the Organization as publisher.

Usage: python3 scripts/help_reviewed_by.py [--month 2026-11 slug ...]
  With no slugs: every guide keeps its current month (from the existing line,
  the 'Last reviewed' line or dateModified).
  With --month and slugs: those guides are stamped with that month and dateModified.
"""
import re, json, sys, glob, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PERSON = {"@type": "Person", "@id": "https://www.click2call.com.au/about/#royce-clark",
          "name": "Royce Clark", "url": "https://www.click2call.com.au/about/"}
ORG = {"@type": "Organization", "@id": "https://www.click2call.com.au/#organization", "name": "Click2Call"}
MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"]
SKIP = {"index", "primary-knowledge-base"}

def line(ym):
    y, m = ym.split("-")
    return ('<div class="help-reviewed mt-4 flex items-center gap-3">'
            '<span class="w-9 h-9 rounded-full flex items-center justify-center text-xs font-bold text-white flex-shrink-0" style="background-color:#3B9C49;" aria-hidden="true">RC</span>'
            f'<p class="text-sm text-gray-600">Reviewed by <a href="/about/" class="font-semibold text-gray-900 hover:text-[#3B9C49]">Royce Clark</a>, Director &middot; Updated <time datetime="{y}-{m}">{MONTHS[int(m)-1]} {y}</time></p></div>')

def process(path, force_month=None, today=None):
    s = open(path, encoding="utf-8").read()
    orig = s
    ym = force_month
    if not ym:
        m = re.search(r'<time datetime="(\d{4}-\d{2})">', s[s.find('help-reviewed'):] if 'help-reviewed' in s else '')
        if 'help-reviewed' in s and m: ym = m.group(1)
    if not ym:
        m = re.search(r'Last reviewed:?\s*(\w+) (\d{4})', s)
        if m and m.group(1) in MONTHS: ym = f"{m.group(2)}-{MONTHS.index(m.group(1))+1:02d}"
    if not ym:
        m = re.search(r'"dateModified":\s*"(\d{4}-\d{2})', s)
        ym = m.group(1) if m else "2026-11"
    new = line(ym)
    if 'help-reviewed' in s:
        s = re.sub(r'<div class="help-reviewed[^"]*">.*?</p></div>', new, s, count=1, flags=re.S)
    elif re.search(r'<p class="mt-3 text-sm text-gray-400">Last reviewed:[^<]*</p>', s):
        s = re.sub(r'<p class="mt-3 text-sm text-gray-400">Last reviewed:[^<]*</p>', new, s, count=1)
    else:
        # after the intro paragraph that follows the H1
        m = re.search(r'(<h1[^>]*>.*?</h1>\s*(?:<p[^>]*>.*?</p>)?)', s, re.S)
        s = s[:m.end()] + "\n" + new + s[m.end():]
    # JSON-LD: main article block
    def fix(mo):
        raw = mo.group(1)
        try: d = json.loads(raw)
        except Exception: return mo.group(0)
        if not isinstance(d, dict) or d.get("@type") not in ("TechArticle", "HowTo", "Article"): return mo.group(0)
        d["author"] = PERSON
        if "publisher" not in d: d["publisher"] = ORG
        dm = d.get("dateModified", "")
        if force_month:
            d["dateModified"] = today
        elif not dm.startswith(ym):
            d["dateModified"] = f"{ym}-01" if not dm or dm[:7] < ym else dm
        return '<script type="application/ld+json">\n' + json.dumps(d, indent=2, ensure_ascii=False) + '\n</script>'
    s = re.sub(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', fix, s, flags=re.S)
    if s != orig:
        open(path, "w", encoding="utf-8").write(s)
        return True
    return False

if __name__ == "__main__":
    args = sys.argv[1:]
    month = None
    if args[:1] == ["--month"]:
        month, args = args[1], args[2:]
    today = datetime.date.today().isoformat()
    paths = [f"{ROOT}/help/{a}.html" for a in args] if args else sorted(glob.glob(f"{ROOT}/help/*.html"))
    n = 0
    for p in paths:
        slug = os.path.basename(p)[:-5]
        if slug in SKIP: continue
        n += process(p, month, today)
    print(f"updated {n} guides")
