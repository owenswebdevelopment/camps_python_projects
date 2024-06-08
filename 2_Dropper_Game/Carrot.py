import pygame
import random

class Carrot:
    def __init__(self, spawn_time, screen_width, screen_height):
        self.width = 281
        self.height = 421
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = random.randint(0, screen_width - 50)
        self.y = - self.height
        self.speed = random.randint(3, 6)
        self.image = pygame.image.load('assets/carrot.png')
        self.resized_image = pygame.transform.scale(self.image, (self.width // 5, self.height // 5))
        self.rect = pygame.Rect(self.x, self.y, self.width // 5, self.height // 5)
        self.spawn_time = spawn_time
        self.spawned = False

    def draw(self, screen):
        screen.blit(self.resized_image, (self.x, self.y))
        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

    def move(self):
        self.y += self.speed

    def update(self, score_text):
        self.rect = pygame.Rect(self.x, self.y, self.width // 5, self.height // 5)
        
        if self.y > self.screen_height:
          self.reset()

    def reset(self):
      self.x = random.randint(0, self.screen_width - 50)
      self.y = - self.height
            

    def detect_collision(self, other_rect):
        return self.rect.colliderect(other_rect)
