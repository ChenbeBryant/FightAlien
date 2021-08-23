import sys
import pygame
from random import randint
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
import time

class AlienInvasion:
    def __init__(self):
        """初始化"""
        pygame.init()
        #设置
        self.settings = Settings()
        self.jineng=0;
        #外星人个数
        self.i=0
        #武器
        self.wuqi=0
        #屏幕设置
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        #背景色
        self.bg_color= self.settings.bg_color

        #子弹
        self.bullets = pygame.sprite.Group()
        #飞船
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")
        #外星人
        self.aliens = pygame.sprite.Group()

#一批外星人
    def _create_fleet(self):
        alien=Alien(self)
        alien_height = alien.rect.y
        while(self.i<10):
            b=randint(0,300)
            if b==0:
                self.i+=1
                k=randint(0,self.settings.screen_width)
                alien = Alien(self)
                alien.x = k
                alien.y = alien_height
                alien.rect.x = alien.x
                alien.rect.y = alien.y
                self.aliens.add(alien)



#开始游戏
    def run_game(self):
        while True:
            self._check_events()
            self._updata_screen()
#按键设置
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key ==pygame.K_LEFT:
                    self.ship.moving_left = True
                if event.key ==pygame.K_UP:
                    self.ship.moving_down = True
                if event.key ==pygame.K_DOWN:
                    self.ship.moving_up = True
                if event.key == pygame.K_p:
                    sys.exit()
                if event.key == pygame.K_a:
                    self._fire_bullet()
                if event.key == pygame.K_q:
                    self.settings.change_bullet_height(5)
                if event.key == pygame.K_w:
                    self.ship.wuqi+=1
                    self.ship.wuqi%=2
                if event.key == pygame.K_e:
                    for bullet in self.bullets.sprites():
                        bullet.wuqi+=1
                        bullet.wuqi%=2
                if event.key == pygame.K_r:
                    self.juesha()
                if event.key == pygame.K_k:
                    self.waigua()



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                if event.key == pygame.K_UP:
                    self.ship.moving_down = False
                if event.key == pygame.K_DOWN:
                    self.ship.moving_up = False
                if event.key == pygame.K_q:
                    self.settings.change_bullet_height(1/5)



#更新画面
    def _updata_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.ship.updata()
        self.bullets.update()
        self._updata_aliens()
        self._create_fleet()
        self.won_or_lose()
        pygame.display.flip()
#开火
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        new_bullet.a = 1
        self.bullets.add(new_bullet)
        self.jineng = 0
#大招
    def juesha(self):
        new_bullet = Bullet(self)
        new_bullet.a=0
        self.bullets.add(new_bullet)
        self.jineng = 1
#外挂
    def waigua(self):
        for alien in self.aliens.sprites():
            self.aliens.remove(alien)
#外星人移动与阵亡
    def _updata_aliens(self):
        for alien in self.aliens.sprites():
            alien.updata()
        for bul in self.bullets.sprites():
            if bul.rect.top<0:
                self.bullets.remove(bul)
            for alien in self.aliens.sprites():
                a0 = bul.rect.right < alien.rect.right
                b0 = bul.rect.left > alien.rect.left
                c0 = bul.rect.bottom > alien.rect.top
                d0 = bul.rect.top < alien.rect.bottom

                a1=bul.rect1.right<alien.rect.right
                b1=bul.rect1.left>alien.rect.left
                a2 = bul.rect1.right > alien.rect.left
                b2 = bul.rect1.left < alien.rect.right
                a3 = bul.rect1.right > alien.rect.right
                b3 =  bul.rect1.left<alien.rect.left
                c1=bul.rect1.bottom>alien.rect.top
                d1=bul.rect1.top<alien.rect.bottom
                if self.jineng == 0:
                    if a0 and b0 and c0 and d0 :
                        self.aliens.remove(alien)
                        self.bullets.remove(bul)
                    else:
                        continue
                elif self.jineng == 1:
                    if(a1 and b1 and c1 and d1) or (a1 and a2 and c1 and d1)  or (b1 and b2 and c1 and d1) or (a3 and b3 and c1 and d1):
                         self.aliens.remove(alien)
#胜负判定
    def won_or_lose(self):
        a=0
        for alien in self.aliens:
            if alien.rect.bottom>self.settings.screen_height:
                a=1
            else:
                continue
        if a == 1:
            print("You lose!")
            time.sleep(3)
            sys.exit()
        elif len(self.aliens) == 0:
            print("You win!")
            time.sleep(3)
            sys.exit()









if  __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()
