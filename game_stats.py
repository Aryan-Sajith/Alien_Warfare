class GameStats:
    """Tracks in-game data for Alien Warfare."""

    def __init__(self, game_instance):
        """Initialize statistics."""
        self.high_score = game_instance.highscore_io.input_high_score()

        # Setup fully dynamic stats
        self.reset_stats(game_instance)

    def reset_stats(self, game_instance):
        """Reset dynamic game statistics"""
        self.setting = game_instance.settings
        self.ships_left = self.setting.ship_limit
        self.score = 0
        self.level = 1

        # Flags
        self.game_active = False
        self.play_button_clicked = False
        self.difficulty_button_clicked = False
