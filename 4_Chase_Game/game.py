# Imports
import pygame
import os

# For the directories to work
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Classes
from Background import Background
from Dog import Dog
from Bone import Bone
from Sound import Sound
from Text import Text
from Rocket import Rocket
from Message import Message

# Sounds
bite = Sound("sounds/bite.wav")

# Screen
screen_width = 960
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# General variables
clock = pygame.time.Clock()
score_text = Text(50, (255, 255, 255), (25, 25))
message = Message('assets/gameover.png', 50, (screen_height / 2) - 100, 100, 100)
game_over = False

# Pygame init
pygame.init()

# Background
background = Background('assets/background.png', 0, 0, screen_width, screen_height)

# Dog
dog_x = 75
dog_y = (screen_height // 2) - 134
dog = Dog(dog_x, dog_y)

# Bone
bone = Bone(screen_width, screen_height)

# Rocket
rocket_x = screen_width
rocket_y = (screen_height // 2) - 134
rocket = Rocket(rocket_x, rocket_y)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    elif keys[pygame.K_LEFT]:
        dog.move('left', screen_width)
    elif keys[pygame.K_RIGHT]:
        dog.move('right', screen_width)
    elif keys[pygame.K_UP]:
        dog.move('up', screen_height)
    elif keys[pygame.K_DOWN]:
        dog.move('down', screen_height)
    else:
        dog.moving = False

    if not game_over:
      # Draw
      background.draw(screen)
      dog.draw(screen)
      rocket.draw(screen, dog.x)
      bone.draw(screen)
      score_text.draw(screen)

      # Update
      dog.update()
      rocket.update(dog.x, dog.y)

      # Collisions
      if bone.detect_collision(dog.rect):
          score_text.update(score_text.score + 1)
          bite.play_sound()
          bone.reset()

      if rocket.detect_collision(dog.rect):
        game_over = True

    else:
        message.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


