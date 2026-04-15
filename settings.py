import random
import pygame

#hydra
# Ustawienia ekranu
WIDTH = 800
HEIGHT = 700
FPS = 30 #liczba kratek na sekundę

#box settings
BOX_WIDTH =130
BOX_HEIGHT =130
BOX_SEP =20
BOX_NUM =6

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PISTACHIO = (147,197,114)
LIGHT_PISTACHIO = (210, 240, 180)
PINK = (222,165,164)
PEACH = (255, 218, 185)
BOTTLE_GREEN = (0, 106, 78)


CURRENT_MAX=100
MUTED = False

# metryki
SPEED = 1
STEP = 5


#background = pygame.image.load("D:\Programowanie\Python\JezykiSkryptowe\super_gra\Get the We Heart It app!.jpeg")
#background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Apple settings
PROBABILITY_APPLES = 30
APPLE_POINTS = 10
# Wall settings
PROBABILITY_WALL = 35


#Cherry settings
PROBABILITY_CHERRY = 250
CHERRY_SPEED_MULTIPLIER = 2
IMMUNITY_DURATION = 5000
