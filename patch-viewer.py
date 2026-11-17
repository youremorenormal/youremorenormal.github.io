p="index.html"; s=open(p,encoding="utf8").read()
a='<a class="btn btn--paper" href="sample/Youre-More-Normal-Than-You-Think-free-sample.pdf">Open the sample (PDF)</a>'
if a in s:
    s=s.replace(a,'<a class="btn btn--paper" href="read/ebook/">Open in the ebook reader</a>')
    s=s.replace('<p class="small">No sign-up. No checkout.</p>','<p class="small">No sign-up. No checkout. <a href="sample/Youre-More-Normal-Than-You-Think-free-sample.pdf">PDF version</a>.</p>',1)
    open(p,"w",encoding="utf8").write(s); print("home patched")
p="read/index.html"; s=open(p,encoding="utf8").read()
i=s.find("Download the sample (PDF)"); print(s[max(0,i-260):i+40])
