#!/usr/bin/env python3

from PIL import Image

card = Image.new("RGBA", (120, 120), (255, 255, 255))
img = Image.open("gp.png").convert("RGBA")
x, y = img.size
card.paste(img, (0, 0, x, y), img)
card.save("test.png", format="png")

card = Image.new("RGBA", (120, 120), (255, 255, 255))
img = Image.open("sechseck.jpg").convert("RGBA")
x, y = img.size
card.paste(img, (0, 0, x, y), img)
card.save("test2.png", format="png")
