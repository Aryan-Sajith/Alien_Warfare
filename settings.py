class Settings:
    """Auxiliary class for all settings of Space Brawl"""

    def __init__(self):
        """Setup game settings"""
        # Main Surface
        self.main_width = 1200
        self.main_height = 800
        self.background_color = (0, 0, 128)

        # Ship
        self.spaceship_speed = 2

        # Bullet
        self.bullet_speed = 1.5
        self.bullet_width = 4
        self.bullet_height = 16
        self.bullet_color = (255, 0, 0)
        self.bullets_limit = 3
