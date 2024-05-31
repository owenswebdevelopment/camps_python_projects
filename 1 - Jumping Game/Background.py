import pygame

class Background:
    def __init__(self, image_path, x, y, width, height):
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y
        self. width = width
        self.height = height
        self.resized_image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, screen):
        screen.blit(self.resized_image, (self.x, self.y))