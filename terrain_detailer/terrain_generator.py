# Please read the README in this folder prior to user this tool
from terrain_detailer.src.perlin_terrain_generator import generate_terrain

# Change this variable's path to point towards your input file
# Assuming a default installation, this file's location is
# C:\Users\USERNAME\PyCharmProjects\PROJECTNAME\terrain_detailer\terrain_generator.py
# ".." goes up one folder level. Assuming a default installation, ".." would be
# C:\Users\USERNAME\PyCharmProjects\PROJECTNAME
# This can be extended. "../.." is two folders above. Assuming a default installation, "../.." would be
# C:\Users\USERNAME\PyCharmProjects
# Additionally, you instead could define an absolute path, starting with the drive name:
# "C:/Program Files (x86)/Steam/steamapps/common/Victoria 2/mod/LOTR/terrain_generation_test_old.bmp"
input_file = "C:/Program Files (x86)/Steam/steamapps/common/Victoria 2/mod/TTA/pre-terrain-generator.bmp"

# Changing these variables are optional. By default, the output file will show up in
# C:\Users\USERNAME\PyCharmProjects\PROJECTNAME\output\output_file
# output_folder must end with a '/' to ensure that the file is saved in the correct place
output_folder = "C:\Users\USERNAME\PyCharmProjects\PROJECTNAME\output\output_file"
output_file = "terrain_output.bmp"


def main():
    generate_terrain(input_file, output_folder, output_file)


# If you are using PyCharm, press the little green play button below to run the script
if __name__ == "__main__":
    main()
