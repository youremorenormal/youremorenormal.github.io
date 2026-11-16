"""Builds /guides/ (hub + one page per approved guide in Work/guides/publish/*.md).
Run at the end of feelings-build.py (exec), so it shares head(), FOOT, FORM, E, BASE, BUY, P, buy().
Each .md starts with 'Page title:', 'Meta description:', 'Suggested slug:', 'Internal links ...:' lines, a line '---', then the article."""
import glob, json, markdown

sm_ = lambda t: E(t, quote=False).replace("'", "&rsquo;")  # curly apostrophes in visible text
GDIR = os.path.abspath("../guides/publish")
guides = []
for f in sorted(glob.glob(GDIR + "/*.md")):
    raw = open(f, encoding="utf8").read()
    meta, art = raw.split("\n---\n", 1)
    m = {}
    for line in meta.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            m[k.strip().lower().split(" (")[0]] = v.strip()
    slug = m["suggested slug"].strip("/").split("/")[-1]
    links = [x.strip() for x in m.get("internal links", "").split(",") if x.strip()]
    art = markdown.markdown(art.strip(), extensions=["extra", "sane_lists", "smarty"],
                            extension_configs={"smarty": {"smart_dashes": False, "substitutions": {"left-single-quote": "&#8216;", "right-single-quote": "&#8217;", "left-double-quote": "&#8220;", "right-double-quote": "&#8221;", "ellipsis": "&#8230;"}}})
    guides.append(dict(slug=slug, title=m["page title"], desc=m["meta description"], links=links, html=art, mtime=os.path.getmtime(f)))

titles = {slug: (h1, ch) for slug, ch, h1, *_r in P}
urls_g = []
for g in guides:
    url = f"{BASE}guides/{g['slug']}/"
    urls_g.append(url)
    k = guides.index(g)
    others = [guides[(k + d) % len(guides)] for d in (1, 2, 3, 4) if guides[(k + d) % len(guides)] is not g][:4]
    more = '<h2>More guides</h2><ol class="list">' + ''.join(f'<li><a href="{BASE}guides/{o["slug"]}/">{sm_(o["title"])}</a></li>' for o in others) + '</ol>' if others else ''
    rel = "".join(f'<li><a href="{BASE}feelings/{s}/">{sm_(titles[s][0])}</a><span>From chapter: {sm_(titles[s][1])}</span></li>' for s in g["links"] if s in titles)
    ld = json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"], "url": url,
                     "inLanguage": "en-GB", "author": {"@type": "Person", "name": "Ahsan Raza"},
                     "datePublished": "2026-11-16", "dateModified": "2026-11-16",
                     "isPartOf": {"@type": "Book", "name": "You're More Normal Than You Think", "author": {"@type": "Person", "name": "Ahsan Raza"}}})
    bc = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "You're More Normal Than You Think", "item": BASE},
        {"@type": "ListItem", "position": 2, "name": "Guides", "item": BASE + "guides/"},
        {"@type": "ListItem", "position": 3, "name": g["title"], "item": url}]})
    extra = f'<script type="application/ld+json">{ld}</script><script type="application/ld+json">{bc}</script>'
    body = f"""<p class="crumb"><a href="{BASE}">The book</a> / <a href="{BASE}guides/">Guides</a> / {sm_(g['title'])}</p>
<article class="guide">{g['html']}</article>
<h2>Related pages</h2><ol class="list">{rel}</ol>{more}
<div class="btns"><a class="btn btn1" href="{buy(g['slug']).replace('utm_medium=feelings','utm_medium=guides')}" rel="noopener">Get the book, $6.99</a><a class="btn btn2" href="{BASE}read/">Read the first chapter free</a></div>""" + FORM
    d = f"guides/{g['slug']}"
    os.makedirs(d, exist_ok=True)
    open(f"{d}/index.html", "w", encoding="utf8").write(head(g["title"], g["desc"], url, extra) + body + FOOT)

hub_url = BASE + "guides/"
items = "".join(f'<li><a href="{g["slug"]}/">{sm_(g["title"])}</a><span>{sm_(g["desc"])}</span></li>' for g in guides)
hub = head("Guides: plain help for worry, comparing and the harsh voice | You're More Normal Than You Think",
           "Plain, evidence-honest guides on the feelings almost everyone has, from the author of You're More Normal Than You Think.", hub_url).replace("../../assets", "../assets") + f"""<p class="crumb"><a href="{BASE}">The book</a> / Guides</p>
<h1>Guides</h1><p class="lede">Short, plain guides on the feelings almost everyone has. Each one links to the chapter of the book that goes further.</p>
<ol class="list">{items}</ol>
<div class="btns"><a class="btn btn1" href="{BUY}&utm_source=site&utm_medium=guides&utm_campaign=hub" rel="noopener">Get the book, $6.99</a><a class="btn btn2" href="{BASE}feelings/">The twelve feelings</a></div>""" + FORM + FOOT
os.makedirs("guides", exist_ok=True)
open("guides/index.html", "w", encoding="utf8").write(hub)

sm = open("sitemap.xml", encoding="utf8").read()
sm = re.sub(r"<url><loc>[^<]*guides/[^<]*</loc>.*?</url>", "", sm)
add = "".join(f"<url><loc>{u}</loc><lastmod>2026-11-16</lastmod></url>" for u in [hub_url] + urls_g)
open("sitemap.xml", "w", encoding="utf8").write(sm.replace("</urlset>", add + "</urlset>"))
print("guides pages:", len(guides) + 1)

# "Guides on this feeling" block on each chapter page (idempotent)
for slug_f in titles:
    fp = f"feelings/{slug_f}/index.html"
    t = open(fp, encoding="utf8").read()
    t = re.sub(r'<div class="more-guides">.*?</div>(?=<div class="btns">)', "", t, flags=re.S)
    rel_g = [g for g in guides if slug_f in g["links"]][:4]
    if not rel_g:
        continue
    blk = '<div class="more-guides"><h2>Guides on this feeling</h2><ol class="list">' + "".join(
        f'<li><a href="{BASE}guides/{g["slug"]}/">{sm_(g["title"])}</a></li>' for g in rel_g) + "</ol></div>"
    t = t.replace('<div class="btns">', blk + '<div class="btns">', 1)
    open(fp, "w", encoding="utf8").write(t)
print("chapter pages linked to guides")
