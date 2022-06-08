from PIL import Image, ImageDraw

im = Image.open('Gangplank.png')

# I'm creating a random shape here
mask = Image.new('RGBA', im.size)
d = ImageDraw.Draw(mask)
d.polygon(((30, 10), (0, 60),(30, 110), (90, 110), (120,60), (90, 10)), fill='#000')

out = Image.new('RGBA', im.size)
out.paste(im, (0, 0), mask)
out.show()
