import pygame
from snailo.settings import PINK, WIDTH, HEIGHT, BLACK, STEP
import snailo.settings


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load("pics/snail.png")
        self.image = pygame.transform.scale(self.original_image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.score = 100
        self.immune = False
        self.immune_timer = 0

    def update(self):
        self.prev_rect = self.rect.copy()
        self.move()
        self.check_screen_collisions()
        self._tick_immunity()

    def _tick_immunity(self):
        if self.immune and pygame.time.get_ticks() - self.immune_timer > settings.IMMUNITY_DURATION:
            self.immune = False
            settings.SPEED /= settings.CHERRY_SPEED_MULTIPLIER

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= STEP * settings.SPEED + 2
        if keys[pygame.K_RIGHT]:
            self.rect.x += STEP * settings.SPEED * +2
        if keys[pygame.K_UP]:
            self.rect.y -= STEP * settings.SPEED * +2
        if keys[pygame.K_DOWN]:
            self.rect.y += STEP * settings.SPEED * +2

    def check_screen_collisions(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT