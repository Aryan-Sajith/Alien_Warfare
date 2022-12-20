import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard
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
        self.stats = GameStats(self)

        # Setup main surface as full screen
        self.screen = pygame.display.set_mode((self.settings.main_width, self.settings.main_height))
        pygame.display.set_caption("Space Brawl")

        # Setup scoreboard
        self.scoreboard = ScoreBoard(self)

        # Setup spaceship
        self.ship = SpaceShip(self)

        # Setup bullets & aliens as a Sprite group
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Create the fleet of aliens!
        self._create_fleet()

        # Setup buttons
        self.play_button = Button(self, "Play", self.settings.play_button_color)
        self.easy_button = Button(self, "Easy", self.settings.easy_button_color)
        self.normal_button = Button(self, "Normal", self.settings.normal_button_color)
        self.hard_button = Button(self, "Hard", self.settings.hard_button_color)

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
        available_space_y = self.settings.main_height - (6 * alien_height) - ship_height
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
        alien.y = alien_height * (1 + 2 * row_number) + 35  # Add spacing to prevent overlap with ships left
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _fire_bullet(self):
        """Create a new bullet and add it to bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Updates the bullets."""
        self.bullets.update()

        # Remove bullets at top of screen.
        for bullet in self.bullets.copy():
            bullet: Bullet
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)

        self._manage_bullet_alien_collisions()

    def _manage_bullet_alien_collisions(self):
        """Manages bullet and alien collisions."""
        # If bullet collided with alien, remove both.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            # Score handling
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.scoreboard.prep_score()

        # If all aliens are killed, empty bullets and create a new fleet.
        if not self.aliens:
            # Reset fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increment the level
            self.stats.level += 1
            self.scoreboard.prep_level()

    def _manage_events(self):
        """Helper method of run_game() to manage user events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit condition.
                sys.exit()
            # Key events
            elif event.type == pygame.KEYDOWN:
                self._manage_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._manage_keyup_events(event)
            # Mouse events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._manage_mousedown_events(mouse_position)

    def _manage_mousedown_events(self, mouse_position):
        """Manages user mousedown events."""
        # Play button
        playing_button_clicked = self.play_button.rect.collidepoint(mouse_position)
        # Pressed play button
        if playing_button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.play_button_clicked = True
        # Sets difficulty, resets level, then starts the game
        elif self.stats.play_button_clicked and not self.stats.game_active:
            self._setting_difficulty(mouse_position)
            self.scoreboard.prep_level()
            self._start_game()

    def _setting_difficulty(self, mouse_position):
        """Set the difficulty and relevant flags."""
        # Easy
        if self.easy_button.rect.collidepoint(mouse_position):
            self.settings._set_difficulty(self.easy_button.button_color)
            self._set_difficulty_flags()
        # Normal
        elif self.normal_button.rect.collidepoint(mouse_position):
            self.settings._set_difficulty(self.normal_button.button_color)
            self._set_difficulty_flags()
        # Hard
        elif self.hard_button.rect.collidepoint(mouse_position):
            self.settings._set_difficulty(self.hard_button.button_color)
            self._set_difficulty_flags()

    def _set_difficulty_flags(self):
        """Sets relevant difficulty flags when a difficulty button is clicked."""
        self.stats.difficulty_button_clicked = True
        pygame.mouse.set_visible(False)

    def _manage_keydown_events(self, event):
        """Helper method of _manage_events() that responds to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:  # Another exit condition
            sys.exit()
        elif event.key == pygame.K_SPACE and self.stats.game_active:
            if len(self.bullets) < self.settings.bullets_limit:
                self._fire_bullet()
        elif event.key == pygame.K_p and not self.stats.game_active:
            self.stats.play_button_clicked = True

    def _start_game(self):
        """Starts the game."""
        # Turn game activity flag on
        self.stats.game_active = True

        # Reset game data
        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

    def _manage_keyup_events(self, event):
        """Helper method of _manage_events() that responds to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_fleet_edges(self):
        """Change fleet motion if any alien reaches a screen edge."""
        for alien in self.aliens:
            alien: Alien
            if alien._check_edges():
                self._change_fleet_motion()
                break

    def _change_fleet_motion(self):
        """Drop the entire fleet and change fleet direction."""
        for alien in self.aliens:
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
                break

    def manage_ship_hit(self):
        """Handles a ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ship count and update scoreboard image
            self.stats.ships_left -= 1
            self.scoreboard.prep_ships()

            # Delete all aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Game pause, for user to recuperate.
            sleep(0.5)
        else:  # Game reset
            # Update high score
            self.stats.high_score = max(self.stats.high_score, self.stats.score)
            # Reset stats
            self.stats.reset_stats(self)
            # Reset scoreboard
            self.scoreboard.prep_score()
            self.scoreboard.prep_high_score()
            self.scoreboard.prep_ships()

            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Helper method of run_game to update main surface and flip screen."""
        # Update background color
        self.screen.fill(self.settings.background_color)

        # Draws rocket ship
        self.ship.blitme()

        # Draws bullets
        for bullet in self.bullets.sprites():
            bullet: Bullet
            bullet.draw_bullet()

        # Draws aliens
        self.aliens.draw(self.screen)

        # Draw scoreboard
        self.scoreboard.show_scoreboard()
        self.scoreboard.ships.draw(self.screen)

        # Display play button if game inactive, and it wasn't clicked
        if not self.stats.game_active and not self.stats.play_button_clicked:
            self.play_button.draw_button()
        # Display difficulty buttons if game inactive, and play button was clicked.
        elif not self.stats.game_active and not self.stats.difficulty_button_clicked:
            self.easy_button.draw_button()
            self.normal_button.draw_button()
            self.hard_button.draw_button()

        # Display updated screen
        pygame.display.flip()


if __name__ == '__main__':
    # Runs the game.
    game = SpaceBrawl()
    game.run_game()
