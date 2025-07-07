# Imports
import pygame
import os

# For the directories to work
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Classes
from Background import Background
from Hare import Hare
from Carrot import Carrot
from Text import Text
from Sound import Sound
from Snowball import Snowball
from Lives import Lives
from Message import Message

# Sounds
coin = Sound("sounds/coin.wav")
rip = Sound("sounds/rip.wav")
lose = Sound("sounds/lose.wav")

# Screen
screen_width = 960
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# General variables
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
score_text = Text(50, (0, 0, 0), (25, 25))
lives_section = Lives(screen_width)
message = Message('assets/gameover.png', 30, (screen_height / 2) - 100, 100, 100)
game_over = False

# Pygame init
pygame.init()

# Background
background = Background('assets/background.png', 0, 0, screen_width, screen_height)

# Hare
hare_x = 250
hare_y = 500
hare = Hare(hare_x, hare_y)

# Carrots
carrots = [
  Carrot(0, screen_width, screen_height), 
  Carrot(1000, screen_width, screen_height), 
  Carrot(2000, screen_width, screen_height)
]

# Snowballs
snowballs = [
  Snowball(0, screen_width, screen_height), 
  Snowball(1000, screen_width, screen_height), 
]

# Game loop
running = True
while running:
  current_time = pygame.time.get_ticks() - start_time
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  keys = pygame.key.get_pressed()
  if keys[pygame.K_ESCAPE]:
    running = False
  elif keys[pygame.K_LEFT]:
    hare.move('left', screen_width)
  elif keys[pygame.K_RIGHT]:
    hare.move('right', screen_width)
  else:
    hare.moving = False

  if not game_over:
            
    # Draw
    background.draw(screen)
    hare.draw(screen)
    score_text.draw(screen)

    for carrot in carrots:
      carrot.draw(screen)
    
    for snowball in snowballs:
      snowball.draw(screen)

    lives_section.draw(screen)

    # Update
    hare.update()
    for carrot in carrots:
      if not carrot.spawned and current_time >= carrot.spawn_time:
        carrot.spawned = True
      if carrot.spawned:
        carrot.move()
        carrot.update(score_text)
        
    for snowball in snowballs:
      if not snowball.spawned and current_time >= snowball.spawn_time:
        snowball.spawned = True
      if snowball.spawned:
        snowball.move()
        snowball.update()

    # Collisions
    for carrot in carrots:
      if carrot.detect_collision(hare.rect):
        score_text.update(score_text.score + 1)
        coin.play_sound()
        carrot.reset()

    for snowball in snowballs:
      if snowball.detect_collision(hare.rect):
        rip.play_sound()
        snowball.reset()
        lives_section.lives -= 1
        if lives_section.lives > 0:
          lives_section.update()
        else:
          lose.play_sound()
          game_over = True
  else:
    message.draw(screen)

  pygame.display.flip()
  clock.tick(60)
pygame.quit()
