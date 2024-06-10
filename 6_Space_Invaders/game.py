# Imports
import pygame
import os

# For the directories to work
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Classes
from Background import Background
from Ufo import Ufo


# Sounds
# coin = Sound("sounds/coin.wav")

# Screen
screen_width = 960
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# General variables
clock = pygame.time.Clock()
# score_text = Text(50, (0, 0, 0), (25, 25))
# message = Message('assets/gameover.png', 30, (screen_height / 2) - 100, 100, 100)
game_over = False

# Pygame init
pygame.init()

# Background
background = Background('assets/background.png', 0, 0, screen_width, screen_height)

# Ufo
ufo = Ufo(screen_width, screen_height)

# Aliens

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
    # hare.move('left', screen_width)
    pass
  elif keys[pygame.K_RIGHT]:
    # hare.move('right', screen_width)
    pass

  if not game_over:
            
    # Draw
    background.draw(screen)
    ufo.draw(screen)

    # Update
    # hare.update()
    # for carrot in carrots:
    #   if not carrot.spawned and current_time >= carrot.spawn_time:
    #     carrot.spawned = True
    #   if carrot.spawned:
    #     carrot.move()
    #     carrot.update(score_text)

    # Collisions
    # for carrot in carrots:
    #   if carrot.detect_collision(hare.rect):
    #     score_text.update(score_text.score + 1)
    #     coin.play_sound()
    #     carrot.reset()
  else:
    # message.draw(screen)
    pass

  pygame.display.flip()
  clock.tick(60)
pygame.quit()
