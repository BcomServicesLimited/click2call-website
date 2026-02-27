#!/usr/bin/env python3
"""Add target=_blank to ALL portal login links across all HTML files."""
import re
from pathlib import Path

ROOT = Path('/home/ubuntu/click2call')
LOGIN_URL = 'portal.click2call.com.au/login.php'
fixes = []

all_html = list(ROOT.glob('*.html')) + list(ROOT.glob('blog/*.html')) + \
           [ROOT/'_header.html', ROOT/'_footer.html']

for f in all_html:
    if not f.exists():
        continue
    content = f.read_text(encoding='utf-8')
    original = content

    def add_blank(m):
        tag = m.group(0)
        if 'target=' not in tag:
            tag = tag.replace('<a ', '<a target="_blank" rel="noopener noreferrer" ', 1)
        return tag

    new_content = re.sub(r'<a [^>]*' + re.escape(LOGIN_URL) + r'[^>]*>', add_blank, content)
    if new_content != original:
        f.write_text(new_content, encoding='utf-8')
        fixes.append(f.name)

print(f"Fixed target=_blank in {len(fixes)} files:")
for name in fixes:
    print(f"  {name}")
