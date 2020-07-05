import pygame.sysfont

class Button():
    """tentativa de modelar um botão"""

    def __init__(self, screen, message):
        """inicializa os atributos do botão"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #definindo as dimensões e as propriedades do botão
        self.width, self.heigth = 200, 50  #dimensões do botão
        self.button_color = (255, 0, 0)    #define a cor do botão
        self.text_color = (255, 255, 255)  #define a cor do texto
        self.font = pygame.font.SysFont(None, 24) #define a fonte padrão (None) e com tamanho 48

        #constrói o objeto rect do botão e o centraliza
        self.rect = pygame.Rect(0, 0, self.width, self.heigth) #cria o rect do botão
        self.rect.center = self.screen_rect.center #define o centro do botão como o centro da tela

        #a mensagem do botão deve ser carregada apenas uma vez
        self.prep_msg(message)
        print(message)

    def prep_msg(self, message):
        """tranforma a string em imagem renderizada e a centraliza no botão"""
        #transforma a string em uma imagem renderizada
        self.msg_image = self.font.render(message, True, self.text_color, self.button_color)

        #obtém o rect da imagem criada
        self.msg_image_rect = self.msg_image.get_rect()

        # transforma o centro da msg no centro do botão
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """desenha um botão em branco e em seguida desenha a mensagem"""
        self.screen.fill(self.button_color, self.rect)#desenha o retângulo do botão
        self.screen.blit(self.msg_image, self.msg_image_rect)#desenha a imagem do texto no botão

