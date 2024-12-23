import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, stars_game):
        super().__init__()
        self.screen = stars_game.screen
        self.settings = stars_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = stars_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)