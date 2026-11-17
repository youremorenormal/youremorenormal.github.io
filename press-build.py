"""Builds /press/ (for reviewers and podcast hosts). Run at the end of feelings-build.py (exec), so it shares head(), FOOT, E, BASE, BUY.
Only the cover image is copied in; never any manuscript or chapter file."""
import json, shutil
from PIL import Image

COVER_SRC = "../releases/v4-2026-16nov-final/apple/Cover-ebook-1600x2560.png"
COVER_FULL = "assets/youre-more-normal-than-you-think-cover-1600x2560.png"
COVER_WEB = "assets/youre-more-normal-than-you-think-cover-480.webp"
shutil.copy(COVER_SRC, COVER_FULL)
im = Image.open(COVER_SRC).convert("RGB"); im.thumbnail((480, 768)); im.save(COVER_WEB, "WEBP", quality=85)

url = BASE + "press/"
title = "For reviewers and podcast hosts | Ahsan Raza"
desc = ("Review copies, cover images and interview talking points for You're More Normal Than You Think by Ahsan Raza. "
        "Ask for a free EPUB or PDF copy by email.")
assert len(title) < 60 and 140 <= len(desc) <= 155, (len(title), len(desc))
MAIL = "hello@youremorenormal.com"
book_ld = {"@context": "https://schema.org", "@type": "Book", "name": "You're More Normal Than You Think",
           "alternateName": "Twelve feelings almost everyone has, and what to do about them",
           "author": {"@type": "Person", "name": "Ahsan Raza", "url": BASE + "about/"}, "inLanguage": "en-GB",
           "genre": "Self-help", "bookFormat": "https://schema.org/EBook", "datePublished": "2026-11",
           "image": BASE + COVER_FULL, "url": BASE}
page_ld = {"@context": "https://schema.org", "@type": "WebPage", "name": "For reviewers and podcast hosts", "url": url,
           "description": desc, "inLanguage": "en-GB", "about": {"@type": "Book", "name": "You're More Normal Than You Think"}}
bc_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "You're More Normal Than You Think", "item": BASE},
    {"@type": "ListItem", "position": 2, "name": "For reviewers and podcast hosts", "item": url}]}
CSS_P = """<style>.pbook{display:grid;grid-template-columns:200px 1fr;gap:28px;align-items:start;margin:20px 0 8px}
.pbook img{width:100%;height:auto;border-radius:6px;box-shadow:0 14px 30px -16px rgba(0,0,0,.55)}
.facts{margin:0;display:grid;grid-template-columns:max-content 1fr;gap:8px 18px;font-size:17px}.facts dt{color:var(--muted)}.facts dd{margin:0}
.press a{color:var(--ink)}.press ul{padding-left:1.2em}.press li{margin:0 0 14px}
.covers{display:grid;grid-template-columns:1fr 2fr;gap:28px;align-items:start;margin:16px 0}.covers figure{margin:0}.covers img{width:100%;height:auto;border-radius:6px}
.covers figcaption{font-size:16px;margin-top:8px}footer a{color:inherit}
@media (max-width:560px){.pbook{grid-template-columns:1fr}.pbook img{max-width:220px}.covers{grid-template-columns:1fr}.covers figure:first-child img{max-width:220px}.facts{grid-template-columns:1fr;gap:0}.facts dd{margin-bottom:10px}}</style>"""
extra = CSS_P + "".join(f'<script type="application/ld+json">{json.dumps(x)}</script>' for x in (book_ld, page_ld, bc_ld))
G = BASE + "guides/"
# Apple Books page returned 404 on 17 Nov 2026 (not on sale yet); set True once books.apple.com/us/book/id6832732682 loads
APPLE_LIVE = False
APPLE_LI = '<li><a href="https://books.apple.com/us/book/id6832732682" rel="noopener">Apple Books</a></li>' if APPLE_LIVE else ""
body = f"""<div class="press"><p class="crumb"><a href="{BASE}">The book</a> / For reviewers and podcast hosts</p>
<h1>For reviewers and podcast hosts</h1>
<p class="lede">If you review books or host a podcast, <em>You&rsquo;re More Normal Than You Think</em> is available for you to review or talk about. Everything you need is on this page.</p>
<h2>The book</h2>
<div class="pbook"><img src="../{COVER_WEB}" width="480" height="768" alt="Cover of You're More Normal Than You Think by Ahsan Raza">
<dl class="facts"><dt>Title</dt><dd>You&rsquo;re More Normal Than You Think</dd>
<dt>Subtitle</dt><dd>Twelve feelings almost everyone has, and what to do about them</dd>
<dt>Author</dt><dd>Ahsan Raza</dd><dt>Genre</dt><dd>Nonfiction, self help</dd>
<dt>Published</dt><dd>November 2026, self published</dd><dt>Language</dt><dd>English (British)</dd>
<dt>Formats</dt><dd>Ebook (EPUB and PDF), with a free printable workbook. A paperback is planned.</dd>
<dt>Price</dt><dd>$6.99</dd></dl></div>
<ul>{APPLE_LI}
<li><a href="{BUY}&utm_source=site&utm_medium=press" rel="noopener">Gumroad (EPUB, PDF and workbook)</a></li>
<li>Free sample: <a href="{BASE}sample/Youre-More-Normal-Than-You-Think-free-sample.pdf">PDF</a> or <a href="{BASE}sample/Youre-More-Normal-Than-You-Think-free-sample.epub" download>EPUB</a></li><li><a href="{BASE}read/">Read the first chapter free</a></li></ul>
<h2>A short description</h2>
<p>Do you ever feel as if everyone else got a simple manual and you got a stranger machine? The worry that wakes you at 2 a.m. The comparing. The harsh voice in your head. The feeling that you&rsquo;ll be found out.</p>
<p>This book takes twelve feelings almost everyone has and does three things with each one: shows you a real moment, tells you the plain truth, and gives you what the research says. Then comes a Do this that takes a few minutes. A free printable workbook goes with it.</p>
<h2>About the author</h2>
<p>Ahsan Raza is based in Lahore, Pakistan. For years he believed that what he felt was his alone. It was the people around him, friends, family and sometimes strangers, who finally helped. He wrote this book to give readers the conversation he wishes he had been able to have: plain, kind, and built on what the research really shows. <a href="{BASE}about/">More about the author</a>.</p>
<h2>Talking points for interviews</h2>
<ul><li><b>Why almost everyone feels behind.</b> We compare our inside with everyone else&rsquo;s outside. Research on comparing suggests people underestimate how often others feel bad, so the picture we measure ourselves against is brighter than the real thing. <a href="{G}why-does-everyone-seem-happier/">Why does everyone seem happier than me?</a></li>
<li><b>The 2 a.m. worry, and one small habit.</b> The version of tomorrow we build at night can be much darker than the one that turns up. One small habit: write the worry down, then check it later against what actually happened. <a href="{G}do-worries-come-true/">Do worries come true?</a></li>
<li><b>Why we give better advice than we take.</b> We see a friend&rsquo;s problem from the outside, where the important parts stand out, and live inside our own. Researchers call this Solomon&rsquo;s paradox, and thinking about your own problem as if it were a friend&rsquo;s helps. <a href="{G}easier-to-give-advice-than-take-it/">Why is it easier to give advice than take it?</a></li></ul>
<h2>Request a free review copy</h2>
<p>Email <a href="mailto:{MAIL}?subject=Review%20copy%20request">{MAIL}</a> with the subject &ldquo;Review copy request&rdquo; and say where you review or which show you host. The book is available as EPUB or PDF, whichever you prefer.</p>
<h2>Cover images</h2>
<div class="covers"><figure><img loading="lazy" src="../{COVER_WEB}" width="480" height="768" alt="Front cover of You're More Normal Than You Think by Ahsan Raza">
<figcaption><a href="../{COVER_FULL}" download>Download the front cover</a> (PNG, 1600 by 2560 pixels)</figcaption></figure>
<figure><img loading="lazy" src="../assets/pair.jpeg" width="900" height="506" alt="Front and back of You're More Normal Than You Think by Ahsan Raza, shown as a printed book">
<figcaption><a href="../assets/social.jpg" download="youre-more-normal-than-you-think-mockup.jpg">Download the book mockup</a> (JPEG, 1200 by 675 pixels)</figcaption></figure></div>
<h2>Contact</h2>
<p>For anything else, email <a href="mailto:{MAIL}">{MAIL}</a>.</p></div>"""
page = head(title, desc, url, extra).replace("../../assets", "../assets") + body + FOOT
for bad in ("–", "—", "ISBN", " AI ", "therapy"):
    assert bad not in body, bad
os.makedirs("press", exist_ok=True)
open("press/index.html", "w", encoding="utf8").write(page)
sm = open("sitemap.xml", encoding="utf8").read()
if url not in sm:
    open("sitemap.xml", "w", encoding="utf8").write(sm.replace("</urlset>", f"<url><loc>{url}</loc><lastmod>2026-11-17</lastmod></url></urlset>"))
print("press ok")
