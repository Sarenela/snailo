from snailo.settings import STEP, APPLE_POINTS, SPEED

import pygame


def player_boxes_collision(player, boxes):
    collided_boxes = pygame.sprite.spritecollide(player, boxes, False)
    if collided_boxes:
        for box in collided_boxes:
            if player.score > 0:
                player.score -= 1
                box.decrease_value(1)
            player.rect = player.prev_rect
            player.rect.y += STEP*SPEED

def player_walls_collision(player, walls):
    collision_walls = pygame.sprite.spritecollideany(player, walls)
    if collision_walls:
        player.rect = player.prev_rect
        player.rect.y += STEP*SPEED

def player_apples_collision(player, apples):
    collision_apples = pygame.sprite.spritecollideany(player, apples)
    if collision_apples:
        player.score += APPLE_POINTS
        collision_apples.kill()