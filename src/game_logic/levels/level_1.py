import pygame
from game_logic import constants,event_handler,blit_text

def level_one(game_running):
    # game loop
    paused=False
    while game_running:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - constants.START_TIME

        constants.SCREEN.blit(constants.TERRAIN_IMAGES["mud"], (0, 0))

        game_running,paused = event_handler.event_handler_level_one(game_running,paused)

        if paused:
            blit_text.display_text(constants.SCREEN,"PAUSED",constants.MAIN_FONT,constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT/2,(255,0,0))
        else:
            blit_text.display_text(constants.SCREEN,"level 1",constants.MAIN_FONT,constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT/2,(255,0,0))




        pygame.display.update() 
        constants.CLOCK.tick(constants.FPS)