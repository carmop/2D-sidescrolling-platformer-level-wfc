import random
from Settings import *

class Tile:
    """"""
    def __init__(self, x, y):
        self.possibilities = list(tileRules.keys())
        self.entropy = len(self.possibilities)
        self.neighbours = dict()
