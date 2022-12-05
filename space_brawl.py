import sys
import pygame

from settings import Settings


class SpaceBrawl:
    """Main class to manage Space Brawl's functionality."""

    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.settings = Settings()

        # Setup main surface.
        self.screen = pygame.display.set_mode((self.settings.main_length, self.settings.main_width))
        pygame.display.set_caption("Space Brawl")

    def run_game(self):
        """The main game loop."""
        while True:
            # Exit condition.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Paints main surface.
            self.screen.fill(self.settings.background_color)

            # Updates main surface.
            pygame.display.flip()


if __name__ == '__main__':
    # Runs the game.
    game = SpaceBrawl()
    game.run_game()
