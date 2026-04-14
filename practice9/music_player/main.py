import pygame
import os
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Музыкальный плеер 🎵")

music_folder = "/Users/admin/25B032016student/practice9/music_player/music"
songs = [
    os.path.join(music_folder, f)
    for f in os.listdir(music_folder)
    if f.endswith(".mp3")
]

player = MusicPlayer(songs)

background = pygame.image.load("practice9/music_player/music_commands_image/tame_impala_.png")
background = pygame.transform.scale(background, (width, height))

back_command_img = pygame.image.load("/Users/admin/25B032016student/practice9/music_player/music_commands_image/back.png")
next_command_img = pygame.image.load("/Users/admin/25B032016student/practice9/music_player/music_commands_image/next.png")
pause_command_img = pygame.image.load("/Users/admin/25B032016student/practice9/music_player/music_commands_image/pause.png")
play_command_img = pygame.image.load("/Users/admin/25B032016student/practice9/music_player/music_commands_image/play.png")

back_command_img = pygame.transform.scale(back_command_img, (120, 120))
next_command_img = pygame.transform.scale(next_command_img, (120, 120))
pause_command_img = pygame.transform.scale(pause_command_img, (120, 120))
play_command_img = pygame.transform.scale(play_command_img, (120, 120))

font = pygame.font.Font(None, 32)
small_font = pygame.font.Font(None, 24)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_p:
                if player.is_playing and not player.is_paused:
                    player.pause()
                else:
                    player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next_track()

            elif event.key == pygame.K_b:
                player.previous_track()

            elif event.key == pygame.K_q:
                running = False

    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    screen.blit(back_command_img, (40, 380))
    screen.blit(next_command_img, (440, 380))

    if player.is_playing and not player.is_paused:
        screen.blit(pause_command_img, (240, 380))
    else:
        screen.blit(play_command_img, (240, 380))

    track_text = font.render(f"Track: {player.get_current_track_name()}", True, (255, 255, 255))
    status_text = font.render(f"Status: {player.get_status()}", True, (255, 255, 255))
    position_text = small_font.render(
        f"Position: {player.get_position_seconds()} sec",
        True,
        (255, 255, 255)
    )

    controls_text = small_font.render(
        "P = Play/Pause   S = Stop   N = Next   B = Back   Q = Quit",
        True,
        (255, 255, 255)
    )

    screen.blit(track_text, (20, 20))
    screen.blit(status_text, (20, 60))
    screen.blit(position_text, (20, 95))
    screen.blit(controls_text, (20, 560))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()