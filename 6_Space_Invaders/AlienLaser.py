import pygame

class AlienLaser:
    def __init__(self, x, y, width, height):
        self.width = 40 // 3
        self.height = 82 // 3
        self.x = x + width // 2 - self.width // 2
        self.y = height
        self.speed = 2
        self.image = pygame.image.load('assets/pink_laser.png')
        self.resized_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        screen.blit(self.resized_image, (self.x, self.y))
        pygame.draw.rect(screen, (0, 0, 255), self.rect, 2)

    def move(self):
        self.y += self.speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def detect_collision(self, other_rect):
        return self.rect.colliderect(other_rect)
