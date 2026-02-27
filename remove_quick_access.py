import re
from pathlib import Path

# The exact block to remove — from the comment down to the closing </div>
# It starts with "  <!-- Quick Access bar -->" and ends with "  </div>\n  <div class=\"border-t border-gray-800\">"
# We'll match from the comment to just before the copyright bar

PATTERN = re.compile(
    r'\s*<!-- Quick Access bar -->\s*'
    r'<div class="border-t border-gray-700">.*?</div>\s*</div>\s*</div>',
    re.DOTALL
)

html_files = list(Path('/home/ubuntu/click2call').glob('*.html'))
# Also check blog subfolder
html_files += list(Path('/home/ubuntu/click2call/blog').glob('*.html'))

fixed = []
skipped = []

for f in sorted(html_files):
    content = f.read_text(encoding='utf-8')
    if '<!-- Quick Access bar -->' not in content:
        skipped.append(f.name)
        continue
    new_content = PATTERN.sub('', content)
    if new_content != content:
        f.write_text(new_content, encoding='utf-8')
        fixed.append(f.name)
    else:
        print(f"WARNING: Pattern did not match in {f.name} — manual check needed")
        skipped.append(f.name)

print(f"\nFixed ({len(fixed)}):", ', '.join(fixed))
print(f"Skipped ({len(skipped)}):", ', '.join(skipped))
