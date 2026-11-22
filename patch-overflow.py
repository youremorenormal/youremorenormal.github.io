"""Stop the closed Browse mega menu from widening the page on phones (some guides scrolled sideways at 390px). Idempotent."""
import glob, re
_CSS = '<style id="ovf-fix">html,body{overflow-x:clip}@media (max-width:560px){.mega{box-sizing:border-box;max-width:calc(100vw - 24px)}.shelf li a b{white-space:normal}}</style>'
_n = 0
for _p in glob.glob("**/index.html", recursive=True):
    _s = _o = open(_p, encoding="utf8").read()
    _s = re.sub(r'<style id="ovf-fix">.*?</style>', "", _s, flags=re.S)
    if "</head>" in _s:
        _s = _s.replace("</head>", _CSS + "</head>", 1)
    if _s != _o: open(_p, "w", encoding="utf8").write(_s); _n += 1
print("overflow", _n)
