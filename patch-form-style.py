"""Restyles the MailerLite embed (classes from MailerLite's own markup) to the site theme. Idempotent."""
CSS = """<style id="ml-css">
.ml-embedded{margin:14px 0 0;max-width:420px}
.ml-embedded .ml-form-embedContainer,.ml-embedded .ml-form-embedWrapper,.ml-embedded .ml-form-embedBody,.ml-embedded .ml-form-successBody{background:transparent!important;border:0!important;box-shadow:none!important;padding:0!important;margin:0!important;width:100%!important;max-width:none!important}
.ml-embedded .ml-form-embedWrapper{background:var(--card,#fffdfa)!important;border:1px solid var(--rule,#ddd2c9)!important;border-radius:14px!important;padding:22px 22px 20px!important;box-shadow:0 16px 36px -26px rgba(0,0,0,.45)!important}
.ml-embedded h4{font:600 24px/1.15 var(--display,Georgia,serif)!important;color:var(--ink,#211a17)!important;margin:0 0 8px!important;letter-spacing:-.01em}
.ml-embedded p,.ml-embedded .label-description,.ml-embedded .label-description p,.ml-embedded label{font:400 15px/1.5 var(--body,system-ui,sans-serif)!important;color:var(--muted,#6b5f58)!important}
.ml-embedded .ml-form-embedContent{margin:0 0 14px!important}
.ml-embedded input.form-control{height:46px!important;border:1px solid var(--rule-2,#c9bdb2)!important;border-radius:10px!important;background:var(--paper,#f8f4f1)!important;color:var(--ink,#211a17)!important;font:500 16px var(--body,system-ui,sans-serif)!important;padding:0 14px!important;box-shadow:none!important}
.ml-embedded input.form-control::placeholder{color:var(--muted,#6b5f58)!important;opacity:.85}
.ml-embedded input.form-control:focus{outline:3px solid var(--accent,#b4472a)!important;outline-offset:1px;border-color:var(--accent,#b4472a)!important}
.ml-embedded .ml-form-checkboxRow{margin:12px 0 4px!important}
.ml-embedded .ml-form-checkboxRow label.checkbox{display:flex!important;gap:10px;align-items:flex-start}
.ml-embedded .label-description,.ml-embedded .label-description p{font-size:13.5px!important;line-height:1.45!important}
.ml-embedded .ml-form-recaptcha{margin:12px 0 4px!important;transform-origin:0 0}
.ml-embedded .ml-form-embedSubmit{margin:14px 0 0!important}
.ml-embedded button.primary{width:100%!important;height:48px!important;border:0!important;border-radius:999px!important;background:var(--ink,#211a17)!important;color:var(--paper,#f8f4f1)!important;font:600 16px var(--body,system-ui,sans-serif)!important;cursor:pointer;transition:transform .15s,opacity .15s}
.ml-embedded button.primary:hover{opacity:.88;transform:translateY(-1px)}
.ml-embedded button.primary:focus-visible{outline:3px solid var(--accent,#b4472a);outline-offset:3px}
.ml-embedded .ml-error input.form-control{border-color:#c0392b!important}
.ml-embedded .ml-form-successContent h4{margin-bottom:6px!important}
@media (max-width:380px){.ml-embedded .ml-form-recaptcha{transform:scale(.88)}}
section#signup{padding:64px 0!important;border-top:1px solid var(--rule,#ddd2c9)}
.signup .sg{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,420px);gap:56px;align-items:center}
.signup .lead{max-width:34ch}.signup .small{margin-top:16px;font-size:15px;color:var(--muted)}.signup .ml-embedded{margin:0;max-width:none}
.signup .ml-form-embedContent{display:none!important}
@media (max-width:900px){section#signup{padding:44px 0!important}.signup .sg{grid-template-columns:minmax(0,1fr);gap:24px}.signup .ml-embedded{max-width:440px}}
</style>"""
for p in ("index.html", "read/index.html"):
    s = open(p, encoding="utf8").read()
    import re
    n = re.sub(r'<style id="ml-css">.*?</style>', "", s, flags=re.S).replace("</head>", CSS + "</head>", 1)
    if n != s: open(p, "w", encoding="utf8").write(n); print("styled", p)
