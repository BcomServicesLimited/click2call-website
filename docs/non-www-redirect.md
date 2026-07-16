# CRITICAL: non-www → www redirect (Cloudflare dashboard task)

**Status: NOT FIXED as of 2026-07-16 — needs a 5-minute dashboard action.**

## The problem

`https://click2call.com.au/` (without www) serves the ENTIRE site as
HTTP 200 instead of redirecting to `https://www.click2call.com.au/`.
Google is crawling and indexing two complete copies of the site.

Confirmed impact in the 2026-07-16 GSC exports:
- Indexed pages collapsed from 80 (April) to 49 (July)
- "Alternate page with proper canonical tag": 38 pages
- "Crawled – currently not indexed": 85 pages
- Clicks split across hosts (homepage: 132 www + 55 non-www;
  blog/cloud-pbx-vs-traditional: 2,193 www + 880 non-www impressions)
- Head terms stuck at position 23–31 with ranking signals split
  between the two hosts

## Why the _redirects file didn't work

`_redirects` on Cloudflare Pages is **path-only** — it cannot match or
redirect between hostnames. The line
`https://click2call.com.au/* → https://www.click2call.com.au/:splat`
was silently ignored (it's now commented out in the file).

## The fix (Cloudflare dashboard, ~5 minutes)

1. Log in to **dash.cloudflare.com** → select the **click2call.com.au** zone
2. Left sidebar: **Rules → Redirect Rules** (on newer dashboards:
   **Rules → Overview → Create rule → Redirect Rule**)
3. **Create rule**, name it `non-www to www`
4. **If…** Custom filter expression:
   - Field: **Hostname** · Operator: **equals** · Value: `click2call.com.au`
5. **Then…** URL Redirect:
   - Type: **Dynamic**
   - Expression: `concat("https://www.click2call.com.au", http.request.uri.path)`
   - Status code: **301**
   - Tick **Preserve query string**
6. **Deploy**

(If the dashboard offers a one-click template called "Redirect from WWW
to Root" — that's the WRONG direction. You want root → www, which is
what the custom rule above does.)

## Verify (Terminal)

```bash
curl -sI https://click2call.com.au/ | head -3
# want:  HTTP/2 301  +  location: https://www.click2call.com.au/

curl -sI https://click2call.com.au/cloud-pbx/ | head -3
# want:  HTTP/2 301  +  location: https://www.click2call.com.au/cloud-pbx/
```

## After it's live

1. In GSC → Page indexing: click **Validate Fix** on
   "Alternate page with proper canonical tag" and "Page with redirect"
2. Expect the non-www URLs to drop out of the index over ~2–6 weeks and
   www positions to consolidate/improve as signals merge
3. Re-check the Coverage report in ~4 weeks — indexed count should
   climb back toward the real page count (~80)
