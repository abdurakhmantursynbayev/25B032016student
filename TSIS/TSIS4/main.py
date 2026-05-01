import pygame
import json
from game import run_game
from db import create_tables, get_top_players


pygame.init()
create_tables()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS4 Menu")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 32)
small_font = pygame.font.SysFont("Verdana", 22)

state = "menu"
username = ""
result = {"score": 0, "level": 1, "best": 0}


def load_settings():
    with open("settings.json", "r") as file:
        return json.load(file)


def save_settings(settings):
    with open("settings.json", "w") as file:
        json.dump(settings, file, indent=4)


settings = load_settings()


def text(msg, x, y, color=(255, 255, 255), f=None):
    if f is None:
        f = font
    screen.blit(f.render(msg, True, color), (x, y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:

            # Main menu
            if state == "menu":
                if event.key == pygame.K_1:
                    username = ""
                    state = "input"
                elif event.key == pygame.K_2:
                    state = "leaderboard"
                elif event.key == pygame.K_3:
                    settings = load_settings()
                    state = "settings"
                elif event.key == pygame.K_4:
                    pygame.quit()
                    exit()

            # Username input
            elif state == "input":
                if event.key == pygame.K_RETURN and username:
                    result = run_game(username)
                    state = "game_over"
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

            # Game over
            elif state == "game_over":
                if event.key == pygame.K_1:
                    state = "input"
                    username = ""
                elif event.key == pygame.K_2:
                    state = "menu"

            # Leaderboard
            elif state == "leaderboard":
                if event.key == pygame.K_ESCAPE:
                    state = "menu"

            # Settings
            elif state == "settings":
                if event.key == pygame.K_g:
                    settings["grid"] = not settings["grid"]

                elif event.key == pygame.K_s:
                    settings["sound"] = not settings["sound"]

                elif event.key == pygame.K_c:
                    colors = [
                        [0, 200, 0],
                        [0, 100, 255],
                        [220, 0, 0],
                        [255, 255, 0],
                        [160, 32, 240]
                    ]

                    i = colors.index(settings["snake_color"])
                    settings["snake_color"] = colors[(i + 1) % len(colors)]

                elif event.key == pygame.K_ESCAPE:
                    save_settings(settings)
                    state = "menu"

    screen.fill((0, 0, 0))

    if state == "menu":
        text("SNAKE TSIS4", 185, 120)
        text("1 - Play", 220, 210, f=small_font)
        text("2 - Leaderboard", 220, 250, f=small_font)
        text("3 - Settings", 220, 290, f=small_font)
        text("4 - Quit", 220, 330, f=small_font)

    elif state == "input":
        text("Enter username:", 160, 200)
        text(username, 220, 260, (255, 255, 0))

    elif state == "game_over":
        text("GAME OVER", 190, 140, (255, 0, 0))
        text(f"Score: {result['score']}", 210, 220, f=small_font)
        text(f"Level: {result['level']}", 210, 260, f=small_font)
        text(f"Best: {result['best']}", 210, 300, f=small_font)
        text("1 - Retry", 210, 370, f=small_font)
        text("2 - Menu", 210, 410, f=small_font)

    elif state == "leaderboard":
        text("TOP 10", 240, 50)

        data = get_top_players()
        y = 110

        for i, row in enumerate(data, 1):
            username_db, score, level, played_at = row
            text(f"{i}. {username_db} | {score} | lvl {level} | {played_at.date()}", 60, y, f=small_font)
            y += 35

        text("ESC - Back", 210, 540, f=small_font)

    elif state == "settings":
        text("SETTINGS", 210, 100)
        text(f"G - Grid: {settings['grid']}", 150, 190, f=small_font)
        text(f"S - Sound: {settings['sound']}", 150, 230, f=small_font)
        text("C - Change color", 150, 270, f=small_font)
        pygame.draw.rect(screen, tuple(settings["snake_color"]), (250, 320, 100, 40))
        text("ESC - Save & Back", 150, 420, f=small_font)

    pygame.display.flip()
    clock.tick(60)