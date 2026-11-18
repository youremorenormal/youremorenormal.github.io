"""Centres the five 'How it works' steps (number, title, text and connector) under the centred section header. Idempotent."""
import re
CSS = ('<style id="steps-css">.steps li{text-align:center}.steps li::before{left:50%;transform:translateX(-50%)}'
       '.steps li::after{left:calc(50% + 28px);right:calc(-50% + 8px)}'
       '@media (max-width:900px){.steps li{padding:56px 0 0!important;min-height:0!important}.steps li::after{display:none!important}}</style>')
s = open("index.html", encoding="utf8").read()
n = re.sub(r'<style id="steps-css">.*?</style>', "", s, flags=re.S).replace("</head>", CSS + "</head>", 1)
if n != s: open("index.html", "w", encoding="utf8").write(n); print("steps centred")
