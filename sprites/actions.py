
from snailo.settings import HEIGHT, STEP, APPLE_POINTS

import snailo.settings
import pygame
def player_boxes_collision(player, boxes):
    collided_boxes = pygame.sprite.spritecollide(player, boxes, False)
    if player.immune:
        return
    if collided_boxes:
        for box in collided_boxes:
            if player.score > 0:
                player.score -= 1
                box.decrease_value(1)
            player.rect = player.prev_rect
            player.rect.y += STEP*settings.SPEED

def player_walls_collision(player, walls):
    if player.immune:
        return
    collision_walls = pygame.sprite.spritecollideany(player, walls)
    if collision_walls:
        player.rect = player.prev_rect
        player.rect.y += STEP*settings.SPEED

def player_apples_collision(player, apples):
    collision_apples = pygame.sprite.spritecollideany(player, apples)
    if collision_apples:
        player.score += APPLE_POINTS
        collision_apples.kill()

def player_cherries_collision(player, cherries):
    hit = pygame.sprite.spritecollideany(player, cherries)
    if hit:
        hit.kill()
        if not player.immune:
            settings.SPEED *= settings.CHERRY_SPEED_MULTIPLIER
        player.immune = True
        player.immune_timer = pygame.time.get_ticks()