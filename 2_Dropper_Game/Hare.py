import pygame

class Hare:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.speed = 0
    self.width = 113
    self.height = 196
    self.image_1 = pygame.image.load('assets/hare-a.png')
    self.image_2 = pygame.image.load('assets/hare-b.png')
    self.image_3 = pygame.image.load('assets/hare-c.png')
    self.resized_image_1 = pygame.transform.scale(self.image_1, (self.width, self.height))
    self.resized_image_2 = pygame.transform.scale(self.image_2, (228, 139))
    self.resized_image_3 = pygame.transform.scale(self.image_3, (161, 161))
    self.flipped_image_1 = pygame.transform.flip(self.resized_image_1, True, False)
    self.flipped_image_2 = pygame.transform.flip(self.resized_image_2, True, False)
    self.flipped_image_3 = pygame.transform.flip(self.resized_image_3, True, False)
    self.standing_image = self.resized_image_1
    self.moving = False
    self.direction = ''
    self.rect = pygame.Rect(x, y, self.width, self.height)

    # Image swap timer
    self.last_swap_time = pygame.time.get_ticks()
    self.current_image_index = 0
    self.moving_images = [self.resized_image_2, self.resized_image_3]
    self.flipped_moving_images = [self.flipped_image_2, self.flipped_image_3]

  def draw(self, screen):
    if self.moving:
      current_time = pygame.time.get_ticks()
      if current_time - self.last_swap_time > 150:
        self.current_image_index = (self.current_image_index + 1) % 2
        self.last_swap_time = current_time

      if self.moving and self.direction == 'right':
        screen.blit(self.moving_images[self.current_image_index], (self.x, self.y))
        self.standing_image = self.resized_image_1

      elif self.moving and self.direction == 'left':
        screen.blit(self.flipped_moving_images[self.current_image_index], (self.x, self.y))
        self.standing_image = self.flipped_image_1
    else:
      screen.blit(self.standing_image, (self.x, self.y))

        # pygame.draw.rect(screen, (0, 0, 255), self.rect, 2)

  def move(self, direction, screen_width):
    self.direction = direction
    self.moving = True

    if direction == 'left':
      if self.x <= 10:
        self.x = 11
      self.x -= 10

    if direction == 'right':
      if self.x >= (screen_width - self.width) - 10:
        self.x = (screen_width - self.width) - 11
      self.x += 10

  def update(self):
    self.rect = pygame.Rect(self.x, self.y, (self.width - 20), (self.height - 15))


  def detect_collision(self, other_rect):
    return self.rect.colliderect(other_rect)
