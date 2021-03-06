# These are the colors that will be printed onto the map depending on what color you used on your input file.
# Unless you know what you are doing, I would suggest that you do not touch this code.
arctic = {
    0: (0xd2, 0xd2, 0xd2),  # 1
    1: (0xb0, 0xb0, 0xb0),  # 2
    2: (0x8c, 0x8c, 0x8c),  # 3
    3: (0x70, 0x70, 0x70)   # 4
}
farmland = {
    0: (0x98, 0xd3, 0x83),  # 8
    1: (0x86, 0xbf, 0x5c),  # 9
    2: (0x6f, 0xa2, 0x39),  # 10
    3: (0x56, 0x7c, 0x1b)   # 11
}
conifer_forest = {
    0: (0x40, 0x61, 0x0c),  # 12
    1: (0x4c, 0x56, 0x04),  # 13
    2: (0x27, 0x42, 0x00),  # 14
    3: (0x21, 0x28, 0x00)   # 15
}
hills = {
    0: (0xa0, 0xd4, 0xdc),  # 16
    1: (0x78, 0xb4, 0xca),  # 17
    2: (0x4b, 0x93, 0xae),  # 18
    3: (0x2d, 0x77, 0x92)   # 19
}
deciduous_forest = {
    0: (0x25, 0x60, 0x7e),  # 20
    1: (0x0f, 0x3f, 0x5a),  # 21
    2: (0x0f, 0x29, 0x4e),  # 22
    3: (0x02, 0x14, 0x29)   # 23
}
mountain = {
    0: (0xb5, 0x6f, 0xb1),  # 26
    1: (0xb4, 0x56, 0xb3),  # 27
    2: (0xa2, 0x27, 0x53),  # 30
    3: (0x7f, 0x18, 0x3c)   # 31
}
low_mountain = {
    0: (0x41, 0x34, 0x79),  # 60
    1: (0x2d, 0x22, 0x5f),  # 61
    2: (0x1a, 0x11, 0x43),  # 62
    3: (0x10, 0x0b, 0x29)   # 63
}
grassland = {
    0: (0xe7, 0x20, 0x37),  # 32
    1: (0xb3, 0x0b, 0x1b),  # 33
    2: (0x8a, 0x0b, 0x1a),  # 34
    3: (0x75, 0x0b, 0x10)   # 35
}
steppe = {
    0: (0x63, 0x07, 0x0b),  # 36
    1: (0x52, 0x04, 0x08),  # 37
    2: (0x3e, 0x02, 0x05),  # 38
    3: (0x27, 0x00, 0x02)   # 39
}
jungle = {
    0: (0x76, 0xf5, 0xd9),  # 40
    1: (0xd1, 0xdc, 0xc1),  # 41
    2: (0x38, 0xc7, 0xa7),  # 42
    3: (0x30, 0xaf, 0x93)   # 43
}
marsh = {
    0: (0x1f, 0x9a, 0x7f),  # 44
    1: (0x10, 0x9a, 0x63),  # 45
    2: (0x02, 0x5e, 0x4a),  # 46
    3: (0x00, 0x49, 0x39)   # 47
}
desert = {
    0: (0xf1, 0xd2, 0x97),  # 48
    1: (0xe1, 0xc0, 0x82),  # 49
    2: (0xce, 0xa9, 0x63),  # 50
    3: (0xae, 0x88, 0x43)   # 51
}
coastal_desert = {
    0: (0x96, 0x71, 0x29),  # 52
    1: (0x7b, 0x5a, 0x1b),  # 53
    2: (0x65, 0x47, 0x07),  # 54
    3: (0x49, 0x32, 0x06)   # 55
}


# This is the mapping of input file colors to output file colors (there are 4 potential output file colors per terrain).
# Unless you know what you are doing, I would suggest that you do not touch this code.
terrain = {
    (): arctic,  # Add in arctic color
    (47, 116, 0): farmland,
    (40, 38, 20): conifer_forest,
    (79, 150, 210): hills,
    (101, 147, 20): deciduous_forest,
    (255, 100, 238): mountain,
    (255, 200, 238): low_mountain,
    (132, 16, 35): grassland,
    (170, 116, 0): steppe,
    (): jungle,
    (0, 78, 58): marsh,
    (): desert,
    (): coastal_desert
}