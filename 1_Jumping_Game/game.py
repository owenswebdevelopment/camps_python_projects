# Imports
import pygame
import os
import random

# For the directories to work
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Classes
from Background import Background
from Dino import Dino
from Sound import Sound
from Cactus import Cactus
from Coin import Coin
from Message import Message
from Text import Text

# Sounds
pop = Sound("sounds/pop.wav")
coin = Sound("sounds/coin.wav")
clown_honk = Sound("sounds/clown_honk.wav")

# Screen
screen_width = 960
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# General variables
clock = pygame.time.Clock()
message = Message('assets/you_lose.png', 30, (screen_height / 2) - 100, 100, 100)
game_over = False
score_text = Text(50, (0, 0, 0), (25, 25))

# Pygame init
pygame.init()

# Background
background = Background('assets/background.png', 0, 0, screen_width, screen_height)

# Characters
dino = Dino(30, 300, 100, 100)
cactus_1 = Cactus(screen_width, screen_width, 330, 70, 70)
cactus_2 = Cactus(screen_width, screen_width + random.randint(600, 900), 330, 70, 70)
coin = Coin(screen_width, screen_width + random.randint(600, 900), 330, 70, 70)

# Game loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
			elif event.key == pygame.K_SPACE:
				if not dino.jumping and not game_over:
					dino.jump()
					pop.play_sound()
	
	if not game_over:
		# Draw
		background.draw(screen)
		dino.draw(screen)
		cactus_1.draw(screen)
		cactus_2.draw(screen)
		coin.draw(screen)
		score_text.draw(screen)

		# Update
		dino.start()
		cactus_1.update(score_text)
		cactus_2.update(score_text)
		coin.update()
		if dino.detect_collision(cactus_1.rect) or dino.detect_collision(cactus_2.rect):
			clown_honk.play_sound()
			game_over = True

		if dino.detect_collision(coin.rect):
			score_text.update(score_text.score + 5)
			coin.reset_position()
	else:
		message.draw(screen)

	pygame.display.flip()
	clock.tick(60)
pygame.quit()
