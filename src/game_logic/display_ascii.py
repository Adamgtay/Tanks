import pygame
from game_logic import blit_text, constants

def display_unit(unit,colour,x,y):
    start_y = y
    for line in unit:
        start_x = x
        for char in line:
            blit_text.display_text(constants.SCREEN,char,constants.MAIN_FONT,start_x,start_y,colour)
            char_width, char_height = constants.MAIN_FONT.size(char)
            start_x += char_width
            # need to have spacing between each character and new line at end of each line
        start_y+=char_height
    return start_y,start_x        
