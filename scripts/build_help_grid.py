"""build_help_grid.py — regenerate the server-rendered #help-article-grid
in help/index.html from the canonical article registry assets/js/articles.js.

WHY: /help/ builds its visible grid from articles.js at runtime
(gridEl.innerHTML = ...). That's fine for humans with JS, but non-JS
crawlers — including most LLM crawlers (GPTBot, ClaudeBot, PerplexityBot)
which do not reliably execute JS — only see the static HTML inside
#help-article-grid. If that static grid drifts from articles.js, those
crawlers miss articles. This script keeps the static grid a 1:1 mirror
of articles.js so every article is crawlable without JS.

RUN: python3 scripts/build_help_grid.py   (after editing articles.js)
Idempotent: same articles.js in → same HTML out.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_JS = ROOT / "assets/js/articles.js"
HELP_INDEX = ROOT / "help/index.html"

# Category order + the short badge label used on each static card.
# Matches the labels already present in the grid.
CATEGORY_ORDER = [
    ("getting-started", "Getting Started"),
    ("phone-numbers",   "Phone Numbers"),
    ("extensions",      "Extensions"),
    ("devices",         "Devices"),
    ("call-flows",      "Call Flows"),
    ("billing",         "Billing"),
    ("ai",              "Ai"),
]

GRID_START_RE = re.compile(
    r'(<div id="help-article-grid"[^>]*>)', re.DOTALL)


def parse_articles(js_text: str):
    """Extract the HELP_ARTICLES array as a list of dicts."""
    m = re.search(r'var HELP_ARTICLES\s*=\s*\[(.*?)\n\];', js_text, re.DOTALL)
    if not m:
        raise SystemExit("Could not locate HELP_ARTICLES array in articles.js")
    body = m.group(1)
    # Split into object blocks on the top-level "{ ... }" boundaries.
    objs = re.findall(r'\{(.*?)\}', body, re.DOTALL)
    articles = []
    for o in objs:
        def field(name):
            fm = re.search(name + r'\s*:\s*"((?:[^"\\]|\\.)*)"', o)
            return fm.group(1) if fm else ""
        art = {
            "url":      field("url"),
            "title":    field("title"),
            "desc":     field("desc"),
            "tags":     field("tags"),
            "category": field("category"),
            "readTime": field("readTime"),
        }
        if art["url"]:
            articles.append(art)
    return articles


def card_html(a: dict, badge_label: str) -> str:
    return (
        '<a class="help-article-card block bg-white rounded-xl border border-gray-200 p-5 '
        'hover:shadow-md hover:border-[#3B9C49] transition-all" '
        f'data-category="{a["category"]}" data-tags="{a["tags"]}" href="{a["url"]}">\n'
        '<div class="flex items-center gap-2 mb-2">\n'
        f'<span class="text-xs font-semibold text-[#3B9C49] uppercase tracking-wider">{badge_label}</span>\n'
        '<span class="text-xs text-gray-400">·</span>\n'
        f'<span class="text-xs text-gray-500">{a["readTime"]}</span>\n'
        '</div>\n'
        f'<h3 class="font-bold text-gray-900 mb-1">{a["title"]}</h3>\n'
        f'<p class="text-sm text-gray-600">{a["desc"]}</p>\n'
        '</a>'
    )


def build_grid(articles) -> str:
    by_cat = {}
    for a in articles:
        by_cat.setdefault(a["category"], []).append(a)
    cards = []
    for cat_key, badge in CATEGORY_ORDER:
        for a in by_cat.get(cat_key, []):
            cards.append(card_html(a, badge))
    return "\n".join(cards)


def main():
    articles = parse_articles(ARTICLES_JS.read_text())
    grid_inner = build_grid(articles)

    html = HELP_INDEX.read_text()
    m = GRID_START_RE.search(html)
    if not m:
        raise SystemExit("Could not find #help-article-grid opening tag")
    open_tag_end = m.end()

    # Find the matching close: the </div> immediately preceding the
    # "Still need help CTA" comment that follows the grid.
    anchor = html.index("<!-- Still need help CTA -->", open_tag_end)
    close_idx = html.rindex("</div>", open_tag_end, anchor)

    new_html = (
        html[:open_tag_end]
        + "\n" + grid_inner + "\n"
        + html[close_idx:]
    )
    HELP_INDEX.write_text(new_html)
    print(f"  Rebuilt #help-article-grid with {len(articles)} articles.")
    cats = {}
    for a in articles:
        cats[a["category"]] = cats.get(a["category"], 0) + 1
    for cat_key, _ in CATEGORY_ORDER:
        print(f"    {cat_key:16s} {cats.get(cat_key, 0)}")


if __name__ == "__main__":
    main()
