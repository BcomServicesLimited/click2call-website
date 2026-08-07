"""build_support_grid.py — server-render the /support/ task tiles and article
clusters from the canonical registry in assets/js/articles.js.

WHY: /support/ shipped both #support-task-tiles and #support-article-groups as
empty divs filled in at runtime by JS. Humans saw the full page; non-JS
crawlers saw two empty containers. Vercel/MERJ measurement across 500M+
GPTBot fetches found no major AI crawler executes JavaScript — GPTBot,
ClaudeBot and PerplexityBot read raw HTML and move on. So every article link
on /support/ (8 pinned tiles + 26 featured cards) was invisible to them, and
the internal linking those cards provide never counted.

This is the same fix already applied to /help/ by build_help_grid.py.

The generated markup is byte-for-byte what the JS would have produced, so the
page looks identical. The inline JS is guarded to skip rebuilding when a
container is already populated, so there is no double render.

RUN: python3 scripts/build_support_grid.py   (after editing articles.js)
Idempotent: same articles.js in -> same HTML out.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_JS = ROOT / "assets/js/articles.js"
SUPPORT_INDEX = ROOT / "support/index.html"

FALLBACK_TILE_ICON = (
    '<svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">'
    '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" '
    'd="M9 5l7 7-7 7"/></svg>'
)
CHEVRON = (
    '<svg class="flex-shrink-0 w-4 h-4 mt-0.5 text-gray-400 '
    'group-hover:text-[#3B9C49] transition-colors" fill="none" '
    'stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" '
    'stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>'
)


def parse_articles(js_text: str):
    """Extract HELP_ARTICLES, including the featured/pinned booleans."""
    m = re.search(r"var HELP_ARTICLES\s*=\s*\[(.*?)\n\];", js_text, re.DOTALL)
    if not m:
        raise SystemExit("Could not locate HELP_ARTICLES array in articles.js")
    articles = []
    for obj in re.findall(r"\{(.*?)\}", m.group(1), re.DOTALL):
        def text_field(name):
            fm = re.search(name + r'\s*:\s*"((?:[^"\\]|\\.)*)"', obj)
            return fm.group(1) if fm else ""

        def bool_field(name):
            return bool(re.search(name + r"\s*:\s*true", obj))

        art = {
            "url": text_field("url"),
            "title": text_field("title"),
            "tags": text_field("tags"),
            "category": text_field("category"),
            "readTime": text_field("readTime"),
            "featured": bool_field("featured"),
            "pinned": bool_field("pinned"),
        }
        if art["url"]:
            articles.append(art)
    return articles


def parse_tile_icons(html: str) -> dict:
    """Read the TILE_ICONS map out of the page's inline JS."""
    block = re.search(r"var TILE_ICONS\s*=\s*\{(.*?)\n  \};", html, re.DOTALL)
    if not block:
        raise SystemExit("Could not locate TILE_ICONS in support/index.html")
    return dict(re.findall(r"'([^']+)'\s*:\s*'(<svg.*?</svg>)'",
                           block.group(1), re.DOTALL))


def parse_cat_meta(html: str):
    """Read CAT_META out of the page's inline JS, preserving declaration order."""
    block = re.search(r"var CAT_META\s*=\s*\{(.*?)\n    \};", html, re.DOTALL)
    if not block:
        raise SystemExit("Could not locate CAT_META in support/index.html")
    entries = re.findall(
        r"'([a-z-]+)'\s*:\s*\{\s*label:\s*'([^']*)',\s*icon:\s*'(<svg.*?</svg>)'\s*\}",
        block.group(1), re.DOTALL)
    if not entries:
        raise SystemExit("CAT_META parsed but no categories matched")
    return entries


def build_tiles(articles, icons) -> str:
    out = []
    for a in [x for x in articles if x["pinned"]]:
        icon = icons.get(a["url"], FALLBACK_TILE_ICON)
        out.append(
            f'<a href="{a["url"]}" class="group flex flex-col items-center '
            'text-center bg-white border border-gray-200 rounded-xl p-5 '
            'hover:border-[#3B9C49] hover:shadow-md transition-all duration-200">'
            '<span class="flex-shrink-0 w-12 h-12 rounded-xl bg-green-50 flex '
            'items-center justify-center text-[#3B9C49] mb-3 '
            f'group-hover:bg-green-100 transition-colors">{icon}</span>'
            '<span class="text-sm font-semibold text-gray-900 '
            'group-hover:text-[#3B9C49] transition-colors leading-snug">'
            f'{a["title"]}</span></a>'
        )
    return "".join(out)


def build_groups(articles, cat_meta) -> str:
    grouped = {}
    for a in [x for x in articles if x["featured"]]:
        grouped.setdefault(a["category"], []).append(a)

    html = ['<div class="space-y-8">']
    for cat_key, label, icon in cat_meta:
        if not grouped.get(cat_key):
            continue
        html.append(f'<div class="support-cat-group" data-cat="{cat_key}">')
        html.append('<div class="flex items-center gap-2 mb-3">')
        html.append('<span class="flex-shrink-0 w-8 h-8 rounded-lg bg-green-50 '
                    f'flex items-center justify-center text-[#3B9C49]">{icon}</span>')
        html.append(f'<h3 class="text-base font-bold text-gray-900">{label}</h3>')
        html.append('</div>')
        html.append('<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">')
        for a in grouped[cat_key]:
            html.append(
                f'<a href="{a["url"]}" class="support-article-card group flex '
                'items-start gap-3 bg-white border border-gray-200 rounded-xl '
                'px-4 py-3 hover:border-[#3B9C49] hover:shadow-sm transition-all '
                f'duration-200" data-tags="{a["tags"]}" data-category="{cat_key}">'
                f'{CHEVRON}'
                '<div><p class="text-sm font-semibold text-gray-900 '
                'group-hover:text-[#3B9C49] transition-colors leading-snug">'
                f'{a["title"]}</p>'
                f'<p class="text-xs text-gray-500 mt-0.5">{a["readTime"]}</p>'
                '</div></a>'
            )
        html.append("</div></div>")
    html.append("</div>")
    return "".join(html)


def replace_container(html: str, container_id: str, inner: str) -> str:
    """Replace the contents of <div id="container_id"> ... </div>.

    Both containers hold only generated markup, so matching to the balanced
    close is a simple depth count from the opening tag.
    """
    m = re.search(r'<div id="%s"[^>]*>' % re.escape(container_id), html)
    if not m:
        raise SystemExit(f"Could not find #{container_id} in support/index.html")
    start = m.end()
    depth, i = 1, start
    while depth:
        nxt = re.search(r"<div\b|</div>", html[i:])
        if not nxt:
            raise SystemExit(f"Unbalanced divs after #{container_id}")
        i += nxt.end()
        depth += 1 if nxt.group(0) != "</div>" else -1
    close = i - len("</div>")
    return html[:start] + "\n" + inner + "\n" + html[close:]


def guard_js(html: str) -> str:
    """Make the inline JS skip containers the server already filled."""
    replacements = [
        ("if (tilesEl && typeof HELP_ARTICLES !== 'undefined') {",
         "if (tilesEl && !tilesEl.children.length && typeof HELP_ARTICLES !== 'undefined') {"),
        ("if (groupsEl && typeof HELP_ARTICLES !== 'undefined') {",
         "if (groupsEl && !groupsEl.children.length && typeof HELP_ARTICLES !== 'undefined') {"),
    ]
    for old, new in replacements:
        if new not in html:
            if old not in html:
                raise SystemExit(f"Could not find JS guard target: {old}")
            html = html.replace(old, new, 1)
    return html


def main():
    articles = parse_articles(ARTICLES_JS.read_text())
    html = SUPPORT_INDEX.read_text()

    icons = parse_tile_icons(html)
    cat_meta = parse_cat_meta(html)

    html = replace_container(html, "support-task-tiles",
                             build_tiles(articles, icons))
    html = replace_container(html, "support-article-groups",
                             build_groups(articles, cat_meta))
    html = guard_js(html)
    SUPPORT_INDEX.write_text(html)

    pinned = sum(1 for a in articles if a["pinned"])
    featured = sum(1 for a in articles if a["featured"])
    print(f"  Server-rendered {pinned} task tiles and {featured} article cards "
          f"across {len(cat_meta)} categories.")


if __name__ == "__main__":
    main()
