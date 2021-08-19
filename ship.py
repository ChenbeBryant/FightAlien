import pygame

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def updata(self):
        if self.moving_right and self.rect.x<1100:
            self.rect.x+=3
        if self.moving_left and self.rect.x>0:
            self.rect.x-=3
        if self.moving_up and self.rect.y<570:
            self.rect.y+=3
        if self.moving_down and self.rect.y>10:
            self.rect.y-=3
    def blitme(self):
        self.screen.blit(self.image, self.rect)