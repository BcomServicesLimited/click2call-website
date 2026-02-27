#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path('/home/ubuntu/click2call')
fixes = []

def read(p): return p.read_text(encoding='utf-8')
def write(p, c): p.write_text(c, encoding='utf-8')

# ── FIX 1: Remove visible [PLACEHOLDER] badge from about.html ──────────────
f = ROOT / 'about.html'
content = read(f)
old = '<p class="mt-2 text-xs text-yellow-700 font-semibold uppercase tracking-wide">[PLACEHOLDER \u2014 To be personalised with the founder\'s story]</p>'
if old in content:
    content = content.replace(old, '')
    write(f, content)
    fixes.append(('about.html', 'Removed visible [PLACEHOLDER] founder story yellow badge'))
else:
    # Try alternate em-dash encoding
    old2 = '[PLACEHOLDER \u2014 To be personalised with the founder'
    if old2 in content:
        # Find and remove the whole paragraph
        content = re.sub(r'<p[^>]*>\[PLACEHOLDER[^\]]*\]</p>', '', content)
        write(f, content)
        fixes.append(('about.html', 'Removed visible [PLACEHOLDER] founder story yellow badge (regex)'))
    else:
        print(f"WARNING: about.html placeholder not found with either pattern")
        # Show what's there
        for i, line in enumerate(content.splitlines(), 1):
            if 'PLACEHOLDER' in line:
                print(f"  Line {i}: {repr(line[:150])}")

# ── FIX 2: Remove visible [PLACEHOLDER] testimonial lines from index.html ──
f = ROOT / 'index.html'
content = read(f)
old_line = '          <p class="text-xs text-gray-400 mt-2 italic">[PLACEHOLDER \u2014 replace with real testimonial]</p>'
count = content.count(old_line)
if count > 0:
    content = content.replace(old_line, '')
    write(f, content)
    fixes.append(('index.html', f'Removed {count} visible [PLACEHOLDER] testimonial lines'))
else:
    # Try regex
    before = content.count('[PLACEHOLDER')
    content = re.sub(r'\s*<p[^>]*>\[PLACEHOLDER[^\]]*\]</p>', '', content)
    after = content.count('[PLACEHOLDER')
    removed = before - after
    if removed > 0:
        write(f, content)
        fixes.append(('index.html', f'Removed {removed} visible [PLACEHOLDER] lines (regex)'))
    else:
        print("WARNING: index.html testimonial placeholders not found")
        for i, line in enumerate(content.splitlines(), 1):
            if 'PLACEHOLDER' in line and '<!--' not in line:
                print(f"  Line {i}: {repr(line[:150])}")

# ── FIX 3: Add target="_blank" to portal login links missing it ─────────────
LOGIN_URL = 'portal.click2call.com.au/login.php'
for fname in ['about.html', 'contact.html', 'support.html']:
    f = ROOT / fname
    content = read(f)
    original = content

    def add_blank(m):
        tag = m.group(0)
        if 'target=' not in tag:
            # Insert target and rel after <a
            tag = tag.replace('<a ', '<a target="_blank" rel="noopener noreferrer" ', 1)
        return tag

    new_content = re.sub(r'<a [^>]*' + re.escape(LOGIN_URL) + r'[^>]*>', add_blank, content)
    if new_content != original:
        write(f, new_content)
        fixes.append((fname, 'Added target="_blank" rel="noopener noreferrer" to portal login link(s)'))

# ── FIX 4: Add Key Takeaways box to privacy.html ────────────────────────────
f = ROOT / 'privacy.html'
content = read(f)
if 'Key Takeaways' not in content:
    takeaways_html = '''
    <!-- Key Takeaways -->
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 mt-8">
      <div class="bg-green-50 border-l-4 border-brand-green-dark rounded-lg p-5">
        <h2 class="text-base font-bold text-brand-green-dark uppercase tracking-wide mb-3">Key Takeaways</h2>
        <ul class="space-y-2 text-sm text-gray-700">
          <li class="flex items-start gap-2"><svg class="w-4 h-4 text-brand-green-dark mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>Click2Call is operated by Bcom Services Pty Ltd (ABN: 92 636 893 108).</li>
          <li class="flex items-start gap-2"><svg class="w-4 h-4 text-brand-green-dark mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>We collect only the personal information necessary to provide our telecommunications services.</li>
          <li class="flex items-start gap-2"><svg class="w-4 h-4 text-brand-green-dark mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>We do not sell your personal data to third parties.</li>
          <li class="flex items-start gap-2"><svg class="w-4 h-4 text-brand-green-dark mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>You may request access to, correction of, or deletion of your personal information at any time.</li>
          <li class="flex items-start gap-2"><svg class="w-4 h-4 text-brand-green-dark mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>Contact us at <a href="mailto:click2call@bcomservices.com" class="text-brand-green-dark underline">click2call@bcomservices.com</a> for any privacy enquiries.</li>
        </ul>
      </div>
    </div>
'''
    # Insert after the first <h1> closing tag
    content = re.sub(r'(<h1[^>]*>.*?</h1>)', r'\1' + takeaways_html, content, count=1, flags=re.DOTALL)
    write(f, content)
    fixes.append(('privacy.html', 'Added Key Takeaways box'))

print(f"\nFixes applied: {len(fixes)}")
for fname, detail in fixes:
    print(f"  FIXED | {fname} | {detail}")
