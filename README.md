# Carmop-WFC_AnxietyCurves_SuperMarioBros

### Description

An implementation of anxiety curves into the wave function collapse algorithm specifically designed to generated 2D side scrolling platformer levels.

- Wave function collapse:
	A generation algorithm which uses pre-set rules or rules inferred from a valid input to 
	generate similar permutations of the input.
	
- Anxiety curves:
	The qualitative curve that describes a player's challenges in traversing a video game 
	level.

This method for procedural generation uses an image file containing level sections (tiles) and a list describing the difficulty values for each section of the level; these inputs are used by the wave function collapse algorithm to place tiles pseudo-randomly while following an arbitrary set of adjacency rules that ensure the level will follow the correct difficulty and will be playable.

### Set up

Install requirement from `requirements.txt` using the `pip install -r requirements` command.

### Running

- Go into the `WFC` directory.
- Run the `WFC.py` file with python: `python WFC.py` or `python3 WFC.py`.
- A pygame window should pop up and display the generation. To close it after generation is done press `ESC`.
	- If running in _interactive_ mode, press `SPACE` to collapse the next tile.
	- To quit during generation, force quit on the terminal window(`CTRL C`).


### Resources
- GODOT documentation: https://docs.godotengine.org/en/stable/index.html

- WFC GODOT Package: https://github.com/AlexeyBond/godot-constraint-solving

### Acknowledgements

- [Teams working on GODOT project](https://godotengine.org/teams/) for the free, open-source game engine 

- [AlexeyBond](https://github.com/AlexeyBond) for the WFC package

- [RottingPixels](https://rottingpixels.itch.io/) for the tileset art used
