import pygame,sys
from game_logic import load_music,constants
from game_logic.levels import startup_screen
from pygame import mixer

pygame.init()
pygame.font.init()
pygame.display.init()
load_music.load_music(constants.MAIN_MUSIC_LOCATION)
game_running = True

startup_screen.startup_screen(game_running)


