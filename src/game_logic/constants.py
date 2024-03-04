from game_logic import display_ascii
from game_logic.levels import level_one_ascii_units
import pygame

pygame.font.init()

# frames per second
FPS = 60
CLOCK = pygame.time.Clock()
START_TIME = pygame.time.get_ticks()

# FONTS
FONT_LOCATION = "/Users/Adam/Desktop/coding/games/tanks/assets/fonts/dogica.ttf"
MAIN_MUSIC_LOCATION = "/Users/Adam/Desktop/coding/games/Tanks/assets/sound/main-theme.wav"
MAIN_FONT = pygame.font.Font(
    "/Users/Adam/Desktop/coding/games/Tanks/assets/fonts/Menlo.ttc", 12)
TITLE_FONT = pygame.font.Font(
    "/Users/Adam/Desktop/coding/games/Tanks/assets/fonts/Menlo.ttc", 24)
CAPTION_FONT = pygame.font.Font(
    "/Users/Adam/Desktop/coding/games/Tanks/assets/fonts/VictorMono-Medium.ttf", 24)
PAUSED_TEXT_COLOUR = (255, 0, 0)

# text elements
# game counters
PLAYER_SCORE = "Score"
SCORE_X, SCORE_Y = 100, 700
SCORE_COLOUR = (255, 0, 0)
TIME_COUNT = "Time left"
TIME_X, TIME_Y = 200, 700
TIME_COLOUR = (255, 0, 0)
MISSILE_SUPPLY = "Missiles"
MISSILE_TEXT_X, MISSILE_TEXT_Y = 300, 700
MISSILE_TEXT_COLOUR = (255, 0, 0)
# other screen texts
GAME_TITLE = "Code Combat: ASCII Strikes Back"
GAME_TITLE_COLOUR = (0, 200, 255)
STARTUP_SCREEN_EXIT = "Press SPACE to continue"
STARTUP_SCREEN_EXIT_COLOUR = (255, 82, 0)
STARTUP_SCREEN_CONTROLS = "Movement: UP | DOWN | LEFT | RIGHT\nFire Weapon: SPACE\nQuit: Q"
STARTUP_SCREEN_CONTROLS_COLOUR = (255, 235, 0)
WIN_TEXT = "Debugging is complete! Victory is ours!"
WIN_TEXT_COLOUR = (255, 235, 0)
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

# ascii
CHAR_SPACING_X = -1
CHAR_SPACING_Y = 4

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


# image dictionarie
# TANK_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/units/level_one")
# TERRAIN_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/terrain/level_one")
# CAPTION_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/captions")
# MISSILE_EXPLOSION_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/explosions/explosion_frames")
# AMMO_CRATE_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/weapons/ammo/missile_crate")
# MISSILE_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/weapons/missile")
