from PIL import Image
from os import path, makedirs
from terrain_detailer.src.terrain import get_index, get_subdivisions, get_points
from terrain_detailer.src.terrain_colors import terrain


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
                print((row, col), "caused an issue")
                continue

    if not path.exists(output_folder):
        makedirs(output_folder)
    terrain_im.save(f"{output_folder}/{output_file}")
