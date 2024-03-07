import pygame
from Level import Level
from Draw import DrawLevel
from Settings import *


# Set whether or not the level generator will be interactive from settings file
interact = INTERACTIVE
key_press = INTERACTIVE_KEYPRESS

pygame.init()
clock = pygame.time.Clock()

# Create surface object, base on size of level and based on level length and y size of 1 tile
displaySurface = pygame.display.set_mode(size=((LEVEL_LENGTH * X_TILE * SCALING) + 5, (LEVEL_H * Y_TILE * SCALING)))

pygame.display.set_caption("Wave Function Collapse in Platformer Level Generation")

# Create level variable to determine level size from settings file
level = Level(LEVEL_LENGTH, LEVEL_H)


# Create level based on size of 'level' variable
drawLevel = DrawLevel(level)

# Checks is level generation has benn completely finished
done = False

# Instantly draws level if `interact` is set to False
if interact is False:
    while done is False:
        result = level.waveFunctionCollapse()
        if result == 0:
            done = True

drawLevel.update()
isRunning = True

# Draws level in real time or by pressing space key if `interact` is set to True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning is False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
            if event.key == pygame.K_SPACE:
                if interact is True and key_press is True:
                    level.waveFunctionCollapse()
                    drawLevel.update()

    if interact is True and key_press is False:
        if not done:
            result = level.waveFunctionCollapse()
            if result == 0:
                done = True
        drawLevel.update()

    drawLevel.draw(displaySurface)

    pygame.display.flip()
    clock.tick(10) # Speed of tile collapsing animation when `key_press` is False and `interact` is True

pygame.quit()
