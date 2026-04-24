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
GRAY = (80, 80, 80)

# FONTS
font = pygame.font.SysFont("Verdana", 24)
game_over_font = pygame.font.SysFont("Verdana", 45)

# GAME VARIABLES
SCORE = 0
LEVEL = 1
FOODS_FOR_NEXT_LEVEL = 4
SPEED = 8

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
            return food_position


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
    if new_head == food:
        SCORE += 1

        # Increase level after several foods
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
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

    # DRAW SNAKE
    draw_snake()

    # DRAW SCORE AND LEVEL
    score_text = font.render(f"Score: {SCORE}", True, WHITE)
    level_text = font.render(f"Level: {LEVEL}", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - level_text.get_width() - 10, 10))

    # UPDATE DISPLAY
    pygame.display.update()

    # GAME SPEED
    clock.tick(SPEED)

pygame.quit()
sys.exit()