from game_logic import make_image_dict


# frames per second
FPS = 60

FONT_LOCATION = "/Users/Adam/Desktop/coding/pfe/tanks/tanks/dogica.ttf"

# image dictionarie
TANK_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/units/level_one")
TERRAIN_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/terrain")
CAPTION_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/tanks/assets/images/captions")
MISSILE_EXPLOSION_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/explosions/explosion_frames")
AMMO_CRATE_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/weapons/ammo/missile_crate")
MISSILE_IMAGES = make_image_dict.load_images_from_directory("/Users/Adam/Desktop/coding/games/Tanks/assets/images/weapons/missile")