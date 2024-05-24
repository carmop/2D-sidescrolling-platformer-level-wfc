import random
from Settings import *


class Tile:
    """Attributes and functionality of tiles objects as well as the method used for collapse.
    
    This class contains methods that add neighbours, get already added neighbours, and get directions of neighbouring tiles
    to most recently collapsed tile for propagating possibilities.
    Also contains method for getting the current possibilities of a given tile.

    The `collapse` method simply choses a random tile from the current possible tiles to be collapsed.
    It can include the weights from the settings file or not depending on the boolean `WEIGHTED`.

    The `constrain` method is responsible for one of the main features of the generation, it will
    remove the tiles that cannot be placed next to the most recently collapsed tile by removing them from
    the `possibilities` list.

    Attributes:

        possibilities: A list made up of the keys of the adjecency 
        rules dictionary (in Stteings.py file).  
        
        entropy: Integer representing the length of possibilities list, 
        a number that represents how many possibilities of tiles can a cell collapse into.
        
        neighbours: An empty dictionary that will be populated with the 
        most recently collapsed tile's neighbours
    """


    def __init__(self, x, y):
        """Defines class' atributes."""

        self.possibilities = list(tileRules.keys()) # `tileRules` is a dict in Settings.py
        self.entropy = len(self.possibilities) # Just how many possibilities a tile can have
        self.neighbours = dict()
        
        self.difficulties = list(tileDifficulty.keys()) 


    def addNeighbour(self, direction, tile):
        """Adds to tiles to neighbours dictionary."""

        self.neighbours[direction] = tile


    def getNeighbour(self, direction):
        """Returns the neighbours in the given direction."""

        return self.neighbours[direction]


    def getDirections(self):
        """Returns a list of directions from neighbours dictionary."""

        return list(self.neighbours.keys())


    def getPossibilities(self):
        """Returns a list of possibilities for picking the next tile."""

        return self.possibilities
    

    def collapse(self, use_weight):
        """Picks a random tile from available possibilities, may be a weighted selection."""

        if use_weight: # WEIGHTED can be set to True of False in Settings.py
            weight = [tileWeights[possibility] for possibility in self.possibilities]
            self.possibilities = random.choices(self.possibilities, weights=weight, k=1)
            self.entropy = 0
        else:
            self.possibilities = random.choices(self.possibilities, weights=None, k=1)
            self.entropy = 0


    def constrain(self, neighbourPossibilities, direction):
            """Returns true if possibilities have been completely reduced."""

            reduced = False

            if self.entropy > 0:
                connectors = []

                # Add neighbouring tiles to `connectors` list
                # The list contains the integers that represent tile edges
                for neighbourPossibility in neighbourPossibilities:
                    connectors.append(tileRules[neighbourPossibility][direction])

                if direction == RIGHT:
                    opposite = LEFT

                if direction == LEFT:
                    opposite = RIGHT
                
                # If a possibility does not fit next to current tile remove it
                for possibility in self.possibilities.copy():
                    
                    # Checks current tile edge with opposite edge from neighbour
                    if tileRules[possibility][opposite] not in connectors:
                        self.possibilities.remove(possibility)
                        reduced = True

                self.entropy = len(self.possibilities)

            return reduced
