import pygame
import random
import json
import os

from db import save_game, get_best_score


def run_game(username):
    pygame.init()

    WIDTH, HEIGHT = 600, 600
    CELL = 20

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("TSIS4 Snake")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Verdana", 22)
    small_font = pygame.font.SysFont("Verdana", 16)

    # Load settings
    with open("settings.json", "r") as file:
        settings = json.load(file)

    snake_color = tuple(settings["snake_color"])
    show_grid = settings["grid"]

    # Optional music
    if settings["sound"] and os.path.exists("sounds/background.mp3"):
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/background.mp3")
        pygame.mixer.music.play(-1)

    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (CELL, 0)

    score = 0
    level = 1
    speed = 8
    best = get_best_score(username)

    foods = []
    obstacles = []
    power = None
    active_power = None
    power_start = 0
    shield = False

    def random_pos():
        # Position should not be on snake or obstacles
        while True:
            pos = (
                random.randrange(0, WIDTH, CELL),
                random.randrange(0, HEIGHT, CELL)
            )
            if pos not in snake and pos not in obstacles:
                return pos

    def new_food(kind="normal"):
        # Normal food has random weight. Poison is dangerous food.
        return {
            "pos": random_pos(),
            "weight": random.choice([1, 1, 2, 3]),
            "kind": kind,
            "time": pygame.time.get_ticks()
        }

    def new_power():
        # One power-up on field
        return {
            "pos": random_pos(),
            "type": random.choice(["boost", "slow", "shield"]),
            "time": pygame.time.get_ticks()
        }

    def make_obstacles():
        # From level 3 obstacles appear.
        # We keep cells around snake head free, so snake is not trapped immediately.
        obs = []
        head = snake[0]

        safe_cells = [
            head,
            (head[0] + CELL, head[1]),
            (head[0] - CELL, head[1]),
            (head[0], head[1] + CELL),
            (head[0], head[1] - CELL)
        ]

        while len(obs) < 5:
            pos = (
                random.randrange(0, WIDTH, CELL),
                random.randrange(0, HEIGHT, CELL)
            )

            if pos not in snake and pos not in obs and pos not in safe_cells:
                obs.append(pos)

        return obs

    def draw_grid():
        for x in range(0, WIDTH, CELL):
            pygame.draw.line(screen, (35, 35, 35), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL):
            pygame.draw.line(screen, (35, 35, 35), (0, y), (WIDTH, y))

    # Start with normal food and poison food
    foods.append(new_food("normal"))
    foods.append(new_food("poison"))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game(username, score, level)
                return {"score": score, "level": level, "best": best}

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, CELL):
                    direction = (0, -CELL)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL):
                    direction = (0, CELL)
                elif event.key == pygame.K_LEFT and direction != (CELL, 0):
                    direction = (-CELL, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                    direction = (CELL, 0)

        now = pygame.time.get_ticks()

        # Power effect timer: boost/slow lasts 5 seconds
        if active_power and active_power != "shield":
            if now - power_start > 5000:
                active_power = None

        # Spawn one power-up randomly
        if power is None and random.randint(1, 120) == 1:
            power = new_power()

        # Power-up disappears after 8 seconds
        if power and now - power["time"] > 8000:
            power = None

        # Move snake
        head = (
            snake[0][0] + direction[0],
            snake[0][1] + direction[1]
        )

        snake.insert(0, head)

        # Collision
        hit_wall = head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT
        hit_self = head in snake[1:]
        hit_obstacle = head in obstacles

        if hit_wall or hit_self or hit_obstacle:
            if shield:
                shield = False
                snake.pop(0)
            else:
                save_game(username, score, level)
                if settings["sound"]:
                    pygame.mixer.music.stop()
                return {"score": score, "level": level, "best": max(best, score)}

        ate = False

        # Foods disappear after 5 seconds
        foods = [f for f in foods if now - f["time"] < 5000]

        # Keep one normal and one poison food
        if not any(f["kind"] == "normal" for f in foods):
            foods.append(new_food("normal"))
        if not any(f["kind"] == "poison" for f in foods):
            foods.append(new_food("poison"))

        # Eat food or poison
        for food in foods[:]:
            if head == food["pos"]:
                if food["kind"] == "poison":
                    # Poison removes 2 segments
                    for _ in range(2):
                        if len(snake) > 1:
                            snake.pop()

                    if len(snake) <= 1:
                        save_game(username, score, level)
                        return {"score": score, "level": level, "best": max(best, score)}

                else:
                    score += food["weight"]
                    ate = True

                    # Level and speed increase
                    level = score // 5 + 1
                    speed = 8 + level

                    # Obstacles from level 3
                    if level >= 3 and not obstacles:
                        obstacles = make_obstacles()

                foods.remove(food)
                break

        # Eat power-up
        if power and head == power["pos"]:
            if power["type"] == "shield":
                shield = True
            else:
                active_power = power["type"]
                power_start = now

            power = None

        # If normal food not eaten, remove tail
        if not ate:
            snake.pop()

        # Current speed
        current_speed = speed
        if active_power == "boost":
            current_speed += 5
        elif active_power == "slow":
            current_speed = max(4, current_speed - 4)

        # Draw
        screen.fill((0, 0, 0))

        if show_grid:
            draw_grid()

        for obs in obstacles:
            pygame.draw.rect(screen, (100, 100, 100), (*obs, CELL, CELL))

        for block in snake:
            pygame.draw.rect(screen, snake_color, (*block, CELL, CELL))

        for food in foods:
            if food["kind"] == "poison":
                color = (120, 0, 0)
            elif food["weight"] == 1:
                color = (220, 0, 0)
            elif food["weight"] == 2:
                color = (255, 255, 0)
            else:
                color = (255, 120, 0)

            pygame.draw.rect(screen, color, (*food["pos"], CELL, CELL))

        if power:
            color = (0, 150, 255)
            if power["type"] == "slow":
                color = (0, 255, 255)
            elif power["type"] == "shield":
                color = (255, 255, 255)

            pygame.draw.rect(screen, color, (*power["pos"], CELL, CELL))

        screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
        screen.blit(font.render(f"Level: {level}", True, (255, 255, 255)), (10, 40))
        screen.blit(font.render(f"Best: {best}", True, (255, 255, 0)), (10, 70))

        if shield:
            screen.blit(small_font.render("Shield ON", True, (0, 150, 255)), (10, 100))

        if active_power:
            screen.blit(small_font.render(f"Power: {active_power}", True, (255, 255, 0)), (10, 125))

        pygame.display.flip()
        clock.tick(current_speed)