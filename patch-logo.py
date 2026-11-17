"""Replaces the 'Ahsan Raza' text in every page header with a small logo (the lit window from the cover + 'More Normal'). Idempotent; also patches the build scripts."""
import glob, re
SVG = ('<svg class="logo-mark" viewBox="0 0 32 32" width="30" height="30" aria-hidden="true"><rect width="32" height="32" rx="9" fill="currentColor"/>'
       '<g fill="var(--paper,#f8f4f1)" opacity=".34"><rect x="6" y="6" width="8.5" height="8.5" rx="2.2"/><rect x="17.5" y="6" width="8.5" height="8.5" rx="2.2"/><rect x="6" y="17.5" width="8.5" height="8.5" rx="2.2"/></g>'
       '<rect x="17.5" y="17.5" width="8.5" height="8.5" rx="2.2" fill="#f2a23a"/></svg>')
LOGO_INNER = SVG + '<span class="logo-word">More Normal</span>'
CSS = ('<style id="logo-css">.logo{display:inline-flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink,#211a17);white-space:nowrap;line-height:1}'
       '.logo-mark{flex:none;display:block}.logo-word{font:600 21px/1 var(--display,Georgia,serif);letter-spacing:-.012em;position:relative;top:1px}'
       '.logo:hover .logo-word{text-decoration:underline;text-underline-offset:5px;text-decoration-thickness:1px}'
       '.logo:focus-visible{outline:3px solid var(--accent,#b4472a);outline-offset:4px;border-radius:6px}@media (max-width:460px){.logo-word{display:none}.logo-mark{width:32px;height:32px}}</style>')
ARIA = ' aria-label="You\'re More Normal Than You Think, home"'
pats = [(r'<a class="mark" href="#top">Ahsan Raza</a>', f'<a class="mark logo" href="#top"{ARIA}>{LOGO_INNER}</a>'),
        (r'(<nav class="wrap">)<a href="(https://youremorenormal\.com/)">Ahsan Raza</a>', rf'\1<a class="logo" href="\2"{ARIA}>{LOGO_INNER}</a>')]
n = 0
for p in glob.glob("**/index.html", recursive=True):
    s = o = open(p, encoding="utf8").read()
    for a, b in pats: s = re.sub(a, b, s, count=1)
    s = re.sub(r'<svg class="logo-mark".*?</svg><span class="logo-word">.*?</span>', lambda m: LOGO_INNER, s, count=1, flags=re.S)
    s = re.sub(r'<style id="logo-css">.*?</style>', "", s, flags=re.S)
    if "logo-mark" in s: s = s.replace("</head>", CSS + "</head>", 1)
    if s != o: open(p, "w", encoding="utf8").write(s); n += 1
print("pages", n)
for p in ("feelings-build.py", "build-site.py", "guides-build.py", "press-build.py"):
    s = o = open(p, encoding="utf8").read()
    s = s.replace('<a class="mark" href="#top">Ahsan Raza</a>', "<a class=\"mark logo\" href=\"#top\">LOGO</a>") if False else s
    if s != o: open(p, "w", encoding="utf8").write(s)
