import pygame
import sys
from game_logic.levels import level_1, level_one_ascii_units
from game_logic import constants, display_ascii


def event_handler_startup(game_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quit
            game_running = False
            # Quit Pygame
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  # move to level one
            if event.key == pygame.K_SPACE:
                level_1.level_one(game_running)
    return game_running


def event_handler_level_one(move_up, move_down, move_left, move_right, paused, player_missiles, player_missile_x_positions, player_missile_y_positions, player_x, player_y):
    # player height and width not correct
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
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
            elif event.key == pygame.K_SPACE:
                player_missiles += 1
                player_missile_x_positions.append(
                    player_x + (constants.PLAYER_WIDTH/2))
                player_missile_y_positions.append(player_y)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up = False
            elif event.key == pygame.K_DOWN:
                move_down = False
            elif event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_LEFT:
                move_left = False

    return move_up, move_down, move_left, move_right, paused, player_missiles, player_missile_x_positions, player_missile_y_positions


def player_movement(player_speed, player_x, player_y, move_up, move_down, move_left, move_right, player_height, player_width, screen_height, screen_width, screen_x_min, screen_y_min):
    # Update tank's position continuously based on movement flags
    if move_up:
        player_y -= player_speed
        if player_y <= screen_y_min:
            player_y = screen_y_min
    if move_down:
        player_y += player_speed
        if player_y + player_height >= screen_height:
            player_y = screen_height - player_height
    if move_right:
        player_x += player_speed
        if player_x + player_width >= screen_width:
            player_x = screen_width - player_width
    if move_left:
        player_x -= player_speed
        if player_x <= screen_x_min:
            player_x = screen_x_min

    return player_x, player_y


def player_missile_update(player_missiles, player_missile_x_positions, player_missile_y_positions, explosion_x, explosion_y, number_of_explosions, explosion_anim_list, missile_explode_anim, explosion_frame_tracker):
    if player_missiles > 0:
        for i in range(player_missiles):
            display_ascii.display_unit(level_one_ascii_units.player_missile["missile"], constants.PLAYER_TANK_COLOUR,
                                       player_missile_x_positions[i], player_missile_y_positions[i], constants.CHAR_SPACING_X, constants.CHAR_SPACING_Y)
            player_missile_y_positions[i] -= constants.MISSILE_ACCELERATION
            if player_missile_y_positions[i] <= constants.SCREEN_Y_MIN + 150:
                player_missiles -= 1
                explosion_x.append(
                    player_missile_x_positions[i] - (constants.EXPLOSION_WIDTH/2))
                explosion_y.append(
                    player_missile_y_positions[i] - (constants.EXPLOSION_HEIGHT/2))
                number_of_explosions += 1
                explosion_anim_list.append(missile_explode_anim)
                explosion_frame_tracker.append(0)
                del player_missile_y_positions[i]
                del player_missile_x_positions[i]
                break

    return player_missiles, player_missile_x_positions, player_missile_y_positions, explosion_x, explosion_y, number_of_explosions, explosion_anim_list, explosion_frame_tracker


def manage_explosions(number_of_explosions, explosion_frame_tracker, explosion_x, explosion_y):
    if number_of_explosions > 0:
        for i in range(number_of_explosions):
            if explosion_frame_tracker[i] < len(level_one_ascii_units.missile_explode_anim):

                display_ascii.display_unit(
                    level_one_ascii_units.missile_explode_anim[explosion_frame_tracker[i]], constants.ENEMY_TANK_COLOUR, explosion_x[i], explosion_y[i], constants.CHAR_SPACING_X, constants.CHAR_SPACING_Y)

                explosion_frame_tracker[i] += 1
    return explosion_frame_tracker
