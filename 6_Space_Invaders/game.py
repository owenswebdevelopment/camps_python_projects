# Imports
import pygame
import os
import random

# For the directories to work
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Classes
from Background import Background
from Ufo import Ufo
from Laser import Laser
from Sound import Sound
from Alien import Alien

# Screen
screen_width = 960
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# General variables
clock = pygame.time.Clock()
game_over = False

# Pygame init
pygame.init()

# Background
background = Background('assets/background.png', 0, 0, screen_width, screen_height)

# Sounds
pew = Sound('sounds/pew.wav')

# Ufo
ufo = Ufo(screen_width, screen_height)

# Ufo Lasers
ufo_lasers = []
next_ufo_laser_time = 0
	
# Aliens
aliens = []
next_alien_time = 0
def create_alien():
	aliens.append(Alien(screen_width))



# Game loop
running = True
while running:
	current_time = pygame.time.get_ticks()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_ESCAPE]:
		running = False
	if keys[pygame.K_LEFT]:
		ufo.move('left', screen_width)
	if keys[pygame.K_RIGHT]:
		ufo.move('right', screen_width)
	if keys[pygame.K_SPACE] and current_time >= next_ufo_laser_time:
		pew.play_sound()
		ufo_lasers.append(Laser(ufo))
		next_ufo_laser_time = current_time + 300

	if not game_over:
		# Draw
		background.draw(screen)
		ufo.draw(screen)
		for ufo_laser in ufo_lasers:
			ufo_laser.draw(screen)
		for alien in aliens:
			alien.draw(screen)

		# Update
		for ufo_laser in ufo_lasers:
			ufo_laser.move()

		if current_time >= next_alien_time:
			aliens.append(Alien(screen_width))
			next_alien_time = current_time + random.randint(1000, 2500)

		for alien in aliens:
			alien.create()
			for ufo_laser in list(ufo_lasers):
				if alien.detect_collision(ufo_laser):
					aliens.remove(alien)
					ufo_lasers.remove(ufo_laser)

	pygame.display.flip()
	clock.tick(120)

pygame.quit()
