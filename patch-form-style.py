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
section#signup:not(.rd-signup){padding:72px 0!important;border-top:1px solid var(--rule,#ddd2c9);background:var(--paper-2,transparent);text-align:center}
.signup .sg{display:block;max-width:560px;margin:0 auto}
.signup .lead{max-width:40ch;margin:12px auto 0}.signup .small{margin-top:14px;font-size:15px;color:var(--muted)}.signup .ml-embedded{margin:26px auto 0;max-width:440px;text-align:left}
.signup .ml-form-embedContent{display:none!important}
@media (max-width:900px){section#signup:not(.rd-signup){padding:48px 0!important}}
section.rd-signup#signup{--card:var(--page,#1f1a15);--paper:var(--bg,#17130f);--rule-2:var(--rule,#3a312a);display:block;text-align:center;margin:40px 0 8px;padding:36px 34px!important;background:var(--page);border:1px solid var(--rule);border-radius:14px}
.rd-signup h2{margin:0 0 10px;font-size:26px;line-height:1.15;color:var(--ink)}.rd-signup p{margin:0 auto 22px;color:var(--ink);font-size:17px;line-height:1.55;max-width:44ch}
.rd-signup .rd-small{margin:20px auto 0;font-size:14px;color:var(--muted)}.rd-signup .rd-small a{color:inherit}
.rd-signup .ml-embedded{margin:0 auto;max-width:440px;text-align:left}.rd-signup .ml-form-embedContent{display:none!important}
.rd-signup .ml-form-embedWrapper{background:transparent!important;border:0!important;box-shadow:none!important;padding:0!important}
.rd-signup .ml-embedded label,.rd-signup .ml-embedded label *,.rd-signup .ml-embedded .label-description,.rd-signup .ml-embedded .label-description *{color:var(--muted)!important}
.rd-signup .ml-embedded input.form-control{background:var(--bg)!important;color:var(--ink)!important}
@media (max-width:700px){section.rd-signup#signup{padding:24px 18px!important}}
html body .ml-embedded input.form-control:not(#a):not(#b){background:var(--paper,#f8f4f1)!important;color:var(--ink,#211a17)!important;border:1px solid var(--rule-2,#c9bdb2)!important}
html body .rd-signup .ml-embedded input.form-control:not(#a):not(#b){background:var(--bg)!important}
html body .rd-signup .ml-embedded .label-description p:not(#a):not(#b),html body .rd-signup .ml-embedded .label-description:not(#a):not(#b){color:var(--muted)!important}
html body .ml-embedded .label-description p:not(#a):not(#b),html body .ml-embedded .label-description:not(#a):not(#b),html body .ml-embedded .ml-form-checkboxRow label:not(#a):not(#b){color:var(--muted,#6b5f58)!important}
section.g-signup{--paper:var(--bg,#f8f4f1);--rule-2:var(--rule,#ddd2c9);display:block;margin:48px 0 0;padding:34px 30px;text-align:center;background:var(--card,#fffdfa);border:1px solid var(--rule,#ddd2c9);border-radius:14px}
.g-signup h2{margin:0 0 10px;font:600 26px/1.15 var(--display,Georgia,serif);color:var(--ink,#211a17)}
.g-signup>p{margin:0 auto 22px;max-width:44ch;color:var(--ink,#211a17);font-size:17px;line-height:1.55}
.g-signup .g-small{margin:18px auto 0;font-size:14px;color:var(--muted,#6b5f58)}.g-signup .g-small a{color:inherit}
.g-signup .ml-embedded{margin:0 auto;max-width:440px;text-align:left}.g-signup .ml-form-embedContent{display:none!important}
.g-signup .ml-embedded .ml-form-embedWrapper{background:transparent!important;border:0!important;box-shadow:none!important;padding:0!important}
html body .g-signup .ml-embedded input.form-control:not(#a):not(#b){background:var(--bg,#f8f4f1)!important}
@media (max-width:640px){section.g-signup{padding:26px 18px}}
</style>"""
import glob
for p in [f for f in glob.glob("**/index.html", recursive=True) if 'class="ml-embedded"' in open(f, encoding="utf8").read()]:
    s = open(p, encoding="utf8").read()
    import re
    n = re.sub(r'<style id="ml-css">.*?</style>', "", s, flags=re.S).replace("</head>", CSS + "</head>", 1)
    if n != s: open(p, "w", encoding="utf8").write(n); print("styled", p)
