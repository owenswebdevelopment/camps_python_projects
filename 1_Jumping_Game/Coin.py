import pygame
import random

class Coin:
	def __init__(self, screen_width, x, y, width, height):
		self.respawn_position = screen_width
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.image = pygame.image.load('assets/coin.png')
		self.resized_image = pygame.transform.scale(self.image, (self.width, self.height))
		self.rect = pygame.Rect(x, y, width, height)

	def draw(self, screen):
		screen.blit(self.resized_image, (self.x, self.y))
      
	def update(self):
		self.x = self.x - 10

		if self.x < (-self.width - 10):
			self.reset_position()

		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

	def detect_collision(self, other_rect):
		return self.rect.colliderect(other_rect)
    
	def reset_position(self):
		self.x = self.respawn_position + random.randint(100, 500)