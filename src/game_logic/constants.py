from game_logic import make_image_dict
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
CAPTION_FONT = pygame.font.Font(
    "/Users/Adam/Desktop/coding/games/Tanks/assets/fonts/VictorMono-Medium.ttf", 24)
PAUSED_TEXT_COLOUR = (255, 0, 0)

# SCREEN SETUP
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_X_MIN = 0
SCREEN_Y_MIN = 0
CENTRE_X = SCREEN_WIDTH/2
CENTRE_Y = SCREEN_HEIGHT/2
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_BKGND = (0, 0, 0)

# PLAYER CONSTANTS
PLAYER_ACCELERATION = 6
MISSILE_ACCELERATION = 20
PLAYER_WIDTH = 66
PLAYER_HEIGHT = 126
PLAYER_TANK_COLOUR = (0, 200, 255)

# enemy constants
ENEMY_TANK_COLOUR = (200, 0, 0)
ENEMY_ACCELERATION = 4
ENEMY_WIDTH = 66
ENEMY_HEIGHT = 126
ENEMY_X_SPACING = 100


# ascii
CHAR_SPACING_X = -1
CHAR_SPACING_Y = 4

# image dictionarie
# TANK_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/units/level_one")
# TERRAIN_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/terrain/level_one")
# CAPTION_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/captions")
# MISSILE_EXPLOSION_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/explosions/explosion_frames")
# AMMO_CRATE_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/weapons/ammo/missile_crate")
# MISSILE_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/weapons/missile")
