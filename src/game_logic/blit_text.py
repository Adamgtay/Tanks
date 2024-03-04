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
