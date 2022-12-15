class Settings:
    """Auxiliary class for all settings of Space Brawl"""

    def __init__(self):
        """Setup game settings"""
        # Main Surface
        self.main_width = 1200
        self.main_height = 800
        self.background_color = (0, 0, 128)

        # Ship
        self.spaceship_speed = 3
        self.ship_limit = 3

        # Bullet
        self.bullet_speed = 7
        self.bullet_width = 10
        self.bullet_height = 20
        self.bullet_color = (255, 0, 0)
        self.bullets_limit = 3

        # Alien
        self.alien_speed = 2
        self.fleet_drop_speed = 90
        self.fleet_direction = 1  # 1 -> Right, -1 -> Left
