import random
from Settings import *

class Tile:
    """
    
    """


    def __init__(self, x, y):
        """"""

        self.possibilities = list(tileRules.keys())
        self.entropy = len(self.possibilities)
        self.neighbours = dict()


    def addNeighbour(self, direction, tile):
        """"""

        self.neighbours[direction] = tile


    def getNeighbour(self, direction):
        """"""

        return self.neighbours[direction]


    def getDirections(self):
        """"""

        return list(self.neighbours.keys())


    def getPossibilities(self):
        """"""

        return self.possibilities
    

    def collapse(self):
        """"""

        if WEIGHTED:
            weight = [tileWeights[possibility] for possibility in self.possibilities]
            self.possibilities = random.choices(self.possibilities, weights=weight, k=1)
            self.entropy = 0
        else:
            self.possibilities = random.choices(self.possibilities, weights=None, k=1)
            self.entropy = 0


def constrain(self, neighbourPossibilities, direction):
        """"""
        
        reduced = False

        if self.entropy > 0:
            connectors = []

            for neighbourPossibility in neighbourPossibilities:
                connectors.append(tileRules[neighbourPossibility][direction])

            if direction == RIGHT:
                opposite = LEFT

            if direction == LEFT:
                opposite = RIGHT
            
            for possibility in self.possibilities.copy():
                if tileRules[possibility][opposite] not in connectors:
                    self.possibilities.remove(possibility)
                    reduced = True

            self.entropy = len(self.possibilities)

        return reduced
    