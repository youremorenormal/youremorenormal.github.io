"""Idempotent: home 'Open the sample (PDF)' -> ebook reader button; /read/ link; sitemap entry for /read/ebook/."""
p = "index.html"; s = open(p, encoding="utf8").read()
a = '<a class="btn btn--paper" href="sample/Youre-More-Normal-Than-You-Think-free-sample.pdf">Open the sample (PDF)</a>'
if a in s:
    s = s.replace(a, '<a class="btn btn--paper" href="read/ebook/">Open in the ebook reader</a>')
    s = s.replace('<p class="small">No sign-up. No checkout.</p>', '<p class="small">No sign-up. No checkout. <a href="sample/Youre-More-Normal-Than-You-Think-free-sample.pdf">PDF version</a>.</p>', 1)
    open(p, "w", encoding="utf8").write(s)
p = "read/index.html"; s = open(p, encoding="utf8").read()
b = '<a class="alt" href="../sample/Youre-More-Normal-Than-You-Think-free-sample.pdf">Download the sample (PDF)</a>'
if b in s and "ebook/" not in s:
    open(p, "w", encoding="utf8").write(s.replace(b, '<a class="alt" href="ebook/">Open in the ebook reader</a>\n      ' + b, 1))
sm = open("sitemap.xml", encoding="utf8").read(); u = "https://youremorenormal.com/read/ebook/"
if u not in sm:
    open("sitemap.xml", "w", encoding="utf8").write(sm.replace("</urlset>", f"<url><loc>{u}</loc><lastmod>2026-11-18</lastmod></url></urlset>"))
