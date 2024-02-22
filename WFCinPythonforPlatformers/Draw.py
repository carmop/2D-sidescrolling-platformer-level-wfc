import pygame
from Settings import *


class DrawLevel:
    """
    
    """
    def __init__(self, level) -> None:
        """"""

        #Text fonts from pygame package 
        self.font0 = pygame.font.Font(pygame.font.get_default_font(), 14)
        self.font1 = pygame.font.Font(pygame.font.get_default_font(), 11)
        self.font2 = pygame.font.Font(pygame.font.get_default_font(), 8)

        self.spritesheet = pygame.image.load(SPRITESHEET_PATH).convert_alpha()

        self.level = level
        self.surface = pygame.Surface(((LEVEL_LENGTH * X_TILE * SCALING), (LEVEL_H * Y_TILE * SCALING)))
