"""Builds /feelings/ (hub + 12 short pages) and adds them to the sitemap and the index chapter list.
Run by build-site.py at its end. Pages hold short summaries only, never manuscript text."""
import os, re, html

BASE = "https://youremorenormal.github.io/"
BUY = "https://ahsanrazabooks.gumroad.com/l/sdpapr?wanted=true"
E = html.escape

# slug, chapter title, page H1, feeling, what the chapter covers, exercise
P = [
 ("everyone-else-seems-to-have-it-figured-out", "Why It's Normal to Feel Not Normal",
  "Why does everyone else seem to have it figured out?",
  "Other people look calmer and further along, and you are the one keeping up appearances. It shows up in a crowded room, or at 1 a.m. when you are reading reviews of a toaster you do not need.",
  "the gap between how you feel inside and what other people show, and why almost everyone is doing the same sum about everyone else.",
  "Two minutes: one post, and what it leaves out."),
 ("cant-stop-worrying-at-night", "Your Brain Is Built to Worry",
  "Why can't I stop worrying at night?",
  "A message lands at twenty to eleven and within ten minutes you have been through every way it could go wrong.",
  "why the mind sounds an alarm for toast, why bad feels stronger than good, and how to give a worry a size instead of fighting it.",
  "Two minutes: say the fear, then say what you know."),
 ("how-to-decide-when-you-keep-asking-everyone", "You May Already Know the Answer",
  "How do I decide when I keep asking everyone else?",
  "You can give a friend calm, clear advice in four minutes, then spend a year on the same question about your own life.",
  "the wise judge you already are for everyone else, and how to ask your own question the way you would ask a friend's.",
  "Three minutes: answer it as a friend."),
 ("why-does-my-day-look-so-grey", "Same Day, Different Lens",
  "Why does my day look so grey?",
  "You photograph the kettle, yesterday's mug and the crumbs, and the picture seems to say everything about your life.",
  "how the same corner of a day can look different when you change how you look at it.",
  "Two minutes: photograph one corner of your day again."),
 ("coping-with-rejection-and-setbacks", "When Things Go Wrong",
  "How do I cope after a rejection or a setback?",
  "You can tell it is bad news from the polite subject line, and the evening stretches out in front of you.",
  "what a setback actually is, how long you expect it to hurt, and a plan for the evening after something goes wrong.",
  "Two minutes: check your Worry log against what happened."),
 ("why-am-i-so-hard-on-myself", "Voice in Your Head",
  "Why am I so hard on myself?",
  "A line runs in your head that nobody else hears: typical, everyone else managed it.",
  "what that voice is doing, what constant comparison does to you, and talking to yourself by name.",
  "Two minutes: start a comparison tally for today."),
 ("why-does-a-small-thing-make-me-cry", "Cry When You Can",
  "Why does a small thing make me cry?",
  "Sometimes a small, ordinary thing opens a feeling that has been waiting for weeks.",
  "the feeling that waits, where you learned to look at the ceiling, and how to put it into words.",
  "Two minutes: name one feeling in one word."),
 ("why-do-i-feel-like-a-fraud-at-work", "Waiting to Be Found Out",
  "Why do I feel like a fraud at work?",
  "You are a few weeks into something new, sure that the next person to glance in will see you are making it up.",
  "the fear of being found out, why it does not leave when you get good, and how to check it against what actually happened.",
  "Two minutes: one time you did it before you felt ready."),
 ("why-do-good-days-disappear", "Small Good Things",
  "Why do the good parts of my day disappear?",
  "A text that made you laugh on the stairs, a child who ate four peas. Each one landed and was gone.",
  "where your mind goes while the good thing happens, and a simple notebook habit.",
  "One evening: what you noticed instead of the phone."),
 ("reaching-out-when-it-feels-awkward", "People Who Hold You Up",
  "How do I reach out to someone when it feels awkward?",
  "You think of a friend you have not spoken to in months, and sending a message feels like more than it should.",
  "why you expect it to be awkward, and how to tell who holds you up from who wears you out.",
  "Under a minute: send it before you close the book."),
 ("why-cant-i-finish-anything-perfectionism", "Perfectly Unfinished",
  "Why can't I finish anything?",
  "It is nearly done, but there is always one more thing to fix, and the finish line keeps moving.",
  "wanting it good and being afraid of getting it wrong, a finish line that keeps moving, and deciding where it stops.",
  "Two minutes: write where it stops, then set the timer."),
 ("do-people-notice-my-mistakes", "No One's Watching",
  "Do people really notice my mistakes?",
  "There is a mark on your cuff at a party, and for two hours it is all you can think about.",
  "why you feel lit up more brightly in your own head than anyone else sees you, and what to do with your hands in an empty room.",
  "Ten minutes: phone face down, then write what your hands did."),
]
N = len(P)
KW = [
 "feeling not normal, everyone else has it figured out, comparing yourself to others, social media comparison, self help book",
 "cant stop worrying, worry at night, anxious thoughts at 2am, overthinking, how to stop worrying",
 "how to make a decision, asking everyone for advice, trust yourself, indecision, self help book",
 "life feels grey, seeing your day differently, everyday life, feeling flat, self help book",
 "rejection email, coping with setbacks, bounce back after failure, feeling disappointed, self help book",
 "harsh inner voice, self criticism, why am i so hard on myself, comparing yourself, negative self talk",
 "crying over small things, suppressed feelings, naming emotions, feelings that wait, self help book",
 "imposter feelings, fraud at work, feeling like a fake, new job doubt, waiting to be found out",
 "good days disappear, small good things, noticing positives, gratitude notebook, self help book",
 "reaching out to friends, awkward to message, loneliness, who supports you, friendship",
 "perfectionism, cant finish anything, fear of getting it wrong, finish line moves, procrastination",
 "do people notice my mistakes, spotlight effect, self conscious, feeling watched, social anxiety feelings",
]

FORM = ('<style>.sub{max-width:720px;margin:44px auto 0;padding:0 20px}.sub label{display:block;font:600 20px/1.3 var(--display,Georgia,serif);margin-bottom:10px}'
        '.sub div{display:flex;gap:8px;flex-wrap:wrap}.sub input[type=email]{flex:1 1 220px;min-height:48px;padding:0 14px;font:inherit;font-size:17px;border:1px solid var(--rule,#ddd2c9);border-radius:10px;background:var(--card,#fffdfa);color:var(--ink,#211a17)}'
        '.sub button{min-height:48px;padding:0 22px;border-radius:10px;border:0;background:var(--ink,#211a17);color:var(--bg,var(--paper,#f8f4f1));font:600 17px var(--body,system-ui,sans-serif);cursor:pointer}'
        'main .sub{padding:0;max-width:none;margin:44px 0 0}.sub small{display:block;margin-top:8px;color:var(--muted,#6b5f58);font-size:15px}.sub input:focus-visible,.sub button:focus-visible{outline:3px solid var(--accent,#b4472a);outline-offset:2px}</style>'
        '<form class="sub" action="https://gumroad.com/follow_from_embed_form" method="post"><label for="sub-email">Want an email from the author when there is something new?</label>'
        '<div><input type="hidden" name="seller_id" value="6138345188489"><input id="sub-email" type="email" name="email" required autocomplete="email" placeholder="Your email address"><button type="submit">Follow</button></div>'
        '<small>You can unsubscribe at any time.</small></form>')

SHELVES = [("A", "Comparing and belonging", (1, 6, 12)), ("B", "Worry and setbacks", (2, 5, 11)),
           ("C", "Feeling and noticing", (4, 7, 9)), ("D", "Doubt and people", (3, 8, 10))]
SHELF_OF = {c: (l, n) for l, n, cs in SHELVES for c in cs}

TOGGLE = ('<button type="button" class="theme-toggle" aria-label="Switch colour theme" title="Switch colour theme">'
          '<svg class="i-moon" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M21 14.5A9 9 0 0 1 9.5 3a9 9 0 1 0 11.5 11.5z"/></svg>'
          '<svg class="i-sun" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><circle cx="12" cy="12" r="4.2" fill="currentColor"/><g stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/></g></svg></button>')
def tools():
    return '<div class="tools">' + TOGGLE + menu() + '</div>'

def menu():
    cols = "".join(
        f'<div class="shelf"><p class="shelf-h">Shelf {l}<span>{E(n)}</span></p><ol>' +
        "".join(f'<li><a href="{BASE}feelings/{P[c-1][0]}/"><i>{c:02d}</i><b>{E(P[c-1][1])}</b></a></li>' for c in cs) + "</ol></div>"
        for l, n, cs in SHELVES)
    return ('<details class="shelves"><summary><span>Browse</span><span class="lg">the shelves</span></summary><div class="mega">' + cols +
            f'<div class="mega-f"><a href="{BASE}read/">Read chapter 1 free</a><a href="{BASE}feelings/">All twelve feelings</a><a href="{BASE}about/">About the author</a></div></div></details>')

MENU_CSS = """.shelves{position:relative}.shelves summary{list-style:none;cursor:pointer;font:600 16px var(--body,system-ui,sans-serif);padding:8px 6px;color:var(--ink,#211a17);display:inline-flex;gap:5px;align-items:center;user-select:none}
.shelves summary::-webkit-details-marker{display:none}.shelves summary::after{content:"";width:7px;height:7px;margin-left:3px;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:rotate(45deg) translateY(-2px)}
.shelves[open] summary::after{transform:rotate(-135deg) translateY(-1px)}.shelves summary:focus-visible,.shelves a:focus-visible{outline:3px solid var(--accent,#b4472a);outline-offset:2px}
.mega{position:absolute;right:-8px;top:calc(100% + 12px);z-index:50;width:min(580px,calc(100vw - 24px));background:var(--card,#fffdfa);border:1px solid var(--rule,#ddd2c9);border-radius:14px;padding:22px 24px 14px;box-shadow:0 18px 40px -20px rgba(0,0,0,.5);display:grid;grid-template-columns:1fr 1fr;gap:22px 30px}
.shelf-h{margin:0 0 4px;font:600 12px/1.2 var(--body,sans-serif);letter-spacing:.08em;text-transform:uppercase;color:var(--accent,#b4472a)}.shelf-h span{display:block;margin-top:3px;font:500 17px/1.25 var(--display,Georgia,serif);letter-spacing:0;text-transform:none;color:var(--ink,#211a17)}
.shelf ol{list-style:none;margin:0;padding:0}.shelf li a{display:flex;gap:10px;align-items:baseline;padding:8px 0;border-bottom:1px dotted var(--rule,#ddd2c9);text-decoration:none;color:var(--ink,#211a17);font:500 15px/1.3 var(--body,sans-serif)}.shelf li:last-child a{border-bottom:0}
.shelf a i{font-style:normal;color:var(--muted,#6b5f58);font-variant-numeric:tabular-nums;font-size:13px;min-width:1.5em}.shelf a b{font-weight:500}.shelf a:hover b{text-decoration:underline;text-underline-offset:3px}
.mega-f{grid-column:1/-1;display:flex;flex-wrap:wrap;gap:6px 22px;border-top:1px solid var(--rule,#ddd2c9);padding-top:12px}.mega-f a{color:var(--ink,#211a17);font:600 14px var(--body,sans-serif)}
@media (max-width:640px){.shelves{position:static}.mega{left:12px;right:12px;width:auto;top:100%;grid-template-columns:1fr;max-height:75vh;overflow:auto}}@media (max-width:480px){.shelves summary .lg{display:none}}
.cat{display:inline-block;border:1px solid var(--rule,#ddd2c9);border-radius:6px;padding:7px 12px;margin:22px 0 4px;font:600 13px var(--body,sans-serif);letter-spacing:.07em;text-transform:uppercase;color:var(--muted,#6b5f58);background:repeating-linear-gradient(0deg,transparent 0 23px,rgba(180,71,42,.12) 23px 24px)}.cat b{color:var(--accent,#b4472a)}
footer.wrap{padding:52px 20px 60px}
.tools{display:flex;align-items:center;gap:10px}.theme-toggle{width:42px;height:42px;border-radius:999px;border:1px solid var(--rule,#ddd2c9);background:transparent;color:var(--ink,#211a17);cursor:pointer;display:inline-flex;align-items:center;justify-content:center;padding:0}.theme-toggle:focus-visible{outline:3px solid var(--accent,#b4472a);outline-offset:2px}.theme-toggle .i-sun{display:none}:root[data-theme=dark] .theme-toggle .i-sun{display:block}:root[data-theme=dark] .theme-toggle .i-moon{display:none}@media (prefers-color-scheme:dark){:root:not([data-theme=light]) .theme-toggle .i-sun{display:block}:root:not([data-theme=light]) .theme-toggle .i-moon{display:none}}nav.wrap{flex-wrap:wrap;gap:8px}@media (max-width:480px){.shelves summary .lg{display:none}}"""
MENU_JS = """<script>(function(){var r=document.documentElement,b=document.querySelector('.theme-toggle');function cur(){return r.dataset.theme||(matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light');}function lab(){if(b){var d=cur()==='dark';b.setAttribute('aria-label',d?'Switch to light theme':'Switch to dark theme');b.title=b.getAttribute('aria-label');}}lab();if(b)b.addEventListener('click',function(){var n=cur()==='dark'?'light':'dark';r.dataset.theme=n;try{localStorage.setItem('ymn-theme',n);}catch(e){}lab();});var d=document.querySelector('.shelves');if(!d)return;document.addEventListener('keydown',function(e){if(e.key==='Escape'&&d.open){d.open=false;d.querySelector('summary').focus();}});document.addEventListener('click',function(e){if(d.open&&!d.contains(e.target))d.open=false;});})();</script>"""

CSS = """:root{--bg:#f8f4f1;--ink:#211a17;--muted:#6b5f58;--rule:#ddd2c9;--accent:#b4472a;--card:#fffdfa;--display:"Newsreader",Georgia,serif;--body:"Hanken Grotesk",system-ui,-apple-system,"Segoe UI",sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#1c1714;--ink:#f1e9e2;--muted:#b3a69d;--rule:#3a312b;--accent:#e0805f;--card:#251f1b}}
:root[data-theme=dark]{--bg:#1c1714;--ink:#f1e9e2;--muted:#b3a69d;--rule:#3a312b;--accent:#e0805f;--card:#251f1b}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:400 19px/1.65 var(--body)}
.wrap{max-width:720px;margin:0 auto;padding:0 20px}
nav{display:flex;justify-content:space-between;align-items:center;padding:18px 0;font-size:16px}
nav a{color:var(--ink);text-decoration:none;font-weight:600}
.crumb{color:var(--muted);font-size:15px;margin-top:28px}.crumb a{color:var(--muted)}
h1{font:600 clamp(32px,6vw,46px)/1.12 var(--display);letter-spacing:-.015em;margin:10px 0 18px}
h2{font:600 24px/1.25 var(--display);margin:40px 0 10px}
p{margin:0 0 16px}.lede{font-size:21px}
.box{background:var(--card);border:1px solid var(--rule);border-radius:14px;padding:18px 22px;margin:28px 0}
.box b{display:block;color:var(--accent);font-size:14px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px}
.btns{display:flex;flex-wrap:wrap;gap:12px;margin:30px 0}
.btn{display:inline-flex;align-items:center;min-height:48px;padding:0 22px;border-radius:12px;font-weight:600;text-decoration:none;font-size:17px}
.btn1{background:var(--ink);color:var(--bg)}.btn2{border:1px solid var(--ink);color:var(--ink)}
.pn{display:flex;justify-content:space-between;gap:16px;border-top:1px solid var(--rule);padding-top:20px;margin-top:40px;font-size:16px}
.pn a{color:var(--ink)}a:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
ol.list{padding-left:1.2em}ol.list li{margin:0 0 12px}ol.list a{color:var(--ink);font-weight:600}ol.list span{display:block;color:var(--muted);font-size:16px;font-weight:400}
footer{color:var(--muted);font-size:15px;padding:40px 0}"""

def head(title, desc, url, extra=""):
    return f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<script>try{{var t=localStorage.getItem('ymn-theme');if(t)document.documentElement.dataset.theme=t;}}catch(e){{}}</script><title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large"><link rel="alternate" hreflang="en-GB" href="{url}"><link rel="alternate" hreflang="x-default" href="{url}"><meta property="og:site_name" content="You're More Normal Than You Think"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="675"><meta property="og:image:alt" content="The book You're More Normal Than You Think by Ahsan Raza"><meta name="twitter:image" content="{BASE}assets/social.jpg"><meta name="twitter:title" content="{E(title)}"><meta name="twitter:description" content="{E(desc)}"><meta property="og:type" content="article"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}assets/social.jpg"><meta property="og:locale" content="en_GB"><meta name="twitter:card" content="summary_large_image">
<meta name="author" content="Ahsan Raza"><meta name="theme-color" content="#f8f4f1">
<link rel="icon" href="../../assets/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="48x48" href="../../assets/favicon-48.png"><link rel="apple-touch-icon" href="../../assets/apple-touch-icon.png">
<link rel="preload" as="font" type="font/woff2" crossorigin href="../../assets/fonts/Newsreader-600.woff2"><link rel="stylesheet" href="../../assets/fonts.css">
<style>{CSS}nav.wrap{{position:relative;padding:28px 24px 12px;max-width:1120px}}nav.wrap>a:first-child{{font:600 19px/1 var(--body);letter-spacing:-.01em}}{MENU_CSS}</style>{extra}</head><body>
<nav class="wrap"><a href="{BASE}">Ahsan Raza</a>{tools()}</nav><main class="wrap">"""

def buy(slug):
    return BUY + f"&utm_source=site&utm_medium=feelings&utm_campaign={slug}"

FOOT = f"""</main><footer class="wrap">&copy; Ahsan Raza. English (British).</footer>{MENU_JS}</body></html>"""
os.makedirs("feelings", exist_ok=True)
urls = [BASE + "feelings/"]

for i, (slug, ch, h1, feel, covers, ex) in enumerate(P, 1):
    d = f"feelings/{slug}"; os.makedirs(d, exist_ok=True)
    url = f"{BASE}{d}/"; urls.append(url)
    title = f"{h1} | You're More Normal Than You Think"
    desc = f"{feel} Chapter {i} of You're More Normal Than You Think looks at {covers}"
    desc = desc if len(desc) <= 300 else desc[:297].rsplit(" ", 1)[0] + "..."
    prev = P[i - 2] if i > 1 else None
    nxt = P[i] if i < N else None
    ld = ('{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
          f'{{"@type":"ListItem","position":1,"name":"You\'re More Normal Than You Think","item":"{BASE}"}},'
          f'{{"@type":"ListItem","position":2,"name":"Twelve feelings","item":"{BASE}feelings/"}},'
          f'{{"@type":"ListItem","position":3,"name":"{E(h1)}","item":"{url}"}}]}}')
    ld2 = ('{"@context":"https://schema.org","@type":"WebPage","name":"' + h1.replace('"', "'") + '","url":"' + url +
           '","inLanguage":"en-GB","author":{"@type":"Person","name":"Ahsan Raza"},"isPartOf":{"@type":"Book","name":"You\'re More Normal Than You Think","author":{"@type":"Person","name":"Ahsan Raza"}}}')
    extra = f'<meta name="keywords" content="{E(KW[i-1])}"><script type="application/ld+json">{ld}</script><script type="application/ld+json">{ld2}</script>'
    pn = "<div class=\"pn\"><span>" + (f'<a href="../{prev[0]}/">&larr; {E(prev[2])}</a>' if prev else "") + "</span><span>" + (f'<a href="../{nxt[0]}/">{E(nxt[2])} &rarr;</a>' if nxt else "") + "</span></div>"
    body = f"""<p class="crumb"><a href="{BASE}">The book</a> / <a href="{BASE}feelings/">Twelve feelings</a> / Chapter {i}</p>
<div class="cat"><b>Shelf {SHELF_OF[i][0]}</b> &middot; {E(SHELF_OF[i][1])} &middot; Chapter {i:02d} of 12</div>
<h1>{E(h1)}</h1>
<p class="lede">{E(feel)}</p>
<h2>You are not the only one</h2>
<p>This is one of the twelve feelings almost everyone has, and almost nobody mentions. It does not mean something is wrong with you.</p>
<h2>What Chapter {i} does with it</h2>
<p>Chapter {i} of <em>You&rsquo;re More Normal Than You Think</em> is called &ldquo;{E(ch)}&rdquo;. It looks at {E(covers)}</p>
<div class="box"><b>Do this now</b>{E(ex)} Every chapter ends with something small like this, so you finish it in a few minutes.</div>
<div class="btns"><a class="btn btn1" href="{buy(slug)}" rel="noopener">Get the book, $6.99</a><a class="btn btn2" href="{BASE}read/">Read the first chapter free</a></div>
{pn}""" + FORM
    open(f"{d}/index.html", "w", encoding="utf8").write(head(title, desc, url, extra) + body + FOOT)

# hub
hub_title = "Twelve feelings almost everyone has | You're More Normal Than You Think"
hub_desc = "The worry at 2 a.m., the comparing, the harsh voice, the fear of being found out. Twelve common feelings, and what to do about each one."
items = "".join(f'<li><a href="{s}/">{E(h)}</a><span>Chapter {i}: {E(c)}</span></li>' for i, (s, c, h, *_r) in enumerate(P, 1))
hub = head(hub_title, hub_desc, BASE + "feelings/").replace("../../assets", "../assets") + f"""<p class="crumb"><a href="{BASE}">The book</a> / Twelve feelings</p>
<h1>Twelve feelings almost everyone has</h1><p class="lede">Pick the one that sounds like tonight. Each links to the chapter of the book that deals with it.</p>
<ol class="list">{items}</ol>
<div class="btns"><a class="btn btn1" href="{BUY}&utm_source=site&utm_medium=feelings&utm_campaign=hub" rel="noopener">Get the book, $6.99</a><a class="btn btn2" href="{BASE}read/">Read the first chapter free</a></div>""" + FORM + FOOT
open("feelings/index.html", "w", encoding="utf8").write(hub)

# sitemap and index links
sm = open("sitemap.xml", encoding="utf8").read()
sm = re.sub(r"<url><loc>[^<]*feelings/[^<]*</loc>.*?</url>", "", sm)
add = "".join(f"<url><loc>{u}</loc><lastmod>2026-11-15</lastmod></url>" for u in urls)
open("sitemap.xml", "w", encoding="utf8").write(sm.replace("</urlset>", add + "</urlset>"))

t = open("index.html", encoding="utf8").read()
for i, (slug, ch, *_r) in enumerate(P, 1):
    li = "<li>" + E(ch, quote=False).replace("'", "&rsquo;") + "</li>"
    assert li in t, li
    t = t.replace(li, f'<li><a href="feelings/{slug}/">{E(ch, quote=False).replace(chr(39), "&rsquo;")}</a></li>', 1)
if 'follow_from_embed_form' not in t:
    t = t.replace('<footer class="wrap">', FORM + "\n" + '<footer class="wrap">', 1)
open("index.html", "w", encoding="utf8").write(t)
for bad in ("–", "—", " loo "):
    for root, _, fs in os.walk("feelings"):
        for f in fs:
            assert bad not in open(os.path.join(root, f), encoding="utf8").read(), (bad, f)
print("feelings pages:", N + 1)

# ---- About the author page (text is the book's own "About the Author") ----
os.makedirs("about", exist_ok=True)
ab = open("../rewrite/z-about-the-author.md", encoding="utf8").read().split("\n\n")[1:]
paras = [E(p.strip(), quote=False).replace("'", "&rsquo;") for p in ab if p.strip()]
url = BASE + "about/"
ld = ('{"@context":"https://schema.org","@type":"ProfilePage","mainEntity":{"@type":"Person","name":"Ahsan Raza","url":"' + url +
      '","description":"Author of You\'re More Normal Than You Think","sameAs":["https://ahsanrazabooks.gumroad.com/"]}}')
page = head("About the author | You're More Normal Than You Think", "About Ahsan Raza, author of You're More Normal Than You Think, and why he wrote it.", url,
            f'<script type="application/ld+json">{ld}</script>')
page = page.replace('href="../../assets', 'href="../assets').replace("<nav", "<nav", 1)
page += (f'<p class="crumb"><a href="{BASE}">The book</a> / About</p><h1>About the author</h1>' + "".join(f"<p>{p}</p>" for p in paras) +
         f'<div class="btns"><a class="btn btn1" href="{BUY}&utm_source=site&utm_medium=about" rel="noopener">Get the book, $6.99</a><a class="btn btn2" href="{BASE}read/">Read the first chapter free</a></div>' + FORM + FOOT)
open("about/index.html", "w", encoding="utf8").write(page)
sm = open("sitemap.xml", encoding="utf8").read()
if url not in sm:
    open("sitemap.xml", "w", encoding="utf8").write(sm.replace("</urlset>", f"<url><loc>{url}</loc><lastmod>2026-11-15</lastmod></url></urlset>"))
t = open("index.html", encoding="utf8").read()
if "about/" not in t:
    t = t.replace('&copy; Ahsan Raza. English (British).</footer>', '&copy; Ahsan Raza. English (British). <a href="about/">About the author</a></footer>', 1)
    open("index.html", "w", encoding="utf8").write(t)
# ---- shelves menu on the home page ----
t = open("index.html", encoding="utf8").read()
if "class=\"shelves\"" not in t:
    t = t.replace('<div class="nav-r">', '<div class="nav-r">' + tools(), 1)
    DARK = ("--paper:oklch(19% .01 40);--paper-2:oklch(23% .011 40);--cotton:oklch(21% .01 40);--card:oklch(25% .011 40);--ink:oklch(94% .008 70);--ink-2:oklch(88% .009 70);--muted:oklch(72% .012 55);"
            "--rule:oklch(33% .01 45);--rule-2:oklch(40% .01 45);--accent:oklch(72% .13 35);--accent-soft:oklch(30% .04 40);--board:oklch(14% .01 40);--board-type:oklch(95% .006 70);--board-muted:oklch(75% .01 60);--board-rule:oklch(30% .012 45);--shade:0% 0 0;--lit:30% .01 50;")
    t = t.replace("</style>", "@media (prefers-color-scheme:dark){:root:not([data-theme=light]){" + DARK + "color-scheme:dark}:root:not([data-theme=light]) .btn--ink{background:oklch(94% .008 70);color:oklch(19% .01 40)}}:root[data-theme=dark]{" + DARK + "color-scheme:dark}:root[data-theme=dark] .btn--ink{background:oklch(94% .008 70);color:oklch(19% .01 40)}" + "</style>", 1)
    t = t.replace("<head>", "<head>\n<script>try{var t=localStorage.getItem('ymn-theme');if(t)document.documentElement.dataset.theme=t;}catch(e){}</script>", 1)
    t = t.replace('<meta name="author" content="Ahsan Raza">', '<meta name="author" content="Ahsan Raza"><meta name="p:domain_verify" content="8101158ac282d84922c6045962ec95ab"><meta name="keywords" content="self help book, you\'re more normal than you think, worry at night, comparing yourself to others, harsh inner voice, imposter feelings, feeling not normal, ebook, Ahsan Raza"><link rel="alternate" hreflang="en-GB" href="' + BASE + '"><link rel="alternate" hreflang="x-default" href="' + BASE + '"><meta property="og:site_name" content="You\'re More Normal Than You Think"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="675"><meta property="og:image:alt" content="The book You\'re More Normal Than You Think by Ahsan Raza">', 1)
    t = t.replace("</style>", ".nav{position:relative;padding-block:28px 12px}footer.wrap{padding-block:52px 60px}" + MENU_CSS + "</style>", 1)
    t = t.replace("</body>", MENU_JS + "</body>", 1)
    open("index.html", "w", encoding="utf8").write(t)
print("about ok")
