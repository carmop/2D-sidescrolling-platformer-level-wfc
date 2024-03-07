import random
from AC import AnxietyCurve
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

        # total_possibilities = tileRules.keys()
        # print(total_possibilities)
        # self.possibilities =[]

        # for possible_tile in total_possibilities:
        #     if possible_tile
        #         self.possibilities.append(possible_tile)

        self.possibilities = list(tileRules.keys()) # `tileRules` is a dict in Settings.py.
        self.entropy = len(self.possibilities) # Just how many possibilities a tile can have.
        self.neighbours = dict()
        
        self.difficulties = list(tileDifficulty.keys()) #!!!!!!!!!!!!!!
        # print("POSSIBILITIES", self.possibilities)
        # self.diff = AnxietyCurve().AC[x]


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
    

    def collapse(self):
        """Picks a random tile from available possibilities, may be a weighted selection."""

        if WEIGHTED: # WEIGHTED can be set to True of False in Settings.py.
            weight = [tileWeights[possibility] for possibility in self.possibilities]
            self.possibilities = random.choices(self.possibilities, weights=weight, k=1)
            self.entropy = 0
        else:
            # ADD A CHECK FOR ADDING 1st TILE WITH CORRECT DIFF
            # if  not in Level.AC[Level.getCell(t)]!!!!!!!!!!!
            self.possibilities = random.choices(self.possibilities, weights=None, k=1)
            self.entropy = 0


    def collapseAC(self, diff): # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """"""

        if WEIGHTED: # WEIGHTED can be set to True of False in Settings.py.
            weight = [tileWeights[possibility] for possibility in self.possibilities]
            self.possibilities = random.choices(self.possibilities, weights=weight, k=1)
            self.entropy = 0
        else:
            # ADD A CHECK FOR ADDING 1st TILE WITH CORRECT DIFF
            # if  not in Level.AC[Level.getCell(t)]!!!!!!!!!!!
            while True:
                self.possibilities = random.choices(self.possibilities, weights=None, k=1)
                # print("@@@@@@@@",type(self.possibilities))
                print("DIFF",diff,"POS",tileDifficulty[self.possibilities[0]][0])
                if tileDifficulty[self.possibilities[0]][0] == diff:
                    self.entropy = 0
                    print("B")
                    break
                else:
                    self.possibilities = list(tileRules.keys())
                    print("C")


    def constrain(self, neighbourPossibilities, direction):
            """Returns true if possibilities have been completely reduced."""

            reduced = False

            if self.entropy > 0:
                connectors = []

                # Add neighbouring tiles to `connectors` list.
                for neighbourPossibility in neighbourPossibilities:
                    connectors.append(tileRules[neighbourPossibility][direction])

                if direction == RIGHT:
                    opposite = LEFT

                if direction == LEFT:
                    opposite = RIGHT
                
                # If a possibility does not fit next to current tile remove it.
                for possibility in self.possibilities.copy():

                    # Checks current tile edge with opposite edge from neighbour.
                    if tileRules[possibility][opposite] not in connectors:
                        self.possibilities.remove(possibility)
                        reduced = True

                self.entropy = len(self.possibilities)

            return reduced
        
        
    def constrainWithAnxiety(self, neighbourPossibilities, direction): #!!!!!!!!!!!!!!!
            """Returns true if possibilities have been completely reduced."""

            reduced = False

            if self.entropy > 0:
                connectors = []
                diff = [1] #!!!!!!!!!!!

                # Add neighbouring tiles to `connectors` list.
                for neighbourPossibility in neighbourPossibilities:
                    connectors.append(tileRules[neighbourPossibility][direction])

                if direction == RIGHT:
                    opposite = LEFT

                if direction == LEFT:
                    opposite = RIGHT
                
                for possibility in self.possibilities.copy():

                    # Checks current tile edge with opposite edge from neighbour.
                    # If a possibility does not fit next to current tile remove it.
                    if (tileRules[possibility][opposite] not in connectors or 
                        tileDifficulty[possibility][0] not in diff): #!!!!!!!!!!!!
                        self.possibilities.remove(possibility)
                        reduced = True

                self.entropy = len(self.possibilities)

            return reduced