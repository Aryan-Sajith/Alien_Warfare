import sys
import pygame

from settings import Settings
from spaceship import SpaceShip


class SpaceBrawl:
    """Main class to manage Space Brawl's functionality."""

    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.settings = Settings()

        # Setup main surface.
        self.screen = pygame.display.set_mode((self.settings.main_length, self.settings.main_width))
        pygame.display.set_caption("Space Brawl")

        # Setup spaceship.
        self.ship = SpaceShip(self)

    def run_game(self):
        """The main game loop."""
        while True:
            # Exit condition.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Update main screen
            self.screen.fill(self.settings.background_color)
            self.ship.blitme()

            # Display updated screen
            pygame.display.flip()


if __name__ == '__main__':
    # Runs the game.
    game = SpaceBrawl()
    game.run_game()
