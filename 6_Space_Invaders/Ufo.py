import pygame

class Ufo:
  def __init__(self, screen_width, screen_height):
    self.width = 548 // 5
    self.height = 458 // 5
    self.x = screen_width // 2 - self.width // 2
    self.y = screen_height - self.height - 15
    self.speed = 5
    self.image = pygame.image.load('assets/ufo.png')
    self.resized_image = pygame.transform.scale(self.image, (self.width, self.height))
    self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

  def draw(self, screen):
    screen.blit(self.resized_image, (self.x, self.y))

    # pygame.draw.rect(screen, (0, 0, 255), self.rect, 2)

  def move(self, direction, screen_width):
    if direction == 'left':
      if self.x <= 10:
        self.x = 11
      self.x -= self.speed

    if direction == 'right':
      if self.x >= (screen_width - self.width) - 10:
        self.x = (screen_width - self.width) - 11
      self.x += self.speed

    self.update()

  def update(self):
    self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        

  def detect_collision(self, other_rect):
    return self.rect.colliderect(other_rect)
