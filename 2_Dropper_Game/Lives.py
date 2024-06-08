import pygame

class Lives:
    def __init__(self, screen_width):
        self.lives = 3
        self.x = screen_width - 180
        self.y = 20
        self.image_1 = pygame.image.load('assets/life_1.png')
        self.image_2 = pygame.image.load('assets/life_2.png')
        self.image_3 = pygame.image.load('assets/life_3.png')
        self.resized_image_1 = pygame.transform.scale(self.image_1, (69, 94))
        self.resized_image_2 = pygame.transform.scale(self.image_2, (115, 96))
        self.resized_image_3 = pygame.transform.scale(self.image_3, (164, 96))
        self.actual_image = self.image_3

    def draw(self, screen):
      screen.blit(self.actual_image, (self.x, self.y))

    def update(self):
        if self.lives == 3:
          self.actual_image = self.image_3
        elif self.lives == 2:
          self.actual_image = self.image_2  
        elif self.lives == 1:
          self.actual_image = self.image_1 
        
    def detect_collision(self, other_rect):
        return self.rect.colliderect(other_rect)
