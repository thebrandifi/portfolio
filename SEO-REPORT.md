# SEO report v3: Appau Kofi Enoch | The Intelligence Mark
24 Nov 2026. Everything below was tested in a local browser. Nothing is claimed about rankings, indexing or traffic: the site is not on a live domain yet, and nobody can guarantee a Google position.

## What was added in this round
| Area | Change |
|---|---|
| Content depth | New /insights/ section with 2 original articles (Facebook Ads vs Google Ads in Ghana; How AI video production works for small businesses). Each has its own title, description, headings, byline, date, internal links and Article schema |
| Entity / Knowledge Graph | Person entity with stable ID, alternate name, occupation, employer, university, 4 certificates, knowsAbout, profile links; WebSite entity; ProfilePage, AboutPage, ContactPage, CollectionPage, Article, Service and FAQPage types; breadcrumbs on every inner page |
| About page | "At a glance" fact block (name, role, location, business, education, certificates, profiles, contact) written as plain text so search engines can read the facts directly |
| Page targeting | Keyworded labels and titles: About Appau Kofi Enoch; Digital marketing services · Accra, Ghana; AI & marketing tools; Works · AI video & social content; Contact · Accra, Ghana |
| Crawling | hreflang (en-GH), sitemap with 9 pages + 8 video entries + portrait image, llms.txt for AI search tools, internal links between pages and articles |
| Speed | Portrait now WebP (about 90 KB instead of 740 KB), font stylesheet no longer blocks rendering, the About portrait loads at high priority |

## Still true from earlier rounds
Separate CSS/JS files with long cache times, robots.txt, 404 page, security headers, one H1 per page, alt text on every image, no keyword stuffing.

## Keyword map (targets only; search volume and difficulty NOT verified)
- Home: digital marketer in Ghana; digital marketer Accra
- About: Appau Kofi Enoch (brand name searches)
- Services: digital marketing services Ghana; Meta Ads management Ghana; Google Ads Ghana; social media management Accra; AI video production Ghana
- Insights: Facebook ads vs Google ads Ghana; AI video production small business
- Check each in Google Keyword Planner and Search Console before investing more effort.

## Next content ideas (write only with real substance)
Social media strategy for Ghanaian businesses; promotional video checklist; how to measure ad results with Google Analytics; one case study per project (goal, your role, tools, documented result).

## Not done on purpose
VideoObject schema (needs the real upload date of each video); LocalBusiness schema (no eligible business address); reviews or ratings; page-per-keyword spam.

## Needs you
Domain and hosting; Search Console and Bing verification; GA4 ID; links to your Facebook, Instagram, TikTok and YouTube profiles; upload dates of the videos; review and approve the two articles.

## Domain
Set to https://appau.thebrandifi.com in every page (canonical, hreflang, Open Graph, schema IDs), sitemap.xml, robots.txt and llms.txt.
After deploying: add `https://appau.thebrandifi.com/` as a URL-prefix property in Google Search Console and Bing Webmaster Tools (verify with the HTML tag or a DNS TXT record on that subdomain), submit sitemap.xml, then request indexing for the home page and About page.
