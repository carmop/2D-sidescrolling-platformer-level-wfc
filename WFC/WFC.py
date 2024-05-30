import pygame
from Level import Level
from Draw import DrawLevel
from Settings import *


def run(levels_to_generate, use_weight, use_ac, interactable, key_input, save_levels):
    """Brings WFC algorithm and Pygame visualization together through 
    instantiating objects necessary for generation and then calling the
    waveFunctionCollapse() function to perform operations for level generation. 
    
    """

    # variables for defining how levels will be displayed
    interact = interactable
    key_press = key_input

    for i in range(levels_to_generate):
        print("GENERATION:",i)
        print("LEVELS LEFT TO GENERATE:", levels_to_generate - i)
        pygame.init()
        clock = pygame.time.Clock()

        # Create surface object, base on size of level and based on level length and y size of 1 tile
        displaySurface = pygame.display.set_mode(size=((LEVEL_LENGTH * X_TILE * SCALING), (LEVEL_H * Y_TILE * SCALING)))

        pygame.display.set_caption("Wave Function Collapse in Platformer Level Generation")



        # Create level variable to determine level size from settings file
        level = Level(LEVEL_LENGTH, LEVEL_H, use_ac, use_weight)


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
                            id=str(drawLevel.update())
                            print(id)

            if interact is True and key_press is False:
                if not done:
                    result = level.waveFunctionCollapse()
                    if result == 0:
                        done = True
                    id=str(drawLevel.update())
                    # print(id)

            drawLevel.draw(displaySurface)

            pygame.display.flip()
            clock.tick(60) # Speed of tile collapsing animation when `key_press` is False and `interact` is True
            if done and save_levels: 

                pygame.image.save(displaySurface,f"result_images/res{id}.png")
                isRunning = False

        pygame.quit()
