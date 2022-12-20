import pygame.font


class ScoreBoard:
    """A class to report game scoreboard information"""

    def __init__(self, game_instance):
        """Initialize the scoreboard"""
        # Main surface and info
        self.screen = game_instance.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game_instance.settings
        self.stats = game_instance.stats

        # Score font settings
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # Prepare score image and position
        self.prep_score()

    def prep_score(self):
        """Turn score into a rendered image positioned on main surface."""
        # Setup score
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.background_color)

        # Position score
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score onto main surface."""
        self.screen.blit(self.score_image, self.score_rect)
