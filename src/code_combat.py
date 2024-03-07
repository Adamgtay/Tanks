import pygame
import sys
from game_logic import load_music, constants
from game_logic.levels import startup_screen
from pygame import mixer

pygame.init()
pygame.font.init()
pygame.display.init()
pygame.mixer.init()

# Load background music
background_music = pygame.mixer.Sound(constants.MAIN_MUSIC_LOCATION)
# Set volume level
background_music.set_volume(0.5)  # Adjust volume as needed

# Play background music on loop
background_music.play(loops=-1)

game_running = True

startup_screen.startup_screen(game_running)
