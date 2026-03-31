import pygame,random
from utils import WHITE, HEIGHT,draw6,BOX_HEIGHT,BOX_WIDTH,BOX_SEP,WIDTH


pygame.init()
class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, value):
        pygame.sprite.Sprite.__init__(self)
        self.value = value

        # Create a surface for the box with value displayed
        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.value), True, (0, 0, 0))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        self.image.blit(text, text_rect)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y+=5
        self.update_text()
        if self.rect.y>HEIGHT:
            self.kill()


    def update_text(self):
        text = pygame.font.Font(None, 24).render(str(self.value), True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.rect.width // 2, self.rect.height // 2))
        self.image.fill(WHITE)
        self.image.blit(text, text_rect)

    def decrease_value(self, amount):
        self.value -= amount
        if self.value <= 0:
             self.value = 0
             self.kill()  # Remove the box from the group
        self.update_text()


def create_box_wall():
    indexes = draw6()
    boxes = pygame.sprite.Group()

    for i in range(6):
        if i in indexes:
            boxes.add(Box(BOX_WIDTH / 2 + (i * (BOX_SEP + BOX_WIDTH)) , BOX_HEIGHT / 2 , BOX_WIDTH, BOX_HEIGHT, random.randint(5, 50)))
    return boxes