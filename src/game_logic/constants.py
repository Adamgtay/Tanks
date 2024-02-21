from game_logic import make_image_dict
import pygame


# frames per second
FPS = 60

FONT_LOCATION = "/Users/Adam/Desktop/coding/pfe/tanks/tanks/dogica.ttf"
CLOCK = pygame.time.Clock()
START_TIME = pygame.time.get_ticks()
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# image dictionarie
TANK_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/units/level_one")
TERRAIN_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/terrain")
CAPTION_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/captions")
MISSILE_EXPLOSION_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/explosions/explosion_frames")
AMMO_CRATE_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/weapons/ammo/missile_crate")
MISSILE_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/weapons/missile")