from pygame.sprite import Sprite
import pygame

class Ground(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        #screen
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        #object dimension
        self.width = 2 * settings.SCREEN_WIDTH
        self.height = settings.ground_height
        self.dimension = (self.width, self.height)
        #object
        self.image = pygame.image.load('images/base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, self.dimension)
        self.rect = self.image.get_rect()
        self.rect.y = self.screen_rect.bottom - self.height
        self.count = 0

    #-------------------------------------------------------------------------------------------------------------------
    def update(self):
        self.rect.x -= 3
        self.count += 3

    #-------------------------------------------------------------------------------------------------------------------
    def check_out(self):
        if self.count >= 400:
            self.count = 0
            return True
        else:
            return False