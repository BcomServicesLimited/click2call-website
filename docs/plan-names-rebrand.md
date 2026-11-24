# Plan names rebrand (approved 24 Nov 2026)

Royce approved new customer-facing plan names on 24 Nov 2026. Prices, fees and the trial did not change.

| Old name (still shown in the portal) | New name | Price (ex GST) | One line |
|---|---|---|---|
| Inbound Business Number | **Business Number** | $10 a month | Receive calls on a business number |
| Cloud PBX User | **Business Line** | $25 a line a month, 300 minutes | Make and receive calls; a line for each person |
| Microsoft Teams User (Teams User plan) | **Teams Line** | $25 a line a month, 300 minutes | A Business Line inside Microsoft Teams |

The sentence to reuse: **a number receives; a line makes and receives.** "Business phone system" is the umbrella: a team's phone system is built from Business Lines.

Set-up terms (Royce settled 24 Nov 2026), shown wherever set-up is described:

1. **Set it up yourself**: free. Online, about 30 minutes, with guides and email support.
2. **Done for you, 1 to 3 lines**: $300 ex GST, configured remotely.
3. **Done for you, 4 or more Business Lines or Teams Lines**: free **on approval** (Click2Call reviews each request), once the first month is paid for those lines (not on trial credit alone).

"Done for you" replaces "Managed setup" as the customer-facing name ("done-for-you (managed) set-up" kept in a few places for search). Scope unchanged: remote, technical configuration only, no training, 1–2 business days. Royce, 24 Nov 2026: Teams set-up follows the same rule ($300 flat for 1 to 3 lines, free on approval for 4+); the separate $50 a user Teams fee and the $50 a user "additional user set-up" fee are gone. No clawback wording.

Code notes: the calculator treats lines = Business Lines + a main number on the 300-minute plan; at 4+ lines done-for-you set-up shows "$0, free on approval" on screen, in the smart recommendation and in the PDF. Under 4 lines it is a flat $300, however many people are on extensions (also in the PDF, which before skipped set-up when there were no lines). The Formspree "Setup Type" value is still "Managed Setup" (read by the PSA).

## What changed

- **Menu and footer** (`_header.html`, `_footer.html`, synced to every page; `index.html` by hand): "Cloud PBX" item is now "Business Phone System". URL `/cloud-pbx/` unchanged.
- **Pricing**: H1, summary and Key Takeaways name the three plans. Three plan cards side by side (Business Number, Business Line marked "For teams", Teams Line), each with a "Shown as … in the portal" note. "Pricing a team?" strip under the cards. Scenario cards are now Just a number ($10), Team of 3 ($85), Team of 5 ($135); builder chips Team of 3 / Team of 5 (presets `team3`, `team5`; `office` and `team` presets kept in code). Calculator, receipt and PDF quote labels renamed; done-for-you set-up shown as free on approval on screen and in the PDF when lines >= 4. `calcState` shape unchanged. The Formspree field **"Cloud PBX Users" is deliberately kept**: the PSA quote parser (`click2call-psa-v2/workers/lib/inbox/quote.js`) reads that label. Teams Line offer added to structured data. Title unchanged.
- **Homepage**: hero and numbers message unchanged. The "Which best describes your business?" section is now two marked doors, "Just a number" ($10) and "A phone system for your team" ($25 a line), moved above Key Takeaways. Services card, Key Takeaways, step 2 and meta description use the new names. `home-v2.css` changed, so `?v=` was re-stamped.
- **/cloud-pbx/**: title, H1 and "cloud PBX" search wording kept; the plan is a Business Line in the body, badges, price cards and FAQ.
- **/microsoft-teams-calling/**: Teams Line throughout; a new hero line leads with what is included (recorded, transcribed and summarised inside Teams with no extra Microsoft recording licence, stored in Australia, no contract) before the price.
- **Medical, care and professional pages** (`voip-medical-clinics-australia`, medical clinic, disability support and accounting firm examples, `voip-real-estate-agents-australia`): Business Line for each person is the lead offer; worked examples with 4+ lines now show done-for-you set-up as free on approval instead of $350–$950.
- **Everywhere else**: about 50 pages renamed (industry and city pages, case studies, compare pages, call centre, AI receptionist, AI voice tools, blog posts, help guides, FAQ, terms). Help guides that tell customers what to pick say the new name plus "shown as … in the portal". The "How to add a phone number" guide had a plan table left over from an older price list (two rows both called the $10 plan, and an Auto Attendant warning that contradicted the pricing page); it now matches the pricing page.
- **llms.txt / llms-full.md**: plan-names paragraph (new names, old names are the same plans, portal still shows the old names, done-for-you set-up terms). `llms-help.md` regenerated with `scripts/build_llms_help.py`.
- Help search tags (`assets/js/articles.js`, `help/index.html`) gained "business line business number teams line" alongside the old words.

## Deliberately not changed

- "Cloud PBX" as a technology/search term (1,000+ mentions), page titles, URLs.
- The three December test pages: `/voip-australia/`, `/voip-melbourne/`, `blog/voip-for-small-business.html` (read ~17 Dec; they still say "Cloud PBX User"/"Inbound Business Number"; rename after the reading).
- Portal UI names in screenshots and field names ("Associated Teams User", the "Microsoft Teams Users" screen, "Line Plan" dropdown alt text).
- Internal, untracked files `help/primary-knowledge-base.html` and `knowledge/`.
- Customer portal, sign-up form, PSA templates and desk knowledge articles (other systems).

Per-page change logs: `docs/pricing-plan-names-change-log.json`, `docs/homepage-plan-names-change-log.json`, `docs/cloud-pbx-plan-names-change-log.json`, `docs/teams-plan-names-change-log.json` (checked with `scripts/compare_pages.py`).

## Portal renamed (24 Nov 2026, later)

Royce renamed the plans in the customer portal: **Business Line**, **Business Number** and **Teams Line** are now the published plan names there (Cloud PBX User and Microsoft Teams User are gone; Inbound Business Number is kept but unpublished, so numbers added before the change may still show it). The "shown as … in the portal" notes were removed from pricing, Cloud PBX, Teams, three help guides and the llms files; the Business Number notes now say older accounts may show Inbound Business Number. Portal screenshots (and their alt text) still show the old names until they are retaken. The December test pages are still untouched.
