from pygame.mixer import Sound
from pygame.mixer import music


class Audio:
    """A class to manage audio files for Alien Warfare"""

    def __init__(self):
        """Initialize the audio used throughout the game."""
        # Setup background music
        self.setup_background_music()
        # Play background music
        self.play_background_music()

        # Setup Sounds
        self.spaceship_laser = Sound("sounds/spaceship_laser.mp3")
        self.spaceship_laser.set_volume(0.03)
        self.alien_bullet_collision = Sound("sounds/alien_bullet_collision.mp3")
        self.alien_bullet_collision.set_volume(0.03)

    def play_spaceship_laser_sound(self):
        """Plays the spaceship laser sound."""
        self.spaceship_laser.play(1000)
        self.spaceship_laser.fadeout(1000)

    def play_alien_bullet_collision_sound(self):
        """Plays the collision sound of the alien and bullet."""
        self.alien_bullet_collision.play(1000)
        self.alien_bullet_collision.fadeout(1000)

    def setup_background_music(self):
        """Set up the background music"""
        music.load("sounds/apocalypse_background.mp3")
        music.set_volume(0.04)

    def play_background_music(self):
        """Plays the background music"""
        music.play(-1)
