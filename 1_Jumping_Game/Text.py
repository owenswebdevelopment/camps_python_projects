import pygame
# pygame.font.init()

class Text:
    def __init__(self, font_size, color, position):
        self.score = 0
        self.text = str(self.score)
        self.font_size = font_size
        self.color = color
        self.position = position
        pygame.font.init()
        self.font = pygame.font.Font(None, self.font_size)

    def render(self):
        return self.font.render(self.text, True, self.color)

    def draw(self, screen):
        text_surface = self.render()
        screen.blit(text_surface, self.position)

    def update(self, new_score):
        self.score = int(new_score)
        self.text = str(new_score)