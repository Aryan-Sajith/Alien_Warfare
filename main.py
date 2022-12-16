import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from spaceship import SpaceShip
from bullet import Bullet
from alien import Alien


class SpaceBrawl:
    """Main class to manage Space Brawl's functionality."""

    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.settings = Settings()

        # Setup main surface as full screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.main_width = self.screen.get_rect().width
        self.settings.main_height = self.screen.get_rect().height
        pygame.display.set_caption("Space Brawl")

        # Setup main statistics.
        self.stats = GameStats(self)

        # Setup spaceship.
        self.ship = SpaceShip(self)

        # Setup bullets & aliens as a Sprite group
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Create the fleet of aliens!
        self._create_fleet()

        # Setup button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """The main game loop."""
        while True:
            self._manage_events()

            if self.stats.game_active:
                self.ship.move_continuously()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _create_fleet(self):
        """Helper method within initializer to creates the fleet of aliens."""
        # Determine the number of aliens placed horizontally
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.main_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens
        ship_height = self.ship.rect.height
        available_space_y = self.settings.main_height - (10 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Helper of  _create_fleet() to create an alien and add it to the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width * (1 + 2 * alien_number)
        alien.rect.x = alien.x
        alien.y = alien_height * (1 + 2 * row_number)
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _fire_bullet(self):
        """Create a new bullet and add it to bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Updates the bullets."""
        self.bullets.update()

        # Remove bullets at bottom of screen.
        for bullet in self.bullets.copy():
            bullet: Bullet
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._manage_bullet_alien_collisions()

    def _manage_bullet_alien_collisions(self):
        """Manages bullet and alien collisions."""
        # If bullet collided with alien, remove both.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # If all aliens are killed, empty bullets and create a new fleet.
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

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
        elif event.key == pygame.K_q:  # Another exit condition
            sys.exit()
        elif event.key == pygame.K_SPACE:
            if len(self.bullets) < self.settings.bullets_limit:
                self._fire_bullet()

    def _manage_keyup_events(self, event):
        """Helper method of _manage_events() that responds to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_fleet_edges(self):
        """Change fleet motion if any alien reaches a screen edge."""
        for alien in self.aliens.sprites():
            alien: Alien
            if alien._check_edges():
                self._change_fleet_motion()
                break

    def _change_fleet_motion(self):
        """Drop the entire fleet and change fleet direction."""
        for alien in self.aliens.sprites():
            alien: Alien
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """Update the aliens on screen."""
        self._check_fleet_edges()
        self.aliens.update()

        # If alien collides with the ship, destroy the ship.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.manage_ship_hit()

        # Handle aliens reaching bottom of screen.
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """If any alien reaches the bottom, respond as if ship got hit."""
        screen_rectangle = self.screen.get_rect()
        for alien in self.aliens:
            if alien.rect.bottom >= screen_rectangle.bottom:
                self.manage_ship_hit()

    def manage_ship_hit(self):
        """Handles a ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ship count
            self.stats.ships_left -= 1

            # Delete all aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Game pause, for user to recuperate.
            sleep(0.5)
        else:
            self.stats.game_active = False
            sys.exit("Game Over!")

    def _update_screen(self):
        """Helper method of run_game to update main surface and flip screen."""
        # Update main screen
        self.screen.fill(self.settings.background_color)

        # Draws rocket ship
        self.ship.blitme()

        # Draws bullets
        for bullet in self.bullets.sprites():
            bullet: Bullet
            bullet.draw_bullet()

        # Draws aliens
        self.aliens.draw(self.screen)

        # Display button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Display updated screen
        pygame.display.flip()


if __name__ == '__main__':
    # Runs the game.
    game = SpaceBrawl()
    game.run_game()
