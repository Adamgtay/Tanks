import pygame
import random

from game_logic import blit_text, constants


def measure_unit_size(unit, char_spacing_x, char_spacing_y):
    unit_height = 0
    unit_width = 0
    max_char_width = 0  # Variable to store the width of the widest character
    # char_count =0

    # Find the width of the widest character
    for line in unit:
        for char in line:
            char_width, _ = constants.MAIN_FONT.size(char)
            if char_width > max_char_width:
                max_char_width = char_width

    # total dimensions of unit with even spacing
    for line in unit:
        unit_width = 0
        for char in line:
            unit_width += max_char_width + char_spacing_x
        unit_height += constants.MAIN_FONT.get_height() + char_spacing_y

    return unit_height, unit_width  # Return the unit dimensions


def display_unit(unit, colour, x, y, char_spacing_x, char_spacing_y):
    start_y = y
    unit_height = 0
    unit_width = 0
    max_char_width = 0  # Variable to store the width of the widest character
    # char_count =0

    # Find the width of the widest character
    for line in unit:
        for char in line:
            char_width, _ = constants.MAIN_FONT.size(char)
            if char_width > max_char_width:
                max_char_width = char_width

    # Display the tank unit with even spacing
    for line in unit:
        unit_width = 0
        start_x = x
        for char in line:
            # Display the character
            blit_text.display_text(
                constants.SCREEN, char, constants.MAIN_FONT, start_x, start_y, colour)

            # Adjust the starting position for the next character
            # Use the width of the widest character for spacing
            start_x += max_char_width + char_spacing_x
            # char_count +=1
            unit_width += max_char_width + char_spacing_x

        # Move to the next line
        # Add some spacing between lines
        start_y += constants.MAIN_FONT.get_height() + char_spacing_y
        # print(char_count)
        unit_height += constants.MAIN_FONT.get_height() + char_spacing_y

    # return unit_height, unit_width  # Return the unit dimensions


# decoding function to display terrain
def display_encoded(unit, colour, x, y, char_spacing_x, char_spacing_y):
    start_y = y

    # Find the maximum width of characters
    max_char_width = max(constants.MAIN_FONT.size(
        char)[0] for line in unit for char in line)

    decoded_terrain = []

    # Decode the terrain and store it in decoded_terrain
    for line in unit:
        decoded_line = ""
        groups = line.split("]")
        for group in groups:
            elements = group.split("[")
            for data in elements:
                if data:  # Check if data is not empty
                    if data[0].isdigit():
                        data_split = data.split(" ")
                        number = int(data_split[0])
                        symbols = data_split[-1]  # Last element is symbols
                        decoded_line += symbols * number
                    else:
                        decoded_line += data
        decoded_terrain.append(decoded_line)

    # Display the terrain unit with even spacing
    for line in decoded_terrain:
        start_x = x
        for char in line:
            # Display the character
            blit_text.display_text(
                constants.SCREEN, char, constants.MAIN_FONT, start_x, start_y, colour)

            # Adjust the starting position for the next character
            start_x += max_char_width + char_spacing_x  # Add max_char_width for spacing

        # Move to the next line
        # Add some spacing between lines
        start_y += constants.MAIN_FONT.get_height() + char_spacing_y


def generate_random_character():
    # Define the range of characters you want to choose from
    character_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+[]{}|;:,.<>?/~"

    # Choose a random character from the character set
    random_character = random.choice(character_set)

    return random_character
