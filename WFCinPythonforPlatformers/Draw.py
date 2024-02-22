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


    def update(self):
        """"""
        lowest_entropy = self.level.getLowestEntropy()

        for y in range(LEVEL_H):
             for x in range(LEVEL_LENGTH):
                  tile_entropy = self.level.getEntropy(x, y)
                  tile_type = self.level.getType(x, y)
                
                  if tile_entropy > 0:
                        tile_image = pygame.Surface((X_TILE, Y_TILE))
                        if tile_entropy == 27:
                            textSurface = self.font2.render(str(tile_entropy), True, "darkgrey")
                            tile_image.blit(textSurface, (3, 3))
                        elif tile_entropy >= 10:
                            textSurface = self.font1.render(str(tile_entropy), True, "grey")
                            tile_image.blit(textSurface, (2, 3))
                        elif tile_entropy < 10:
                            if tile_entropy == lowest_entropy:
                                textSurface = self.font0.render(str(tile_entropy), True, "green")
                            else:
                                textSurface = self.font0.render(str(tile_entropy), True, "white")
                            tile_image.blit(textSurface, (4, 1))
                    #
                            
                  else:  
                    pos = tileSprites[EASY_STRAIGHT_MID] # Use 1 instead of EASY_STRAIGHT_MID ?
                    tile_image = self.spritesheet.subsurface(pygame.Rect(pos[0], pos[1], X_TILE, Y_TILE))
                    tile_image = pygame.transform.scale_by(tile_image, (SCALING, SCALING))
                    self.surface.blit(tile_image, (x * X_TILE * SCALING, y * Y_TILE * SCALING))
                    pos = tileSprites[tile_type]
                    tile_image = self.spritesheet.subsurface(pygame.Rect(pos[0], pos[1], X_TILE, Y_TILE))
                
                  tile_image = pygame.transform.scale_by(tile_image, (SCALING, SCALING))
                  self.surface.blit(tile_image, (x * X_TILE * SCALING, y * Y_TILE * SCALING))


    def draw(self, displaySurface):
     
     displaySurface.blit(self.surface, (0, 0))

                            
                        
