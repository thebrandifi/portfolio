#!/usr/bin/env python3
"""Usage: python3 set-domain.py yourdomain.com
Fills in canonical URL, Open Graph URL/image, sitemap, robots.txt and schema URLs."""
import sys, re, json, pathlib
if len(sys.argv) != 2: sys.exit(__doc__)
d = re.sub(r'^https?://', '', sys.argv[1]).strip('/')
root = pathlib.Path(__file__).parent
for n in ('index.html', 'robots.txt', 'sitemap.xml'):
    p = root / n; t = p.read_text(encoding='utf-8')
    t = t.replace('<!--DOMAIN-BLOCK', '').replace('DOMAIN-BLOCK-->', '').replace('YOUR-DOMAIN', d)
    t = t.replace('name="twitter:card" content="summary"', 'name="twitter:card" content="summary_large_image"')
    if n == 'index.html':
        m = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', t, re.S)
        ld = json.loads(m.group(2))
        for g in ld['@graph']:
            if g['@type'] in ('ProfilePage', 'Person'): g['url'] = f'https://{d}/'
            if g['@type'] == 'Person': g['image'] = f'https://{d}/assets/portrait.webp'
        t = t[:m.start(2)] + json.dumps(ld, ensure_ascii=False) + t[m.end(2):]
    p.write_text(t, encoding='utf-8')
print(f'Done. Now deploy, then submit https://{d}/sitemap.xml in Google Search Console.')
