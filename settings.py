class Settings:
    """Auxiliary class for all settings of Space Brawl"""

    def __init__(self):
        """Setup game settings"""
        # Main Surface
        self.main_width = 1200
        self.main_height = 800
        self.background_color = (0, 0, 128)

        # Ship
        self.ship_limit = 3

        # Bullet
        self.bullet_width = 2000
        self.bullet_height = 20
        self.bullet_color = (255, 0, 0)
        self.bullets_limit = 3

        # Alien
        self.fleet_drop_speed = 100

        # Rate of change
        self.speedup_scale = 1.1
        # Dynamic settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.spaceship_speed = 4
        self.bullet_speed = 7
        self.alien_speed = 1
        self.fleet_direction = 1  # 1 -> Right, -1 -> Left

    def increase_speed(self):
        """Increase dynamic settings."""
        self.spaceship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
