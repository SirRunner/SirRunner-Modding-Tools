from os import path, walk, remove
from unidecode import unidecode
from csv import DictReader
from history_file_functions.src.map_files import get_provinces, get_regions
from history_file_functions.src.localisation import localize

continent_to_province = {}
climate_to_province = {}

def process_line(row, provinces, full_path):
    prov_id = row.pop('id')
    name = unidecode(row.pop('name'))
    provinces[prov_id] = name

    with open(f"{full_path}/{prov_id} - {name}.txt", "w") as f:
        if 'comment' in row:
            comment = row.pop('comment')
            if comment:
                f.write(f"# {comment}\n")

        for attribute in row:
            if attribute == "continent":
                continent = row[attribute]

                if continent == "-":
                    continent = "middle_earth"

                if continent in continent_to_province:
                    continent_to_province[continent].append(prov_id)
                else:
                    continent_to_province[continent] = [prov_id]
            elif attribute == "climate":
                climate = row[attribute]

                if climate == "-":
                    climate = "middle_earth"

                if climate in climate_to_province:
                    climate_to_province[climate].append(prov_id)
                else:
                    climate_to_province[climate] = [prov_id]
            elif row[attribute] == "-":
                pass
            elif attribute == "guilds":
                guilds = row[attribute].split(" ")

                for guild in guilds:
                    f.write("state_building = {\n")
                    f.write("\tlevel = 1\n")
                    f.write(f"\tbuilding = {guild}\n")
                    f.write("\tupgrade = yes\n")
                    f.write("}\n")
            elif attribute == "cores":
                cores = row[attribute].split()
                for core in cores:
                    f.write(f"add_core = {core}\n")
            else:
                f.write(f"{attribute} = {row[attribute]}\n")


def read_data(infile, provinces, full_path):
    with open(infile, "r", encoding="utf-8") as province_history:
        reader = DictReader(province_history)

        for row in reader:
            process_line(row, provinces, full_path)

        with open("../output/continent.txt", "w", encoding="ANSI") as wf:
            for continent in continent_to_province:
                wf.write(f"{continent} = {{\n")
                wf.write(f"\tprovinces = {{\n\t\t")
                for province in continent_to_province[continent]:
                    wf.write(f"{province} ")
                    if int(province) % 30 == 0:
                        wf.write('\n\t\t')
                wf.write(f"\n\t}}")
                wf.write(f"\n}}\n\n")

        with open("../output/climate.txt", "w", encoding="ANSI") as wf:
            for climate in climate_to_province:
                wf.write(f"{climate} = {{\n\t")
                for province in climate_to_province[climate]:
                    wf.write(f"{province} ")
                    if int(province) % 30 == 0:
                        wf.write('\n\t')
                wf.write(f"\n}}\n\n")


def define_remaining_provinces(starting_id, ending_id, default_rgo, provinces, full_path):
    for i in range(ending_id - starting_id + 1):
        prov_id = str(i + 1)
        province_name = unidecode(provinces[prov_id])
        if not path.exists(f"{full_path}/{prov_id} - {province_name}.txt"):
            with open(f"{full_path}/{prov_id} - {province_name}.txt", "w") as f:
                f.write(f"trade_goods = {default_rgo}\n")
                f.write("life_rating = 5\n")
                f.write("\n")


def clear_directory(full_path):
    for root, dirs, files in walk(full_path):
        for filename in files:
            remove(f"{root}/{filename}")


def generate_history_files(directory, mod_folder, infile, starting_id, ending_id, sea_provinces, default_rgo, outfile, out_folder):
    full_path = f"{mod_folder}/history/provinces/{directory}"
    clear_directory(full_path)
    provinces = get_provinces(f"{mod_folder}/map/definition.csv")
    localisation_provinces = dict(provinces)
    regions = get_regions(f"{mod_folder}/map/region.txt")

    read_data(infile, provinces, full_path)
    define_remaining_provinces(starting_id, ending_id, default_rgo, provinces, full_path)
    localize(localisation_provinces, regions, outfile, out_folder, starting_id, ending_id, sea_provinces)
