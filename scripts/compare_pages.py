"""compare_pages.py — "nothing lost by accident" check for a page redesign.

Compares an old and a new version of a page and reports every difference in what search
engines and AI assistants read: title, meta description, canonical, robots, structured data,
headings, sentences of visible text, internal links, tracked buttons and element IDs.

A JSON change log lists the differences that were made on purpose. The check fails (exit 1)
if any difference is not on the log.

    python3 scripts/compare_pages.py OLD.html NEW.html [--log changes.json] [--write-log out.json]

--write-log writes the current differences as a starter change log to review and approve.
Standard library only.
"""
import argparse, html, json, re, sys


def text_of(fragment):
    fragment = re.sub(r'<(script|style|svg|noscript)[^>]*>.*?</\1>', ' ', fragment, flags=re.S)
    fragment = re.sub(r'<[^>]+>', ' ', fragment)
    return ' '.join(html.unescape(fragment).split())


def parse(path):
    s = open(path, encoding='utf-8').read()
    head = s[:s.index('</head>')]
    body = s[s.index('</head>'):]
    main = body[body.index('<main'):body.index('</main>')] if '<main' in body else body
    meta = lambda name: (re.search(r'<meta[^>]+name="%s"[^>]+content="([^"]*)"' % name, head) or re.search(r'<meta[^>]+content="([^"]*)"[^>]+name="%s"' % name, head))
    out = {
        'title': text_of((re.search(r'<title>(.*?)</title>', head, re.S) or [None, ''])[1]),
        'description': (meta('description') or [None, ''])[1],
        'robots': (meta('robots') or [None, ''])[1],
        'canonical': (re.search(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', head) or [None, ''])[1],
        'jsonld': [],
        'headings': [],
        'sentences': [],
        'links': sorted(set(re.findall(r'href="(/[^"#?]*)', main))),
        'events': sorted(set(re.findall(r"gtag\('event', '([a-z_]+)', \{[^}]*'event_label': '([^']+)'", main))),
        'ids': sorted(set(re.findall(r'\bid="(speakable-[^"]+|faq-accordion)"', main))),
        'img_alts': sorted(set(a for a in re.findall(r'<img[^>]+alt="([^"]*)"', main) if a)),
    }
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        out['jsonld'].append(json.loads(block))
    for lvl, h in re.findall(r'<h([1-4])[^>]*>(.*?)</h\1>', main, re.S):
        out['headings'].append(f'h{lvl}: ' + text_of(h))
    # Text units: break at block elements, then at sentence ends, so moving a block
    # elsewhere on the page is not reported as a change.
    blocky = re.sub(r'<(script|style|svg|noscript)[^>]*>.*?</\1>', ' ', main, flags=re.S)
    blocky = re.sub(r'</?(h[1-6]|p|li|div|section|article|ul|ol|table|tr|td|th|button|figure|figcaption|header|footer|br)\b[^>]*>', '\n', blocky)
    units = set()
    for line in re.sub(r'<[^>]+>', ' ', blocky).split('\n'):
        line = ' '.join(html.unescape(line).split())
        for x in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"“(])', line):
            x = x.strip()
            if len(x) > 2:
                units.add(x)
    out['sentences'] = sorted(units)
    return out


def norm_jsonld(blocks):
    def strip(o):
        if isinstance(o, dict):
            return {k: strip(v) for k, v in o.items() if k != 'dateModified'}
        if isinstance(o, list):
            return [strip(v) for v in o]
        return o
    return sorted(json.dumps(strip(b), sort_keys=True) for b in blocks)


def diff(old, new):
    d = []
    for k in ('title', 'description', 'robots', 'canonical'):
        if old[k] != new[k]:
            d.append({'kind': k, 'old': old[k], 'new': new[k]})
    if norm_jsonld(old['jsonld']) != norm_jsonld(new['jsonld']):
        d.append({'kind': 'jsonld', 'old': 'structured data differs (ignoring dateModified)', 'new': ''})
    for k in ('headings', 'sentences', 'links', 'events', 'ids', 'img_alts'):
        o, n = old[k], new[k]
        if k == 'events':
            o = [f'{a}|{b}' for a, b in o]; n = [f'{a}|{b}' for a, b in n]
        if k == 'headings':
            for h in o:
                if h not in n:
                    alt = [x for x in n if x.split(': ', 1)[1] == h.split(': ', 1)[1]]
                    d.append({'kind': 'heading-level' if alt else 'heading-removed', 'old': h, 'new': alt[0] if alt else ''})
            for h in n:
                if h not in o and not any(x.split(': ', 1)[1] == h.split(': ', 1)[1] for x in o):
                    d.append({'kind': 'heading-added', 'old': '', 'new': h})
            continue
        for x in o:
            if x not in n:
                d.append({'kind': k + '-removed', 'old': x, 'new': ''})
        for x in n:
            if x not in o:
                d.append({'kind': k + '-added', 'old': '', 'new': x})
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('old'); ap.add_argument('new')
    ap.add_argument('--log', help='approved change log (JSON list of {kind, old, new, reason})')
    ap.add_argument('--write-log', help='write current differences as a starter change log')
    a = ap.parse_args()
    old, new = parse(a.old), parse(a.new)
    d = diff(old, new)
    approved = json.load(open(a.log)) if a.log else []
    key = lambda x: (x['kind'], x['old'], x['new'])
    ok = {key(x) for x in approved}
    unexpected = [x for x in d if key(x) not in ok]
    print(f"old: {len(old['sentences'])} sentences, {len(old['headings'])} headings, {len(old['links'])} internal links, {len(old['events'])} tracked buttons, {len(old['jsonld'])} structured data blocks")
    print(f"new: {len(new['sentences'])} sentences, {len(new['headings'])} headings, {len(new['links'])} internal links, {len(new['events'])} tracked buttons, {len(new['jsonld'])} structured data blocks")
    print(f"differences: {len(d)}  approved: {len(d) - len(unexpected)}  NOT approved: {len(unexpected)}")
    for x in unexpected:
        print(f"  [{x['kind']}]\n     old: {x['old'][:160]}\n     new: {x['new'][:160]}")
    if a.write_log:
        json.dump([dict(x, reason='') for x in d], open(a.write_log, 'w'), indent=1, ensure_ascii=False)
        print('starter log written to', a.write_log)
    sys.exit(1 if unexpected else 0)


if __name__ == '__main__':
    main()
