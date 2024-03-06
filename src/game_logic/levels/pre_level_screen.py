import pygame
from game_logic import constants, event_handler, blit_text
from game_logic.levels import level_1


def pre_level_screen(game_running):
    countdown = [5, 4, 3, 2, 1]

    # game loop
    while game_running:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - constants.START_TIME) / \
            1000  # time in seconds
        constants.SCREEN.fill(constants.SCREEN_BKGND)  # black background

        # motivation line!
        blit_text.display_text(constants.SCREEN, constants.MOTIVATE_TEXT, constants.TITLE_FONT,
                               constants.CENTRE_X, constants.CENTRE_Y-30, constants.GAME_TITLE_COLOUR)

        blit_text.display_countdown(
            elapsed_time, countdown, game_running, 5, 200)

        game_running = event_handler.event_handler_pre_level_screen(
            game_running)

        pygame.display.update()
        constants.CLOCK.tick(constants.FPS)
