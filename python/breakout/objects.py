import pygame
from pygame.sprite import Sprite

class Objects(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/obj.png')
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)