"""Phase 4 — insert city-handoff banner, service cross-link block,
and pricing sticky-CTA into the relevant pages. Idempotent: each
insertion is wrapped in a marker comment and skipped on re-run.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


CITY_BANNER = """<!-- ===== PHASE4: REGIONAL HANDOFF ===== -->
<div class="bg-gray-50 border-y border-gray-100">
<div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-4 text-center text-sm text-gray-700">
<span class="font-semibold text-gray-900">Also serving:</span>
Adelaide, Canberra, Hobart, Darwin, Newcastle, Wollongong, Gold Coast and Sunshine Coast &mdash;
see <a class="text-[#3B9C49] font-semibold hover:underline" href="/voip-australia/">VoIP across Australia</a>.
</div>
</div>
<!-- ===== END PHASE4 REGIONAL HANDOFF ===== -->
"""

CITY_PAGES = [
    "voip-sydney/index.html",
    "voip-melbourne/index.html",
    "voip-brisbane/index.html",
    "voip-perth/index.html",
]


def service_block(self_slug: str) -> str:
    """Build a 4-card service cross-link block excluding self_slug."""
    services = [
        ("cloud-pbx",                "Cloud PBX",                 "Hosted phone system with auto-attendant, ring groups, mobile + desk apps."),
        ("ai-receptionist",          "AI Receptionist",           "AI answers your calls, qualifies the lead, and routes to the right person."),
        ("ai-voice-tools",           "AI Voice Tools",            "Call recording, transcription, sentiment analysis on every conversation."),
        ("microsoft-teams-calling",  "Microsoft Teams Calling",   "Make and receive calls inside Teams with Australian numbers and SIP backbone."),
        ("sip-trunks",               "SIP Trunks",                "Bring-your-own-PBX SIP trunks for existing phone systems and contact centres."),
        ("api",                      "Developer API",             "REST + webhooks for click-to-call, voice agents and call automation."),
    ]
    others = [s for s in services if s[0] != self_slug][:4]
    cards = []
    for slug, name, desc in others:
        cards.append(
            '<a href="/' + slug + '/" class="group block bg-white rounded-xl border border-gray-200 p-5 hover:shadow-md hover:border-[#3B9C49] transition-all">'
            '<div class="text-sm font-bold text-[#3B9C49] mb-1.5">' + name + '</div>'
            '<p class="text-sm text-gray-600 leading-relaxed">' + desc + '</p>'
            '</a>'
        )
    return (
        '<!-- ===== PHASE4: EXPLORE THE PLATFORM ===== -->\n'
        '<section class="bg-gray-50 py-14 border-t border-gray-100">\n'
        '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">\n'
        '<div class="text-center mb-10">\n'
        '<h2 class="text-2xl font-bold text-gray-900">Explore the Click2Call platform</h2>\n'
        '<p class="mt-2 text-gray-600">One Australian Cloud PBX. Services designed to work together out of the box.</p>\n'
        '</div>\n'
        '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">\n'
        + "\n".join(cards) + "\n"
        '</div>\n'
        '</div>\n'
        '</section>\n'
        '<!-- ===== END PHASE4 EXPLORE ===== -->\n'
    )


SERVICE_PAGES = [
    ("cloud-pbx/index.html",               "cloud-pbx"),
    ("ai-receptionist/index.html",         "ai-receptionist"),
    ("ai-voice-tools/index.html",          "ai-voice-tools"),
    ("microsoft-teams-calling/index.html", "microsoft-teams-calling"),
    ("sip-trunks/index.html",              "sip-trunks"),
]


STICKY_CTA = """<!-- ===== PHASE4: PRICING STICKY CTA ===== -->
<div id="sticky-trial-cta" class="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 shadow-lg z-40 transform translate-y-full transition-transform duration-300 hidden">
<div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between gap-3">
<div class="text-sm text-gray-900">
<span class="font-bold">$25</span><span class="text-gray-600">/user/mo ex GST &middot; no lock-in &middot; set up in under an hour</span>
</div>
<a href="https://portal.click2call.com.au/join/" target="_blank" rel="noopener noreferrer"
   class="inline-flex items-center gap-1 px-5 py-2 rounded-lg text-white font-bold text-sm whitespace-nowrap hover:opacity-90 transition-opacity"
   style="background-color: #3B9C49;"
   onclick="gtag('event', 'begin_free_trial', {'event_category': 'CTA', 'event_label': 'Sticky Trial Bar'});">
Start Free Trial
<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M13 7l5 5m0 0l-5 5m5-5H6" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg>
</a>
</div>
</div>
<script>
(function(){
  var bar = document.getElementById('sticky-trial-cta');
  if (!bar) return;
  var calc = document.getElementById('calculator');
  var threshold = calc ? calc.offsetTop + 600 : 1200;
  function onScroll(){
    if (window.scrollY > threshold) {
      bar.classList.remove('hidden');
      requestAnimationFrame(function(){ bar.classList.remove('translate-y-full'); });
    } else {
      bar.classList.add('translate-y-full');
    }
  }
  window.addEventListener('scroll', onScroll, {passive: true});
})();
</script>
<!-- ===== END PHASE4 STICKY CTA ===== -->
"""


def insert_once(file_path: Path, marker: str, anchor: str, block: str) -> str:
    """Insert block immediately before anchor if marker not already present.
    Returns one of: 'inserted', 'already-present', 'anchor-missing'."""
    text = file_path.read_text()
    if marker in text:
        return "already-present"
    if anchor not in text:
        return "anchor-missing"
    new_text = text.replace(anchor, block + anchor, 1)
    file_path.write_text(new_text)
    return "inserted"


def main():
    anchor_city = "<!-- Key Takeaways -->"
    anchor_footer = "<!-- ===================== FOOTER ====================="

    print("=== City handoff banners ===")
    for rel in CITY_PAGES:
        status = insert_once(ROOT / rel, "PHASE4: REGIONAL HANDOFF", anchor_city, CITY_BANNER)
        print(f"  {rel:40s} -> {status}")

    print("\n=== Service cross-link blocks ===")
    for rel, slug in SERVICE_PAGES:
        block = service_block(slug)
        status = insert_once(ROOT / rel, "PHASE4: EXPLORE THE PLATFORM", anchor_footer, block)
        print(f"  {rel:40s} -> {status}")

    print("\n=== Pricing sticky CTA ===")
    status = insert_once(ROOT / "pricing/index.html", "PHASE4: PRICING STICKY CTA", anchor_footer, STICKY_CTA)
    print(f"  pricing/index.html                       -> {status}")


if __name__ == "__main__":
    main()
