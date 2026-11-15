"""One-off patch of feelings-build.py: theme toggle, responsive nav, extra SEO tags. Run once: python -I patch-theme.py"""
p = "feelings-build.py"
s = open(p, encoding="utf8").read()
def sub(old, new, count=1):
    global s
    assert old in s, old[:60]
    s = s.replace(old, new, count)

# 1. dark theme only when not forced light, and when forced dark
sub("@media (prefers-color-scheme:dark){:root{--bg:#1c1714;--ink:#f1e9e2;--muted:#b3a69d;--rule:#3a312b;--accent:#e0805f;--card:#251f1b}}",
    "@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#1c1714;--ink:#f1e9e2;--muted:#b3a69d;--rule:#3a312b;--accent:#e0805f;--card:#251f1b}}\n"
    ":root[data-theme=dark]{--bg:#1c1714;--ink:#f1e9e2;--muted:#b3a69d;--rule:#3a312b;--accent:#e0805f;--card:#251f1b}")

# 2. short label on phones
sub('<summary>Browse the shelves</summary>', '<summary>Browse<span class="lg"> the shelves</span></summary>')

# 3. toggle and tools wrapper
sub("def menu():", '''TOGGLE = ('<button type="button" class="theme-toggle" aria-label="Switch colour theme" title="Switch colour theme">'
          '<svg class="i-moon" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M21 14.5A9 9 0 0 1 9.5 3a9 9 0 1 0 11.5 11.5z"/></svg>'
          '<svg class="i-sun" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><circle cx="12" cy="12" r="4.2" fill="currentColor"/><g stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/></g></svg></button>')
def tools():
    return '<div class="tools">' + TOGGLE + menu() + '</div>'

def menu():''')
sub('<nav class="wrap"><a href="{BASE}">Ahsan Raza</a>{menu()}</nav>', '<nav class="wrap"><a href="{BASE}">Ahsan Raza</a>{tools()}</nav>')

# 4. JS: toggle logic
sub("MENU_JS = \"\"\"<script>(function(){var d=document.querySelector('.shelves');if(!d)return;",
    "MENU_JS = \"\"\"<script>(function(){var r=document.documentElement,b=document.querySelector('.theme-toggle');function cur(){return r.dataset.theme||(matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light');}function lab(){if(b){var d=cur()==='dark';b.setAttribute('aria-label',d?'Switch to light theme':'Switch to dark theme');b.title=b.getAttribute('aria-label');}}lab();if(b)b.addEventListener('click',function(){var n=cur()==='dark'?'light':'dark';r.dataset.theme=n;try{localStorage.setItem('ymn-theme',n);}catch(e){}lab();});var d=document.querySelector('.shelves');if(!d)return;")

# 5. css for toggle, nav wrap, label
sub("footer.wrap{padding:52px 20px 60px}",
    "footer.wrap{padding:52px 20px 60px}\n"
    ".tools{display:flex;align-items:center;gap:10px}.theme-toggle{width:42px;height:42px;border-radius:999px;border:1px solid var(--rule,#ddd2c9);background:transparent;color:var(--ink,#211a17);cursor:pointer;display:inline-flex;align-items:center;justify-content:center;padding:0}"
    ".theme-toggle:focus-visible{outline:3px solid var(--accent,#b4472a);outline-offset:2px}.theme-toggle .i-sun{display:none}:root[data-theme=dark] .theme-toggle .i-sun{display:block}:root[data-theme=dark] .theme-toggle .i-moon{display:none}"
    "@media (prefers-color-scheme:dark){:root:not([data-theme=light]) .theme-toggle .i-sun{display:block}:root:not([data-theme=light]) .theme-toggle .i-moon{display:none}}"
    "nav.wrap{flex-wrap:wrap;gap:8px}@media (max-width:480px){.shelves summary .lg{display:none}}")

# 6. head: theme init, hreflang, site name, image meta
sub('<title>{E(title)}</title>', "<script>try{{var t=localStorage.getItem('ymn-theme');if(t)document.documentElement.dataset.theme=t;}}catch(e){{}}</script><title>{E(title)}</title>")
sub('<meta name="robots" content="index,follow,max-image-preview:large">',
    '<meta name="robots" content="index,follow,max-image-preview:large"><link rel="alternate" hreflang="en-GB" href="{url}"><link rel="alternate" hreflang="x-default" href="{url}"><meta property="og:site_name" content="You\'re More Normal Than You Think"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="The book You\'re More Normal Than You Think by Ahsan Raza"><meta name="twitter:image" content="{BASE}assets/social.jpg"><meta name="twitter:title" content="{E(title)}"><meta name="twitter:description" content="{E(desc)}">')

# 7. keywords on pages
sub("    extra = f'<script type=\"application/ld+json\">{ld}</script><script type=\"application/ld+json\">{ld2}</script>'",
    "    extra = f'<meta name=\"keywords\" content=\"{E(KW[i-1])}\"><script type=\"application/ld+json\">{ld}</script><script type=\"application/ld+json\">{ld2}</script>'")
sub("N = len(P)\n", '''N = len(P)
KW = [
 "feeling not normal, everyone else has it figured out, comparing yourself to others, social media comparison, self help book",
 "cant stop worrying, worry at night, anxious thoughts at 2am, overthinking, how to stop worrying",
 "how to make a decision, asking everyone for advice, trust yourself, indecision, self help book",
 "life feels grey, seeing your day differently, everyday life, feeling flat, self help book",
 "rejection email, coping with setbacks, bounce back after failure, feeling disappointed, self help book",
 "harsh inner voice, self criticism, why am i so hard on myself, comparing yourself, negative self talk",
 "crying over small things, suppressed feelings, naming emotions, feelings that wait, self help book",
 "imposter feelings, fraud at work, feeling like a fake, new job doubt, waiting to be found out",
 "good days disappear, small good things, noticing positives, gratitude notebook, self help book",
 "reaching out to friends, awkward to message, loneliness, who supports you, friendship",
 "perfectionism, cant finish anything, fear of getting it wrong, finish line moves, procrastination",
 "do people notice my mistakes, spotlight effect, self conscious, feeling watched, social anxiety feelings",
]
''')
open(p, "w", encoding="utf8").write(s)
print("patched")
