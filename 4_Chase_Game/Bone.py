import pygame
import random

class Bone:
    def __init__(self, screen_width, screen_height):
        self.width = 92
        self.height = 59
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)
        self.image = pygame.image.load('assets/bone.png')
        self.resized_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        screen.blit(self.resized_image, (self.x, self.y))
        # pygame.draw.rect(screen, (0, 0, 255), self.rect, 2)

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def reset(self):
      self.x = random.randint(0, self.screen_width - self.width)
      self.y = random.randint(0, self.screen_height - self.height)
      self.update()
            

    def detect_collision(self, other_rect):
        return self.rect.colliderect(other_rect)
