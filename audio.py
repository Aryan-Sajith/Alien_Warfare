import pygame


class Audio:
    """A class to manage audio files for Space Brawl"""

    def __init__(self):
        """Initialize the audio used throughout the game."""
        self.spaceship_laser = pygame.mixer.Sound("sounds/spaceship_laser.mp3")

    def play_spaceship_laser_sound(self):
        """Plays the spaceship laser sound."""
        self.spaceship_laser.play(1000)
        self.spaceship_laser.fadeout(1000)
