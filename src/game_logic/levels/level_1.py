import pygame
from game_logic import constants,event_handler,blit_text,level_countdowns,display_ascii
from game_logic.levels import level_one_ascii_units


def level_one(game_running):
    # game loop
    paused=False
    while game_running:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - constants.START_TIME) /1000

        constants.SCREEN.blit(constants.TERRAIN_IMAGES["mud"], (0, 0))

        game_running,paused = event_handler.event_handler_level_one(game_running,paused)

        if not paused:
            display_ascii.display_unit(level_one_ascii_units.player_tank["straight"])
            level_countdowns.level_one_countdown(elapsed_time)

        else:
            blit_text.display_text(constants.SCREEN,"PAUSED",constants.MAIN_FONT,constants.CENTRE_X,constants.CENTRE_Y,(255,0,0))

        pygame.display.update() 
        constants.CLOCK.tick(constants.FPS)