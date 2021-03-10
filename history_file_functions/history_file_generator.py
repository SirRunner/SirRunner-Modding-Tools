# Please read the README in this folder prior to using this tool
from history_file_functions.src.history_file_creation import generate_history_files

# Change this variable's path to point towards your input file
# For example:
# "C:/Program Files (x86)/Steam/steamapps/common/Victoria 2/mod/LOTR/terrain_generation_test_old.bmp"
input_file = "C:/Users/USERNAME/Downloads/Provinces - Sheet1.csv"

# Change this varaible's path to point towards your mod's path
mod_folder = "C:/Program Files (x86)/Steam/steamapps/common/Victoria 2/mod/TTA"

# Change this variable's name to that of the folder which you are editing in the history folder
directory = "middle earth"

# Change these variables to the starting and ending ids that the file generator makes.
# For instance, starting_id = 1 and ending_id = 5 would make 5 history files (1, 2, 3, 4, 5)
starting_id = 1
ending_id = 513

# Change this variable to the default rgo for ids not defined within your input file.
default_rgo = "food"

# Changing these variables is optional. However, if you changed your
# installation, changing these variables is required.
# By default, the output file will show up in
# C:\Users\USERNAME\PyCharmProjects\PROJECTNAME\output\map.csv
output_folder = f"../output"
output_file = "map.csv"


def main():
    generate_history_files(directory, mod_folder, input_file, starting_id, ending_id, default_rgo, output_file, output_folder)


# If you are using PyCharm, press the little green play button below to run the script
if __name__ == "__main__":
    main()
