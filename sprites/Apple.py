import pygame,random
from snailo.settings import WHITE, HEIGHT, BOX_HEIGHT,BOX_WIDTH,BOX_SEP,WIDTH, RED, STEP, PROBABILITY_APPLES
import snailo.settings

class Apple(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((30,30))
        # self.image.fill(RED)
        self.original_image = pygame.image.load("pics/clipart1288.png")
        self.image = pygame.transform.scale(self.original_image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y+= STEP*settings.SPEED
        if self.rect.y>HEIGHT:
            self.kill()



def create_apples(boxes, walls, apples):
    if random.randint(0,PROBABILITY_APPLES) == 2:
        x = random.randint(0,WIDTH)
        apple = Apple(x, 0)
        if not pygame.sprite.spritecollide(apple, walls, False) and \
            not pygame.sprite.spritecollide(apple, boxes, False) and \
                not pygame.sprite.spritecollide(apple, apples, False) :
            apples.add(apple)
    return apples




