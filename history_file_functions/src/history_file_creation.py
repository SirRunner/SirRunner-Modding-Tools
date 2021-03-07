from os import path, walk, remove
from unidecode import unidecode
from csv import DictReader
from history_file_functions.src.map_files import get_provinces, get_regions
from history_file_functions.src.localisation import localize


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
            if row[attribute] == "-":
                pass
            elif attribute != "cores":
                f.write(f"{attribute} = {row[attribute]}\n")
            else:
                cores = row[attribute].split()
                for core in cores:
                    f.write(f"add_core = {core}\n")


def read_data(infile, provinces, full_path):
    with open(infile, "r", encoding="utf-8") as province_history:
        reader = DictReader(province_history)

        for row in reader:
            process_line(row, provinces, full_path)


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


def generate_history_files(directory, mod_folder, infile, starting_id, ending_id, default_rgo, outfile, out_folder):
    full_path = f"{mod_folder}/history/provinces/{directory}"
    clear_directory(full_path)
    provinces = get_provinces(f"{mod_folder}/map/definition.csv")
    localisation_provinces = dict(provinces)
    regions = get_regions(f"{mod_folder}/map/region.txt")

    read_data(infile, provinces, full_path)
    define_remaining_provinces(starting_id, ending_id, default_rgo, provinces, full_path)
    localize(localisation_provinces, regions, outfile, out_folder, starting_id, ending_id)
