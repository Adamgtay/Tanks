import pygame
from game_logic import constants
from game_logic import event_handler

def level_one(game_running):
    # game loop
    while game_running:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - constants.START_TIME

        game_running = event_handler.event_handler(game_running)

        pygame.display.update() 
        constants.CLOCK.tick(constants.FPS)