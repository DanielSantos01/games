from pygame.sprite import Sprite
import pygame

class PipeUp(Sprite):
    def __init__(self, screen, settings, number):
        super().__init__()
        self.screen = screen
        self.settings =settings
        self.number = number
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/pipe-green.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_rect().width, self.settings.up_height[self.number]))
        self.rect = self.image.get_rect()
        self.rect.right = self.screen_rect.right
        self.rect.bottom = self.screen_rect.bottom - settings.ground_height

    def update(self):
        self.rect.x -= 3

    def is_out(self):
        if self.rect.right <= 0:
            return True
        else:
            return False