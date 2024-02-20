from game_logic import make_image_dict
import pygame


# frames per second
FPS = 60
CLOCK = pygame.time.Clock()
GAME_DURATION = 60000
START_TIME = pygame.time.get_ticks()
FONT_LOCATION = "/Users/Adam/Desktop/coding/pfe/tanks/tanks/dogica.ttf"

# create screen
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# title
GAME_TITLE = "TANKS!"
pygame.display.set_caption(GAME_TITLE)

