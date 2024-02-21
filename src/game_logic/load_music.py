import pygame
from pygame import mixer
# background sound - continuous
# Initialize pygame mixer
def load_music(path_to_music):
    pygame.mixer.init()

    # Load the sound file
    main_sound_theme = pygame.mixer.Sound(path_to_music)

    # You can now play the loaded sound
    main_sound_theme.play()