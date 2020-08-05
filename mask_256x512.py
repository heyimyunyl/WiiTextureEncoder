from PIL import Image
import os

fnames = os.listdir('INPUT_256x512')
os.makedirs('OUTPUT_256x512', exist_ok=True)

for fname in fnames:
    img = Image.open(f'INPUT_256x512/{fname}')

    # img top
    im2 = img.convert("RGB")
    img_top = im2

    # img bottom
    img_bottom_bg = Image.new('RGBA', size=img.size, color='black')

    px = img.load()
    for x in range(img.width):
        for y in range(img.height):
            px[x, y] = tuple(pixel if index == 3 else 255 for index, pixel in enumerate(px[x, y]))

    img_bottom = Image.alpha_composite(img_bottom_bg, img)

    # img final
    img_final = Image.new(mode='RGBA', size=(img.width, img.height * 2))
    img_final.paste(img_top, box=(0, 0))
    img_final.paste(img_bottom, box=(0, img_top.height))

    # ask size
    size = (256, 512)

    img_final = img_final.resize(size=size)
    img_final.save(f'OUTPUT_256x512/{fname}')
