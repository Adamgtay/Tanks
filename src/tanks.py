import pygame
from game_logic import load_music
from game_logic.levels import startup_screen
from pygame import mixer

pygame.init()
pygame.font.init()
pygame.display.init()



load_music.load_music("/Users/Adam/Desktop/coding/games/Tanks/assets/sound/main-theme.wav")
game_running = True

startup_screen.startup_screen(game_running)
