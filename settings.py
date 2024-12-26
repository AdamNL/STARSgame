class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (20, 10, 20)

        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 230, 230)
        self.bullet_allowed = 20

        self.ship_speed = 3
        self.ship_limit = 3

        self.alien_speed = 1.0
        self.fleet_drop_speed = 2
        self.fleet_direction = 1