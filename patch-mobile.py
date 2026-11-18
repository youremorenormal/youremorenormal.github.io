"""Phone layout: puts button pairs/groups on fewer rows (shorter labels + small CSS). Idempotent; run from build-site.py."""
import glob, re
TXT = [("Read the first chapter free</a></div>", "Read chapter 1 free</a></div>")]
CSS_INNER = ('<style id="mob-css">@media (max-width:560px){.btns{flex-wrap:nowrap;gap:8px}.btns .btn{flex:1 1 0;min-width:0;text-align:center;padding-inline:10px;white-space:nowrap;font-size:15px}}</style>')
CSS_HOME = ('<style id="mob-css">@media (max-width:560px){.sample .btns{display:grid;grid-template-columns:1fr 1fr;max-width:none}.sample .btns .btn:first-child{grid-column:1/-1}}</style>')
CSS_READ = ('<style id="mob-css">.bar .buy .s{display:none}@media (max-width:560px){.row{display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}.row .buy{grid-column:1/-1;justify-content:center}.row .alt{justify-content:center;padding-inline:4px;white-space:nowrap;font-size:15px}'
            '.bar .in{gap:6px;padding:8px}.bar .in .sp{display:none}.bar .ctl{gap:4px}.bar .ctl button{min-width:34px;min-height:36px;padding:0 8px;font-size:14px}.bar .buy{min-height:36px;padding:0 10px;font-size:14px}.bar .buy .l{display:none}.bar .buy .s{display:inline}}</style>')
n = 0
for p in glob.glob("**/index.html", recursive=True):
    q = p.replace("\\", "/")
    if q == "read/ebook/index.html": continue
    s = o = open(p, encoding="utf8").read()
    css = None
    if q == "index.html":
        s = s.replace(">Open in the ebook reader</a>", ">Ebook reader</a>").replace(">Get the sample (EPUB)</a>", ">Download EPUB</a>"); css = CSS_HOME
    elif q == "read/index.html":
        s = s.replace('rel="noopener">Get the book</a>', 'rel="noopener"><span class="l">Get the book</span><span class="s">Buy</span></a>', 1) if 'class="buy s"' not in s and '<span class="l">' not in s else s
        s = s.replace(">Open in the ebook reader</a>", ">Ebook reader</a>").replace(">Download the sample (PDF)</a>", ">Sample PDF</a>").replace(">Download the sample (EPUB)</a>", ">Sample EPUB</a>"); css = CSS_READ
    elif 'class="btn btn1"' in s:
        for a, b in TXT: s = s.replace(a, b)
        css = CSS_INNER
    s = re.sub(r'<style id="mob-css">.*?</style>', "", s, flags=re.S)
    if css: s = s.replace("</head>", css + "</head>", 1)
    if s != o: open(p, "w", encoding="utf8").write(s); n += 1
print("mobile", n)
