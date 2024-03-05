import pygame
from game_logic import constants, event_handler, blit_text
from game_logic.levels import level_1


def pre_level_screen(game_running):
    countdown = [5, 4, 3, 2, 1]
    last_update_time = pygame.time.get_ticks()  # Initialize timer

    # game loop
    while game_running:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - constants.START_TIME) / \
            1000  # time in seconds
        constants.SCREEN.fill(constants.SCREEN_BKGND)  # black background

        # motivation line!
        blit_text.display_text(constants.SCREEN, constants.MOTIVATE_TEXT, constants.TITLE_FONT,
                               constants.CENTRE_X, constants.CENTRE_Y-30, constants.GAME_TITLE_COLOUR)

        if elapsed_time >= 6:
            level_1.level_one(game_running, 5)  # Decrement every second
        elif elapsed_time >= 5:
            blit_text.display_text(constants.SCREEN, str(countdown[4]), constants.BIG_SCORE_FONT,
                                   constants.CENTRE_X, constants.CENTRE_Y + 200, constants.STARTUP_SCREEN_EXIT_COLOUR)
        elif elapsed_time >= 4:
            blit_text.display_text(constants.SCREEN, str(countdown[3]), constants.BIG_SCORE_FONT,
                                   constants.CENTRE_X, constants.CENTRE_Y + 200, constants.STARTUP_SCREEN_EXIT_COLOUR)
        elif elapsed_time >= 3:
            blit_text.display_text(constants.SCREEN, str(countdown[2]), constants.BIG_SCORE_FONT,
                                   constants.CENTRE_X, constants.CENTRE_Y + 200, constants.STARTUP_SCREEN_EXIT_COLOUR)
        elif elapsed_time >= 2:
            blit_text.display_text(constants.SCREEN, str(countdown[1]), constants.BIG_SCORE_FONT,
                                   constants.CENTRE_X, constants.CENTRE_Y + 200, constants.STARTUP_SCREEN_EXIT_COLOUR)
        elif elapsed_time >= 1:
            blit_text.display_text(constants.SCREEN, str(countdown[0]), constants.BIG_SCORE_FONT,
                                   constants.CENTRE_X, constants.CENTRE_Y + 200, constants.STARTUP_SCREEN_EXIT_COLOUR)

        print(elapsed_time)
        game_running = event_handler.event_handler_pre_level_screen(
            game_running)

        pygame.display.update()
        constants.CLOCK.tick(constants.FPS)
