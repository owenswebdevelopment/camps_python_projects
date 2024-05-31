# Imports
import pygame
import os

# For the directories to work
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Classes
from Background import Background
from Dino import Dino

# General variables
clock = pygame.time.Clock()

# Pygame init
pygame.init()


# Screen
screen_width = 960
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Background
background = Background('assets/background.png', 0, 0, screen_width, screen_height)

# Dino
dino = Dino(30, 300, 100, 100)


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
                if not dino.jumping:
                    dino.jump()

    # Draw
    background.draw(screen)
    dino.draw(screen)

    # Update
    dino.start()


    pygame.display.flip()
    clock.tick(60)
pygame.quit()