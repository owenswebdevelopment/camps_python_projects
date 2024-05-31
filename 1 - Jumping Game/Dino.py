import pygame

class Dino:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.speed = 0
        self.width = width
        self.height = height
        self.image_1 = pygame.image.load('assets/dino_1.png')
        self.image_2 = pygame.image.load('assets/dino_2.png')
        self.resized_image_1 = pygame.transform.scale(self.image_1, (self.width, self.height))
        self.resized_image_2 = pygame.transform.scale(self.image_2, (self.width, self.height))
        self.jumping = False

    def draw(self, screen):
        if self.jumping:
            screen.blit(self.resized_image_2, (self.x, self.y))
        else:
            screen.blit(self.resized_image_1, (self.x, self.y))

    def start(self):
        if self.jumping:
            self.speed = self.speed + 0.5
            self.y = self.y + self.speed

        if self.y >= 300:
            self.jumping = False
            self.speed = 0

    def jump(self):
        self.jumping = True
        self.speed = -18