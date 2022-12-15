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
        self.screen_rectangle = game_instance.screen.get_rect()  # Treats screen as rectangle.

        # Spaceship setup.
        self.image = pygame.image.load("images/rocket.bmp")
        self.rect = self.image.get_rect()  # Treats spaceship as rectangle.

        # Spaceship positioned on screen.
        self.rect.midbottom = self.screen_rectangle.midbottom

        # Float value for ship's horizontal position
        self.x = float(self.rect.x)

        # Continuous movement flags
        self.moving_left = False
        self.moving_right = False

    def blitme(self):
        """Draws image to screen at specified position."""
        self.screen.blit(self.image, self.rect)

    def move_continuously(self):
        """Updates spaceship position based on movement flag and stays within the main screen"""
        # Updates decimal position x
        if self.moving_right and self.rect.right < self.screen_rectangle.right:
            self.x += self.settings.spaceship_speed
        if self.moving_left and self.rect.left > self.screen_rectangle.left:
            self.x -= self.settings.spaceship_speed

        # Updates actual position relative to decimal position x
        self.rect.x = self.x
