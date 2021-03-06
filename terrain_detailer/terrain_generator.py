# Please read the README in this folder prior to using this tool
from terrain_detailer.src.perlin_terrain_generator import generate_terrain

# Change this variable's path to point towards your input file
# For example:
# "C:/Program Files (x86)/Steam/steamapps/common/Victoria 2/mod/LOTR/terrain_generation_test_old.bmp"
input_file = "C:/Program Files (x86)/Steam/steamapps/common/Victoria 2/mod/TTA/pre-terrain-generator.bmp"

# Changing these variables is optional. However, if you changed your
# installation, changing these variables is required.
# By default, the output file will show up in
# C:\Users\USERNAME\PyCharmProjects\modding_tools\output\output_file
output_folder = "output"
output_file = "terrain_output.bmp"


def main():
    generate_terrain(input_file, output_folder, output_file)


# If you are using PyCharm, press the little green play button below to run the script
if __name__ == "__main__":
    main()
