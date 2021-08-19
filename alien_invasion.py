import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        """初始化"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        #背景色
        self.bg_color= (230, 230 ,230)
        #子弹
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        while True:
            self._check_events()
            self.ship.updata()
            self.bullets.update()
            self._updata_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key ==pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key ==pygame.K_UP:
                    self.ship.moving_down = True
                elif event.key ==pygame.K_DOWN:
                    self.ship.moving_up = True
                elif event.key == pygame.K_p:
                    sys.exit()
                elif event.key == pygame.K_a:
                    self._fire_bullet()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_UP:
                    self.ship.moving_down = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_up = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def _updata_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()





if  __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()
