from game_logic import display_ascii
from game_logic.levels import level_one_ascii_units
import pygame
import os

pygame.font.init()

# frames per second
FPS = 60
CLOCK = pygame.time.Clock()
START_TIME = pygame.time.get_ticks()

# FONTS
FONT_LOCATION = "/Users/Adam/Desktop/coding/games/tanks/assets/fonts/dogica.ttf"
MAIN_MUSIC_LOCATION = "/Users/Adam/Desktop/coding/games/tanks/assets/sound/main-theme.wav"
MAIN_FONT = pygame.font.Font(
    "/Users/Adam/Desktop/coding/games/Tanks/assets/fonts/Menlo.ttc", 12)
MISSILE_FONT = pygame.font.Font(
    "/Users/Adam/Desktop/coding/games/Tanks/assets/fonts/Menlo.ttc", 18)
TITLE_FONT = pygame.font.Font(
    "/Users/Adam/Desktop/coding/games/Tanks/assets/fonts/VictorMono-Medium.ttf", 46)
BIG_TITLE_FONT = pygame.font.Font(
    "/Users/Adam/Desktop/coding/games/Tanks/assets/fonts/VictorMono-Medium.ttf", 72)
BIG_SCORE_FONT = pygame.font.Font(
    "/Users/Adam/Desktop/coding/games/Tanks/assets/fonts/VictorMono-Medium.ttf", 120)
SUB_TITLE_FONT = pygame.font.Font(
    "/Users/Adam/Desktop/coding/games/Tanks/assets/fonts/VictorMono-Medium.ttf", 30)
CAPTION_FONT = pygame.font.Font(
    "/Users/Adam/Desktop/coding/games/Tanks/assets/fonts/VictorMono-Medium.ttf", 24)


# text elements

# colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)


# game counters
PLAYER_SCORE = "Score"
SCORE_X, SCORE_Y = 100, 700
SCORE_COLOUR = RED
TIME_COUNT = "Time left"
TIME_X, TIME_Y = 200, 700
TIME_COLOUR = RED
MISSILE_SUPPLY = "Missiles"
MISSILE_TEXT_X, MISSILE_TEXT_Y = 300, 700
MISSILE_TEXT_COLOUR = RED

# ascii
CHAR_SPACING_X = -1
CHAR_SPACING_Y = 4
LETTER_SPACING = 10
# other screen texts
DOTTED_LINE = "*------------------*"

# titles

GAME_TITLE_1 = "CODE COMBAT:"
GAME_TITLE_2 = "ASCII Strikes Back"
GAME_TITLE_COLOUR = YELLOW
STARTUP_SCREEN_EXIT = "Press SPACE to continue"
KEY_TO_RESTART = "Press ENTER to play again"
STARTUP_SCREEN_EXIT_COLOUR = RED
STARTUP_SCREEN_CONTROLS = "Movement: UP | DOWN | LEFT | RIGHT\nFire Weapon: SPACE\nQuit: Q\nPause: P"
STARTUP_SCREEN_CONTROLS_COLOUR = CYAN
WIN_SCORE_LARGE = "BUGS"
WIN_TEXT_WITH_SCORE = "Terminated with extreme prejudice!"
WIN_TEXT = "Debugging is complete!\nVictory is ours!"
WIN_TEXT_COLOUR = YELLOW
GAME_OVER_TEXT = "GAME OVER"
Q_TO_QUIT_TEXT = "or Q to quit"
NO_MISSILES_TEXT = "Your ASCII artillery has been fully depleted!"
NO_TIME_TEXT = "Time's up! Better luck next compile!"
DEFEAT_TEXT = "Don't let this defeat discourage you!\nThe ASCII universe awaits your return!"
MOTIVATE_TEXT = "It's not a feature, it's a bug!"
PAUSED_TEXT_COLOUR = CYAN
# SCREEN SETUP
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_X_MIN = 0
SCREEN_Y_MIN = 0
CENTRE_X = SCREEN_WIDTH/2
CENTRE_Y = SCREEN_HEIGHT/2
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_BKGND = (0, 0, 0)
SCREEN_BKGND_TRANSP = (0, 0, 0, 128)


# PLAYER CONSTANTS
PLAYER_ACCELERATION = 6
MISSILE_ACCELERATION = 20
MISSILE_HEIGHT, MISSILE_WIDTH = display_ascii.measure_unit_size(
    level_one_ascii_units.player_missile["missile"], CHAR_SPACING_X, CHAR_SPACING_Y)
PLAYER_HEIGHT, PLAYER_WIDTH = display_ascii.measure_unit_size(
    level_one_ascii_units.player_tank["straight"], CHAR_SPACING_X, CHAR_SPACING_Y)
PLAYER_TANK_COLOUR = (0, 200, 255)

# enemy constants
ENEMY_TANK_COLOUR = (200, 0, 0)
ENEMY_ACCELERATION = 4
ENEMY_HEIGHT, ENEMY_WIDTH = display_ascii.measure_unit_size(
    level_one_ascii_units.enemy_tank["straight"], CHAR_SPACING_X, CHAR_SPACING_Y)
ENEMY_X_SPACING = 100

# missiles
COLLISION_TOL = 20
# explosions
EXPLOSION_HEIGHT, EXPLOSION_WIDTH = display_ascii.measure_unit_size(
    level_one_ascii_units.missile_explode["1"], CHAR_SPACING_X, CHAR_SPACING_Y)
EXPLOSION_COLOUR = YELLOW
EXPLOSION_SOUND = "../assets/sound/explode.wav"
LAUNCH_SOUND = "../assets/sound/launch.wav"


# image dictionarie
# TANK_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/units/level_one")
# TERRAIN_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/terrain/level_one")
# CAPTION_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/captions")
# MISSILE_EXPLOSION_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/explosions/explosion_frames")
# AMMO_CRATE_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/weapons/ammo/missile_crate")
# MISSILE_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/weapons/missile")
