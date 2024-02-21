

# Function to display text with a specified font
def display_text(screen,text, font,x, y,color):
    text_surface = font.render(text, True, color)
    text_width, text_height = text_surface.get_size()
    text_x_centre = text_width/2
    text_y_centre = text_height/2
    screen.blit(text_surface,(x-text_x_centre,y-text_y_centre))
