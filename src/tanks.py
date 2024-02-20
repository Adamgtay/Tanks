import pygame
from game_logic import constants
from game_logic.ascii_graphics import ascii_tanks
from game_logic import event_handler
from game_logic.levels import level_one
from game_logic import load_music
from pygame import mixer

pygame.init()

load_music.load_music("/Users/Adam/Desktop/coding/games/Tanks/assets/sound/main-theme.wav")

game_running = True

level_one.level_one(game_running)