import pygame

class Button:
    def __init__(self, text, x, y, width, height, position, font_size=36):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font_size = font_size
        self.color = (100, 100, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(None, self.font_size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
