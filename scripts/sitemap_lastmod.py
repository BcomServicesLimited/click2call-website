#!/usr/bin/env python3
"""sitemap_lastmod.py — set every <lastmod> in sitemap.xml from the page's real last change.

For each <loc>, find the HTML file it serves. Its date is:
  - today, if the file has uncommitted changes (it is about to be committed), else
  - the date of the last git commit that touched the file.

Shared header/footer lines and the asset-stamp line (?v=...) changing does not count as a content change: commits
whose diff for the file is only ?v= stamps are skipped, so a site-wide CSS rebuild doesn't
make every page look freshly edited.

Run by `npm run prepush`. `--check` prints the dates that would change and exits 1 if any.
"""
import datetime, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP = os.path.join(ROOT, 'sitemap.xml')
HOST = 'https://www.click2call.com.au'
STAMP = re.compile(r'\?v=[0-9a-f]+')
# Lines of the shared header/footer partials: a site-wide menu or footer edit isn't a page content change.
PARTIAL = set()
for _p in ('_header.html', '_footer.html'):
    try:
        PARTIAL |= {STAMP.sub('', l).strip() for l in open(os.path.join(ROOT, _p), encoding='utf-8') if l.strip()}
    except OSError:
        pass


def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True).stdout


def file_for(loc):
    path = loc[len(HOST):].lstrip('/')
    for cand in (path, path + 'index.html', path + '/index.html', path + '.html'):
        full = os.path.join(ROOT, cand)
        if cand and os.path.isfile(full):
            return cand
    return None


def content_date(rel):
    today = datetime.date.today().isoformat()
    diff = git('diff', 'HEAD', '-U0', '--', rel)
    if real_change(diff):
        return today
    for line in git('log', '--format=%H %cs', '--', rel).splitlines():
        sha, day = line.split()
        if real_change(git('show', '-U0', '--format=', sha, '--', rel)):
            return day
    return None


def real_change(diff):
    minus, plus = [], []
    for line in diff.splitlines():
        if line.startswith(('---', '+++')):
            continue
        if line.startswith(('-', '+')):
            text = STAMP.sub('', line[1:])
            if text.strip() in PARTIAL:
                continue
            (minus if line[0] == '-' else plus).append(text)
    if not minus and not plus:
        return False
    return minus != plus


def main():
    check = '--check' in sys.argv
    xml = open(SITEMAP, encoding='utf-8').read()
    changed = []

    def fix(m):
        block = m.group(0)
        loc = re.search(r'<loc>([^<]+)</loc>', block).group(1)
        rel = file_for(loc)
        if not rel:
            return block
        day = content_date(rel)
        if not day:
            return block
        old = re.search(r'<lastmod>([^<]*)</lastmod>', block)
        if old and old.group(1) == day:
            return block
        changed.append((loc, old.group(1) if old else None, day))
        if old:
            return block.replace(old.group(0), f'<lastmod>{day}</lastmod>')
        return block.replace('</loc>', f'</loc>\n    <lastmod>{day}</lastmod>', 1)

    xml = re.sub(r'<url>.*?</url>', fix, xml, flags=re.S)
    for loc, old, new in changed:
        print(f'{old} -> {new}  {loc}')
    if check:
        sys.exit(1 if changed else 0)
    if changed:
        open(SITEMAP, 'w', encoding='utf-8').write(xml)
    print(f'{len(changed)} lastmod date(s) updated')


if __name__ == '__main__':
    main()
