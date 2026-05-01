import pygame
import random
import sys

# INITIALIZATION
pygame.init()

# SCREEN SETTINGS
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 120, 0)
RED = (220, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (160, 32, 240)

# FONTS
font = pygame.font.SysFont("Verdana", 24)
small_font = pygame.font.SysFont("Verdana", 16)
game_over_font = pygame.font.SysFont("Verdana", 45)

# GAME VARIABLES
SCORE = 0
LEVEL = 1
FOODS_FOR_NEXT_LEVEL = 4
SPEED = 8

# Food disappears after this time
FOOD_LIFETIME = 5000  # 5000 milliseconds = 5 seconds

# Snake starts from center
snake = [
    [WIDTH // 2, HEIGHT // 2],
    [WIDTH // 2 - CELL_SIZE, HEIGHT // 2],
    [WIDTH // 2 - 2 * CELL_SIZE, HEIGHT // 2]
]

# Snake starts moving to the right
direction = "RIGHT"
next_direction = "RIGHT"


# FOOD FUNCTION
def generate_food():
    while True:
        # Food position must be inside the playing area
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)

        food_position = [x, y]

        # Food must not appear on snake
        if food_position not in snake:
            # Food can have different weights
            weight = random.choice([1, 1, 1, 2, 2, 3])

            # Save food position, weight and spawn time
            food = {
                "pos": food_position,
                "weight": weight,
                "spawn_time": pygame.time.get_ticks(),
                "lifetime": FOOD_LIFETIME
            }

            return food


# GAME OVER FUNCTION
def game_over():
    screen.fill(BLACK)

    text = game_over_font.render("GAME OVER", True, RED)
    score_text = font.render(f"Score: {SCORE}", True, WHITE)
    level_text = font.render(f"Level: {LEVEL}", True, WHITE)

    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 80))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 20))
    screen.blit(level_text, (WIDTH // 2 - level_text.get_width() // 2, HEIGHT // 2 + 20))

    pygame.display.update()
    pygame.time.delay(2000)

    pygame.quit()
    sys.exit()


# DRAW SNAKE FUNCTION
def draw_snake():
    for index, block in enumerate(snake):
        # First block is snake head
        if index == 0:
            pygame.draw.rect(screen, DARK_GREEN, (block[0], block[1], CELL_SIZE, CELL_SIZE))
        else:
            pygame.draw.rect(screen, GREEN, (block[0], block[1], CELL_SIZE, CELL_SIZE))


# DRAW FOOD FUNCTION
def draw_food(food):
    # Food color depends on weight
    if food["weight"] == 1:
        color = RED
    elif food["weight"] == 2:
        color = YELLOW
    else:
        color = PURPLE

    x, y = food["pos"]

    # Draw food
    pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))

    # Draw food weight text
    weight_text = small_font.render(f"+{food['weight']}", True, WHITE)
    screen.blit(weight_text, (x, y - 18))


# CREATE FIRST FOOD
food = generate_food()

# MAIN GAME LOOP
running = True

while running:
    # CHECK EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Change snake direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                next_direction = "UP"

            if event.key == pygame.K_DOWN and direction != "UP":
                next_direction = "DOWN"

            if event.key == pygame.K_LEFT and direction != "RIGHT":
                next_direction = "LEFT"

            if event.key == pygame.K_RIGHT and direction != "LEFT":
                next_direction = "RIGHT"

    # CHECK FOOD TIMER
    current_time = pygame.time.get_ticks()

    # If food stayed too long, generate new food
    if current_time - food["spawn_time"] > food["lifetime"]:
        food = generate_food()

    # UPDATE DIRECTION
    direction = next_direction

    # MOVE SNAKE HEAD
    head_x = snake[0][0]
    head_y = snake[0][1]

    if direction == "UP":
        head_y -= CELL_SIZE

    if direction == "DOWN":
        head_y += CELL_SIZE

    if direction == "LEFT":
        head_x -= CELL_SIZE

    if direction == "RIGHT":
        head_x += CELL_SIZE

    new_head = [head_x, head_y]

    # CHECK WALL COLLISION
    if (
        head_x < 0 or
        head_x >= WIDTH or
        head_y < 0 or
        head_y >= HEIGHT
    ):
        game_over()

    # CHECK SELF COLLISION
    if new_head in snake:
        game_over()

    # ADD NEW HEAD
    snake.insert(0, new_head)

    # CHECK FOOD COLLISION
    if new_head == food["pos"]:
        # Add food weight to score
        SCORE += food["weight"]

        # Increase level after several score points
        if SCORE % FOODS_FOR_NEXT_LEVEL == 0:
            LEVEL += 1
            SPEED += 2

        # Generate new food not on snake
        food = generate_food()
    else:
        # Remove tail if food was not eaten
        snake.pop()

    # DRAW BACKGROUND
    screen.fill(BLACK)

    # DRAW FOOD
    draw_food(food)

    # DRAW SNAKE
    draw_snake()

    # DRAW SCORE AND LEVEL
    score_text = font.render(f"Score: {SCORE}", True, WHITE)
    level_text = font.render(f"Level: {LEVEL}", True, WHITE)

    # Draw food timer
    time_left = max(0, (food["lifetime"] - (pygame.time.get_ticks() - food["spawn_time"])) // 1000)
    timer_text = small_font.render(f"Food time: {time_left}", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - level_text.get_width() - 10, 10))
    screen.blit(timer_text, (10, 45))

    # UPDATE DISPLAY
    pygame.display.update()

    # GAME SPEED
    clock.tick(SPEED)

pygame.quit()
sys.exit()