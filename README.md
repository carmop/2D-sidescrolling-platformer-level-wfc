# Carmop-WFC_AnxietyCurves_SuperMarioBros

### Description

An implementation of anxiety curves into the wave function collapse algorithm specifically designed to generated 2D side scrolling platformer levels.

- **Wave function collapse** [^1]:
	A generation algorithm which uses pre-set rules or rules inferred from a valid input to generate similar permutations of the input.
	
- **Anxiety curves** [^2]:
	The curve that describes a player's challenges in traversing a video game level.

This method for procedural generation uses an image file containing level sections (tiles) and a list describing the difficulty values for each section of the level; these inputs are used by the wave function collapse algorithm to place tiles pseudo-randomly while following an arbitrary set of adjacency rules that ensure the level will follow the correct difficulty and will be playable.

### Set up

Make sure [Python](https://www.python.org/) is installed (version 3.10.12 was used for development).

Install requirement from `requirements.txt` using the `pip install -r requirements` command.

### Running

- Go into the `WFC` directory.
- Run the `main.py` file with python: `python main.py` or `python3 main.py`.
- A pygame [^3] window should pop up and display the generation. To close it after generation is done press `ESC`.
	- If running in _interactive_ mode, press `SPACE` to collapse the next tile.
	- To quit during generation, force quit on the terminal window(`CTRL C`).

- Finished level images are saved in `/result_images` directory (if program is being run with saving option on).

### Changing the Generation Parameters:

#### Basic Command Line Arguments:

- Running the program with a number after `main.py` will change the number of levels that will be generated, the default value is one, so the program will generate a single level.

	- Example: `python main.py 10` will generate 10 levels consecutively. 

- Adding `--press` will make the program collapse each cell only when prompted by the user pressing `SPACE`.

- Adding `--weight` will have the algorithm utilize weighted values when choosing which tile to collapse. The weight values are found in the `Settings.py` file.

- Adding `--ac` will have the algorithm utilize anxiety curve values when choosing which tile to collapse. These values are also found in the `Settings.py` file.

- Adding `--instant` will make the generation process _visually_ instantaneous rather than each cell collapsing one after the other.

- Adding `--save` will make the program save the generated levels as images in the `/result_images` directory.

_*These additional arguments can be combined to influence the program's behavior. By default, the generation process will not use anxiety curve or weight values, nor it will save the level images, and it will display the collapse as it happens instead of instantaneously showing the finished level._

#### Advanced Parameters:

***In the `Settings.py` file there are variables that can be altered to change the difficulty curve given to the algorithm for generation, or the weights related to each tile, or the tile set as a whole:***

- The list variable `AC` holds a list that represents the anxiety curve values that will be used in generation. The values will define what difficulty tile the level generator has to place at that index. 
	- The list indexes correspond to the position of the tiles in the level while the values represent how difficult a tile in that index has to be.
	- The values in the list can range from **0,1, or 2** because those values represent the difficulties easy, medium, and hard respectively.

- `LEVEL_LENGTH`: An integer that represents how many cells/tiles each level has horizontally. **In order to change this values you must also change the length of the list `AC` so that it matches the amount of cells you wish to use in generation.**
	- If set to 25 for instance the `AC` variable must be a list with 25 entries.

- `tileWeights`: A dictionary that holds weight values related to each tile so that if needed tiles can be chosen more often than others. 
	- The dictionary is formatted using the tile name/tile ID for the key and an integer for the weight value.

**Changing Tile Set:**

***Changing the tile set will require a lot of work unless new tile set is formatted in the exact same way as the current tile set is.***

- To change the tile set, follow the rules in the `Advanced_Settings.md` file inside `/WFC` directory.

## References

[^1]: Gumin, M. (2016). Wave Function Collapse Algorithm (Version 1.0) [Computer software]. https://github.com/mxgmn/WaveFunctionCollapse

[^2]: N. Sorenson, P. Pasquier and S. DiPaola, "A Generic Approach to Challenge Modeling for the Procedural Creation of Video Game Levels," in IEEE Transactions on Computational Intelligence and AI in Games, vol. 3, no. 3, pp. 229-244, Sept. 2011

[^3]: Pygame . Pygame Front Page - pygame v2.6.0 documentation. (n.d.). https://www.pygame.org/docs/ 