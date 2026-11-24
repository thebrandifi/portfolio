#!/usr/bin/env python3
"""Usage: python3 set-domain.py yourdomain.com
Fills in canonical URLs, hreflang, Open Graph URL/image, breadcrumbs, schema (entity IDs, URLs, images),
sitemap.xml, robots.txt and llms.txt on every page."""
import sys, re, json, pathlib
if len(sys.argv) != 2: sys.exit(__doc__)
d = re.sub(r'^https?://', '', sys.argv[1]).strip('/')
root = pathlib.Path(__file__).parent
files = list(root.rglob('index.html')) + [root / n for n in ('robots.txt', 'sitemap.xml', 'llms.txt')]
def absid(o):
    if isinstance(o, dict):
        return {k: (f'https://{d}/{v}' if k == '@id' and isinstance(v, str) and v.startswith('#') else absid(v)) for k, v in o.items()}
    if isinstance(o, list): return [absid(x) for x in o]
    return o
for p in files:
    if not p.exists(): continue
    t = p.read_text(encoding='utf-8')
    t = t.replace('<!--DOMAIN-BLOCK', '').replace('DOMAIN-BLOCK-->', '').replace('YOUR-DOMAIN', d)
    t = t.replace('# Sitemap:', 'Sitemap:').replace('name="twitter:card" content="summary"', 'name="twitter:card" content="summary_large_image"')
    if p.name == 'index.html':
        page_url = f'https://{d}/' + ('' if p.parent == root else p.parent.relative_to(root).as_posix() + '/')
        def fix(m):
            try: ld = json.loads(m.group(2))
            except Exception: return m.group(0)
            ld = absid(ld)
            for g in ld.get('@graph', []):
                ty = g.get('@type')
                if ty in ('ProfilePage', 'AboutPage', 'ContactPage', 'CollectionPage', 'WebPage'): g['url'] = page_url
                if ty == 'WebSite': g['url'] = f'https://{d}/'
                if ty == 'Person' and 'name' in g and 'description' in g:
                    g['url'] = f'https://{d}/'; g['image'] = f'https://{d}/assets/appau_kofi_enoch.webp'
                if ty == 'Article': g['mainEntityOfPage'] = page_url; g['image'] = [f'https://{d}/og-image.png']; g['url'] = page_url
                if ty == 'Service': g['url'] = f'https://{d}/services/'
            return m.group(1) + json.dumps(ld, ensure_ascii=False) + m.group(3)
        t = re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)', fix, t, flags=re.S)
    p.write_text(t, encoding='utf-8')
print(f'Done. Deploy, then submit https://{d}/sitemap.xml in Google Search Console.')
