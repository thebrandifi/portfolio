# SEO report v2: Appau Kofi Enoch | The Intelligence Mark
22 Nov 2026. Everything below was tested in a local browser. Nothing is claimed about rankings, indexing or traffic: the site is not on a live domain yet.

## 1. Audit: what was wrong, what changed
| Issue found | Fix |
|---|---|
| Page weighed about 6 MB (videos and logos built into the HTML), the biggest Core Web Vitals risk | Production build: index.html is now ~75 KB. Media are separate files with long-term caching, video poster images and lazy loading |
| H1 words ran together for crawlers ("GhanaStrategy") | Fixed; H1 reads "Digital Marketing Expert in Ghana Strategy meets creativity. Impact follows." |
| Experience headings all at one level | Entries are now H4 under their H3 groups: one H1 and a clean H2/H3/H4 outline |
| Thin structured data | Person + ProfilePage + 10 Service entries (provider = you; area = Ghana and remote) + FAQPage matching the on-page FAQ |
| Works section had no descriptive text | Added a short keyword-relevant intro (health, retail, recruitment) |
| No share image, manifest, 404, caching or security headers | Added og-image.png (1200x630), site.webmanifest, 404.html, _headers |
| Canonical/OG URL/sitemap need a domain | `set-domain.py yourdomain.com` fills everything in one step |

## 2. Keyword map (targets only; volume and difficulty NOT verified)
Check each in Google Keyword Planner and Search Console before investing effort.
- Home: digital marketing expert in Ghana; digital marketing specialist Accra
- Services: Meta Ads management Ghana; Google Ads specialist Ghana; social media management Accra; AI video production Ghana; Google Analytics
- Works: promotional video; AI-assisted motion graphics; health and retail marketing content
- International: AI video production services; AI-powered marketing content

## 3. Next content (build only with real substance)
Separate pages once you have original material for each: AI Video Production; Meta and Google Ads; one case study per project (objective, your role, tools, documented result); then the 8 article topics from your brief, each with a unique search intent. Do not publish thin or repeated pages.

## 4. Local and authority plan
- Keep name, phone and email identical everywhere: site, LinkedIn, Facebook, Instagram.
- Optimise LinkedIn (headline "Digital Marketing Expert in Accra, Ghana") and link it to the site.
- Google Business Profile only if you have a genuine eligible address; never invent one.
- Earn links honestly: Ghanaian business directories, digital marketing communities, guest posts, case studies that clients or partners reference. Never buy links.

## 5. Measurement plan
Search Console: clicks, impressions, CTR, average position, queries, indexed pages. GA4: events for form submit, WhatsApp click, email click and video plays; organic conversion rate. Review monthly; allow 8-12 weeks for changes to show.

## 6. Still needs you
Domain and hosting; Search Console and Bing verification; your GA4 ID; documented client results; a clean downloadable CV; WhatsApp's official logo.

## 7. Not done on purpose
VideoObject schema (add after hosting, with real thumbnails and upload dates); fake reviews or ratings; LocalBusiness schema (no eligible business address); extra pages without real content.
