#!/usr/bin/env python3
"""
Click2Call — Full Site QA Audit Script
Checks every HTML file plus root files against the QA checklist.
Auto-fixes issues where possible and records all findings.
"""
import os, re, glob
from pathlib import Path

ROOT = Path('/home/ubuntu/click2call')
HTML_FILES = sorted([p for p in ROOT.glob('*.html') if not p.name.startswith('_')])
BLOG_HTML  = sorted(ROOT.glob('blog/*.html'))
ALL_HTML   = HTML_FILES + BLOG_HTML

issues   = []   # (file, check, detail)
fixes    = []   # (file, check, detail)
manual   = []   # items needing human action

def issue(f, check, detail=''):
    issues.append((str(f).replace(str(ROOT)+'/', ''), check, detail))

def fix(f, check, detail=''):
    fixes.append((str(f).replace(str(ROOT)+'/', ''), check, detail))

def read(p):
    return p.read_text(encoding='utf-8')

def write(p, content):
    p.write_text(content, encoding='utf-8')

# ─── CRITICAL: Placeholder checks ──────────────────────────────────────────
print("=== CRITICAL CHECKS ===")

for f in ALL_HTML + [ROOT/'llms.txt', ROOT/'llms-full.md']:
    content = f.read_text(encoding='utf-8')
    # Visible [PLACEHOLDER PRICE]
    visible_price = [l.strip() for l in content.splitlines()
                     if '[PLACEHOLDER PRICE]' in l and '<!--' not in l]
    for line in visible_price:
        issue(f, '[PLACEHOLDER PRICE] visible', line[:100])

    # Visible [PLACEHOLDER] (not in HTML comments)
    visible_ph = [l.strip() for l in content.splitlines()
                  if '[PLACEHOLDER' in l and '<!--' not in l]
    for line in visible_ph:
        issue(f, '[PLACEHOLDER] visible to users', line[:100])

    # Visible [NEEDS BACKEND]
    visible_nb = [l.strip() for l in content.splitlines()
                  if '[NEEDS BACKEND]' in l and '<!--' not in l]
    for line in visible_nb:
        issue(f, '[NEEDS BACKEND] visible to users', line[:100])

# brand.css exists
brand_css = ROOT / 'assets/css/brand.css'
if not brand_css.exists():
    issue(ROOT, 'brand.css missing', '')
else:
    css = brand_css.read_text()
    for cls in ['brand-charcoal', 'brand-green-dark', 'brand-green-light',
                'brand-gray-50', 'brand-gray-100']:
        if cls not in css:
            issue(brand_css, f'brand.css missing class .{cls}', '')

# ─── PRICING CHECKS ─────────────────────────────────────────────────────────
print("=== PRICING CHECKS ===")
pricing = (ROOT / 'pricing.html').read_text()
for check, pattern in [
    ('$29 Cloud PBX DIY Core', r'\$29'),
    ('$39 Cloud PBX Business', r'\$39'),
    ('$49 Cloud PBX Managed', r'\$49'),
    ('$7.00 SIP Trunk', r'\$7\.00'),
    ('$0.12/min call rates', r'\$0\.12'),
    ('$8.00 DDI', r'\$8\.00'),
    ('$18.00 Toll Free', r'\$18\.00'),
]:
    if not re.search(pattern, pricing):
        issue(ROOT/'pricing.html', f'pricing.html missing {check}', '')

for fname, label in [('llms.txt', 'llms.txt'), ('llms-full.md', 'llms-full.md')]:
    content = (ROOT/fname).read_text()
    for price in ['$29', '$39', '$49', '$7.00', '$8.00', '$18.00', '$0.12']:
        if price not in content:
            issue(ROOT/fname, f'{label} missing price {price}', '')

# ─── LINKS ──────────────────────────────────────────────────────────────────
print("=== LINK CHECKS ===")
LOGIN_URL  = 'portal.click2call.com.au/login.php'
JOIN_URL   = 'portal.click2call.com.au/join/'

for f in ALL_HTML:
    content = read(f)
    if LOGIN_URL not in content:
        issue(f, 'Header missing Login portal link', '')
    if JOIN_URL not in content:
        issue(f, 'Header missing Get Started portal link', '')
    # Check _blank on portal links
    for url in [LOGIN_URL, JOIN_URL]:
        # Find the anchor tag containing this URL
        anchors = re.findall(r'<a[^>]*' + re.escape(url) + r'[^>]*>', content)
        for a in anchors:
            if 'target="_blank"' not in a and "target='_blank'" not in a:
                issue(f, f'Portal link missing target="_blank"', url)

# Internal links with .html — check for obviously broken ones
KNOWN_PAGES = {
    'index.html', 'cloud-pbx.html', 'ai-voice-tools.html', 'ai-receptionist.html',
    'microsoft-teams-calling.html', 'sip-trunks.html', 'pricing.html', 'compare.html',
    'about.html', 'support.html', 'contact.html', 'faq.html', 'voip-australia.html',
    'privacy.html', 'case-studies.html', 'blog/index.html',
}
for f in ALL_HTML:
    content = read(f)
    hrefs = re.findall(r'href=["\']([^"\'#?]+\.html)["\']', content)
    for href in hrefs:
        # Normalise
        href_clean = href.lstrip('./')
        if href_clean.startswith('/'):
            href_clean = href_clean.lstrip('/')
        # Skip blog articles and case study sub-pages (expected not to exist)
        if href_clean.startswith('blog/') and href_clean != 'blog/index.html':
            continue
        if href_clean.startswith('case-studies/'):
            continue
        if href_clean not in KNOWN_PAGES and href_clean != '':
            issue(f, f'Possible broken internal link: {href}', '')

# ─── METADATA ───────────────────────────────────────────────────────────────
print("=== METADATA CHECKS ===")
titles = {}
for f in ALL_HTML:
    content = read(f)
    fname = str(f).replace(str(ROOT)+'/', '')

    # Title
    m = re.search(r'<title>(.+?)</title>', content)
    if not m:
        issue(f, 'Missing <title>', '')
    else:
        t = m.group(1)
        if t in titles.values():
            issue(f, f'Duplicate <title>: {t}', '')
        titles[fname] = t

    # Meta description
    if not re.search(r'<meta\s+name=["\']description["\']', content):
        issue(f, 'Missing <meta name="description">', '')

    # Canonical
    if not re.search(r'<link\s+rel=["\']canonical["\']', content):
        issue(f, 'Missing canonical link', '')

    # og:url — check for double dots or wrong domain
    og_url = re.search(r'og:url["\'][^>]*content=["\']([^"\']+)["\']', content)
    if not og_url:
        og_url = re.search(r'content=["\']([^"\']+)["\'][^>]*og:url', content)
    if og_url:
        url_val = og_url.group(1)
        if '..' in url_val or 'click2call.com.au' not in url_val:
            issue(f, f'og:url looks wrong: {url_val}', '')
    else:
        issue(f, 'Missing og:url', '')

    # og:title
    if not re.search(r'og:title', content):
        issue(f, 'Missing og:title', '')

    # og:description
    if not re.search(r'og:description', content):
        issue(f, 'Missing og:description', '')

    # GA4
    if 'G-ST0JCEZ54X' not in content:
        issue(f, 'Missing Google Analytics G-ST0JCEZ54X', '')

# ─── CONTENT ────────────────────────────────────────────────────────────────
print("=== CONTENT CHECKS ===")
SERVICE_PAGES = [
    ROOT/'cloud-pbx.html', ROOT/'ai-voice-tools.html', ROOT/'ai-receptionist.html',
    ROOT/'microsoft-teams-calling.html', ROOT/'sip-trunks.html',
]
for f in SERVICE_PAGES:
    content = read(f)
    faq_count = len(re.findall(r'faq-answer-\d+', content))
    if faq_count < 10:
        issue(f, f'Service page has only {faq_count} FAQ answers (need ≥10)', '')

for f in ALL_HTML:
    content = read(f)
    if 'Key Takeaways' not in content:
        issue(f, 'Missing Key Takeaways box', '')
    if 'application/ld+json' not in content:
        issue(f, 'Missing JSON-LD structured data', '')
    if '2026' not in content:
        issue(f, 'Missing © 2026 copyright', '')
    if '92 636 893 108' not in content:
        issue(f, 'Missing ABN 92 636 893 108', '')
    if 'tel:1300884879' not in content:
        issue(f, 'Missing clickable phone tel:1300884879', '')
    if 'click2call@bcomservices.com' not in content:
        issue(f, 'Missing email click2call@bcomservices.com', '')

# ─── LLM / ROOT FILES ───────────────────────────────────────────────────────
print("=== LLM / ROOT FILE CHECKS ===")
robots = (ROOT/'robots.txt').read_text()
for bot in ['GPTBot', 'ClaudeBot', 'PerplexityBot', 'Google-Extended', 'anthropic-ai']:
    if bot not in robots:
        issue(ROOT/'robots.txt', f'robots.txt missing {bot}', '')

sitemap = (ROOT/'sitemap.xml').read_text()
sitemap_urls = re.findall(r'<loc>(.+?)</loc>', sitemap)
if len(sitemap_urls) < 16:
    issue(ROOT/'sitemap.xml', f'sitemap.xml has only {len(sitemap_urls)} URLs (need 16)', '')
for url in sitemap_urls:
    if 'click2call.com.au' not in url:
        issue(ROOT/'sitemap.xml', f'sitemap URL missing domain: {url}', '')

llms_txt = (ROOT/'llms.txt').read_text()
for check in ['Cloud PBX', 'SIP Trunk', 'AI Receptionist', 'Microsoft Teams',
              '1300 884 879', 'click2call@bcomservices.com',
              'portal.click2call.com.au/login.php', 'portal.click2call.com.au/join/']:
    if check not in llms_txt:
        issue(ROOT/'llms.txt', f'llms.txt missing: {check}', '')

llms_full = (ROOT/'llms-full.md').read_text()
for check in ['Cloud PBX', 'SIP Trunk', 'AI Receptionist', 'Microsoft Teams',
              '1300 884 879', 'click2call@bcomservices.com', 'ABN']:
    if check not in llms_full:
        issue(ROOT/'llms-full.md', f'llms-full.md missing: {check}', '')

# ─── REPORT ─────────────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print(f"ISSUES FOUND: {len(issues)}")
for f, check, detail in issues:
    print(f"  ISSUE | {f} | {check}" + (f" | {detail}" if detail else ''))

print(f"\nFIXES APPLIED: {len(fixes)}")
for f, check, detail in fixes:
    print(f"  FIXED | {f} | {check}" + (f" | {detail}" if detail else ''))
