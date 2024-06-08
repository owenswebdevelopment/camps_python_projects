import pygame

class Message:
    def __init__(self, image_path, x, y, width, height):
        self.image_path = image_path
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(self.image_path)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))