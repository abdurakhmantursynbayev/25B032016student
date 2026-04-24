import pygame
import sys

# INITIALIZATION
pygame.init()

# SCREEN SETTINGS
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

# BASE LAYER
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill("black")
screen.fill("black")

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
PURPLE = (160, 32, 240)

# GAME VARIABLES
LMBpressed = False
THICKNESS = 5

startX = startY = 0
currX = currY = 0
prevX = prevY = 0

current_color = RED
current_tool = "brush"

font = pygame.font.SysFont("Verdana", 18)


# HELPER FUNCTIONS
def calculate_rect(x1, y1, x2, y2):
    # Creates correct rectangle even if we drag left or up
    return pygame.Rect(
        min(x1, x2),
        min(y1, y2),
        abs(x1 - x2),
        abs(y1 - y2)
    )


def calculate_circle(x1, y1, x2, y2):
    # Center is start point, radius depends on mouse distance
    radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    return radius


def draw_ui():
    # Shows current tool, color and thickness
    tool_text = font.render(f"Tool: {current_tool}", True, WHITE)
    color_text = font.render("1-Red  2-Green  3-Blue  4-Yellow  5-Purple  6-White", True, WHITE)
    help_text = font.render("B-Brush  R-Rect  O-Circle  E-Eraser  C-Clear  +/- Thickness", True, WHITE)
    thickness_text = font.render(f"Thickness: {THICKNESS}", True, WHITE)

    screen.blit(tool_text, (10, 10))
    screen.blit(color_text, (10, 35))
    screen.blit(help_text, (10, 60))
    screen.blit(thickness_text, (10, 85))


def commit_screen():
    # Saves finished drawing to base_layer
    base_layer.blit(screen, (0, 0))


def draw_preview():
    # Restores old drawing first
    screen.blit(base_layer, (0, 0))

    # Draws live preview depending on selected tool
    if current_tool == "rect":
        pygame.draw.rect(
            screen,
            current_color,
            calculate_rect(startX, startY, currX, currY),
            THICKNESS
        )

    elif current_tool == "circle":
        radius = calculate_circle(startX, startY, currX, currY)
        pygame.draw.circle(
            screen,
            current_color,
            (startX, startY),
            radius,
            THICKNESS
        )


# MAIN LOOP
running = True

while running:
    for event in pygame.event.get():

        # QUIT
        if event.type == pygame.QUIT:
            running = False

        # KEYBOARD CONTROL
        if event.type == pygame.KEYDOWN:

            # Tool selection
            if event.key == pygame.K_b:
                current_tool = "brush"

            if event.key == pygame.K_r:
                current_tool = "rect"

            if event.key == pygame.K_o:
                current_tool = "circle"

            if event.key == pygame.K_e:
                current_tool = "eraser"

            # Color selection
            if event.key == pygame.K_1:
                current_color = RED

            if event.key == pygame.K_2:
                current_color = GREEN

            if event.key == pygame.K_3:
                current_color = BLUE

            if event.key == pygame.K_4:
                current_color = YELLOW

            if event.key == pygame.K_5:
                current_color = PURPLE

            if event.key == pygame.K_6:
                current_color = WHITE

            # Thickness control
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1

            if event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)

            # Clear both layers
            if event.key == pygame.K_c:
                screen.fill(BLACK)
                base_layer.fill(BLACK)

        # MOUSE BUTTON DOWN
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True

            startX, startY = event.pos
            currX, currY = event.pos
            prevX, prevY = event.pos

        # MOUSE MOTION
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX, currY = event.pos

                # Brush tool draws immediately
                if current_tool == "brush":
                    pygame.draw.line(
                        screen,
                        current_color,
                        (prevX, prevY),
                        (currX, currY),
                        THICKNESS
                    )
                    commit_screen()

                # Eraser draws black line
                elif current_tool == "eraser":
                    pygame.draw.line(
                        screen,
                        BLACK,
                        (prevX, prevY),
                        (currX, currY),
                        THICKNESS
                    )
                    commit_screen()

                # Rect and circle use base_layer preview
                elif current_tool == "rect" or current_tool == "circle":
                    draw_preview()

                prevX, prevY = currX, currY

        # MOUSE BUTTON UP
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False

            currX, currY = event.pos

            # Commit rectangle
            if current_tool == "rect":
                screen.blit(base_layer, (0, 0))
                pygame.draw.rect(
                    screen,
                    current_color,
                    calculate_rect(startX, startY, currX, currY),
                    THICKNESS
                )
                commit_screen()

            # Commit circle
            if current_tool == "circle":
                screen.blit(base_layer, (0, 0))
                radius = calculate_circle(startX, startY, currX, currY)

                pygame.draw.circle(
                    screen,
                    current_color,
                    (startX, startY),
                    radius,
                    THICKNESS
                )
                commit_screen()

    # DRAW UI
    screen.blit(base_layer, (0, 0))

    if LMBpressed and (current_tool == "rect" or current_tool == "circle"):
        draw_preview()

    draw_ui()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()