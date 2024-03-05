import pygame
import sys
from game_logic import constants, event_handler, blit_text, level_countdowns, display_ascii, make_enemies, collisions, blit_text
from game_logic.levels import level_one_ascii_units, startup_screen


def level_one(game_running, number_of_enemies):
    # Reset game start time and time left
    constants.START_TIME = pygame.time.get_ticks()
    constants.TIME_LEFT = 60

    # game loop
    paused = False
    # player data
    player_x = constants.CENTRE_X
    player_y = constants.CENTRE_Y+150
    player_alive = True
    player_win = False
    player_score = 0
    # missiles
    player_missiles = 0
    missile_supply = 30
    player_missile_x_positions = []
    player_missile_y_positions = []
    player_win_score = 10
    # explosions
    explosion_x = []
    explosion_y = []
    number_of_explosions = 0
    explosion_anim_list = []
    explosion_frame_tracker = []
    # enemy data
    enemy_kills = 0
    number_of_enemy_units_to_respawn = 5
    enemy_respawn = False
    enemy_tank_x_positions = []
    enemy_tank_y_positions = []
    enemy_tank_accelerations = []
    number_of_enemy_tanks = number_of_enemies
    enemy_tank_x_positions, enemy_tank_y_positions, enemy_tank_accelerations = make_enemies.make_enemies(
        number_of_enemy_tanks, enemy_tank_x_positions, enemy_tank_y_positions, enemy_tank_accelerations, constants.ENEMY_ACCELERATION)

    # movement flags
    move_up, move_down, move_left, move_right = False, False, False, False

    while game_running:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - constants.START_TIME) / \
            1000  # time in seconds

        # Calculate remaining time
        constants.TIME_LEFT = max(60 - int(elapsed_time), 0)

        constants.SCREEN.fill(constants.SCREEN_BKGND)  # black background

        if not paused:
            if player_win:  # blit current screen state in background with transparency
                player_score_message = str(
                    player_score) + " " + constants.WIN_SCORE_LARGE
                blit_text.display_text(constants.SCREEN, player_score_message, constants.BIG_SCORE_FONT,
                                       constants.CENTRE_X, constants.CENTRE_Y-200, constants.STARTUP_SCREEN_EXIT_COLOUR)
                blit_text.display_text(constants.SCREEN, constants.WIN_TEXT_WITH_SCORE, constants.TITLE_FONT,
                                       constants.CENTRE_X, constants.CENTRE_Y-100, constants.STARTUP_SCREEN_EXIT_COLOUR)

                blit_text.display_multiline_text(constants.SCREEN, constants.WIN_TEXT, constants.TITLE_FONT,
                                                 constants.CENTRE_X, constants.CENTRE_Y, constants.WIN_TEXT_COLOUR)
                # press space to continue
                if (elapsed_time*1000) % 1000 < 500:  # Toggles visibility every half-second
                    blit_text.display_text(constants.SCREEN, constants.SPACE_TO_RESTART, constants.SUB_TITLE_FONT,
                                           constants.CENTRE_X, constants.CENTRE_Y+200, constants.STARTUP_SCREEN_EXIT_COLOUR)
                blit_text.display_text(constants.SCREEN, constants.Q_TO_QUIT_TEXT, constants.SUB_TITLE_FONT,
                                       constants.CENTRE_X, constants.CENTRE_Y+280, constants.STARTUP_SCREEN_EXIT_COLOUR)
                game_running = event_handler.event_handler_end_of_level_one(
                    game_running)

            elif player_alive:
                # event handlers
                move_up, move_down, move_left, move_right, paused, player_missiles, player_missile_x_positions, player_missile_y_positions, missile_supply = event_handler.event_handler_level_one(
                    move_up, move_down, move_left, move_right, paused, player_missiles, player_missile_x_positions, player_missile_y_positions, player_x, player_y, missile_supply)

                # player movement
                player_x, player_y = event_handler.player_movement(constants.PLAYER_ACCELERATION, player_x, player_y, move_up, move_down, move_left, move_right,
                                                                   constants.PLAYER_HEIGHT, constants.PLAYER_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_WIDTH, constants.SCREEN_X_MIN, constants.SCREEN_Y_MIN)

                # update enemy tank positions
                enemy_tank_x_positions, enemy_tank_y_positions, enemy_tank_accelerations = make_enemies.update_enemy_tank_positions(
                    number_of_enemy_tanks, enemy_tank_accelerations, enemy_tank_x_positions, enemy_tank_y_positions)

                # blit enemy tanks
                make_enemies.draw_enemy_tanks(
                    number_of_enemy_tanks, enemy_tank_x_positions, enemy_tank_y_positions)

                # update player missile positions
                player_missiles, player_missile_x_positions, player_missile_y_positions = event_handler.player_missile_update(
                    player_missiles, player_missile_x_positions, player_missile_y_positions)

                # explosions
                explosion_frame_tracker = event_handler.manage_explosions(
                    number_of_explosions, explosion_frame_tracker, explosion_x, explosion_y)

                # player_missile to enemy_tank collisions
                number_of_enemy_tanks, enemy_tank_x_positions, enemy_tank_y_positions, player_missiles, player_missile_x_positions, player_missile_y_positions, number_of_explosions, explosion_frame_tracker, explosion_x, explosion_y, player_score, enemy_kills = event_handler.manage_missile_collisions(
                    number_of_enemy_tanks, enemy_tank_x_positions, enemy_tank_y_positions, player_missiles, player_missile_x_positions, player_missile_y_positions, number_of_explosions, explosion_frame_tracker, explosion_x, explosion_y, player_score, enemy_kills)

                # enemy respawn
                # print("enemy kills:", enemy_kills) # only showing one tank respawn visually
                if enemy_kills >= 3:
                    enemy_tank_x_positions, enemy_tank_y_positions, enemy_tank_accelerations = make_enemies.make_enemies(
                        number_of_enemy_units_to_respawn, enemy_tank_x_positions, enemy_tank_y_positions, enemy_tank_accelerations, constants.ENEMY_ACCELERATION)

                    enemy_kills = 0
                    number_of_enemy_tanks += number_of_enemy_units_to_respawn

                # blit player position
                display_ascii.display_unit(
                    level_one_ascii_units.player_tank["straight"], constants.PLAYER_TANK_COLOUR, player_x, player_y, constants.CHAR_SPACING_X, constants.CHAR_SPACING_Y)
                # display_ascii.display_terrain(level_one_ascii_units.terrain["mud"],(200,0,0),0,0,-1,-1 )

                # blit score /time /missile supply
                blit_text.display_text(constants.SCREEN, constants.PLAYER_SCORE+" "+str(player_score), constants.MAIN_FONT,
                                       constants.SCORE_X, constants.SCORE_Y, constants.SCORE_COLOUR)
                # blit score / kills / time /missile supply
                blit_text.display_text(constants.SCREEN, constants.TIME_COUNT+" "+str(constants.TIME_LEFT), constants.MAIN_FONT,
                                       constants.TIME_X, constants.TIME_Y, constants.TIME_COLOUR)
                blit_text.display_text(constants.SCREEN, constants.MISSILE_SUPPLY+" "+str(missile_supply), constants.MAIN_FONT,
                                       constants.MISSILE_TEXT_X, constants.MISSILE_TEXT_Y, constants.MISSILE_TEXT_COLOUR)

                if player_score >= player_win_score:
                    player_win = True
                elif missile_supply <= 0:
                    player_alive = False

            elif not player_alive:
                blit_text.display_text(constants.SCREEN, constants.GAME_OVER_TEXT, constants.TITLE_FONT,
                                       constants.CENTRE_X, constants.CENTRE_Y-90, constants.STARTUP_SCREEN_EXIT_COLOUR)
                if missile_supply <= 0:
                    blit_text.display_text(constants.SCREEN, constants.NO_MISSILES_TEXT, constants.SUB_TITLE_FONT,
                                           constants.CENTRE_X, constants.CENTRE_Y-30, constants.STARTUP_SCREEN_EXIT_COLOUR)

                blit_text.display_multiline_text(constants.SCREEN, constants.DEFEAT_TEXT, constants.SUB_TITLE_FONT,
                                                 constants.CENTRE_X, constants.CENTRE_Y+30, constants.WIN_TEXT_COLOUR)
                # press space to continue
                if (elapsed_time*1000) % 1000 < 500:  # Toggles visibility every half-second
                    blit_text.display_text(constants.SCREEN, constants.SPACE_TO_RESTART, constants.SUB_TITLE_FONT,
                                           constants.CENTRE_X, constants.CENTRE_Y+200, constants.STARTUP_SCREEN_EXIT_COLOUR)
                blit_text.display_text(constants.SCREEN, constants.Q_TO_QUIT_TEXT, constants.SUB_TITLE_FONT,
                                       constants.CENTRE_X, constants.CENTRE_Y+280, constants.STARTUP_SCREEN_EXIT_COLOUR)
                game_running = event_handler.event_handler_end_of_level_one(
                    game_running)

        elif paused:
            blit_text.display_text(constants.SCREEN, "PAUSED", constants.MAIN_FONT,
                                   constants.CENTRE_X, constants.CENTRE_Y, constants.PAUSED_TEXT_COLOUR)
            move_up, move_down, move_left, move_right, paused, player_missiles, player_missile_x_positions, player_missile_y_positions, missile_supply = event_handler.event_handler_level_one(
                move_up, move_down, move_left, move_right, paused, player_missiles, player_missile_x_positions, player_missile_y_positions, player_x, player_y, missile_supply)

        pygame.display.update()
        constants.CLOCK.tick(constants.FPS)
