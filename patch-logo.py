"""Replaces the 'Ahsan Raza' text in every page header with a small logo (the lit window from the cover + 'More Normal'). Idempotent; also patches the build scripts."""
import glob, re
SVG = ('<svg class="logo-mark" viewBox="0 0 32 32" width="30" height="30" aria-hidden="true"><rect width="32" height="32" rx="8" fill="currentColor"/>'
       '<g fill="var(--paper,#f8f4f1)" opacity=".38"><rect x="5.5" y="5.5" width="9" height="9" rx="2"/><rect x="17.5" y="5.5" width="9" height="9" rx="2"/><rect x="5.5" y="17.5" width="9" height="9" rx="2"/></g>'
       '<rect x="17.5" y="17.5" width="9" height="9" rx="2" fill="#f2a23a"/><circle cx="22" cy="20.6" r="1.5" fill="#2a1d10"/><path d="M19.4 26.5v-1.4a2.6 2.6 0 0 1 5.2 0v1.4z" fill="#2a1d10"/></svg>')
LOGO_INNER = SVG + '<span class="logo-word">More Normal</span>'
CSS = ('<style id="logo-css">.logo{display:inline-flex;align-items:center;gap:9px;text-decoration:none;color:var(--ink,#211a17);white-space:nowrap}'
       '.logo-mark{flex:none;display:block}.logo-word{font:600 18px/1 var(--display,Georgia,serif);letter-spacing:-.01em}'
       '.logo:hover .logo-word{text-decoration:underline;text-underline-offset:4px;text-decoration-thickness:1px}'
       '.logo:focus-visible{outline:3px solid var(--accent,#b4472a);outline-offset:4px;border-radius:6px}</style>')
ARIA = ' aria-label="You\'re More Normal Than You Think, home"'
pats = [(r'<a class="mark" href="#top">Ahsan Raza</a>', f'<a class="mark logo" href="#top"{ARIA}>{LOGO_INNER}</a>'),
        (r'(<nav class="wrap">)<a href="(https://youremorenormal\.com/)">Ahsan Raza</a>', rf'\1<a class="logo" href="\2"{ARIA}>{LOGO_INNER}</a>')]
n = 0
for p in glob.glob("**/index.html", recursive=True):
    s = o = open(p, encoding="utf8").read()
    for a, b in pats: s = re.sub(a, b, s, count=1)
    if "logo-mark" in s and 'id="logo-css"' not in s: s = s.replace("</head>", CSS + "</head>", 1)
    if s != o: open(p, "w", encoding="utf8").write(s); n += 1
print("pages", n)
for p in ("feelings-build.py", "build-site.py", "guides-build.py", "press-build.py"):
    s = o = open(p, encoding="utf8").read()
    s = s.replace('<a class="mark" href="#top">Ahsan Raza</a>', "<a class=\"mark logo\" href=\"#top\">LOGO</a>") if False else s
    if s != o: open(p, "w", encoding="utf8").write(s)
