"""Rebuild the guides after adding or editing Work/guides/publish/*.md.  Run from Work/site:  python rebuild-guides.py
Why not build-site.py / feelings-build.py: they are not re-runnable once index.html has been patched (assert fails).
This loads only the shared helpers (head, FOOT, FORM, buy, P ...: feelings-build.py up to the line starting 'os.makedirs("feelings"'),
runs guides-build.py (guide pages, hub, sitemap guide entries, 'Guides on this feeling' blocks), then re-applies every patch-*.py
in build-site.py's order. All of it is idempotent. Each guide .md may carry 'Published: YYYY-MM-DD' in its header (default 2026-11-16)."""
import os, re, html, glob as _g
_home = open("index.html", "rb").read()  # a non-glob patch reorders its <style> blocks; restore at the end
_src = open("feelings-build.py", encoding="utf8").read()
exec(_src[:_src.index('os.makedirs("feelings"')])
exec(open("guides-build.py", encoding="utf8").read())
# Patch only guide pages: re-patching old pages reorders their <style> blocks (harmless but noisy diffs).
_real_glob = _g.glob
_g.glob = lambda pat, *a, **k: [x for x in _real_glob(pat, *a, **k) if x.replace("\\", "/").startswith("guides/")]
for _p in ("patch-viewer.py", "patch-form.py", "patch-form-style.py", "patch-logo.py", "patch-steps.py", "patch-nav.py", "patch-mobile.py", "patch-footer.py", "patch-buttons.py", "patch-overflow.py"):
    exec(open(_p, encoding="utf8").read())
open("index.html", "wb").write(_home)
