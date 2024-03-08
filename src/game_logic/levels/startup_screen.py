import pygame
from game_logic import constants, event_handler, blit_text


def startup_screen(game_running):

    # game loop
    while game_running:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - constants.START_TIME
        constants.SCREEN.fill(constants.SCREEN_BKGND)  # black background

        blit_text.display_text(constants.SCREEN, constants.GAME_TITLE_1, constants.BIG_TITLE_FONT,
                               constants.CENTRE_X, constants.CENTRE_Y-100, constants.GAME_TITLE_COLOUR)
        blit_text.display_text(constants.SCREEN, constants.GAME_TITLE_2, constants.TITLE_FONT,
                               constants.CENTRE_X, constants.CENTRE_Y-30, constants.GAME_TITLE_COLOUR)
        # dotted
        blit_text.display_text(constants.SCREEN, constants.DOTTED_LINE, constants.TITLE_FONT,
                               constants.CENTRE_X, constants.CENTRE_Y-150, constants.GAME_TITLE_COLOUR)
        blit_text.display_text(constants.SCREEN, constants.DOTTED_LINE, constants.TITLE_FONT,
                               constants.CENTRE_X, constants.CENTRE_Y+10, constants.GAME_TITLE_COLOUR)
        # press space to continue
        if elapsed_time % 1000 < 500:  # Toggles visibility every half-second
            blit_text.display_text(constants.SCREEN, constants.STARTUP_SCREEN_EXIT, constants.SUB_TITLE_FONT,
                                   constants.CENTRE_X, constants.CENTRE_Y+270, constants.STARTUP_SCREEN_EXIT_COLOUR)
        # movement controls
        blit_text.display_multiline_text(constants.SCREEN, constants.STARTUP_SCREEN_CONTROLS, constants.CAPTION_FONT,
                                         constants.CENTRE_X, constants.CENTRE_Y+80, constants.STARTUP_SCREEN_CONTROLS_COLOUR)

        game_running = event_handler.event_handler_startup(game_running)

        pygame.display.update()
        constants.CLOCK.tick(constants.FPS)
