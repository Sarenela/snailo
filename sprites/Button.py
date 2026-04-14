import pygame
import sys
from snailo.settings import LIGHT_PISTACHIO,BLACK,PINK
class Button:
    def __init__(self, x, y, width, height, text, font):
        self.rect = pygame.Rect(x - width // 2, y - height // 2, width, height)
        self.color = pygame.Color(PINK)
        self.text = text
        self.font = font
        self.clicked = False

    def update(self):
        self.clicked = False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)