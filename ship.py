import pygame

class Ship:

    def __init__(self, ai_game):
        self.wuqi=0
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/paotai1.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def updata(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.x+=3
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.rect.x-=3
        if self.moving_up and self.rect.bottom<self.screen_rect.bottom:
            self.rect.y+=3
        if self.moving_down and self.rect.top>self.screen_rect.top:
            self.rect.y-=3
        if self.wuqi == 0:
            self.image = pygame.image.load('images/paotai1.png')
        elif self.wuqi == 1:
            self.image = pygame.image.load('images/paotai2.png')
    def blitme(self):
        self.screen.blit(self.image, self.rect)