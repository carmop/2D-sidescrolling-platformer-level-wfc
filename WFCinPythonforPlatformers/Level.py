import random
from Tile import Tile
from Stack import Stack
from Settings import *

# from AC import AnxietyCurve

class Level:
    """Performs WFC and propagates probabilities by using the tiles' entropy values. 
    
    Builds a representation of the level tiles in through the list `tiles` 
    which contains `Tile` objects.

    Also adds tiles to `neighbours` dictionary for probability propagation 
    after collapse.
    """

    def __init__(self, sizeX, sizeY) -> None:
        """Level class that represents the environment of the platformer level.
        
        The class creates an array (of size determined by LEVEL_LENGTH variable in Settings.py file)
        populated with tile objects which can have their `possibilities` atribute
        include all tile possibilities or include only the 
        tile possibilities that follow the anxiety curve (that is also determined in the Settings.py file, as the `AC variable).

        The final step in generating the array that represents the level 
        is to map all neighbours of a tile to that tile's `neighbours` atribute. 
        """

        self.AC = AC # Anxiety curve list from the Settings.py file
        self.cols = sizeX
        self.rows = sizeY

        self.tileRows = []
        for y in range(sizeY):
            tiles = []
            for x in range(sizeX):
                tile = Tile(x,y)
                possibilities = tile.possibilities.copy()
                
                if ANXIETY_CURVE: # Only culls the tiles if user wants to generate with anxiety curve parameter
                    for i in range(len(possibilities)):

                        if tileDifficulty[tile.possibilities[i]][0] is not self.AC[x]:
                            possibilities.remove(tile.possibilities[i])

                    tile.possibilities = possibilities
                
                tiles.append(tile)

            self.tileRows.append(tiles)
            

        for y in range(sizeY):
            for x in range(sizeX):
                tile = self.tileRows[y][x]

                # Adds neighbouring tiles to a list, 
                # for checking left and right sides of current tile
                # so that after collapse step probability can be propagated
                if x < sizeX - 1:
                    tile.addNeighbour(RIGHT, self.tileRows[y][x+1])
                if x > 0: 
                    tile.addNeighbour(LEFT, self.tileRows[y][x-1])


    def getEntropy(self, x, y):
        """Returns entropy of tile object."""

        return self.tileRows[y][x].entropy


    def getType(self, x, y):
        """Returns first item in possibilities list.
        
        The possibilities list is a list made from the key values
        of the dictionary of adjecency rules.
        """

        return self.tileRows[y][x].possibilities[0] 
    

    def getLowestEntropy(self):
        """Returns  which entropy value is the lowest in current WFC step."""

        lowest = len(list(tileRules.keys()))

        for y in range(self.rows):
            for x in range(self.cols):
                tileEntropy = self.tileRows[y][x].entropy

                if tileEntropy < lowest:
                    lowest = tileEntropy

        return lowest
    

    def getTilesLowestEntropy(self):
        """Returns list of lowest entropy tiles."""

        lowest = len(list(tileRules.keys()))
        tileList = []

        for y in range(self.rows):
            for x in range(self.cols):
                tileEntropy = self.tileRows[y][x].entropy
              
                if tileEntropy > 0:
                    if tileEntropy < lowest:
                        tileList.clear()
                        lowest = tileEntropy
                    if tileEntropy == lowest:
                        tileList.append(self.tileRows[y][x])
       
        return tileList


    def getCell(self, tile):
        """Returns index of the cell a given tile object is in."""

        return self.tileRows[0].index(tile)


    def waveFunctionCollapse(self):
        """Main WFC function. Handles tile collapsing and propagation.
        
        First it defines the lowest entropy among current tiles,
        then it choses a tile to be collapsed amongst all 
        tiles that share the lowest entropy (if there is more than 1).

        Then it uses a stack to propagate entropy to neibouring tiles which
        affects which tile is possible to be collapsed next.
        """

        tilesLowestEntropy = self.getTilesLowestEntropy() # list of lowest entropy tile objects

        if tilesLowestEntropy == []: # If there is no lowest entropy WFC is finished
            return 0

        tileToCollapse = random.choice(tilesLowestEntropy) # Choose random tile from lowest entropy tiles
        tileToCollapse.collapse()
       
        stack = Stack()
        stack.push(tileToCollapse)

        while(not stack.is_empty()):
            tile = stack.pop()
            tilePossibilities = tile.getPossibilities() # Which tiles are allowed next to current tile
            
            # Direction to propagate the possibilities, 
            # since this is implementation is simplified as a 1D problem 
            # it can only have up to 2 directions (left and right)
            directions = tile.getDirections() 

            for direction in directions:
                neighbour = tile.getNeighbour(direction)

                # Constrain possibilities of neighbouring tiles
                if neighbour.entropy != 0:
                    reduced = neighbour.constrain(tilePossibilities, direction)

                    if reduced == True:
                        stack.push(neighbour)    # When possibilities were reduced need to propagate further

        return 1