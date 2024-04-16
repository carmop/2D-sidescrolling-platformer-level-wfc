import pygame
from Settings import *


class DrawLevel:
    """Pygame code for drawing the WFC generated level.

    Uses pygame built in functionality to create game window,
    draw level grid, write entropy values on each grid cell,
    and finally draw the collapsed tiles.  
    """

    
    def __init__(self, level) -> None:
        """Chose fonts and load image path."""

        #Text fonts from pygame package 
        self.font0 = pygame.font.Font(pygame.font.get_default_font(), 14)
        self.font1 = pygame.font.Font(pygame.font.get_default_font(), 11)
        self.font2 = pygame.font.Font(pygame.font.get_default_font(), 8)

        self.spritesheet = pygame.image.load(SPRITESHEET_PATH).convert_alpha()

        self.level = level
        self.surface = pygame.Surface(((LEVEL_LENGTH * X_TILE * SCALING), (LEVEL_H * Y_TILE * SCALING)))


    def update(self):
        """Get tiles' entropy to display its numeric value in the cells, and draw collapsed tiles."""

        level_id = []

        lowest_entropy = self.level.getLowestEntropy()

        for y in range(LEVEL_H):
             for x in range(LEVEL_LENGTH):
                tile_entropy = self.level.getEntropy(x, y)
                tile_type = self.level.getType(x, y)
                # Different entropy values will be written with different colors.
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

                # When entropy is 0 tile will be collapsed so it has to be drawn.            
                else:
                    pos = tileSprites[TILE_001] # Will always draw tile 1 first. Then it will be drawn over later

                    # Get image from spritesheet and scale properly.
                    tile_image = self.spritesheet.subsurface(pygame.Rect(pos[0], pos[1], X_TILE, Y_TILE))
                    tile_image = pygame.transform.scale_by(tile_image, (SCALING, SCALING))

                    # Draw tile in correct positon and overwrite tile 1.
                    self.surface.blit(tile_image, (x * X_TILE * SCALING, y * Y_TILE * SCALING))
                    pos = tileSprites[tile_type] 
                    tile_image = self.spritesheet.subsurface(pygame.Rect(pos[0], pos[1], X_TILE, Y_TILE))
                level_id.append(str(tile_type))
                # print(level_id)
                tile_image = pygame.transform.scale_by(tile_image, (SCALING, SCALING))
                self.surface.blit(tile_image, (x * X_TILE * SCALING, y * Y_TILE * SCALING))
        
        return level_id


    def draw(self, displaySurface):
     """Draws the level."""
     
     displaySurface.blit(self.surface, (0, 0))

                            
                        
