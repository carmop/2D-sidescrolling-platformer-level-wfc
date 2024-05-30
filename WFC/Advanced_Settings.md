## Changing Tile Set:

### Step 1: Understanding the `Settings` File

- Tile name/Tile ID: The `Settings.py` file contains tile variables named in the format "tile_number" (for example `TILE_001`). These variables are used for the program to know what each distinct tile is and how they should be treated. 
	- There are also tile _duplicates_ which are the same tile (visually at least) but with different properties for generation. These are marked by the letter `D` at the end of their name (`TILE_005D` for example).
	- There are special tiles included in the generation which were hand made for special edge cases, these tiles' names include the word `ADDENDUM` or `ALL` (like `TILE_ADDENDUM_1` or `TILE_ALL_1LL` for example).

- For this implementation of WFC to work each tile needs a set of rules to communicate to the program which other tiles can be placed next to them. The dictionary `tileRules` holds these adjacency rules.
    - The dictionary is formatted by having the keys correspond to the tile's ID and the value be a list of 2 tile edges (one for the left side of the tile, one for the right side of the tile).
        - For example, the tile `TILE_001 : [LOW, LOW]` has a `LOW` value on its left edge and a `LOW` value in its right edge which will allow other tiles with `LOW` edges to connect to it. While the tile `TILE_055 : [MID, LOW]` has a `MID` and a `LOW` edge, which allows tiles with a `MID` edge to connect to its left while only tiles with a `LOW` value can connect to its right.

- For the anxiety curve to be used in generation, each tile must also have a difficulty value associated with it. These values can be `EASY`,`MEDIUM`,or `HARD`.
    - The `tileDifficulty` dictionary holds key value pairs where the tile ID is the key and a single item list is the difficulty value. For example, the difficulty that corresponds to `TILE_001` is stored as `TILE_001: [EASY]`. 

- In order to actually render the tile images we have to give the program the location of every tile in the tile sheet. In order to accomplish this we create a dictionary of the position of the top left corner of each tile and create variables that contain the size of the tiles. This way the program only needs one coordinate per tile to know how many pixels each tile takes and how to display it.
    - The `tileSprites` dictionary holds the coordinates for the upper left corner of each tile in the tile sheet as tuples. For the first tile the dictionary entry is `TILE_001 : (0, 0)`, then for every tile afterwards the Y position will remain the same(because the tiles are side by side in the tile sheet) but the X position will shift by 160 (because every tile is 160 pixels wide). So the next entries are `TILE_002 : (160, 0),TILE_003 : (320, 0),TILE_004 : (480, 0),`. 
        - The tuples are set up so that the values are X pixel position then Y pixel position, `(X,Y)`.
    - The variables `Y_TILE` and `X_TILE` represent how many pixels tall and how many pixels wide each tile is so that the program can render them properly.
    - Lastly the `SCALING` variables will affect how much the program should stretch out the images when rendering them.

### Step 2: Preparing the Sprite Sheet

- The current tile set included in this repo is made up of sections of _Super Mario Bros._ levels. These sections have all been placed into the same gigantic image file which the program splits into each individual tile. 
    - In order to change the tile set one must arrange a tile sheet/sprite sheet in the same way and include the path to that image in the `SPRITESHEET_PATH` variable.
        - To make such tile sheet you must gather or create your tile images and place them next to each other until they are all in one file. They must be 160 pixels wide and around 240 pixels tall. 
        - If that is not the case you will have to change the variables `Y_TILE` and `X_TILE`. However, changing those also means that your tile positions are not configured correctly, so you must change the `tileSprites` dictionary (or probably create a new one from scratch). When making your new `tileSprites` dictionary the first entry's value should be a tuple that contains the upper left corner of your first tile and the subsequent entries should be the left corner of each of the corresponding tiles.

### Step 3: Adding the Sprite Sheet Information

- The current sprite sheet has 197 different tiles and the `Settings` file has 277 tile IDs including all IDs for duplicates and extra tile configurations.
    - To add your own sprite sheet you will need to replace the tile variables (`TILE_001`, `TILE_002`, `TILE_003`...) with values that reflect your tile sheet.
        - This means adding more tile IDs or removing necessary ones.

    - When you have all your new tile IDs ready, you might want to adjust the dictionaries `tileRules`, `tileDifficulty`. `tileWeights`, and `tileSprites` to contain the new tile IDs as keys.

_* The tile IDs do not have to follow any convention necessarily, they are formatted in the way they are only for convenience._

## Changing the Rules:

In order to change the generation rules you must change the dictionary entries that correspond with the change you want to make or create a new dictionary and implement the necessary code to parse through it in the generation process.

- To change the adjacency behavior of the algorithm you must change the values inside the `tileRules`. 
    - For example, if you would like to change a tile's adjacency to reflect a change you've made in the sprite sheet you may just modify the values to match the new edge of the tile in the sprite sheet. If `TILE_001`, for instance, was changed in the sprite sheet and no longer fit well with a `LOW` right edge you may change to `TOP` or `MID`.

    - However, if you'd like to add a new adjacency rule you must declare a new variable in the `Settings` file (outside the dictionary) like the variables `LOW`, `MID`, and `TOP`. This new variable must have a different integer value than the other edge values because it otherwise the algorithm won't be able to differentiate between them.

- Similarly, to change the difficulty rules, simply alter the values in the `tileDifficulty` dictionary.
    - For example, if the first tile is now considered hard instead of easy its entry can be changed to `TILE_001: [HARD]`. 
    - Adding a new type of difficulty follows the same idea as before, create a new variable to represent this difficulty and set its value to an integer that is not being used by any of the other difficulties.

    