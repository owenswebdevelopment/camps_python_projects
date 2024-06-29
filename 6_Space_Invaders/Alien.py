import pygame, random
from AlienLaser import AlienLaser

class Alien:
    def __init__(self, screen_width):
        self.width = 493 // 5
        self.height = 420 // 5
        self.speed = 2.5
        self.direction = random.choice(['right', 'left']) 
        self.screen_width = screen_width
        self.x = self.assign_x()
        self.y = 0 - self.height
        self.image = pygame.image.load('assets/alien.png')
        self.resized_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.next_shoot_time = pygame.time.get_ticks() + random.randint(1000, 3000)

    def draw(self, screen):
        screen.blit(self.resized_image, (self.x, self.y))
        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
    
    def assign_x(self):
        if self.direction == 'right':
            return 0
        elif self.direction == 'left':
            return self.screen_width - self.width

    def create(self):
        if self.y < 0:
            self.y += self.speed
        else:
            self.move()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        if self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        self.check_boundaries()

    def check_boundaries(self):
        if self.x > self.screen_width:
            self.y += self.height
            self.direction = 'left'
        elif self.x < -self.width:
            self.y += self.height
            self.direction = 'right'

    def detect_collision(self, other_rect):
        return self.rect.colliderect(other_rect)

    def shoot(self, current_time):
        if current_time >= self.next_shoot_time:
            laser = AlienLaser(self)
            self.next_shoot_time = current_time + random.randint(1000, 3000)
            return laser
        return None
