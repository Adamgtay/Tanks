from game_logic import constants, blit_text
from game_logic.levels import level_1


def display_text(screen, text, font, x, y, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def display_multiline_text(screen, text, font, x, y, color):
    # Split the text into lines based on newline character
    lines = text.split('\n')
    line_spacing = font.get_linesize()  # Get the height of each line

    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(midtop=(x, y + i * line_spacing))
        screen.blit(text_surface, text_rect)


def display_countdown(elapsed_time, countdown, game_running, number_of_enemies_start_next_level, y_offset):
    if elapsed_time >= 6:
        # Decrement every second
        level_1.level_one(game_running, number_of_enemies_start_next_level)
    elif elapsed_time >= 1:
        index = int(0 + elapsed_time-1)
        blit_text.display_text(constants.SCREEN, str(countdown[index]), constants.BIG_SCORE_FONT,
                               constants.CENTRE_X, constants.CENTRE_Y + y_offset, constants.STARTUP_SCREEN_EXIT_COLOUR)
