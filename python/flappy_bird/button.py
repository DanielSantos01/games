import pygame
class Button():

    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        self.width, self.height = 200, 50
        self.button_image = pygame.image.load('images/message.png')
        self.rect = self.button_image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery - 48

    def draw_button(self):
        self.screen.blit(self.button_image, self.rect)