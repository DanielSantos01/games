import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Tentativa de modelar o comportamento de uma espaçonave"""
    def __init__(self, screen, game_settings):                    #método construtor, recebe a tela na qual serão feitas alterações
        super().__init__()
        """Inicializa a espaçonave e define a sua posição inicial"""
        self.screen = screen                                      #faz com que a tela faça parte da classe
        self.game_settings = game_settings                        #recebe o atrinuto responsável pelas configurações do jogo
        self.shot_sound = pygame.mixer.Sound('sounds/swoosh.ogg')

                                    #carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('imagens/ship.bmp')        #carrega a imagem na tela
        self.rect = self.image.get_rect()                         #pega o espaço ocupado pela imagem
        self.screen_rect = screen.get_rect()                      #pega a dimensão da tela

                                 #inicia cada nova espaçonave na parte inferior da tela
        self.rect.centerx = self.screen_rect.centerx              #define a posição x da imagem no centro da tela
        self.rect.bottom = self.screen_rect.bottom                #alinha a parte de baixo da imagem com a parte de baixo da tela

        self.center = float(self.rect.centerx)                    #armazena um valor decimal para o centro da espaçonave

                                               #flags de movimento
        self.moving_right = False                                 #inicia o jogo com a nave sem se movimentar para a direita
        self.moving_left = False                                  #inicia o jogo com a nave sem se movimentar para a esquerda

    #-------------------------------------------------------------------------------------------------------------------
    def update(self):
        """atualiza a posição da espaçonave de acordo com a flag de movimento"""
        #o uso de dois if's faz com que a posição seja incrementada e decrementada se as teclas forem pressionadas juntas (nave parada)
        if self.moving_right and \
        self.rect.right < self.screen_rect.right:                #caso a tecla esteja pressionada e a imagem estiver distante da borda
            self.center += self.game_settings.ship_speed_factor  #atualiza a posição da nave (direita)

        if self.moving_left and self.rect.left > 0:              #caso a seta esteja sendo pressionada e a imagem estiver
            self.center -= self.game_settings.ship_speed_factor  #atualiza a posição da nave (esquerda)

        self.rect.centerx = self.center

    #-------------------------------------------------------------------------------------------------------------------
    def blitme(self):
        """desenha a espaçonave na sua posição atual"""
        self.screen.blit(self.image, self.rect)                  #desenha na tela o objeto (imagem) na posição definida pelo rect (x e y)

    #-------------------------------------------------------------------------------------------------------------------
    def center_ship(self):
        """centraliza a espaçonave quando é atingida"""
        self.center = self.screen_rect.centerx

    def shot(self):
        self.shot_sound.play()