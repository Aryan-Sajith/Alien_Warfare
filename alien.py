import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class that represents an Alien from the fleet."""

    def __init__(self, game_instance):
        """Initialize an alien from the fleet and set its starting position."""
        super().__init__()
        self.screen = game_instance.screen

        # Setup alien image and rectangle container
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Position alien rectangle at top-left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's horizontal position
        self.x = float(self.rect.x)
