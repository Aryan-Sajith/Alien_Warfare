import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class that represents an Alien from the fleet."""

    def __init__(self, game_instance):
        """Initialize an alien from the fleet and set its starting position."""
        super().__init__()
        self.screen = game_instance.screen
        self.screen_rectangle = self.screen.get_rect()
        self.settings = game_instance.settings

        # Setup alien image and rectangle container
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Position alien rectangle at top-left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's horizontal position
        self.x = float(self.rect.x)

    def _check_edges(self):
        """Returns true if alien has hit either edge of the screen."""
        if self.rect.right >= self.screen_rectangle.right or self.rect.left <= 0:
            return True

    def update(self):
        """Moves the alien left and right."""
        self.x += self.settings.fleet_direction * self.settings.alien_speed
        self.rect.x = self.x
