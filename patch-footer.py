"""Replaces the one-line footer on every page (home, read, about, press, privacy, feelings, guides) with a centred site footer. Idempotent; run from build-site.py."""
import glob, re
B = "https://youremorenormal.com/"
SVG = ('<svg class="sf-mark" viewBox="0 0 32 32" width="32" height="32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="currentColor"/>'
       '<g fill="var(--paper,var(--bg,#f8f4f1))" opacity=".34"><rect x="6" y="6" width="8.5" height="8.5" rx="2.2"/><rect x="17.5" y="6" width="8.5" height="8.5" rx="2.2"/><rect x="6" y="17.5" width="8.5" height="8.5" rx="2.2"/></g>'
       '<rect x="17.5" y="17.5" width="8.5" height="8.5" rx="2.2" fill="#f2a23a"/></svg>')
LINKS = [("Read chapter 1 free", "read/"), ("Ebook reader", "read/ebook/"), ("All twelve feelings", "feelings/"), ("Guides", "guides/"),
         ("About the author", "about/"), ("For reviewers and podcast hosts", "press/"), ("Privacy", "privacy/")]
nav = "".join(f'<a href="{B}{u}">{t}</a>' for t, u in LINKS) + '<a href="mailto:hello@youremorenormal.com">Contact</a>'
FOOT = ('<footer class="site-foot"><div class="sf-in">'
        f'<a class="sf-brand" href="{B}" aria-label="You\'re More Normal Than You Think, home">{SVG}<span>You&rsquo;re More Normal Than You Think</span></a>'
        '<p class="sf-tag">Twelve feelings almost everyone has, and what to do about them.</p>'
        f'<a class="sf-cta" href="https://ahsanrazabooks.gumroad.com/l/sdpapr?wanted=true&amp;utm_source=site&amp;utm_medium=footer" rel="noopener">Get the book</a>'
        f'<nav class="sf-nav" aria-label="Footer">{nav}</nav>'
        '<p class="sf-legal">&copy; 2026 Ahsan Raza &middot; English (British)</p></div></footer>')
CSS = ('<style id="foot-css">footer.site-foot{max-width:none!important;margin:0!important;padding:60px 20px 104px!important;border-top:1px solid var(--rule,#ddd2c9);text-align:center;color:var(--muted,#6b5f58);font:400 15px/1.5 var(--body,system-ui,sans-serif)!important}'
       '.sf-in{max-width:760px;margin:0 auto}.sf-brand{display:inline-flex;align-items:center;gap:11px;text-decoration:none;color:var(--ink,#211a17);font:600 21px/1 var(--display,Georgia,serif);letter-spacing:-.01em}'
       '.sf-mark{flex:none;display:block}.sf-tag{margin:14px auto 22px;max-width:36ch;font-size:16px;color:var(--muted,#6b5f58)}'
       '.sf-cta{display:inline-block;padding:12px 26px;border-radius:999px;background:var(--ink,#211a17);color:var(--bg,var(--paper,#f8f4f1))!important;font:600 15px var(--body,system-ui,sans-serif);text-decoration:none}'
       '.sf-cta:hover{opacity:.88}.sf-nav{display:flex;flex-wrap:wrap;justify-content:center;gap:10px 26px;margin:34px auto 0;padding-top:28px;border-top:1px solid var(--rule,#ddd2c9);max-width:660px}'
       '.sf-nav a{color:var(--ink,#211a17);text-decoration:none;font-weight:500;font-size:15px}.sf-nav a:hover{text-decoration:underline;text-underline-offset:4px}'
       'footer.site-foot a:focus-visible{outline:3px solid var(--accent,#b4472a);outline-offset:3px;border-radius:6px}.sf-legal{margin:28px 0 0;font-size:13.5px}'
       '@media (max-width:560px){footer.site-foot{padding:48px 20px 108px!important}.sf-nav{gap:10px 20px}}</style>')
n = 0
for p in glob.glob("**/index.html", recursive=True):
    if p.replace("\\", "/") == "read/ebook/index.html": continue
    s = o = open(p, encoding="utf8").read()
    s = re.sub(r'<footer[^>]*>.*?</footer>', lambda m: FOOT, s, count=1, flags=re.S)
    s = re.sub(r'<style id="foot-css">.*?</style>', "", s, flags=re.S)
    if "site-foot" in s: s = s.replace("</head>", CSS + "</head>", 1)
    if s != o: open(p, "w", encoding="utf8").write(s); n += 1
print("footers", n)
