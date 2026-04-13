import time

import pygame,random
from snailo.sprites import Box
from settings import BOX_NUM,WIDTH,HEIGHT,PISTACHIO,BLACK


#SCREEN
def init_screen():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("supi dupi game")
    return screen

SCREEN = init_screen()

def set_speed(value):
    global SPEED
    SPEED = value

def set_curr_max(value):
    global CURRENT_MAX
    CURRENT_MAX = value

#helper methods
def draw_missing():
    return set(random.sample(range(BOX_NUM +1), k=2))
def create_box_wall():
    missing = draw_missing()
    boxes = pygame.sprite.Group()

    width= (WIDTH - 10*BOX_NUM)/BOX_NUM

    print(width)

    for i in range(BOX_NUM):
        if i not  in missing:
            print(i)
            boxes.add(Box( 10+ i *(width +10),0, width, width, random.randint(5, 50)))
    return boxes