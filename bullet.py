import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_game):
        super().__init__()
        self.wuqi=0
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/zidan.png')
        self.a=-1
        self.rect1 = self.image.get_rect()
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,self.settings.bullet_height)
        self.rect1.midbottom = ai_game.ship.rect.midtop
        self.rect.midbottom = ai_game.ship.rect.midtop
        self.y1 = float(self.rect1.y)
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        self.y1 -= self.settings.bullet_speed
        self.rect1.y = self.y1
        if self.wuqi == 0:
            self.image = pygame.image.load('images/zidan.png')
        elif self.wuqi == 1:
            self.image = pygame.image.load('images/zidan2.png')

    def draw_bullet(self):
        if self.a==1:
            pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)
        elif self.a == 0:
            self.screen.blit(self.image, self.rect1)


