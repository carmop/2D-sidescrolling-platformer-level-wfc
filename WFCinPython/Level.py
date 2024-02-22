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