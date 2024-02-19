import os, pygame

# Function to load images from a directory (png and jpeg only)
def load_images_from_directory(directory):
    image_dict = {}
    for filename in os.listdir(directory):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_path = os.path.join(directory, filename)
            image = pygame.image.load(image_path)
            # Remove the file extension to use as the key
            key = os.path.splitext(filename)[0]
            image_dict[key] = image
    return image_dict