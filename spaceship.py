import pygame


class SpaceShip:
    """A class to handle the spaceship."""

    def __init__(self, game_instance):
        """Initialize spaceship."""
        # Main surface retrieval.
        self.screen = game_instance.screen
        self.screen_rectangle = game_instance.screen.get_rect()  # Treats screen as rectangle.

        # Spaceship setup.
        self.image = pygame.image.load("images/rocket.bmp")
        self.spaceship_rectangle = self.image.get_rect()  # Treats spaceship as rectangle.

        # Spaceship positioned on screen.
        self.spaceship_rectangle.midbottom = self.screen_rectangle.midbottom

        # Continuous movement flags
        self.moving_left = False
        self.moving_right = False

    def blitme(self):
        """Draws image to screen at specified position."""
        self.screen.blit(self.image, self.spaceship_rectangle)

    def move_continuously(self):
        """Updates spaceship position based on movement flag"""
        if self.moving_right:
            self.spaceship_rectangle.x += 1
        if self.moving_left:
            self.spaceship_rectangle.x -= 1
