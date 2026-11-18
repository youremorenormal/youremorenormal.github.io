"""One-off, safe to re-run: adds the MailerLite form + privacy page. Works on built files (build-site.py is not re-runnable)."""
import re
UNI = ("<!-- MailerLite Universal -->\n<script>\n(function(w,d,e,u,f,l,n){w[f]=w[f]||function(){(w[f].q=w[f].q||[])\n"
       ".push(arguments);},l=d.createElement(e),l.async=1,l.src=u,\nn=d.getElementsByTagName(e)[0],n.parentNode.insertBefore(l,n);})\n"
       "(window,document,'script','https://assets.mailerlite.com/js/universal.js','ml');\nml('account', '2803635');\n</script>\n<!-- End MailerLite Universal -->\n")
FORM = '<div class="ml-embedded" data-form="j1marl"></div>'
def edit(path, fn):
    s = open(path, encoding="utf8").read(); t = fn(s)
    if t != s: open(path, "w", encoding="utf8").write(t); print("patched", path)

def home(s):
    if 'id="signup"' in s: return s
    if "universal.js" not in s: s = s.replace("</head>", UNI + "</head>", 1)
    # drop the earlier in-section form (it stretched the sample section)
    s = re.sub(r'\s*(?:<h3 style="margin:28px 0 8px;font-size:20px">[^<]*</h3>|<div style="height:22px"></div>)\s*<div class="ml-embedded" data-form="j1marl"></div>\s*<p class="small">Email goes through MailerLite\. <a href="privacy/">Privacy note</a>\.</p>', "", s, count=1)
    band = ('<section class="signup" id="signup"><div class="wrap"><div class="sg"><div><p class="eyebrow">By email</p>'
            '<h2 style="margin-top:14px">Take the first chapter with you</h2>'
            '<p class="lead">Leave your email and the first chapter arrives in your inbox, with new guides when they are published. No spam.</p>'
            '<p class="small">Email goes through MailerLite. <a href="privacy/">Privacy note</a>.</p></div>' + FORM + '</div></div></section>')
    k = s.index('<section class="sample"'); e = s.index("</section>", k) + len("</section>")
    return s[:e] + band + s[e:]
def read(s):
    if "ml-embedded" in s: return s
    s = s.replace("</head>", UNI + "</head>", 1)
    blk = ('<section style="max-width:680px;margin:48px auto 0;padding:0 16px"><h2 style="font-size:24px">Want more like this?</h2>' + FORM +
           '<p style="font-size:15px">Email goes through MailerLite. <a href="../privacy/">Privacy note</a>.</p></section>')
    return s.replace("</main>", blk + "</main>", 1)
edit("index.html", home); edit("read/index.html", read)

# footer link to /privacy/ on top-level pages
for p, pre in (("index.html", ""), ("read/index.html", "../"), ("about/index.html", "../"), ("press/index.html", "../")):
    def f(s, pre=pre):
        if "privacy/" in s.split("<footer")[-1]: return s
        return re.sub(r'(For reviewers and podcast hosts</a>)(</footer>)', r'\1 &middot; <a href="%sprivacy/">Privacy</a>\2' % pre, s, 1)
    edit(p, f)

# privacy page, cloned from /press/ so head, nav, footer and theme script match
s = open("press/index.html", encoding="utf8").read()
i = s.index('<div class="press">'); j = s.index("</div></main>") + len("</div>")
T = "Privacy note | Ahsan Raza"; D = "What this site and the free first chapter email collect, who handles it, and how to be removed. Short and plain."
head = s[:i].replace("/press/", "/privacy/").replace("For reviewers and podcast hosts | Ahsan Raza", T)
head = re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*', lambda m: m.group(1) + D, head)
head = re.sub(r'<script type="application/ld\+json">.*?</script>', "", head, flags=re.S)
head = re.sub(r"<style>\.pbook.*?</style>", "", head, flags=re.S)
body = ('<div class="press"><p class="crumb"><a href="https://youremorenormal.com/">The book</a> / Privacy note</p><h1>Privacy note</h1>'
 '<p class="lede">Short version: this site does not track you. The only personal thing it ever collects is an email address, and only if you type one into the form.</p>'
 '<h2>The website</h2><p>The pages are plain static files. There are no analytics, advertising or tracking scripts. Your browser may remember your light or dark choice on your own device. Nothing about that is sent to me.</p>'
 '<h2>The free first chapter email</h2><p>If you use the form, I receive your email address (and your first name if you give it). It is used to send you the free first chapter, plus new guides when they are published. You confirm by email first, and every email has an unsubscribe link. The form and the emails are handled by <a href="https://www.mailerlite.com/legal/privacy-policy" rel="noopener">MailerLite</a>, which loads its own script on the pages where the form appears. I do not sell or share the list.</p>'
 '<h2>Buying the book</h2><p>Purchases are handled by Gumroad or the store you buy from. I do not see your card details.</p>'
 '<h2>Removing your details</h2><p>Use the unsubscribe link in any email, or write to <a href="mailto:hello@youremorenormal.com">hello@youremorenormal.com</a> and I will delete your address.</p></div>')
page = head + body + s[j:]
import os; os.makedirs("privacy", exist_ok=True)
open("privacy/index.html", "w", encoding="utf8").write(page)
sm = open("sitemap.xml", encoding="utf8").read(); u = "https://youremorenormal.com/privacy/"
if u not in sm: open("sitemap.xml", "w", encoding="utf8").write(sm.replace("</urlset>", f"<url><loc>{u}</loc><lastmod>2026-11-18</lastmod></url></urlset>"))
print("ok")
