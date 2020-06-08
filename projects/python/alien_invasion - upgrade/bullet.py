import pygame
from pygame.sprite import Sprite #usada para agrupar elementos e atuar sobre todos de uma só vez

class Bullet(Sprite):
    """classe que administra os projetos lançados pela espaçonave"""

    def __init__(self, game_settings, screen, ship):
        super().__init__()                                                                #inicia a classe filha dando inicio a classe pai
        self.screen = screen                                                              #recebe o objeto que representa a tela

        #cria um retangulo para o projétil em 0,0 e em seguida define a posição correta
        self.rect = pygame.Rect(0 , 0, game_settings.bullet_width, game_settings.bullet_height) #Rect (r maiusculo) desenha um retângulo
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.game_settings = game_settings

        self.y = float(self.rect.y)                                                       #armazena a posição do projétil como decimal
        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    #-------------------------------------------------------------------------------------------------------------------
    def update(self):
        """move o projetil para cima na tela"""
        if self.game_settings.flag_direction == 1:
            self.y -= self.speed_factor                                                   #atualiza a posição do projétil
        else:
            self.y += self.speed_factor

        self.rect.y = self.y                                                              #atualiza a posição do rect

    #-------------------------------------------------------------------------------------------------------------------
    def draw_bullet(self):
        """desenha o projétil na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)