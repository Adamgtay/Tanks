import pygame
from game_logic import constants,event_handler,blit_text,level_countdowns,display_ascii,make_enemies
from game_logic.levels import level_one_ascii_units



def level_one(game_running):
    # game loop
    paused=False
    player_x = constants.CENTRE_X
    player_y = constants.CENTRE_Y+150
    player_alive = True
    player_win = False
    # missiles
    player_missiles =0
    player_missile_x_positions=[]
    player_missile_y_positions=[]

    # enemy data
    enemy_tank_x_positions = []
    enemy_tank_y_positions = []
    enemy_tank_accelerations = []
    number_of_enemy_tanks = 5
    enemy_tank_x_positions, enemy_tank_y_positions, enemy_tank_accelerations = make_enemies.make_enemies(number_of_enemy_tanks,enemy_tank_x_positions,enemy_tank_y_positions,enemy_tank_accelerations,constants.ENEMY_ACCELERATION,constants.ENEMY_X_SPACING,0)
    
    
    # Define movement flags
    move_up, move_down,move_left,move_right = False,False,False,False

    while game_running:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - constants.START_TIME) /1000 # time in seconds

        constants.SCREEN.fill(constants.SCREEN_BKGND) # black background

        if not paused:
            if player_win:
                blit_text.display_text(constants.SCREEN,"YOU WIN",constants.CAPTION_FONT,constants.CENTRE_X,constants.CENTRE_Y,constants.PAUSED_TEXT_COLOUR)

            elif player_alive: 
                # event handlers
                move_up,move_down,move_left,move_right,paused,player_missiles,player_missile_x_positions,player_missile_y_positions = event_handler.event_handler_level_one(move_up,move_down,move_left,move_right,paused,player_missiles,player_missile_x_positions,player_missile_y_positions,player_x,player_y)
                
                #player movement
                player_x,player_y= event_handler.player_movement(constants.PLAYER_ACCELERATION,player_x,player_y,move_up,move_down,move_left,move_right,constants.PLAYER_HEIGHT,constants.PLAYER_WIDTH,constants.SCREEN_HEIGHT,constants.SCREEN_WIDTH,constants.SCREEN_X_MIN,constants.SCREEN_Y_MIN)

                # update player missile positions
                player_missiles,player_missile_x_positions,player_missile_y_positions = event_handler.player_missile_update(player_missiles,player_missile_x_positions,player_missile_y_positions)

                # update enemy tank positions
                enemy_tank_x_positions,enemy_tank_y_positions,enemy_tank_accelerations = make_enemies.update_enemy_tank_positions(number_of_enemy_tanks,enemy_tank_accelerations,enemy_tank_x_positions,enemy_tank_y_positions)

                display_ascii.display_unit(level_one_ascii_units.player_tank["straight"],constants.PLAYER_TANK_COLOUR,player_x,player_y,constants.CHAR_SPACING_X,constants.CHAR_SPACING_Y)
                display_ascii.display_unit(level_one_ascii_units.enemy_tank["straight"],constants.ENEMY_TANK_COLOUR,constants.CENTRE_X,constants.CENTRE_Y,constants.CHAR_SPACING_X,constants.CHAR_SPACING_Y)
                #display_ascii.display_terrain(level_one_ascii_units.terrain["mud"],(200,0,0),0,0,-1,-1 )


        
        elif paused:
            blit_text.display_text(constants.SCREEN,"PAUSED",constants.MAIN_FONT,constants.CENTRE_X,constants.CENTRE_Y,constants.PAUSED_TEXT_COLOUR)
            move_up,move_down,move_left,move_right,paused = event_handler.event_handler_level_one(move_up,move_down,move_left,move_right,paused)

        



        pygame.display.update() 
        constants.CLOCK.tick(constants.FPS)