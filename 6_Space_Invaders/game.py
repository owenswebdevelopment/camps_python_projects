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
from Message import Message
from Text import Text

# Screen
screen_width = 960
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# General variables
clock = pygame.time.Clock()
game_over = False
message = Message('assets/gameover.png', 50, (screen_height / 2) - 100, 100, 100)
score_text = Text(50, (255, 255, 255), (25, 25))

# Pygame init
pygame.init()

# Background
background = Background('assets/background.png', 0, 0, screen_width, screen_height)

# Sounds
pew = Sound('sounds/pew.wav')
pop = Sound('sounds/pop.wav')

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

# Aliens Lasers
alien_lasers = []

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
        # Draw Background
        background.draw(screen)
        score_text.draw(screen)

        # Draw Ufo
        ufo.draw(screen)
        for ufo_laser in ufo_lasers:
            ufo_laser.draw(screen)

        # Draw alien
        for alien in aliens:
            alien.draw(screen)
        for alien_laser in alien_lasers:
            alien_laser.draw(screen)

        # Update ufo
        for ufo_laser in ufo_lasers:
            ufo_laser.move()

        # Update Aliens
        if current_time >= next_alien_time:
            aliens.append(Alien(screen_width))
            next_alien_time = current_time + random.randint(1000, 2500)

        for alien in aliens:
            alien.create()
            laser = alien.shoot(current_time)
            if laser:
                pew.play_sound()
                alien_lasers.append(laser)

            for ufo_laser in list(ufo_lasers):
                if alien.detect_collision(ufo_laser):
                    pop.play_sound()
                    score_text.update(score_text.score + 1)
                    aliens.remove(alien)
                    ufo_lasers.remove(ufo_laser)

        # Update alien lasers
        for alien_laser in list(alien_lasers):
            alien_laser.move()
            if alien_laser.y > screen_height:
                alien_lasers.remove(alien_laser)
                
        # Collision
        for alien_laser in list(alien_lasers):
            if ufo.detect_collision(alien_laser):
                game_over = True
    else:
        message.draw(screen)
        pass

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
