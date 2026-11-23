# Deploying the website (5 steps)
1. Pick a host that serves static files (Cloudflare Pages, Netlify, Vercel or any web host) and upload everything in this folder.
2. Connect your own domain and make sure HTTPS is on.
3. Run once on your computer before uploading: `python3 set-domain.py yourdomain.com`
   (fills in the canonical URL, share image, sitemap, robots.txt and schema URLs). Or edit those files by hand.
4. Add the site to Google Search Console and Bing Webmaster Tools, then submit `https://yourdomain.com/sitemap.xml`.
5. Add your Google Analytics 4 tag (your own G- ID) before `</head>`, and mark form/WhatsApp clicks as conversions.
`_headers` (security and caching) works on Cloudflare Pages and Netlify; on other hosts copy the same rules into your server config.
