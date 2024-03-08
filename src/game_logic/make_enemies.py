from game_logic import constants, display_ascii
from game_logic.levels import level_one_ascii_units
import random


def make_enemies(number_of_enemy_tanks, enemy_tank_x_positions, enemy_tank_y_positions, enemy_tank_accelerations, enemy_speed):
    y_pos = 25
    for i in range(number_of_enemy_tanks):
        x_pos = random.randint(constants.SCREEN_X_MIN,
                               constants.SCREEN_WIDTH-constants.ENEMY_WIDTH)
        enemy_tank_x_positions.append(x_pos)
        y_pos = random.randint(constants.SCREEN_Y_MIN,
                               constants.SCREEN_HEIGHT-800)

        enemy_tank_y_positions.append(y_pos)
        enemy_tank_accelerations.append(enemy_speed)

    return enemy_tank_x_positions, enemy_tank_y_positions, enemy_tank_accelerations


def update_enemy_tank_positions(number_of_enemy_tanks, enemy_tank_accelerations, enemy_tank_x_positions, enemy_tank_y_positions, player_alive):
    for i in range(number_of_enemy_tanks):
        if enemy_tank_accelerations[i] > 0 and enemy_tank_x_positions[i] < constants.SCREEN_WIDTH:
            enemy_tank_x_positions[i] += enemy_tank_accelerations[i]
            if enemy_tank_x_positions[i] + constants.ENEMY_WIDTH >= constants.SCREEN_WIDTH:
                enemy_tank_x_positions[i] = constants.SCREEN_WIDTH - \
                    constants.ENEMY_WIDTH
                enemy_tank_y_positions[i] += constants.ENEMY_HEIGHT
                enemy_tank_accelerations[i] = -enemy_tank_accelerations[i]
        elif enemy_tank_accelerations[i] < 0 and enemy_tank_x_positions[i] > constants.SCREEN_X_MIN:
            enemy_tank_x_positions[i] += enemy_tank_accelerations[i]
            if enemy_tank_x_positions[i] <= constants.SCREEN_X_MIN:
                enemy_tank_x_positions[i] = constants.SCREEN_X_MIN
                enemy_tank_y_positions[i] += constants.ENEMY_HEIGHT
                enemy_tank_accelerations[i] = -enemy_tank_accelerations[i]
        if enemy_tank_y_positions[i] >= constants.SCREEN_HEIGHT:
            player_alive = False

    return enemy_tank_x_positions, enemy_tank_y_positions, enemy_tank_accelerations, player_alive


def draw_enemy_tanks(number_of_enemy_tanks, enemy_tank_x_positions, enemy_tank_y_positions):
    for i in range(number_of_enemy_tanks):
        display_ascii.display_unit(level_one_ascii_units.enemy_tank["straight"], constants.ENEMY_TANK_COLOUR,
                                   enemy_tank_x_positions[i], enemy_tank_y_positions[i], constants.CHAR_SPACING_X, constants.CHAR_SPACING_Y)
