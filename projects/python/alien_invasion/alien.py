import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """classe que representa um único alienígena do jogo"""
    def __init__(self, game_settings, screen):
        """inicia o alienígena e define a sua posição inicial"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        self.shot_down_sound = pygame.mixer.Sound('sounds/shot.ogg')

        self.image = pygame.image.load('imagens/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    #-------------------------------------------------------------------------------------------------------------------
    def blitme(self):
        """desenha o alienígena em sua posição atual"""
        self.screen.blit(self.image, self.rect)

    #-------------------------------------------------------------------------------------------------------------------
    def update(self):
        """move o alienígena para a direita"""
        self.x += (self.game_settings.alien_speed_factor*self.game_settings.fleet_direction)
        self.rect.x = self.x

    #-------------------------------------------------------------------------------------------------------------------
    def check_edges(self):
        """devolve true se o alienígena estiver na borda da tela"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def shot_down(self):
        self.shot_down_sound.play()