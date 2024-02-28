from game_logic import make_image_dict
import pygame

pygame.font.init()

# frames per second
FPS = 60
CLOCK = pygame.time.Clock()
START_TIME = pygame.time.get_ticks()

#FONTS
FONT_LOCATION = "/Users/Adam/Desktop/coding/games/tanks/assets/fonts/dogica.ttf"
MAIN_MUSIC_LOCATION = "/Users/Adam/Desktop/coding/games/Tanks/assets/sound/main-theme.wav"
MAIN_FONT = pygame.font.Font("/Users/Adam/Desktop/coding/games/Tanks/assets/fonts/Menlo.ttc", 12)
CAPTION_FONT = pygame.font.Font("/Users/Adam/Desktop/coding/games/Tanks/assets/fonts/VictorMono-Medium.ttf", 24)

# SCREEN SETUP
SCREEN_WIDTH=1200
SCREEN_HEIGHT=800
CENTRE_X = SCREEN_WIDTH/2
CENTRE_Y = SCREEN_HEIGHT/2
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# PLAYER CONSTANTS
PLAYER_ACCELERATION=6
MISSILE_ACCELERATION = 20
PLAYER_WIDTH = 72
PLAYER_HEIGHT = 126

# image dictionarie
#TANK_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/units/level_one")
#TERRAIN_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/terrain/level_one")
#CAPTION_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/captions")
#MISSILE_EXPLOSION_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/explosions/explosion_frames")
#AMMO_CRATE_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/weapons/ammo/missile_crate")
#MISSILE_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/weapons/missile")