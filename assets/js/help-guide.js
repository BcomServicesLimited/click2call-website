/* help-guide.js — how people use the help guides, and a "Did this guide help?" feedback box.
 *
 * Loaded on every guide under /help/ (not the /help/ index). Added 25 Nov 2026 (Royce) for the
 * help-guide feedback loop: a weekly review reads these events and proposes edits to the guides.
 *
 * PostHog events (sent only where analytics.js has loaded PostHog, i.e. on www.click2call.com.au):
 *   help_section_view   a section heading (h2) scrolled into view       { guide, section, section_index, sections_total }
 *   help_read_end       the reader reached the end of the guide          { guide, seconds }
 *   help_copy           text copied from the guide (e.g. a setting)      { guide, section, chars }
 *   help_link_click     a link in the guide was clicked                  { guide, section, href, kind }
 *                       kind: guide | support_email | portal | web_phone | site | external
 *   help_feedback       the feedback box was answered                    { guide, helpful, reason?, comment? }
 *
 * No personal details are collected on purpose; the comment box asks people not to type any.
 * Styles are inline so the Tailwind build cannot purge them.
 */
(function () {
  'use strict';
  var path = location.pathname.replace(/\.html$/, '').replace(/\/$/, '');
  if (path.indexOf('/help/') !== 0 || path === '/help') return;
  var guide = path.slice('/help/'.length);
  var main = document.querySelector('main');
  if (!main) return;

  function send(event, props) {
    props = props || {};
    props.guide = guide;
    try { if (window.posthog && window.posthog.capture) window.posthog.capture(event, props); } catch (e) {}
  }

  /* ---- Sections read ---- */
  var heads = Array.prototype.filter.call(main.querySelectorAll('h2'), function (h) {
    var t = (h.textContent || '').trim();
    return t && !/^(Still need help\?|Related Guides|Did this guide help\?)$/i.test(t);
  });
  function sectionOf(node) {
    var current = '';
    for (var i = 0; i < heads.length; i++) {
      if (heads[i].compareDocumentPosition(node) & Node.DOCUMENT_POSITION_FOLLOWING) current = heads[i].textContent.trim();
    }
    return current.slice(0, 120) || '(intro)';
  }
  var started = Date.now();
  if ('IntersectionObserver' in window) {
    var seen = {};
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var i = heads.indexOf(en.target);
        if (seen[i]) return;
        seen[i] = true;
        send('help_section_view', { section: en.target.textContent.trim().slice(0, 120), section_index: i + 1, sections_total: heads.length });
        io.unobserve(en.target);
      });
    }, { threshold: 0.6 });
    heads.forEach(function (h) { io.observe(h); });
  }

  /* ---- Copies and clicks ---- */
  document.addEventListener('copy', function () {
    var sel = window.getSelection && window.getSelection();
    if (!sel || !sel.rangeCount || !main.contains(sel.anchorNode)) return;
    send('help_copy', { section: sectionOf(sel.anchorNode), chars: String(sel).length });
  });
  main.addEventListener('click', function (e) {
    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
    if (!a || a.closest('#help-feedback')) return;
    var href = a.getAttribute('href') || '';
    var kind = /^mailto:/i.test(href) ? 'support_email'
      : /portal\.click2call\.com\.au/i.test(href) ? 'portal'
      : /phone\.click2call\.com\.au/i.test(href) ? 'web_phone'
      : /^\/help\//.test(href) || /click2call\.com\.au\/help\//.test(href) ? 'guide'
      : /^\//.test(href) || /click2call\.com\.au/.test(href) ? 'site' : 'external';
    send('help_link_click', { section: sectionOf(a), href: href.replace(/^mailto:([^?]*).*/i, 'mailto:$1').slice(0, 200), kind: kind });
  });

  /* ---- Feedback box ---- */
  var GREEN = '#3B9C49';
  var box = document.createElement('section');
  box.id = 'help-feedback';
  box.setAttribute('aria-label', 'Guide feedback');
  box.style.cssText = 'background:#fff;border:1px solid #E5E7EB;border-radius:16px;padding:24px;margin:32px 0;';
  var btn = 'display:inline-flex;align-items:center;justify-content:center;min-width:88px;padding:10px 18px;border-radius:12px;font-weight:600;font-size:15px;cursor:pointer;border:2px solid ' + GREEN + ';';
  box.innerHTML =
    '<h2 style="font-size:18px;font-weight:700;color:#111827;margin:0 0 4px;">Did this guide help?</h2>' +
    '<p style="font-size:14px;color:#6B7280;margin:0 0 16px;">Your answer helps us improve this guide.</p>' +
    '<div data-step="ask" style="display:flex;gap:12px;flex-wrap:wrap;">' +
      '<button type="button" data-helpful="yes" style="' + btn + 'background:' + GREEN + ';color:#fff;">Yes</button>' +
      '<button type="button" data-helpful="no" style="' + btn + 'background:#fff;color:' + GREEN + ';">No</button>' +
    '</div>' +
    '<form data-step="why" hidden style="margin-top:4px;">' +
      '<fieldset style="border:0;padding:0;margin:0 0 12px;"><legend style="font-size:15px;font-weight:600;color:#111827;margin-bottom:8px;">What went wrong?</legend>' +
      ['The steps didn’t match what I see', 'Information I needed is missing', 'It was hard to follow', 'Something else'].map(function (r, i) {
        return '<label style="display:flex;gap:8px;align-items:center;font-size:15px;color:#374151;margin:6px 0;cursor:pointer;"><input type="radio" name="reason" value="' +
          ['steps_dont_match', 'missing_info', 'hard_to_follow', 'other'][i] + '"' + (i === 0 ? ' required' : '') + '> ' + r + '</label>';
      }).join('') +
      '</fieldset>' +
      '<label for="help-fb-comment" style="display:block;font-size:15px;font-weight:600;color:#111827;margin-bottom:6px;">What were you trying to do? <span style="font-weight:400;color:#6B7280;">(optional)</span></label>' +
      '<textarea id="help-fb-comment" maxlength="300" rows="3" style="width:100%;box-sizing:border-box;border:1px solid #D1D5DB;border-radius:12px;padding:10px 12px;font-size:15px;font-family:inherit;"></textarea>' +
      '<p style="font-size:13px;color:#6B7280;margin:6px 0 12px;">Please don’t include passwords, account numbers or other personal details. For help with your account, email <a href="mailto:support@click2call.com.au" style="color:' + GREEN + ';font-weight:600;">support@click2call.com.au</a>.</p>' +
      '<button type="submit" style="' + btn + 'background:' + GREEN + ';color:#fff;">Send</button>' +
    '</form>' +
    '<p data-step="thanks" hidden role="status" style="font-size:15px;color:#374151;margin:0;"></p>';

  var still = Array.prototype.filter.call(main.querySelectorAll('h2'), function (h) { return /Still need help\?/i.test(h.textContent); })[0];
  var anchor = still ? still.closest('div.rounded-2xl') || still.parentNode : null;
  if (anchor && anchor.parentNode) anchor.parentNode.insertBefore(box, anchor);
  else (main.querySelector('.max-w-3xl, .max-w-4xl, .max-w-5xl') || main).appendChild(box);

  var ask = box.querySelector('[data-step="ask"]'), why = box.querySelector('[data-step="why"]'), thanks = box.querySelector('[data-step="thanks"]');
  function show(el, on) { el.hidden = !on; el.style.display = on ? '' : 'none'; }
  function done(text) { show(ask, false); show(why, false); show(thanks, true); thanks.textContent = text; }
  ask.addEventListener('click', function (e) {
    var b = e.target.closest('button[data-helpful]');
    if (!b) return;
    if (b.getAttribute('data-helpful') === 'yes') {
      send('help_feedback', { helpful: 'yes' });
      done('Thanks! Glad it helped.');
    } else {
      show(ask, false); show(why, true);
      var first = why.querySelector('input'); if (first) first.focus();
    }
  });
  why.addEventListener('submit', function (e) {
    e.preventDefault();
    var r = why.querySelector('input[name="reason"]:checked');
    var c = (why.querySelector('textarea').value || '').trim()
      .replace(/[\w.+-]+@[\w-]+\.[\w.]+/g, '[email]').replace(/\+?\d[\d\s-]{6,}\d/g, '[number]').slice(0, 300);
    send('help_feedback', { helpful: 'no', reason: r ? r.value : 'other', comment: c || undefined });
    done('Thanks for telling us. We read every answer and use it to fix the guide.');
  });

  /* ---- Reached the end ---- */
  if ('IntersectionObserver' in window) {
    var endSeen = false;
    var endIo = new IntersectionObserver(function (entries) {
      if (endSeen || !entries[0].isIntersecting) return;
      endSeen = true;
      send('help_read_end', { seconds: Math.round((Date.now() - started) / 1000) });
      endIo.disconnect();
    }, { threshold: 0.5 });
    endIo.observe(box);
  }
})();
