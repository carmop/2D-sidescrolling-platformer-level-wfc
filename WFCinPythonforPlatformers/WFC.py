import pygame
from Level import Level
from Draw import DrawLevel
from Settings import *


#Set whether or not the level generator will be interactive from settings file
interact = INTERACTIVE
key_press = INTERACTIVE_KEYPRESS

pygame.init()
clock = pygame.time.Clock()

#Create surface object, base on size of level and based on level length and y size of 1 tile
displaySurface = pygame.display.set_mode(size=((LEVEL_LENGTH * X_TILE * SCALING) + 5, (LEVEL_H * Y_TILE * SCALING)))
# displaySurface = pygame.display.set_mode(((WORLD_X * TILESIZE * SCALETILE) + 10, (WORLD_Y * TILESIZE * SCALETILE) + 10), flags=pygame.FULLSCREEN)

pygame.display.set_caption("WFC Algo")

#Create level variable to determine level size from settings file
level = Level(LEVEL_LENGTH, LEVEL_H)
# level = Level(10, 1) #debug/test value

#Create level based on size of 'level' variable
drawLevel = DrawLevel(level)

#Checks is level has benn completely finished
done = False

#Instantly draws level
if interact is False:
    while done is False:
        result = level.waveFunctionCollapse()
        if result == 0:
            done = True

drawLevel.update()
isRunning = True

#Draws level in real time
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
    clock.tick(10)

pygame.quit()
