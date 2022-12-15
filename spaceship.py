import pygame
from pygame.sprite import Sprite


class SpaceShip(Sprite):
    """A class to handle the spaceship."""

    def __init__(self, game_instance):
        """Initialize spaceship."""
        super().__init__()

        # Setup settings and main screen
        self.screen = game_instance.screen
        self.settings = game_instance.settings
        self.rect = game_instance.screen.get_rect()  # Treats screen as rectangle.

        # Spaceship setup.
        self.image = pygame.image.load("images/rocket.bmp")
        self.spaceship_rectangle = self.image.get_rect()  # Treats spaceship as rectangle.

        # Spaceship positioned on screen.
        self.spaceship_rectangle.midbottom = self.rect.midbottom

        # Float value for ship's horizontal position
        self.x = float(self.spaceship_rectangle.x)

        # Continuous movement flags
        self.moving_left = False
        self.moving_right = False

    def blitme(self):
        """Draws image to screen at specified position."""
        self.screen.blit(self.image, self.spaceship_rectangle)

    def move_continuously(self):
        """Updates spaceship position based on movement flag and stays within the main screen"""
        # Updates decimal position x
        if self.moving_right and self.spaceship_rectangle.right < self.rect.right:
            self.x += self.settings.spaceship_speed
        if self.moving_left and self.spaceship_rectangle.left > self.rect.left:
            self.x -= self.settings.spaceship_speed

        # Updates actual position relative to decimal position x
        self.spaceship_rectangle.x = self.x
