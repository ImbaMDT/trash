#!/usr/bin/env python3

from PIL import Image

# Open overlay image
img = Image.open('test.png')
img_w, img_h = img.size


background = Image.open('test2.png')
bg_w, bg_h = background.size
background.paste(img, img)
background.save('result.png')
background.show()
