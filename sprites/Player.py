import pygame
from utils import PINK, WIDTH, HEIGHT, BLACK
from sprites.Wall import walls
from sprites.Box import create_box_wall

boxes = create_box_wall()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        old_rect = self.rect.copy()

        # Poruszanie gracza
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 6
        if keys[pygame.K_RIGHT]:
            self.rect.x += 6
        if keys[pygame.K_UP]:
            self.rect.y -= 6
        if keys[pygame.K_DOWN]:
            self.rect.y += 6

        # Sprawdzenie kolizji z granicami ekranu
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        # Sprawdzenie kolizji z ścianami

        if pygame.sprite.spritecollide(self, walls, False):
            self.image.fill(BLACK)

        collided_boxes = pygame.sprite.spritecollide(self, boxes, False)
        if collided_boxes:
            for box in collided_boxes:
                box.decrease_value(1)
                self.rect = old_rect
                self.rect.y+=5