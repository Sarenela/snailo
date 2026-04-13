import pygame
import sys


from settings import WIDTH, HEIGHT, FPS, LIGHT_PISTACHIO, BLACK, SPEED
from sprites.Player import Player
from sprites.Wall import create_walls
from sprites.Apple import create_apples
from sprites.Button import Button
from utils import SCREEN
from sprites.actions import player_boxes_collision, player_walls_collision, player_apples_collision
from sprites.Box import create_box_wall
import settings



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


def update_sprites(player, boxes, walls, apples):
    player.update()
    boxes.update()
    walls.update()
    walls = create_walls(boxes, walls, apples)
    apples.update()
    apples = create_apples(boxes, walls, apples)
    player_boxes_collision(player, boxes)
    player_walls_collision(player, walls)
    player_apples_collision(player, apples)

def update_speed(score):
    if  score > settings.CURRENT_MAX +100:
        SPEED = settings.SPEED*2
        settings.CURRENT_MAX = score
        print("haloo " ,SPEED)


def draw_screen(all_sprites, walls, boxes, apples, player, font):
    SCREEN.fill(LIGHT_PISTACHIO)
    walls.draw(SCREEN)
    boxes.draw(SCREEN)
    apples.draw(SCREEN)
    all_sprites.draw(SCREEN)

    text_surface = font.render("Score: " + str(player.score), True, BLACK)
    SCREEN.blit(text_surface, (WIDTH - text_surface.get_width() - 20, 0))
    text_surface = font.render("Speed: " + str(SPEED), True, BLACK)
    SCREEN.blit(text_surface, (WIDTH - text_surface.get_width() - 20, text_surface.get_height() + 10))

    pygame.display.flip()




def main_game_loop():
    pygame.init()

    font = pygame.font.Font(None, 36)
    boxes = create_box_wall()
    walls = pygame.sprite.Group()
    apples = pygame.sprite.Group()
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)


    running = True
    while running:

        # Częstotliwość odświeżania ekranu
        pygame.time.Clock().tick(FPS)

        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update_sprites(player, boxes, walls, apples)

        update_speed(player.score)

        draw_screen(all_sprites, walls, boxes, apples, player, font)
        if len(boxes) == 0:
            boxes = create_box_wall()

    # Zamknięcie programu
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    start_screen_loop()
