import pygame
from pygame.sprite import Sprite


    def update(self):
        self.y -= self.speed/4
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)