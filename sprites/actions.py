
from snailo.settings import HEIGHT, STEP, APPLE_POINTS

import snailo.settings as settings
import pygame

_eat_sound = None

def _play_eat_sound():
    global _eat_sound
    if settings.MUTED:
        return
    if _eat_sound is None:
        _eat_sound = pygame.mixer.Sound("music/freesound_community-eating_aple-37444.mp3")
        _eat_sound.set_volume(1.0)
    _eat_sound.play(maxtime=800)
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
        _play_eat_sound()

def player_cherries_collision(player, cherries):
    hit = pygame.sprite.spritecollideany(player, cherries)
    if hit:
        hit.kill()
        player.cherry_count += 1
        _play_eat_sound()