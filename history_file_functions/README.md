# History File Generator

The history file generator is able to take a formatted csv file and create history files in one directory. For example, 
if given an input file and the directory "middle earth", any history file created will be placed into
`installation_folder\Victoria II\mod\modname\history\provinces\middle earth`. Additionally, for provinces and their 
regions which have an entry in the input file will be localised (should be in ANSI) in the specified output file.

### Requirements
Python 3.8
 - Unidecode module
 
*If you followed the provided installation instructions for the repository, you can ignore the above requirements
as you have already installed them*  

Your mod **must** have a `\map\definitions.csv` file with the following "header row" (first row in file):
`province;red;green;blue;name;x;`

Your mod **must** have a `\map\region.txt` file with the following format: `region = { province_ids } # Region Name`
For example: `GON_4 = { 4 1 2 3 5 6 7 } # Far Anórien`

Input file must be a .csv file. The "header row" must have "id" (holding the province ids) and "name" (holding the province name)
 - "comment" is a reserved header. A column labeled "comment" will be put into the history files as `# comment value` if it exists
 - any other column headers will be used exactly as they are written. As such, a province's life rating column header name should be "life_rating"
  
### Usage
 - **Required** You must change the input_file, mod_folder, directory, starting_id, ending_id and default_rgo variables (lines 7, 10, 13, 17, 18, 21)
 - **Optional** you can change the output file and folder variables (lines 13 and 14); **Required** if you changed your installation location
 - Outputs an ANSI-encoded csv file that can be placed directly into the mod's localisation directory
 
**NOTE**: Running this will **delete all files and folders in the specified history folder**. This is to ensure that 
there are no duplicate files created (which can cause weird non-crashing issues in game).
 
### Current Status
Currently Supports:
 - "Basic" one line entry in history files such as forts, naval bases, terrain, life ratings, etc.
Coming Soon:
 - Factories
 
Known issues:
 - If the names in the input file and definition files differ, will default to the definitions file.