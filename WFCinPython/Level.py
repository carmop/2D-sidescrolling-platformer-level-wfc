import random
from Tile import Tile
from Stack import Stack
from Settings import *

class Level:
    """
    
    """

    def __init__(self, sizeX, sizeY) -> None:
        
        self.cols = sizeX
        self.rows = sizeY

        self.tileRows = []
        for y in range(sizeY):
            tiles = []
            for x in range(sizeX):
                tile = Tile(x,y)
                tiles.append(tile)
            self.tileRows.append(tiles)

        for y in range(sizeY):
            for x in range(sizeX):
                tile = self.tileRows[y][x]

                # Add neighbouring tiles to a list, 
                # for checking left and right sides of current tile
                # for propagating probability
                if x < sizeX - 1:
                    tile.addNeighbour(RIGHT, self.tileRows[y][x+1])
                if x > 0: 
                    tile.addNeighbour(LEFT, self.tileRows[y][x-1])


    def getEntropy(self, x, y):
        """"""
        return self.tileRows[y][x].entropy


    def getType(self, x, y):
        """"""
        return self.tileRows[y][x].possibilities[0]
    

    def getLowestEntropy(self):
        """"""
        lowest = len(list(tileRules.keys()))

        for y in range(self.rows):
            for x in range(self.cols):
                tileEntropy = self.tileRows[y][x].entropy

                if tileEntropy < lowest:
                    lowest = tileEntropy

        return lowest
    

    def waveFunctionCollapse(self):
        """"""

        tilesLowestEntropy = self.getTilesLowestEntropy()

        if tilesLowestEntropy == []:
            return 0

        tileToCollapse = random.choice(tilesLowestEntropy)
        tileToCollapse.collapse()

        stack = Stack()
        stack.push(tileToCollapse)

        while(not stack.is_empty()):
            tile = stack.pop()
            tilePossibilities = tile.getPossibilities()
            directions = tile.getDirections()

            for direction in directions:
                neighbour = tile.getNeighbour(direction)

                if neighbour.entropy != 0:
                    reduced = neighbour.constrain(tilePossibilities, direction)

                    if reduced == True:
                        stack.push(neighbour)    # When possibilities were reduced need to propagate further

        return 1