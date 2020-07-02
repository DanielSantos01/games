import pygame
from game_functions import  rotate_image
from pygame.sprite import Sprite

class Ship(Sprite):
    """Tentativa de modelar o comportamento de uma espaçonave"""
    def __init__(self, screen, game_settings):                    #método construtor, recebe a tela na qual serão feitas alterações
        """Inicializa a espaçonave e define a sua posição inicial"""
        super().__init__()                                        #dá inicio aos atributos da classe pai
        self.screen = screen                                      #faz com que a tela faça parte da classe
        self.game_settings = game_settings                        #recebe o atrinuto responsável pelas configurações do jogo

                                    #carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('imagens/white_theme/ship.png')        #carrega a imagem na tela
        self.image =  pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()                         #pega o espaço ocupado pela imagem
        self.screen_rect = screen.get_rect()                      #pega a dimensão da tela

                                 #inicia cada nova espaçonave na parte inferior da tela
        self.rect.centerx = self.screen_rect.centerx              #define a posição x da imagem no centro da tela
        self.rect.bottom = self.screen_rect.bottom                #alinha a parte de baixo da imagem com a parte de baixo da tela
        self.bottom = self.rect.bottom
        #self.rect.top = self.rect.bottom - self.image.get_height()

        self.center = float(self.rect.centerx)                    #armazena um valor decimal para o centro da espaçonave

                                               #flags de movimento
        self.moving_right = False                                 #inicia o jogo com a nave sem se movimentar para a direita
        self.moving_left = False                                  #inicia o jogo com a nave sem se movimentar para a esquerda
        self.moving_up = False
        self.moving_down = False
        self.rotate = 1

    #-------------------------------------------------------------------------------------------------------------------
    def update(self):
        """atualiza a posição da espaçonave de acordo com a flag de movimento"""
        #o uso de dois if's faz com que a posição seja incrementada e decrementada se as teclas forem pressionadas juntas (nave parada)
        if self.moving_right and \
        self.rect.right < self.screen_rect.right:                #caso a tecla esteja pressionada e a imagem estiver distante da borda
            self.center += self.game_settings.ship_speed_factor  #atualiza a posição da nave (direita)

        if self.moving_left and self.rect.left > 0:              #caso a seta esteja sendo pressionada e a imagem estiver
            self.center -= self.game_settings.ship_speed_factor  #atualiza a posição da nave (esquerda)

        if self.moving_up and self.rect.top >= 0:
            self.bottom -= self.game_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.bottom += self.game_settings.ship_speed_factor

        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    #-------------------------------------------------------------------------------------------------------------------
    def blitme(self):
        """desenha a espaçonave na sua posição atual"""
        self.screen.blit(self.image, self.rect)                  #desenha na tela o objeto (imagem) na posição definida pelo rect (x e y)

    #-------------------------------------------------------------------------------------------------------------------
    def center_ship(self):
        """centraliza a espaçonave quando é atingida"""
        #self.center = self.screen_rect.centerx
        #self.bottom = self.screen_rect.bottom
        if self.game_settings.flag_direction == -1:
            #rotate_image(self)
            #self.game_settings.flag_direction = 1
            self.align_ship_top()
        else:
            self.align_ship_bottom()

    def align_ship_top(self):
        self.center = self.screen_rect.centerx
        self.bottom = self.rect.height
        self.blitme()

    def align_ship_bottom(self):
        self.center = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom
        self.blitme()
