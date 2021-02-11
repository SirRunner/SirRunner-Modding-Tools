# Please read the README in this folder prior to user this tool

from PIL import Image
from random import choice

mountain = {
    0: (0xb5, 0x6f, 0xb1),
    1: (0xb4, 0x56, 0xb3),
    2: (0xa2, 0x27, 0x53),
    3: (0x7f, 0x18, 0x3c)
}
farmland = {
    0: (0x98, 0xd3, 0x83),
    1: (0x86, 0xbf, 0x5c),
    2: (0x6f, 0xa2, 0x39),
    3: (0x56, 0x7c, 0x1b)
}
hills = {}
forest = {}
grassland = {}
marsh = {}

terrain = {
    (47, 116, 0): farmland,
    (255, 100, 238): mountain
}

location = "../../../../Program Files (x86)/Steam/steamapps/common/Victoria 2/mod/LOTR/terrain_generation_test.jpg"
terrain_im = Image.open(location)
pixels = terrain_im.load()
width, height = terrain_im.size
used_colors = set()
for row in range(width):
    for col in range(height):
        try:
            old_color = pixels[row, col]
            color = choice(terrain[old_color])
            terrain_im.putpixel((row, col), color)
            used_colors.add(color)
        except:
            print(row, col)
            continue
print(used_colors)
terrain_im.save("../../../../Program Files (x86)/Steam/steamapps/common/Victoria 2/mod/LOTR/terrain_generation_test.bmp")
