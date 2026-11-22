"""Centre every .btn label (flex needs justify-content) and stop 2-line wrapping on phones. Idempotent."""
import glob, re
_CSS = '<style id="btn-fix">.btn{justify-content:center;text-align:center;white-space:nowrap}@media (max-width:560px){.sample .btns .btn{font-size:15px;padding-inline:8px}}</style>'
_n = 0
for _p in glob.glob("**/index.html", recursive=True):
    _s = _o = open(_p, encoding="utf8").read()
    _s = re.sub(r'<style id="btn-fix">.*?</style>', "", _s, flags=re.S)
    if 'class="btn' in _s or "class='btn" in _s:
        _s = _s.replace("</head>", _CSS + "</head>", 1)
    if _s != _o: open(_p, "w", encoding="utf8").write(_s); _n += 1
print("buttons", _n)
