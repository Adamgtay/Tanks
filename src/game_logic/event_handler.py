import pygame

def event_handler(game_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    return game_running        