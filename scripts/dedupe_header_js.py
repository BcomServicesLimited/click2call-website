"""Phase 6.5 — Remove duplicate header-JavaScript blocks.

Many pages contain TWO back-to-back copies of the header dropdown
JavaScript: the `Services dropdown` / mobile-menu / mobile-services
accordion handler. The blocks are wrapped in this comment header:

    <!--
      ── Header JavaScript ──
      ...
    -->
    <script>
    (function () {
      'use strict';
      /* ── Services dropdown (desktop) ── */
      ...
    }());
    </script>

When the same block appears twice in a row (separated only by
whitespace), keep the first and delete the second.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Pattern: an OPTIONAL "Header JavaScript" comment header, then the
# <script>(function(){ 'use strict'; /* ── Services dropdown (desktop) ── */
# ... }());</script> block. Comment is optional because some pages keep
# the second block raw (without the comment wrapper).
BLOCK_RE = re.compile(
    r"(?:<!--\s*\n\s*──\s*Header JavaScript\s*──.*?-->\s*)?"
    r"<script>\s*\(function\s*\(\)\s*\{\s*'use strict';\s*"
    r"/\*\s*──\s*Services dropdown \(desktop\)\s*──\s*\*/"
    r".*?\}\(\)\);?\s*</script>",
    re.DOTALL,
)


def dedupe(text: str) -> tuple[str, int]:
    """Return (new_text, removed_count)."""
    matches = list(BLOCK_RE.finditer(text))
    if len(matches) < 2:
        return text, 0
    # Keep first, delete the rest. Walk from end so offsets stay valid.
    removed = 0
    new_text = text
    for m in reversed(matches[1:]):
        # Absorb trailing whitespace up to the next non-whitespace
        end = m.end()
        while end < len(new_text) and new_text[end] in " \t":
            end += 1
        if end < len(new_text) and new_text[end] == "\n":
            end += 1
        new_text = new_text[: m.start()] + new_text[end:]
        removed += 1
    return new_text, removed


def main():
    htmls = [p for p in ROOT.rglob("*.html") if "node_modules" not in p.parts]
    touched = 0
    total_blocks_removed = 0
    for p in htmls:
        text = p.read_text()
        new_text, removed = dedupe(text)
        if removed:
            p.write_text(new_text)
            rel = p.relative_to(ROOT)
            print(f"  {rel}: removed {removed} duplicate block(s)")
            touched += 1
            total_blocks_removed += removed
    print(f"\n  Touched {touched} files, removed {total_blocks_removed} duplicate block(s) total.")


if __name__ == "__main__":
    main()
