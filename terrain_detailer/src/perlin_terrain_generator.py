from PIL import Image
from os import path, makedirs
from terrain_detailer.src.terrain import get_index, get_subdivisions, get_points

# These are the colors that will be printed onto the map depending on what color you used on your input file.
# Unless you know what you are doing, I would suggest that you do not touch this code.
mountain = {
    0: (0xb5, 0x6f, 0xb1),
    1: (0xb4, 0x56, 0xb3),
    2: (0xa2, 0x27, 0x53),
    3: (0x7f, 0x18, 0x3c)
}
low_mountain = {
    0: (0x41, 0x34, 0x79),
    1: (0x2d, 0x22, 0x5f),
    2: (0x1a, 0x11, 0x43),
    3: (0x10, 0x0b, 0x29)
}
steppe = {
    0: (0x63, 0x07, 0x0b),
    1: (0x52, 0x04, 0x08),
    2: (0x3e, 0x02, 0x05),
    3: (0x27, 0x00, 0x02),
}
farmland = {
    0: (0x98, 0xd3, 0x83),
    1: (0x86, 0xbf, 0x5c),
    2: (0x6f, 0xa2, 0x39),
    3: (0x56, 0x7c, 0x1b)
}
hills = {
    0: (0xa0, 0xd4, 0xdc),
    1: (0x78, 0xb4, 0xca),
    2: (0x4b, 0x93, 0xae),
    3: (0x2d, 0x77, 0x92)
}
marsh = {
    0: (0x1f, 0x9a, 0x7f),
    1: (0x10, 0x9a, 0x63),
    2: (0x02, 0x5e, 0x4a),
    3: (0x00, 0x49, 0x39)
}
grassland = {
    0: (0xe7, 0x20, 0x37),
    1: (0xb3, 0x0b, 0x1b),
    2: (0x8a, 0x0b, 0x1a),
    3: (0x75, 0x0b, 0x10)
}
conifer_forest = {
    0: (0x40, 0x61, 0x0c),
    1: (0x4c, 0x56, 0x04),
    2: (0x27, 0x42, 0x00),
    3: (0x21, 0x28, 0x00)
}
deciduous_forest = {
    0: (0x25, 0x60, 0x7e),
    1: (0x0f, 0x3f, 0x5a),
    2: (0x0f, 0x29, 0x4e),
    3: (0x02, 0x14, 0x29)
}

# This is the mapping of input file colors to output file colors (there are 4 potential output file colors per terrain).
# Unless you know what you are doing, I would suggest that you do not touch this code.
terrain = {
    (47, 116, 0): farmland,
    (255, 100, 238): mountain,
    (255, 200, 238): low_mountain,
    (170, 116, 0): steppe,
    (79, 150, 210): hills,
    (0, 78, 58): marsh,
    (132, 16, 35): grassland,
    (40, 38, 20): conifer_forest,
    (101, 147, 20): deciduous_forest
}


def generate_terrain(input_file, output_folder, output_file):
    terrain_im = Image.open(input_file)
    pixels = terrain_im.load()
    width, height = terrain_im.size
    subsets = 4
    maximum_size = int(width * height / subsets)
    lst = get_points(width, height)
    sections = get_subdivisions(sorted(lst.values()), maximum_size)

    for row in range(width):
        for col in range(height):
            index = get_index(lst, row - width / 2, col - height / 2, sections)
            try:
                old_color = pixels[row, col]
                if old_color in terrain:
                    color = terrain[old_color][index]
                    terrain_im.putpixel((row, col), color)
            except:
                print(row, col)
                continue

    if not path.exists(output_folder):
        makedirs(output_folder)
    terrain_im.save(f"{output_folder}{output_file}")
