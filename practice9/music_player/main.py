import pygame
pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))

background = pygame.image.load("practice9/music_player/music_commands_image/tame_impala_.png")
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill((255,255,255))
    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit