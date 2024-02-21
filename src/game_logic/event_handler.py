import pygame
from game_logic.levels import level_1

def event_handler_startup(game_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    level_1.level_one(game_running)    
    return game_running


def event_handler_level_one(game_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    return game_running

  