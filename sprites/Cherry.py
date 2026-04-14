import pygame, random
from snailo.settings import HEIGHT, WIDTH, STEP
import snailo.settings

class Cherry(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load("pics/cherry.png")
        self.image = pygame.transform.scale(self.original_image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += STEP * settings.SPEED
        if self.rect.y > HEIGHT:
            self.kill()


def create_cherries(boxes, walls, cherries):
    if random.randint(0, settings.PROBABILITY_CHERRY) == 2:
        x = random.randint(0, WIDTH)
        cherry = Cherry(x, 0)
        if not pygame.sprite.spritecollide(cherry, walls, False) and \
           not pygame.sprite.spritecollide(cherry, boxes, False) and \
           not pygame.sprite.spritecollide(cherry, cherries, False):
            cherries.add(cherry)
    return cherries