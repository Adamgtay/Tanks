import pygame
from game_logic import constants,event_handler,blit_text

def level_one(game_running):
    # game loop
    while game_running:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - constants.START_TIME

        constants.SCREEN.fill((255,255,255))
        blit_text.display_text(constants.SCREEN,"level 1",constants.MAIN_FONT,constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT/2,(255,0,0))


        game_running = event_handler.event_handler_level_one(game_running)


        pygame.display.update() 
        constants.CLOCK.tick(constants.FPS)