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
        # Prepare scoreboard
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Turn score into a rendered image positioned on main surface."""
        # Setup score
        rounded_score = int(round(self.stats.score, -1))
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.background_color)

        # Position score
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn high score into rendered image on main screen."""
        # Setup high score
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                                 self.settings.background_color)

        # Center the image on top center of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.x = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def show_score(self):
        """Draw score onto main surface."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
