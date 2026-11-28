# AI-answer gaps: Teams calling and an office of five (28 Nov 2026)

Why: on 28 Nov 2026 ChatGPT (anonymous, eight questions) left Click2Call out of two answers: "how do I add phone calling to Microsoft Teams for a small business in Australia" and "best business phone system for a small office of 5 people in Australia". Assistants quote providers' own pages, so each page now answers its question in the first screen, in plain, quotable sentences. Pillars: **Cited** (answer-first text an assistant can lift) and **Mentioned** (Click2Call appears in the answer), with **Trusted** for the dated Microsoft sources.

## Facts checked on 28 Nov 2026

- Microsoft Learn, [Availability in Australia](https://learn.microsoft.com/en-us/microsoftteams/phone-reference/plan-availability/availability-in-australia) (updated 26 Aug 2026): "Calling Plans are available to purchase? No".
- Microsoft Learn, [PSTN connectivity options](https://learn.microsoft.com/en-us/microsoftteams/pstn-connectivity): Calling Plan, Operator Connect, Teams Phone Mobile, Direct Routing.
- Microsoft Learn, add-on licensing: Direct Routing and Operator Connect need a Teams Phone licence; qualifying business base plans are Microsoft 365 Business Basic, Standard or Premium (or Teams Essentials).
- microsoft.com/en-au: Teams Phone Standard **AU$15.00** a user a month; Microsoft 365 Business Basic **AU$10.50**; both "paid yearly", ex GST.
- Microsoft Learn, compliance recording: needs a certified third-party recording product plus a qualifying licence.
- Click2Call pricing page (live): Business Line $25, Business Number $10, 300 minutes (AU and NZ landlines and mobiles), then 10c/min landlines and 20c/min mobiles ex GST; set-up $300 ex GST flat; porting $100 inc GST.

## The office-of-five figure (identical everywhere)

5 Business Lines + 1 main Business Number = **$135 a month ex GST ($148.50 inc GST)**. One-off: done-for-you set-up $300 ex GST (optional; self set-up free), $100 inc GST per number moved across. On Teams: 5 Teams Lines $125 + 5 Teams Phone Standard $75 = $200 ex GST ($252.50 with Business Basic).

## Subject first (Royce's reminder, 28 Nov)

Each answer explains the subject for any Australian business before Click2Call's offer: the Teams section defines Calling Plans, Operator Connect and Direct Routing (and a session border controller) in plain words, then the Microsoft licences any route needs (cited to Microsoft's licensing page), then the Teams Line. The office-of-five lines first say what such a phone system consists of (a line each, a main number that rings everyone, call handling), then the Click2Call price. Sentences name their subject so they read correctly when quoted alone.

## What changed

- **/microsoft-teams-calling/**: hero summary answers the question (Operator Connect or Direct Routing; Microsoft does not sell Calling Plans in Australia; Teams Line facts; licence price). "In short" box replaced by six short question sections (three ways, Teams Line, Microsoft licence, office-of-five table, what's included, steps with help-guide links). Cost section dated 28 Nov with exact Microsoft prices. Comparison table and two FAQ answers (schema in step) say Calling Plans are not sold in Australia. Every "unlimited" on the page removed. Telstra Calling for Office 365 section kept. Title, H1 and URL unchanged.
- **/pricing/**: office-of-five paragraph in the hero; Team of 5 card made complete; inc GST added to the "Pricing a team?" strip; worked example names the $300 set-up it mentions; hosted-PBX FAQ (schema in step) gives $135 with the main number. Calculator, PDF quote and presets untouched (team5 preset already = $135).
- **/cloud-pbx/**: office-of-five line in the hero; cost section gives $135 and call rates past 300 minutes.
- **/voip-medical-clinics-australia/**: existing five-person table total gains "($148.50 inc GST)".
- **/voip-real-estate-agents-australia/**: one-line "agency of five" example under the pricing cards.
- **/voip-it-companies-australia/**: Teams section says Calling Plans are not sold in Australia (sourced), exact licence price, link to the worked total.
- **llms.txt / llms-full.md**: new Q&A "What does a phone system for an office of five cost?"; Teams answer extended with the Australian options, Microsoft prices and the Teams office-of-five total; llms-full "covers the majority of typical business usage" removed (usage hint).

No titles, URLs, CSS or help pages changed (so no `?v=` bump and no `llms-help.md` rebuild). No new FAQ items; FAQ structured data matches visible text on all six pages. No sideways scroll at 375 px. Change logs: `docs/*-ai-answers-change-log.json` (checked with `scripts/compare_pages.py`).

## Follow-ups Royce approved (28 Nov, "OK plus 1, 2 and 3")

1. **Usage hints removed** (Royce's 27 Nov rule: no figures or hints about how much customers use). Gone: "300 minutes…, more than most people use" (pricing ×4, home ×2); "Most of our $10 customers spend under $5 a month on calls" (pricing ×4, blog cost post); "Most people choose this" (pricing calculator); "covers the (vast) majority of typical business usage" (FAQ, llms-full).
2. **"Unlimited" removed** from 30 tracked pages plus llms.txt, llms-full.md and llms-help.md (regenerated). "Unlimited inbound/incoming calls" became "free incoming calls to local numbers" (shorter where the sentence already names the number); extensions are "free extensions for the whole team"; queue settings say "no limit"; "There is no unlimited plan" became "Every plan charges for calls past its included minutes". FAQ structured data changed word for word. Left on purpose: the four mentions describing Telstra's own TIPT Complete Calling plan on /compare/click2call-vs-telstra/ (a fact about Telstra's product), and the December test page /voip-melbourne/ (4 mentions; fix after the ~17 Dec reading).
3. **Retired $50 Teams set-up fee** removed from the two llms example-setup lines (the case-study page itself was already right).

Noted, not changed: two homepage FAQ answers ("Is there a lock-in contract?", "Is Click2Call the same as a click-to-call widget?") already differed between structured data and visible text before today.
