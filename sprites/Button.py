import pygame
import sys
import snailo.settings as settings
from snailo.settings import LIGHT_PISTACHIO,BLACK,PINK


class SpeakerButton:
    SIZE = 40

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, self.SIZE, self.SIZE)
        self.muted = False

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def toggle(self):
        self.muted = not self.muted
        settings.MUTED = self.muted
        if self.muted:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def draw(self, screen):
        cx = self.rect.x
        cy = self.rect.y
        s = self.SIZE

        # Speaker body (small rectangle)
        body = pygame.Rect(cx + int(s * 0.10), cy + int(s * 0.35), int(s * 0.25), int(s * 0.30))
        pygame.draw.rect(screen, BLACK, body)

        # Horn (triangle pointing right)
        horn = [
            (cx + int(s * 0.10), cy + int(s * 0.35)),
            (cx + int(s * 0.10), cy + int(s * 0.65)),
            (cx + int(s * 0.50), cy + int(s * 0.80)),
            (cx + int(s * 0.50), cy + int(s * 0.20)),
        ]
        pygame.draw.polygon(screen, BLACK, horn)

        if not self.muted:
            # Sound wave arcs
            arc_rect1 = pygame.Rect(cx + int(s * 0.45), cy + int(s * 0.30), int(s * 0.20), int(s * 0.40))
            pygame.draw.arc(screen, BLACK, arc_rect1, -0.6, 0.6, 3)
            arc_rect2 = pygame.Rect(cx + int(s * 0.55), cy + int(s * 0.18), int(s * 0.32), int(s * 0.64))
            pygame.draw.arc(screen, BLACK, arc_rect2, -0.8, 0.8, 3)
        else:
            # Red cross-out line
            pygame.draw.line(screen, (200, 0, 0),
                             (cx + int(s * 0.55), cy + int(s * 0.20)),
                             (cx + int(s * 0.90), cy + int(s * 0.80)), 3)
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