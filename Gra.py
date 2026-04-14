import pygame
import sys

from sprites.Cherry import create_cherries
from snailo.settings import SPEED
from sprites.Box import create_box_wall

from snailo.settings import WIDTH, HEIGHT, FPS, LIGHT_PISTACHIO, BLACK
from sprites.Player import Player
import snailo.settings
from sprites.Wall import create_walls
from sprites.Apple import create_apples
from sprites.Button import Button
from utils import SCREEN
from sprites.actions import player_boxes_collision, player_walls_collision, player_apples_collision, \
    player_cherries_collision


def handle_events():
    for event in pygame.event.get():
        return not event.type == pygame.QUIT


def start_screen_loop():
    font = pygame.font.Font(None, 36)

    start_button = Button(WIDTH // 2, HEIGHT // 2, 200, 50, "Start", font)

    while True:
        pygame.time.Clock().tick(FPS)

        SCREEN.fill(LIGHT_PISTACHIO)
        start_button.update()
        start_button.draw(SCREEN)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if start_button.is_clicked(pos):
                    main_game_loop()
            else:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



def game_over_screen_loop(player, elapsed_seconds):
    font = pygame.font.Font(None, 36)
    retry_button = Button(WIDTH // 2, HEIGHT // 2, 200, 50, "Retry", font)

    # Format as MM:SS
    minutes = elapsed_seconds // 60
    seconds = elapsed_seconds % 60
    time_str = f"Time: {minutes:02}:{seconds:02}"

    while True:
        pygame.time.Clock().tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if retry_button.is_clicked(pos):
                    main_game_loop()

        SCREEN.fill(LIGHT_PISTACHIO)
        retry_button.update()
        retry_button.draw(SCREEN)

        score_text = font.render("Score: " + str(player.score), True, BLACK)
        SCREEN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 100))

        time_text = font.render(time_str, True, BLACK)
        SCREEN.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, HEIGHT // 2 - 60))

        pygame.display.flip()

def update_sprites(player, boxes, walls, apples, cherries):
    player.update()
    boxes.update()
    walls.update()
    walls = create_walls(boxes, walls, apples)
    apples.update()
    apples = create_apples(boxes, walls, apples)
    cherries.update()
    cherries = create_cherries(boxes, walls, cherries)
    player_boxes_collision(player, boxes)
    player_walls_collision(player, walls)
    player_apples_collision(player, apples)
    player_cherries_collision(player, cherries)
    return cherries


def update_speed(score):
    if  score >settings.CURRENT_MAX +100:
        settings.SPEED = settings.SPEED +1
        settings.CURRENT_MAX = score
        print("haloo " ,SPEED)

def draw_screen(all_sprites, walls, boxes, apples, player, font, start_time, cherries):
    SCREEN.fill(LIGHT_PISTACHIO)
    walls.draw(SCREEN)
    boxes.draw(SCREEN)
    apples.draw(SCREEN)
    cherries.draw(SCREEN)                                      # ← renamed
    all_sprites.draw(SCREEN)

    elapsed = (pygame.time.get_ticks() - start_time) // 1000
    minutes, seconds = divmod(elapsed, 60)

    score_surface = font.render("Score: " + str(player.score), True, BLACK)
    SCREEN.blit(score_surface, (WIDTH - score_surface.get_width() - 20, 0))

    speed_surface = font.render("Speed: " + str(round(settings.SPEED, 2)), True, BLACK)
    SCREEN.blit(speed_surface, (WIDTH - speed_surface.get_width() - 20, score_surface.get_height() + 10))

    time_surface = font.render(f"Time: {minutes:02}:{seconds:02}", True, BLACK)
    SCREEN.blit(time_surface, (20, 0))

    if player.immune:
        remaining = (settings.IMMUNITY_DURATION // 1000) - (pygame.time.get_ticks() - player.immune_timer) // 1000
        immune_surface = font.render(f"IMMUNE: {remaining}s", True, (220, 20, 60))
        SCREEN.blit(immune_surface, (20, 30))

    pygame.display.flip()


def main_game_loop():
    pygame.init()
    font = pygame.font.Font(None, 36)

    boxes = create_box_wall()
    walls = pygame.sprite.Group()
    apples = pygame.sprite.Group()
    cherries = pygame.sprite.Group()
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    start_time = pygame.time.get_ticks()

    running = True
    while running:
        pygame.time.Clock().tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        cherries = update_sprites(player, boxes, walls, apples, cherries)

        update_speed(player.score)
        draw_screen(all_sprites, walls, boxes, apples, player, font, start_time, cherries)

        if len(boxes) == 0:
            boxes = create_box_wall()
        if player.rect.bottom >= HEIGHT:
            elapsed_seconds = (pygame.time.get_ticks() - start_time) // 1000
            game_over_screen_loop(player, elapsed_seconds)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    start_screen_loop()
