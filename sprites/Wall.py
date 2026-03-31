import pygame
import random
from utils import WHITE, HEIGHT, WIDTH

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Utworzenie grupy ścian
walls = pygame.sprite.Group()

# Dodanie ściany do grupy
wall = Wall(30, 30, 10, HEIGHT)
walls.add(wall)


