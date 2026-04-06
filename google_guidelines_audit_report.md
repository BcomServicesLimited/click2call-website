# Google Search Central Guidelines Audit Report

This report details the findings from a comprehensive scan of all 61 HTML pages on the Click2Call website, evaluated against the five Google Search Central guidelines provided (Robots meta tags, JavaScript SEO, Image SEO, and Google Discover).

## Executive Summary

The Click2Call website is generally well-structured and adheres to many of Google's best practices. All pages use standard HTML `<img>` tags with `alt` attributes for content images, and there are no instances of the `nosnippet` tag blocking AI Overviews. However, there are several areas where the site falls short of the specific requirements for **Google Discover** eligibility and optimal image indexing.

The audit identified **0 High**, **89 Medium**, and **77 Low** priority issues across the site.

---

## 1. Google Discover Eligibility (Medium Priority)

Google Discover requires specific signals to feature content prominently. The audit revealed that the site is currently missing key elements required for optimal Discover performance.

### Missing `max-image-preview:large`
According to the Google Discover guidelines, publishers must explicitly enable large image previews to increase the likelihood of appearing in Discover feeds.

* **Issue:** The `<meta name="robots" content="max-image-preview:large">` tag is missing across the entire site.
* **Impact:** Without this tag, Google may only show standard or no image previews in Discover, significantly reducing click-through rates.
* **Recommendation:** Add `<meta name="robots" content="max-image-preview:large, max-snippet:-1, max-video-preview:-1">` to the `<head>` of all blog posts, service pages, and the homepage.

### Generic or Missing `og:image` Tags
Discover relies heavily on the `og:image` tag to select the thumbnail image. The guidelines state: *"Avoid using generic images (for example, your site logo) in the schema.org markup or og:image meta tag."*

* **Issue 1:** 32 pages (including all Help Centre guides, the About page, and the Contact page) are using a generic fallback image (`click2call_og_image.jpg`).
* **Issue 2:** Several blog posts reference `og:image` files that do not exist on the server (e.g., `teams_hero.webp`, `voip_australia_hero.webp`, `support_hero.webp`, `contact_hero.webp`, `pricing_hero.webp`).
* **Recommendation:** Ensure every blog post and major service page has a unique, high-quality `og:image` that is at least 1200px wide and uses a 16:9 aspect ratio. Fix the broken image links in the blog post `<head>` sections.

---

## 2. Image SEO & Indexing (Medium Priority)

Google's Image SEO guidelines specify that Googlebot does not index CSS background images. Images must be embedded using standard HTML `<img>` or `<picture>` elements to be discovered and indexed.

### CSS Background Images
* **Issue:** 13 pages (the homepage and all 12 local city pages, e.g., `voip-brisbane/index.html`) use CSS `background-image: url(...)` for their primary hero images.
* **Impact:** Google Images cannot index these hero images, meaning the site misses out on potential visual search traffic for local VoIP queries.
* **Recommendation:** Refactor the hero sections on the homepage and city pages to use an `<img>` tag with `object-fit: cover` instead of CSS background images.

### Missing Image Dimensions
* **Issue:** 61 pages are missing the `og:image:width` and `og:image:height` meta tags.
* **Impact:** While not strictly required, providing these dimensions helps social platforms and Google Discover process the image faster and ensures the 16:9 aspect ratio is immediately recognised.
* **Recommendation:** Add `<meta property="og:image:width" content="1200">` and `<meta property="og:image:height" content="675">` (or the exact dimensions) alongside the `og:image` tag.

---

## 3. Structured Data (Medium Priority)

The guidelines recommend using schema.org markup to specify the primary image of a page, which can influence the thumbnail chosen for Discover and enable rich results in Google Images.

### Missing Image in JSON-LD
* **Issue:** Several key pages (e.g., `blog/index.html`, `help/how-to-set-up-ai-receptionist.html`) have JSON-LD structured data but lack an `"image"` or `"primaryImageOfPage"` property.
* **Impact:** These pages may be ineligible for image-based rich results or prominent badges in Google Images.
* **Recommendation:** Update the JSON-LD scripts on all blog posts and service pages to include the `"image"` property, pointing to the same high-resolution image used in the `og:image` tag.

---

## 4. Content & Technical SEO (Low Priority)

### Thin Content
* **Issue:** The `help/how-to-add-user.html` page has a very low word count (349 words).
* **Impact:** Google's JavaScript SEO guidelines warn against "soft 404s" and thin content. Pages with very little text may struggle to rank or be deemed unhelpful.
* **Recommendation:** Expand the content on this guide to provide more comprehensive instructions, similar to the newly created Outbound Caller ID guide.

### Canonical URL Formatting
* **Issue:** The canonical URL for `blog/how-to-get-a-business-phone-number.html` includes the `.html` extension.
* **Impact:** Minor inconsistency if the server is configured to serve extensionless URLs.
* **Recommendation:** Ensure canonical URLs match the exact format of the preferred serving URL.

### Meta Description Lengths
* **Issue:** Several local city pages (e.g., Brisbane, Gold Coast, Melbourne) have meta descriptions exceeding 165 characters.
* **Impact:** Google will likely truncate these descriptions in search results.
* **Recommendation:** Review and trim meta descriptions to remain under 155-160 characters for optimal display.

---

## Action Plan

To align the Click2Call website with Google's Search Central guidelines, the following steps should be taken in order of priority:

1. **Global Header Update:** Add `<meta name="robots" content="max-image-preview:large, max-snippet:-1, max-video-preview:-1">` to the global `_header.html` file.
2. **Fix Broken OG Images:** Generate and upload the missing hero images for the blog posts (`teams_hero.webp`, `voip_australia_hero.webp`, etc.).
3. **Replace Generic OG Images:** Create unique 1200x675px WebP images for the main service pages and replace the generic `click2call_og_image.jpg` reference.
4. **Refactor Hero Images:** Update the homepage and 12 city pages to use `<img>` tags instead of CSS `background-image` for their hero sections.
5. **Update Structured Data:** Ensure all JSON-LD blocks include an `"image"` property.

*Prompt completed: scan my entire website and give me a report of recommended changes to allign with these google guidelines*
