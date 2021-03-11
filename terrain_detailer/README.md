# Terrain Detailer
The Terrain Detailer is able to take images like this  
![Old Image](../images/terrain%20detailer/terrain_generation_test_old.jpg)  

and turn them into images like this  
![New Image](../images/terrain%20detailer/terrain_generation_test.jpg)

### Requirements
Python 3.8
- Pillow Module

*If you followed the provided installation instructions for the repository, you can ignore the above requirements
as you have already installed them*  

Your terrain textures must follow a similar pattern as vanilla Victoria 2 (texture 0-3 must be arctic, 4-7 plains, etc.)  

Additionally, textures 26, 27, 30, 31 must be snow covered mountains, and 61 - 64 must be non-snowy mountains.

### Usage
 - Input file must be an image. I would recommend a .bmp (have not encountered any problems with 24 bit .bmp files)
 - **Required** you must change the input file variable (line 7)
 - **Optional** you can change the output file and folder variables (lines 13 and 14); **Required** if you changed your installation location
 - Outputs a detailed terrain to the specified file
 
The output file is **not** in the correct format to be directly read by the engine. You will have messed up terrain
if you do not convert the terrain to the correct type of .bmp file. I suggest using GIMP for this.

The following are the specific RGB colors associated with each type of supported terrain:
 - 47 116 0 = farmland
 - 255 100 238 = mountain
 - 255 200 238 = low_mountain
 - 170 116 0 = steppe
 - 79 150 210 = hills
 - 0 78 58 = marsh
 - 132 16 35 = grassland
 - 40 38 20 = conifer_forest
 - 101 147 20 = deciduous_forest
 - 255 237 76 = desert
 
Any pixel that does not have one of these colors the detailer will ignore. Conversely, any pixel that has one of the above
color will be converted to its actual terrain color.

### Versions
There are two versions in here: the normal terrain detailer and the simple one.  

1. The normal terrain detailer uses Perlin noise to create the output image.  

   - **NOTE**: I would not recommend running the normal terrain detailer on the entire map. Because of the large amount of
information that would have to be stored, you **may** run out of RAM and get a MemoryError (I got it with 16 gigs of RAM).
Instead, run it on smaller sections of the map by making new .bmp files.

   - **NOTE**: Additionally, because of how the math and indexing is currently implemented ensure that both the width and 
height of the file you are pulling from are even numbers.  

2. The simple terrain detailer just randomly samples the specific terrain. For this one, you should be able to pass through
your entire terrain map should you wish.

   - **NOTE**: The simple terrain detailer is not fully implemented at the moment. Please do not use it

### Current Status
Normal (Perlin) Detailer:
 - Currently Supports:
   - Mountains, with the ability to transition from snow (mountain) covered to non-snow covered (low_mountain)
   - Steppe
   - Farmland
   - Hills
   - Marsh
   - Grassland (Plains)
   - Conifer Forest (Forest)
   - Deciduous Forest (Woods)
   - Desert
 - Coming soon:
   - Arctic
   - Jungle
   - Coastal Desert
   - Ability to dictate where denser Forest, Jungle and Woods lie
  
Simple Detailer:
 - Currently Supports:
   - Mountains
   - Farmland
 - Coming Soon:
   - Steppe
   - Hills
   - Marsh
   - Grassland (Plains)
   - Conifer Forest (Forest)
   - Deciduous Forest (Woods)
   - Arctic
   - Jungle
   - Desert
   - Coastal Desert
   - Ability to dictate where denser Forest, Jungle and Woods lie
   - Ability to dictate add non-snow covered mountains