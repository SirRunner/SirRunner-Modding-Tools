from csv import DictReader


def get_provinces(definition_file):
    internal_provinces = {}

    with open(definition_file, "r", encoding="ANSI") as definitions:
        reader = DictReader(definitions, delimiter=";")

        for row in reader:
            internal_provinces[row['province']] = row['name']

    return internal_provinces


def get_regions(region_file):
    regions = {}

    with open(region_file, "r") as f:
        for line in f.readlines():
            if line != "\n":
                split_line = line.split()
                region_provinces = []
                backend_name = ""
                front_end_name = ""
                frontend_name_parts = []
                in_region = False
                found_backend_name = False
                found_hashtag = False

                if not split_line[0][0:3] == "OTH":
                    for part in split_line:
                        if not found_backend_name:
                            backend_name = part
                            found_backend_name = True
                        elif part == "=":
                            pass
                        elif not in_region and part == "{":
                            in_region = True
                        elif in_region and part == "}":
                            in_region = False
                        elif in_region:
                            region_provinces.append(part)
                        elif part == "#":
                            found_hashtag = True
                        elif found_hashtag:
                            frontend_name_parts.append(part)
                        else:
                            print(f"WTF. {part} from line {line} made it to the else")

                for part in frontend_name_parts:
                    front_end_name += f"{part} "
                front_end_name = front_end_name.strip()

                regions[backend_name] = [front_end_name, region_provinces]
    return regions
