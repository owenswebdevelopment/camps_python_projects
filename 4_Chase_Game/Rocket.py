import pygame
import math

class Rocket:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.speed = 2
		self.width = 370
		self.height = 243

		self.image_1 = pygame.image.load('assets/rocket_1.png')
		self.image_2 = pygame.image.load('assets/rocket_2.png')
		self.image_3 = pygame.image.load('assets/rocket_3.png')
		self.image_4 = pygame.image.load('assets/rocket_4.png')

		self.resized_image_1 = pygame.transform.scale(self.image_1, (self.width // 2, self.height // 2))
		self.resized_image_2 = pygame.transform.scale(self.image_2, (426 // 2, 218 // 2))
		self.resized_image_3 = pygame.transform.scale(self.image_3, (373 // 2, 246 // 2))
		self.resized_image_4 = pygame.transform.scale(self.image_4, (356 // 2, 292 // 2))

		self.rect = pygame.Rect(x, y, self.width // 2, self.height // 2)

		# Image swap timer
		self.last_swap_time = pygame.time.get_ticks()
		self.current_image_index = 0
		self.moving_images = [
			self.resized_image_1,
			self.resized_image_2,
			self.resized_image_3,
			self.resized_image_4,
		]

	def draw(self, screen, dog_x):
		current_time = pygame.time.get_ticks()
		if current_time - self.last_swap_time > 300:
			self.current_image_index = (self.current_image_index + 1) % 4
			self.last_swap_time = current_time

		if dog_x < screen.get_width() // 2:
			rotated_image = pygame.transform.flip(self.moving_images[self.current_image_index], True, False)
		else:
			rotated_image = self.moving_images[self.current_image_index]

		screen.blit(rotated_image, (self.x, self.y))
		# pygame.draw.rect(screen, (0, 0, 255), self.rect, 2)

	def update(self, target_x, target_y):
		dx = target_x - self.x
		dy = target_y - self.y
		distance = math.hypot(dx, dy)

		if distance > 1:
			dx /= distance
			dy /= distance

			self.x += dx * self.speed
			self.y += dy * self.speed

		self.rect = pygame.Rect(self.x, self.y, self.width // 2, self.height // 2)

	def detect_collision(self, other_rect):
		return self.rect.colliderect(other_rect)

def reset(self):
    self.x = 960  # assuming screen_width is 960
    self.y = (720 // 2) - 75  # adjust based on your rocket's height
