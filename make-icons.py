"""One-off: draws the favicon set (navy square, lit orange window with a small figure) into assets/."""
from PIL import Image, ImageDraw
S = 1024
im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
d.rounded_rectangle((0, 0, S - 1, S - 1), radius=200, fill=(15, 27, 51))
d.rounded_rectangle((250, 190, 774, 834), radius=40, fill=(244, 164, 61))
d.line((512, 190, 512, 834), fill=(15, 27, 51), width=26); d.line((250, 512, 774, 512), fill=(15, 27, 51), width=26)
d.ellipse((420, 590, 604, 774), fill=(15, 27, 51)); d.pieslice((360, 700, 664, 1004), 180, 360, fill=(15, 27, 51))
for n, sz in (("favicon-48.png", 48), ("favicon-192.png", 192), ("apple-touch-icon.png", 180), ("icon-512.png", 512)):
    im.resize((sz, sz), Image.LANCZOS).save("assets/" + n)
im.resize((256, 256), Image.LANCZOS).save("assets/favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
