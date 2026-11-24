# Deploying the multi-page website
Pages (each is a folder with an index.html, so the web addresses are clean):
/ (Home) · /about/ · /services/ · /ai-tools/ · /works/ · /insights/ · /insights/facebook-ads-vs-google-ads-ghana/ · /insights/ai-video-production-small-business/ · /contact/

1. Upload everything in this folder to a static host (Cloudflare Pages, Netlify, Vercel or any web host) and connect your domain with HTTPS on.
2. The domain **appau.thebrandifi.com** is already set in every page, sitemap.xml, robots.txt and llms.txt. (To change it later: `python3 set-domain.py newdomain.com` only works on a fresh copy, so keep the original multipage zip.)
3. Add the site to Google Search Console and Bing Webmaster Tools, then submit `https://appau.thebrandifi.com/sitemap.xml`.
4. Add your Google Analytics 4 tag (your own G- ID) before `</head>` on each page.

## Server settings (caching, "expires" headers, compression)
- Cloudflare Pages / Netlify: `_headers` is read automatically. Vercel: `vercel.json`. Apache/cPanel: `.htaccess`.
- Nginx: add `expires 1y; add_header Cache-Control "public, immutable";` for `location /assets/` and `location /favicon/`, and enable `gzip on;`.
If you change `assets/css/main.css` or `assets/js/main.js`, bump the `?v=` number on their links in every page.

## Notes
- Shared look: `assets/css/main.css`. Shared behaviour: `assets/js/main.js`.
- The header, footer and contact details repeat on each page, so change them in every file.
- Portrait: `assets/appau_kofi_enoch.webp`. Videos and posters: `assets/video/`. Tool logos: `assets/logos/`.
- The two Insights articles were drafted for you: read them, correct anything that does not match your experience, and change the date if you publish later.
