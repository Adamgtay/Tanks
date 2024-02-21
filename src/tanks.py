import pygame
from game_logic.ascii_graphics import ascii_tanks
from game_logic.levels import level_one
from game_logic import load_music

pygame.init()

load_music.load_music("/Users/Adam/Desktop/coding/games/Tanks/assets/sound/main-theme.wav")

# Set up font
ascii_font = pygame.font.Font("/Users/Adam/Desktop/coding/games/Tanks/assets/fonts/dogica.ttf", 36)

game_running = True

level_one.level_one(game_running)