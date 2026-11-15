"""One-off: replaces the shelves dropdown (menu() and its CSS) in feelings-build.py with a calmer two-column index."""
p = "feelings-build.py"
L = open(p, encoding="utf8").read().split("\n")
start = next(i for i, l in enumerate(L) if l.startswith("def menu():"))
end = next(i for i, l in enumerate(L) if l.startswith(".cat{display:inline-block"))
new = '''def menu():
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
"""'''.split("\n")
L[start:end] = new
open(p, "w", encoding="utf8").write("\n".join(L))
print("ok", start, end)
