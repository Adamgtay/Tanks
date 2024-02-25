import pygame,sys
from game_logic.levels import level_1
from game_logic import constants

def event_handler_startup(game_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # quit
            game_running = False
            # Quit Pygame
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # move to level one
                if event.key == pygame.K_SPACE:
                    level_1.level_one(game_running)    
    return game_running


def event_handler_level_one(game_running,paused,player_x,player_y,move_up,move_down,move_left,move_right):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
            elif event.key == pygame.K_UP:
                move_up = True
            elif event.key == pygame.K_DOWN:
                move_down = True
            elif event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up = False
            elif event.key == pygame.K_DOWN:
                move_down = False
            elif event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_LEFT:
                move_left = False
    # Update tank's position continuously based on movement flags
    if move_up:
        player_y -= constants.PLAYER_ACCELERATION
    if move_down:
        player_y += constants.PLAYER_ACCELERATION
    if move_right:
        player_x += constants.PLAYER_ACCELERATION
    if move_left:
        player_x -= constants.PLAYER_ACCELERATION            

    return game_running,paused,player_x,player_y,move_up,move_down,move_left,move_right

  