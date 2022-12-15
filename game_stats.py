class GameStats:
    """Tracks in-game data for Space Brawl."""

    def __init__(self, game_instance):
        """Initialize statistics."""
        self.setting = game_instance.settings
        self.ships_left = self.setting.ship_limit
