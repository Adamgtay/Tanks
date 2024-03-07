import pygame
import sys
from game_logic.levels import level_1, level_one_ascii_units, pre_level_screen
from game_logic import constants, display_ascii, collisions, blit_text, load_music


def event_handler_startup(game_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quit
            game_running = False
            # Quit Pygame
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  # move to level one
            if event.key == pygame.K_SPACE:
                pre_level_screen.pre_level_screen(game_running)
            if event.key == pygame.K_q:
                game_running = False
                # Quit Pygame
                pygame.quit()
                sys.exit()

    return game_running


def event_handler_pre_level_screen(game_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quit
            game_running = False
            # Quit Pygame
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  # move to level one
            if event.key == pygame.K_q:
                game_running = False
                # Quit Pygame
                pygame.quit()
                sys.exit()

    return game_running


def event_handler_end_of_level_one(game_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quit
            game_running = False
            # Quit Pygame
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  # move to level one
            if event.key == pygame.K_RETURN:
                level_1.level_one(game_running, 5)
            if event.key == pygame.K_q:
                game_running = False
                # Quit Pygame
                pygame.quit()
                sys.exit()

    return game_running


def event_handler_level_one(move_up, move_down, move_left, move_right, paused, player_missiles, player_missile_x_positions, player_missile_y_positions, player_x, player_y, missile_supply):
    # player height and width not correct
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
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
                missile_supply -= 1
                player_missile_x_positions.append(
                    player_x + (constants.PLAYER_WIDTH/2))
                player_missile_y_positions.append(player_y)
                load_music.load_music(constants.LAUNCH_SOUND)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up = False
            elif event.key == pygame.K_DOWN:
                move_down = False
            elif event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_LEFT:
                move_left = False

    return move_up, move_down, move_left, move_right, paused, player_missiles, player_missile_x_positions, player_missile_y_positions, missile_supply


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


def player_missile_update(player_missiles, player_missile_x_positions, player_missile_y_positions):
    if player_missiles > 0:
        for i in range(player_missiles):
            blit_text.display_text(constants.SCREEN, display_ascii.generate_random_character(
            ), constants.MISSILE_FONT, player_missile_x_positions[i], player_missile_y_positions[i], constants.PLAYER_TANK_COLOUR)
            player_missile_y_positions[i] -= constants.MISSILE_ACCELERATION
            if player_missile_y_positions[i] <= constants.SCREEN_Y_MIN:
                player_missiles -= 1
                # print("player missiles", player_missiles)
                del player_missile_y_positions[i]
                del player_missile_x_positions[i]
                break

    return player_missiles, player_missile_x_positions, player_missile_y_positions


def enenmy_missiles_initiate(player_x, number_of_enemy_tanks, enemy_tank_x_positions, enemy_tank_y_positions, enemy_missile_x_positions, enemy_missile_y_positions, number_of_enemy_missiles):
    for position in range(number_of_enemy_tanks):
        if enemy_tank_x_positions[position] == player_x and enemy_tank_y_positions[position] <= (constants.SCREEN_HEIGHT-constants.PLAYER_HEIGHT):
            enemy_missile_x_positions.append(
                enemy_tank_x_positions[position])
            enemy_missile_y_positions.append(
                enemy_tank_y_positions[position])
            number_of_enemy_missiles += 1
    return number_of_enemy_tanks, enemy_tank_x_positions, enemy_tank_y_positions, enemy_missile_x_positions, enemy_missile_y_positions, number_of_enemy_missiles


def enemy_missile_update(player_missiles, player_missile_x_positions, player_missile_y_positions):
    if player_missiles > 0:
        for i in range(player_missiles):
            blit_text.display_text(constants.SCREEN, display_ascii.generate_random_character(
            ), constants.MISSILE_FONT, player_missile_x_positions[i] + (constants.ENEMY_WIDTH/2), player_missile_y_positions[i] + constants.ENEMY_HEIGHT, constants.ENEMY_TANK_COLOUR)
            player_missile_y_positions[i] += constants.MISSILE_ACCELERATION
            if player_missile_y_positions[i] >= constants.SCREEN_HEIGHT:
                player_missiles -= 1
                # print("player missiles", player_missiles)
                del player_missile_y_positions[i]
                del player_missile_x_positions[i]
                break

    return player_missiles, player_missile_x_positions, player_missile_y_positions


def manage_explosions(number_of_explosions, explosion_frame_tracker, explosion_x, explosion_y):
    if number_of_explosions > 0:
        for i in range(number_of_explosions):
            if explosion_frame_tracker[i] < len(level_one_ascii_units.missile_explode_anim):

                display_ascii.display_unit(
                    level_one_ascii_units.missile_explode_anim[explosion_frame_tracker[i]], constants.EXPLOSION_COLOUR, explosion_x[i], explosion_y[i], constants.CHAR_SPACING_X, constants.CHAR_SPACING_Y)
                if explosion_frame_tracker[i] < 9:
                    explosion_frame_tracker[i] += 1
                else:
                    number_of_explosions -= 1
                    del explosion_x[i]
                    del explosion_y[i]
                    del explosion_frame_tracker[i]
                    break

    return explosion_frame_tracker, explosion_x, explosion_y, number_of_explosions


def manage_missile_collisions(number_of_enemy_tanks, enemy_tank_x_positions, enemy_tank_y_positions, player_missiles, player_missile_x_positions, player_missile_y_positions, number_of_explosions, explosion_frame_tracker, explosion_x, explosion_y, player_score, enemy_kills):
    missiles_to_remove = []
    tanks_to_remove = []

    if player_missiles > 0:
        for i in range(player_missiles):
            for j in range(number_of_enemy_tanks):
                if collisions.isCollision(enemy_tank_x_positions[j], enemy_tank_y_positions[j], player_missile_x_positions[i], player_missile_y_positions[i], constants.COLLISION_TOL):
                    player_score += 1
                    enemy_kills += 1
                    number_of_explosions += 1
                    explosion_frame_tracker.append(0)
                    explosion_x.append(enemy_tank_x_positions[j])
                    explosion_y.append(enemy_tank_y_positions[j])
                    missiles_to_remove.append(i)
                    tanks_to_remove.append(j)
                    load_music.load_music(constants.EXPLOSION_SOUND)

                    break

    # Remove collided missiles and enemy tanks
    for i in reversed(missiles_to_remove):
        del player_missile_x_positions[i]
        del player_missile_y_positions[i]

    for j in reversed(tanks_to_remove):
        del enemy_tank_x_positions[j]
        del enemy_tank_y_positions[j]

    return number_of_enemy_tanks - len(tanks_to_remove), enemy_tank_x_positions, enemy_tank_y_positions, player_missiles - len(missiles_to_remove), player_missile_x_positions, player_missile_y_positions, number_of_explosions, explosion_frame_tracker, explosion_x, explosion_y, player_score, enemy_kills


def manage_enemy_missile_collisions(number_of_enemy_missiles, player_x, player_y, enemy_missile_x_positions, enemy_missile_y_positions, explosion_frame_tracker, explosion_x, explosion_y, player_alive, number_of_explosions):
    missiles_to_remove = []
    tanks_to_remove = []
    if number_of_enemy_missiles > 0:
        for i in range(number_of_enemy_missiles):

            if collisions.isCollision(player_x, player_y, enemy_missile_x_positions[i], enemy_missile_y_positions[i], constants.COLLISION_TOL):
                number_of_explosions += 1
                explosion_frame_tracker.append(0)
                explosion_x.append(player_x)
                explosion_y.append(player_y)
                load_music.load_music(constants.EXPLOSION_SOUND)
                player_alive = False

                break

    # Remove collided missiles and player tank
    for i in reversed(missiles_to_remove):
        del enemy_missile_x_positions[i]
        del enemy_missile_y_positions[i]

    for j in reversed(tanks_to_remove):
        del player_x
        del player_y

    return explosion_frame_tracker, explosion_x, explosion_y, player_alive, number_of_explosions
