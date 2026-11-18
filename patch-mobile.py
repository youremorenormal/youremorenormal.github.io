"""Phone layout: puts button pairs/groups on fewer rows (shorter labels + small CSS). Idempotent; run from build-site.py."""
import glob, re
TXT = [("Read the first chapter free</a></div>", "Read chapter 1 free</a></div>")]
CSS_INNER = ('<style id="mob-css">@media (max-width:560px){.btns{flex-wrap:nowrap;gap:8px}.btns .btn{flex:1 1 0;min-width:0;text-align:center;padding-inline:10px;white-space:nowrap;font-size:15px}}</style>')
CSS_HOME = ('<style id="mob-css">@media (max-width:560px){.sample .btns{display:grid;grid-template-columns:1fr 1fr;max-width:none}.sample .btns .btn:first-child{grid-column:1/-1}}</style>')
CSS_READ = ('<style id="mob-css">@media (max-width:560px){.row{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}.row .buy{grid-column:1/-1;text-align:center}.row .alt{text-align:center;padding-inline:6px;white-space:nowrap}}</style>')
n = 0
for p in glob.glob("**/index.html", recursive=True):
    q = p.replace("\\", "/")
    if q == "read/ebook/index.html": continue
    s = o = open(p, encoding="utf8").read()
    css = None
    if q == "index.html":
        s = s.replace(">Open in the ebook reader</a>", ">Ebook reader</a>").replace(">Get the sample (EPUB)</a>", ">Download EPUB</a>"); css = CSS_HOME
    elif q == "read/index.html":
        s = s.replace(">Open in the ebook reader</a>", ">Ebook reader</a>").replace(">Download the sample (PDF)</a>", ">Sample PDF</a>").replace(">Download the sample (EPUB)</a>", ">Sample EPUB</a>"); css = CSS_READ
    elif 'class="btn btn1"' in s:
        for a, b in TXT: s = s.replace(a, b)
        css = CSS_INNER
    s = re.sub(r'<style id="mob-css">.*?</style>', "", s, flags=re.S)
    if css: s = s.replace("</head>", css + "</head>", 1)
    if s != o: open(p, "w", encoding="utf8").write(s); n += 1
print("mobile", n)
