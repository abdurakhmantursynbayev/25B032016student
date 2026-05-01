import pygame
import random
import sys
import os

# INITIALIZATION
pygame.init()
pygame.mixer.init()

# SCREEN SETTINGS
WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

clock = pygame.time.Clock()
FPS = 60


# COLORS AND FONTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

font = pygame.font.SysFont("Verdana", 24)
small_font = 3
game_over_font = pygame.font.SysFont("Verdana", 45)

# GAME VARIABLES
SPEED = 5
COINS_COLLECTED = 0

#game variables for enemy
speed_increase_every = 5   # increase speed of enemy every 5coin
last_speed_level = 0

# LOAD IMAGES
background_image = pygame.image.load("/Users/admin/25B032016student/practice10/images/AnimatedStreet.png")
player_image = pygame.image.load("/Users/admin/25B032016student/practice10/images/Player.png")
enemy_image = pygame.image.load("/Users/admin/25B032016student/practice10/images/Enemy.png")
coin_image = pygame.image.load("/Users/admin/25B032016student/practice10/images/coin.png")

background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
player_image = pygame.transform.scale(player_image, (50, 90))
enemy_image = pygame.transform.scale(enemy_image, (50, 90))
coin_image = pygame.transform.scale(coin_image, (35, 35))

# LOAD SOUNDS
crash_sound = pygame.mixer.Sound("/Users/admin/25B032016student/practice10/sounds/crash.wav")

pygame.mixer.music.load("/Users/admin/25B032016student/practice10/sounds/background.wav")
pygame.mixer.music.play(-1)


# PLAYER CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Set player image
        self.image = player_image

        # Get rectangle for position and collision
        self.rect = self.image.get_rect()

        # Start position
        self.rect.center = (WIDTH // 2, HEIGHT - 100)

    def move(self):
        # Get pressed keys
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5

        if pressed_keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5

        if pressed_keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 5

        if pressed_keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += 5


# ENEMY CLASS
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Set enemy image
        self.image = enemy_image

        # Get rectangle for position and collision
        self.rect = self.image.get_rect()

        # Start enemy above the screen
        self.respawn()

    def move(self):
        # Enemy moves down
        self.rect.y += SPEED

        if self.rect.top > HEIGHT:
            self.respawn()

    def respawn(self):
        # Random position on the road
        self.rect.center = (
            random.randint(45, WIDTH - 45),
            random.randint(-600, -100)
        )


# COIN CLASS
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #it's weight
        self.weight = 1

        # Set coin image
        self.image = coin_image

        # Get rectangle for position and collision
        self.rect = self.image.get_rect()

        # Start coin above the screen
        self.respawn()

    def move(self):
        # Coin moves down
        self.rect.y += SPEED

        if self.rect.top > HEIGHT:
            self.respawn()

    def respawn(self):
        #random weight
        self.set_weight()
        # Random position on the road
        self.rect.center = (
            random.randint(45, WIDTH - 45),
            random.randint(-700, -50)
        )
    def set_weight(self):
        self.weight = random.choice([1, 1, 1, 2, 2, 3])
        if self.weight == 1:
            size = 30
        elif self.weight == 2:
            size = 38
        elif self.weight == 3:
            size = 46
        
        self.image = pygame.transform.scale(coin_image, (size, size))
        self.rect = self.image.get_rect()

# GAME OVER FUNCTION
def game_over():
    global running

    # Stop music and play crash sound
    pygame.mixer.music.stop()
    crash_sound.play()

    screen.fill(BLACK)

    game_over_text = game_over_font.render("GAME OVER", True, RED)
    coins_text = font.render(f"Coins: {COINS_COLLECTED}", True, WHITE)

    screen.blit(
        game_over_text,
        (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 60)
    )

    screen.blit(
        coins_text,
        (WIDTH // 2 - coins_text.get_width() // 2, HEIGHT // 2)
    )

    pygame.display.update()
    pygame.time.delay(2000)

    pygame.quit()
    sys.exit()


# CREATE OBJECTS
player = Player()
enemy = Enemy()

coin1 = Coin()
coin2 = Coin()
coin3 = Coin()

# SPRITE GROUPS
enemies = pygame.sprite.Group()
enemies.add(enemy)

coins = pygame.sprite.Group()
coins.add(coin1, coin2, coin3)

all_sprites = pygame.sprite.Group()
all_sprites.add(player, enemy, coin1, coin2, coin3)


# MAIN GAME LOOP
running = True

while running:
    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.blit(background_image, (0, 0))

    # Move objects
    player.move()

    for enemy_car in enemies:
        enemy_car.move()

    for coin in coins:
        coin.move()

    # Check collision with enemy
    if pygame.sprite.spritecollideany(player, enemies):
        game_over()

    # Check collision with coins
    collected_coins = pygame.sprite.spritecollide(player, coins, False)

    for coin in collected_coins:
        COINS_COLLECTED += coin.weight
        coin.respawn()
    current_speed_level = COINS_COLLECTED // speed_increase_every
    if current_speed_level > last_speed_level:
        SPEED +=1
        last_speed_level = current_speed_level
    # Draw all objects
    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect)

    # Show coins in top right corner
    coins_text = font.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    screen.blit(coins_text, (WIDTH - coins_text.get_width() - 10, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()