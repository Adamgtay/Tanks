from game_logic import constants, display_ascii
from game_logic.levels import level_one_ascii_units


def make_enemies(number_of_enemy_tanks, enemy_tank_x_positions, enemy_tank_y_positions, enemy_tank_accelerations, enemy_speed, enemy_spacing_x, enemy_spacing_y):
    x_pos = 25
    y_pos = 25
    for i in range(number_of_enemy_tanks):
        enemy_tank_x_positions.append(x_pos)
        x_pos += enemy_spacing_x
        enemy_tank_y_positions.append(y_pos)
        y_pos += enemy_spacing_y
        enemy_tank_accelerations.append(enemy_speed)

    return enemy_tank_x_positions, enemy_tank_y_positions, enemy_tank_accelerations


def update_enemy_tank_positions(number_of_enemy_tanks, enemy_tank_accelerations, enemy_tank_x_positions, enemy_tank_y_positions):
    for i in range(number_of_enemy_tanks):
        # if tank is moving left to right and inside screen limit
        if enemy_tank_accelerations[i] > 0 and enemy_tank_x_positions[i] < constants.SCREEN_WIDTH:
            enemy_tank_x_positions[i] += enemy_tank_accelerations[i]
            # if x pos at screen max width limit
            if enemy_tank_x_positions[i] + constants.ENEMY_WIDTH >= constants.SCREEN_WIDTH:
                enemy_tank_x_positions[i] = constants.SCREEN_WIDTH - \
                    constants.ENEMY_WIDTH
                enemy_tank_y_positions[i] += constants.ENEMY_HEIGHT
                enemy_tank_accelerations[i] = - enemy_tank_accelerations[i]
                display_ascii.display_unit(level_one_ascii_units.enemy_tank["straight"], constants.ENEMY_TANK_COLOUR,
                                           enemy_tank_x_positions[i], enemy_tank_y_positions[i], constants.CHAR_SPACING_X, constants.CHAR_SPACING_Y)

            else:
                display_ascii.display_unit(level_one_ascii_units.enemy_tank["straight"], constants.ENEMY_TANK_COLOUR,
                                           enemy_tank_x_positions[i], enemy_tank_y_positions[i], constants.CHAR_SPACING_X, constants.CHAR_SPACING_Y)
        elif enemy_tank_accelerations[i] < 0 and enemy_tank_y_positions[i] > constants.SCREEN_X_MIN:
            enemy_tank_x_positions[i] += enemy_tank_accelerations[i]
            # if x pos at screen min limit
            if enemy_tank_x_positions[i] <= constants.SCREEN_X_MIN:
                enemy_tank_x_positions[i] = constants.SCREEN_X_MIN
                enemy_tank_y_positions[i] += constants.ENEMY_HEIGHT
                enemy_tank_accelerations[i] = - enemy_tank_accelerations[i]
                display_ascii.display_unit(level_one_ascii_units.enemy_tank["straight"], constants.ENEMY_TANK_COLOUR,
                                           enemy_tank_x_positions[i], enemy_tank_y_positions[i], constants.CHAR_SPACING_X, constants.CHAR_SPACING_Y)
            else:
                display_ascii.display_unit(level_one_ascii_units.enemy_tank["straight"], constants.ENEMY_TANK_COLOUR,
                                           enemy_tank_x_positions[i], enemy_tank_y_positions[i], constants.CHAR_SPACING_X, constants.CHAR_SPACING_Y)

    return enemy_tank_x_positions, enemy_tank_y_positions, enemy_tank_accelerations, number_of_enemy_tanks
