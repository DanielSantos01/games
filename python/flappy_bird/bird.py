import pygame
from pygame.sprite import Sprite

class Bird(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        #config
        self.settings = settings
        self.sound_hit = pygame.mixer.Sound('sounds/hit.ogg')
        self.sound_wing = pygame.mixer.Sound('sounds/wing.ogg')
        self.sound_point = pygame.mixer.Sound('sounds/point.ogg')
        self.sound_fall = pygame.mixer.Sound('sounds/die.ogg')
        #tela
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        #objeto
        self.images = [pygame.image.load('images/bluebird-upflap.png').convert_alpha(),
                       pygame.image.load('images/bluebird-midflap.png').convert_alpha(),
                       pygame.image.load('images/bluebird-downflap.png').convert_alpha()]
        self.up_image =  self.images[2]
        self.angle = 0
        self.image = self.images[1]
        self.rect = self.images[0].get_rect()
        self.number_image = 0
        #posição
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    #-------------------------------------------------------------------------------------------------------------------
    def blitme(self):
        if self.settings.flag_run_game:
            if self.angle > -91:
                self.up_image = pygame.transform.rotate(self.image, self.angle)
                self.angle -= 5
        self.screen.blit(self.up_image, self.rect)

    #-------------------------------------------------------------------------------------------------------------------
    def update(self):
        #change image
        self.number_image += 1
        if self.number_image > 2:
            self.number_image = 0
        self.image = self.images[self.number_image]
        #change position
        self.settings.fall += self.settings.gravity
        if self.rect.top >= self.screen_rect.top:
            self.rect.y += self.settings.fall
        else:
            self.rect.y += 2

    #-------------------------------------------------------------------------------------------------------------------
    def pause(self):
        self.number_image += 1
        if self.number_image > 2:
            self.number_image = 0
        self.image = self.images[self.number_image]
        self.center_bird()
        self.screen.blit(self.image, self.rect)

    #-------------------------------------------------------------------------------------------------------------------
    def up(self):
        self.settings.fall = -self.settings.const_up
        self.angle = 60

    #-------------------------------------------------------------------------------------------------------------------
    def center_bird(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    #-------------------------------------------------------------------------------------------------------------------
    def hit(self):
        self.sound_hit.play()

    #-------------------------------------------------------------------------------------------------------------------
    def wing(self):
        self.sound_wing.play()

    #-------------------------------------------------------------------------------------------------------------------
    def point(self):
        self.sound_point.play()

    #-------------------------------------------------------------------------------------------------------------------
    def fall(self):
        self.sound_fall.play()