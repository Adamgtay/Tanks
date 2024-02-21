import pygame
from game_logic import load_music
from game_logic.levels import level_1
from pygame import mixer

pygame.init()
load_music.load_music("/Users/Adam/Desktop/coding/games/Tanks/assets/sound/main-theme.wav")
game_running = True

level_1.level_one(game_running)

