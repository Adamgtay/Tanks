import pygame
from game_logic import constants, event_handler, blit_text


def startup_screen(game_running):
    # game loop
    while game_running:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - constants.START_TIME

        blit_text.display_text(constants.SCREEN, constants.STARTUP_SCREEN_EXIT, constants.MAIN_FONT,
                               constants.CENTRE_X, constants.CENTRE_Y+100, constants.STARTUP_SCREEN_EXIT_COLOUR)
        blit_text.display_text(constants.SCREEN, constants.GAME_TITLE, constants.MAIN_FONT,
                               constants.CENTRE_X, constants.CENTRE_Y, constants.GAME_TITLE_COLOUR)

        game_running = event_handler.event_handler_startup(game_running)

        pygame.display.update()
        constants.CLOCK.tick(constants.FPS)
