import pygame
import random

class Cactus:
    def __init__(self, screen_width, x, y, width, height):
        self.respawn_position = screen_width
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load('assets/cactus.png')
        self.resized_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        screen.blit(self.resized_image, (self.x, self.y))

    def update(self, score_text):
        self.x = self.x - 10

        if self.x < (-self.width - 10):
            self.x = self.respawn_position + random.randint(100, 500)
            score_text.update(score_text.score + 1)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def detect_collision(self, other_rect):
        return self.rect.colliderect(other_rect)