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
- Run the `WFC.py` file with python: `python WFC.py` or `python3 WFC.py`.
- A pygame [^3] window should pop up and display the generation. To close it after generation is done press `ESC`.
	- If running in _interactive_ mode, press `SPACE` to collapse the next tile.
	- To quit during generation, force quit on the terminal window(`CTRL C`).

- Finished level images are saved in `/result_images` directory (if program is being run with saving option on).

#### Changing the Generation Parameters:

##### In the `Settings.py` file there are variables that control the program's running instructions:

- `INTERACTIVE`: When set to `True` will show the level as collapse takes place step by step.

- `INTERACTIVE_KEYPRESS`: When `True`, will wait for the user to press `SPACE` to collapse the next tile.

##### Then there are variables that control the generation parameters:

- `WEIGHTED`: If set to `True` will take into account the weights of each tile which will affect a given tiles chance to be picked in the generation process.
	- The weights are stored in the `tileWeights` dictionary in the `Settings.py` file.

- `ANXIETY_CURVE`: When set to `True`, the algorithm will take into account the specified anxiety curve, stored in the variable `AC`, in the generation process. 

- `LEVELS`: An integer that corresponds to how many levels will be generated when the algorithm runs.

- `AC`: A list that represents the anxiety curve values. It contains values which will define what difficulty the level generator has to place at that index. 
	- The list indexes correspond to the position of the tiles in the level while the values represent how difficult a tile in that index has to be.

- `LEVEL_LENGTH`: An integer that represents how many cells/tiles each level has horizontally. **In order to change this values you must also change the `AC` length to match the amount of cells you wish to use in generation.**
	- If set to 25 for instance the `AC` variable must be a list with 25 entries.

## References

[^1]: Gumin, M. (2016). Wave Function Collapse Algorithm (Version 1.0) [Computer software]. https://github.com/mxgmn/WaveFunctionCollapse

[^2]: N. Sorenson, P. Pasquier and S. DiPaola, "A Generic Approach to Challenge Modeling for the Procedural Creation of Video Game Levels," in IEEE Transactions on Computational Intelligence and AI in Games, vol. 3, no. 3, pp. 229-244, Sept. 2011

[^3]: Pygame . Pygame Front Page - pygame v2.6.0 documentation. (n.d.). https://www.pygame.org/docs/ 