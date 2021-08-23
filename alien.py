import pygame
from pygame.sprite import Sprite
from random import randint
class Alien(Sprite):

    def __init__(self,ai_game):
        self.speed = 1
        super().__init__()
        self.bul = ai_game.bullets
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.direction = randint(0,1)
        self.p=1
        self.jian=-1

    def updata(self):
        self.jiance()
        if self.jian == 1:
            self.move_left()
        elif self.jian == 0:
            self.move_right()
        else:
            a_r = randint(0, 3)
            if a_r == 0:
                self.smoothly_move()
                self.move_bottom()
        self.jian = -1

    def jiance(self):
        for bul in self.bul:
            a0 = bul.rect.right < self.rect.right
            b0 = bul.rect.left > self.rect.left
            c0 = bul.rect.midtop > self.rect.midtop
            if a0 and b0 and c0:
                self.jian = 1
            elif a0 and b0 and(1-c0):
                self.jian = 0
            else:
                continue
    def move_right(self):
        if self.rect.right<self.screen_rect.right:
            self.rect.x+=self.speed
    def move_left(self):
        if self.rect.left > self.screen_rect.left:
            self.rect.x-=self.speed
    def move_bottom(self):
            self.rect.y+=self.speed
    def move_top(self):
        if self.rect.top>self.screen_rect.top:
            self.rect.y-=self.speed

    def smoothly_move(self):
        pp=randint(0,1)
        self.p+=pp
        p0=self.p//100
        if p0%2==self.direction:
            self.move_right()
        else:
            self.move_left()

    def brown_move(self):
        a = randint(0, 1)
        b = randint(0, 100)
        if a ==1 and self.rect.right<self.screen_rect.right:
            self.move_right()
        elif a==0 and self.rect.left>self.screen_rect.left:
            self.move_left()
        if b ==0 :
            self.move_top()
        elif b==1 and self.rect.x<self.screen_rect.top:
            self.move_bottom()


