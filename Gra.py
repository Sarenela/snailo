import pygame
import sys

from sprites.Cherry import create_cherries
from snailo.settings import SPEED
from sprites.Box import create_box_wall

from snailo.settings import WIDTH, HEIGHT, FPS, LIGHT_PISTACHIO, BLACK
from sprites.Player import Player
import snailo.settings as settings
from sprites.Wall import create_walls
from sprites.Apple import create_apples
from sprites.Button import Button, SpeakerButton
from utils import SCREEN
from sprites.actions import player_boxes_collision, player_walls_collision, player_apples_collision, \
    player_cherries_collision


def handle_events():
    for event in pygame.event.get():
        return not event.type == pygame.QUIT


def start_screen_loop():
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 26)

    start_button = Button(WIDTH // 2, HEIGHT * 3 // 4, 200, 50, "Start", font)

    title = font.render("SNAILO", True, BLACK)

    instructions = [
        "Survive as long as possible!",
        "",
        "Arrow keys  -  move the snail",
        "Avoid walls (you can no not go trough them) ",
        "Avoid boxes (they cost points)"
        "Collect apples for bonus points",
        "Collect cherries and press SPACE",
        "  to activate immunity + speed boost",
    ]

    while True:
        pygame.time.Clock().tick(FPS)

        SCREEN.fill(LIGHT_PISTACHIO)

        SCREEN.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 4))

        for i, line in enumerate(instructions):
            surf = small_font.render(line, True, BLACK)
            SCREEN.blit(surf, (WIDTH // 2 - surf.get_width() // 2, HEIGHT // 4 + 50 + i * 28))

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



def game_over_screen_loop(player, elapsed_seconds, speaker_button):
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
                if speaker_button.is_clicked(pos):
                    speaker_button.toggle()
                elif retry_button.is_clicked(pos):
                    main_game_loop(speaker_button)

        SCREEN.fill(LIGHT_PISTACHIO)
        retry_button.update()
        retry_button.draw(SCREEN)

        score_text = font.render("Score: " + str(player.score), True, BLACK)
        SCREEN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 100))

        time_text = font.render(time_str, True, BLACK)
        SCREEN.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, HEIGHT // 2 - 60))

        speaker_button.draw(SCREEN)
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

def draw_screen(all_sprites, walls, boxes, apples, player, font, start_time, cherries, speaker_button):
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

    cherry_surface = font.render("Cherries: " + str(player.cherry_count), True, (180, 0, 60))
    SCREEN.blit(cherry_surface, (WIDTH - cherry_surface.get_width() - 20, score_surface.get_height() + speed_surface.get_height() + 20))

    time_surface = font.render(f"Time: {minutes:02}:{seconds:02}", True, BLACK)
    SCREEN.blit(time_surface, (20, 0))

    if player.immune:
        remaining = (settings.IMMUNITY_DURATION // 1000) - (pygame.time.get_ticks() - player.immune_timer) // 1000
        immune_surface = font.render(f"IMMUNE: {remaining}s", True, (220, 20, 60))
        SCREEN.blit(immune_surface, (20, 30))

    speaker_button.draw(SCREEN)
    pygame.display.flip()


def main_game_loop(speaker_button=None):
    pygame.init()
    pygame.mixer.music.load("music/paulyudin-be-funny-153884.mp3")
    pygame.mixer.music.play(-1)
    font = pygame.font.Font(None, 36)

    if speaker_button is None:
        speaker_button = SpeakerButton(10, HEIGHT - SpeakerButton.SIZE - 10)
    elif speaker_button.muted:
        pygame.mixer.music.pause()
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.activate_cherry()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if speaker_button.is_clicked(pygame.mouse.get_pos()):
                    speaker_button.toggle()

        cherries = update_sprites(player, boxes, walls, apples, cherries)

        update_speed(player.score)
        draw_screen(all_sprites, walls, boxes, apples, player, font, start_time, cherries, speaker_button)

        if len(boxes) == 0:
            boxes = create_box_wall()
        if player.rect.bottom >= HEIGHT:
            elapsed_seconds = (pygame.time.get_ticks() - start_time) // 1000
            pygame.mixer.music.stop()
            if not settings.MUTED:
                fail_sound = pygame.mixer.Sound("music/fail.mp3")
                fail_sound.play()
                pygame.time.wait(int(fail_sound.get_length() * 1000))
            game_over_screen_loop(player, elapsed_seconds, speaker_button)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    start_screen_loop()
