import os
import pygame


class MusicPlayer:
    def __init__(self, songs):
        if not songs:
            raise FileNotFoundError("No mp3 files found in music folder")

        self.songs = songs
        self.current_index = 0
        self.is_playing = False
        self.is_paused = False

    def load_current_song(self):
        pygame.mixer.music.load(self.songs[self.current_index])

    def play(self):
        if not self.is_playing:
            self.load_current_song()
            pygame.mixer.music.play()
            self.is_playing = True
            self.is_paused = False
        elif self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False

    def pause(self):
        if self.is_playing and not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True

    def next_track(self):
        self.current_index = (self.current_index + 1) % len(self.songs)
        self.load_current_song()
        pygame.mixer.music.play()
        self.is_playing = True
        self.is_paused = False

    def previous_track(self):
        self.current_index = (self.current_index - 1) % len(self.songs)
        self.load_current_song()
        pygame.mixer.music.play()
        self.is_playing = True
        self.is_paused = False

    def get_current_track_name(self):
        return os.path.basename(self.songs[self.current_index])

    def get_status(self):
        if self.is_playing:
            if self.is_paused:
                return "Paused"
            return "Playing"
        return "Stopped"

    def get_position_seconds(self):
        pos = pygame.mixer.music.get_pos()
        if pos < 0:
            return 0
        return pos // 1000