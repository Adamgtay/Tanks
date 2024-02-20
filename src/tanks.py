import pygame
from game_logic import constants
from game_logic import ascii_tanks
from game_logic import event_handler
from game_logic.levels import level_one
from game_logic import music
from pygame import mixer

pygame.init()

music.load_music("/Users/Adam/Desktop/coding/games/Tanks/assets/sound/main-theme.wav")

game_running = True

level_one.level_one(game_running)