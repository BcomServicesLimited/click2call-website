/* analytics.js — PostHog product analytics for www.click2call.com.au.
 *
 * Loaded on every page that has Google Analytics (GA keeps running unchanged).
 * What it records: page views, page leaves (time on page, scroll depth),
 * clicks (autocapture, which also feeds heatmaps), and one named event,
 * `trial_click`, for every link to the portal sign-up form, with the button's
 * ?src= tag as `placement`.
 *
 * What it does not do: session recordings are OFF until the privacy policy
 * says so (set disable_session_recording to false to turn them on). No person
 * profiles are created for anonymous visitors (person_profiles: identified_only).
 *
 * It only sends from the live site, never from *.pages.dev previews or local
 * copies. POSTHOG_KEY is the project's public key (phc_...): it is designed to
 * sit in page source, like the GA measurement ID.
 */
(function () {
  var POSTHOG_KEY = 'phc_CUNgvaq8DJhdCc4x68TWNQvM4YdtgUm52cridK2dSvuX';
  var POSTHOG_HOST = 'https://us.i.posthog.com';
  var LIVE_HOST = 'www.click2call.com.au';

  if (location.hostname !== LIVE_HOST || POSTHOG_KEY.indexOf('phc_') !== 0) return;

  /* PostHog's standard loader, copied from the project's install page (Oct 2026): a stub that queues calls until array.js arrives. */
  !function(t,e){var o,n,p,r;e.__SV||(window.posthog && window.posthog.__loaded)||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}p||((p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",p.onerror=function(){p=null},(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r));var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],Object.defineProperty(u,"toString",{configurable:!0,enumerable:!0,writable:!0,value:function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e}}),Object.defineProperty(u.people,"toString",{configurable:!0,enumerable:!0,writable:!0,value:function(){return u.toString(1)+".people (stub)"}}),o="gu mu yu bu ku init Qu Zu Wu Vu Yu el Gu ec zu lc uc cc hc dc vc capture getExtension Ju fu mc calculateEventProperties gc register register_once register_for_session unregister unregister_for_session wc Uu yc getFeatureFlag getFeatureFlagPayload getFeatureFlagResult getAllFeatureFlags isFeatureEnabled reloadFeatureFlags updateFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSurveysLoaded onSessionId getSurveys getActiveMatchingSurveys onActiveMatchingSurveysChanged renderSurvey displaySurvey cancelPendingSurvey canRenderSurvey canRenderSurveyAsync kc identify setPersonProperties unsetPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset Sc shutdown setIdentity clearIdentity get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException addExceptionStep captureLog startExceptionAutocapture stopExceptionAutocapture loadToolbar get_property getSessionProperty bc rc createPersonProfile setInternalOrTestUser Cu xu opt_in_capturing opt_out_capturing $u has_opted_in_capturing has_opted_out_capturing get_explicit_consent_status is_capturing clear_opt_in_out_capturing nc debug il Os getPageViewId captureTraceFeedback captureTraceMetric Nu".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);

  window.posthog.init(POSTHOG_KEY, {
    api_host: POSTHOG_HOST,
    defaults: '2026-05-30',
    person_profiles: 'identified_only',
    capture_pageview: true,
    capture_pageleave: true,
    autocapture: true,
    enable_heatmaps: true,
    disable_session_recording: true
  });

  /* One clean event per trial button, named by its ?src= tag (e.g. voip-sydney-hero). */
  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest ? e.target.closest('a[href*="portal.click2call.com.au/join"]') : null;
    if (!a) return;
    var placement = 'untagged';
    try { placement = new URL(a.href).searchParams.get('src') || 'untagged'; } catch (err) {}
    window.posthog.capture('trial_click', { placement: placement, page_path: location.pathname });
  }, true);
})();
