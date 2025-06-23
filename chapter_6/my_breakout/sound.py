# sound.py
import pygame

class SoundManager:
    def __init__(self, bounce_file, brick_file, game_over_file=None):
        """
        bounce_file:     path to .wav played on paddle or wall bounces
        brick_file:      path to .wav played when a brick is hit
        game_over_file:  optional .wav for game-over
        """
        # 1) Initialize the mixer (once per game)
        pygame.mixer.init()

        # 2) Load sound effects into memory
        self.snd_bounce    = pygame.mixer.Sound(bounce_file)
        self.snd_brick     = pygame.mixer.Sound(brick_file)
        self.snd_game_over = pygame.mixer.Sound(game_over_file) if game_over_file else None

    def play_bounce(self):
        """Play the bounce sound without delay."""
        self.snd_bounce.play()

    def play_brick(self):
        """Play the brick-hit sound without delay."""
        self.snd_brick.play()

    def play_game_over(self):
        """Play game-over jingle if provided."""
        if self.snd_game_over:
            self.snd_game_over.play()
