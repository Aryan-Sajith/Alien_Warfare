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
        self.bullet_width = 10
        self.bullet_height = 20
        self.bullet_color = (255, 0, 0)
        self.bullets_limit = 3

        # Buttons
        self.play_button_color = (0, 200, 0)
        self.easy_button_color = (0, 255, 0)
        self.normal_button_color = (255, 165, 0)
        self.hard_button_color = (255, 0, 0)

        # Rate of change
        self.speedup_scale = 1.1
        # Dynamic settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.spaceship_speed = 2
        self.bullet_speed = 2
        self.alien_speed = 0.5
        self.fleet_direction = 1  # 1 -> Right, -1 -> Left
        self.fleet_drop_speed = 10

    def increase_speed(self):
        """Increase dynamic settings."""
        self.spaceship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.fleet_drop_speed += int(self.speedup_scale)
