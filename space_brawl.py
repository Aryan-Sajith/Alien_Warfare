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
            self._manage_events()
            self.ship.move_continuously()
            self._update_screen()

    def _update_screen(self):
        """Helper method of run_game to update main surface and flip screen."""
        # Update main screen
        self.screen.fill(self.settings.background_color)
        self.ship.blitme()

        # Display updated screen
        pygame.display.flip()

    def _manage_events(self):
        """Helper method of run_game() to manage user events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit condition.
                sys.exit()
            # Continuous movement
            elif event.type == pygame.KEYDOWN:
                self._manage_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._manage_keyup_events(event)

    def _manage_keydown_events(self, event):
        """Helper method of _manage_events() that responds to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _manage_keyup_events(self, event):
        """Helper method of _manage_events() that responds to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


if __name__ == '__main__':
    # Runs the game.
    game = SpaceBrawl()
    game.run_game()
