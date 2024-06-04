import pygame

class Sound:
    def __init__(self, sound_path):
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(sound_path)

    def play_sound(self):
        self.sound.play()
        # pygame.time.delay(int(sound.get_length() * 1000))