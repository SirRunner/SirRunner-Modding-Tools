# This code was taken from https://github.com/hnhaefliger/pyTerrain/blob/master/terrain.py
# and adapted to work for a terrain detailer
from terrain_detailer.src.perlin import noise
import math


def get_points(width, length):
    n1div = 30  # landmass distribution
    n2div = 4  # boulder distribution
    n3div = 1  # rock distribution

    n1scale = 20  # landmass height
    n2scale = 40  # boulder scale
    n3scale = 40  # rock scale

    noise1 = noise(width / n1div, length / n1div)  # landmass / mountains
    noise2 = noise(width / n2div, length / n2div)  # boulders
    noise3 = noise(width / n3div, length / n3div)  # rocks

    zroot = 2
    zpower = 2.5

    points = {}
    for x in range(-int(width / 2), int(width / 2)):
        for y in range(-int(length / 2), int(length / 2)):
            x1 = x + width / 2
            y1 = y + length / 2
            z = noise1.perlin(x1 / n1div, y1 / n1div) * n1scale  # add landmass
            z += noise2.perlin(x1 / n2div, y1 / n2div) * n2scale  # add boulders
            z += noise3.perlin(x1 / n3div, y1 / n3div) * n3scale  # add rocks
            if z >= 0:
                z = -math.sqrt(z)
            else:
                z = ((-z) ** (1 / zroot)) ** zpower
            points[x, y] = z

    return points


def divide_chunks(lst, size):
    # looping till length l
    for i in range(0, len(lst), size):
        yield lst[i:i + size]


def get_subdivisions(lst, max_values):
    subdivisions = list(divide_chunks(lst, max_values))
    ret_dict = {}
    i = 0

    for subdivision in subdivisions:
        ret_dict[i] = (subdivision[0], subdivision[len(subdivision) - 1])
        i += 1

    return ret_dict


def get_index(points, x, y, ret_dict):
    value = points[x,y]

    for i in range(len(ret_dict)):
        min, max = ret_dict[i]
        if value >= min and value <= max:
            return i

    raise ValueError(f"Something went wrong: {value}\n{ret_dict}")
