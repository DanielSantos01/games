import pygame.sysfont

class Score():

    def __init__(self, screen, settings):
        """inicializa os atributos do botão"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        #definindo as dimensões e as propriedades do botão
        self.width, self.heigth = 100, 30  #dimensões do botão
        self.button_color = (0, 0, 0)    #define a cor do botão
        self.text_color = (255, 255, 255)  #define a cor do texto
        self.font = pygame.font.SysFont(None, 24) #define a fonte padrão (None) e com tamanho 48

        #constrói o objeto rect do botão e o centraliza
        self.rect = pygame.Rect(0, 0, self.width, self.heigth) #cria o rect do botão
        #self.rect.center = self.screen_rect.center #define o centro do botão como o centro da tela

        self.prep_chances(3)

    def prep_chances(self, number):
        """tranforma a string em imagem renderizada e a centraliza no botão"""
        #transforma a string em uma imagem renderizada
        message = str(number) + ' chances left'
        self.msg_image = self.font.render(message, True, self.text_color, self.button_color)

        #obtém o rect da imagem criada
        self.msg_image_rect = self.msg_image.get_rect()

        #transforma o centro da msg no centro do botão
        self.msg_image_rect.x = 0
        self.msg_image_rect.y = 0

    def draw(self):
        """desenha um botão em branco e em seguida desenha a mensagem"""
        self.screen.fill(self.button_color, self.rect)#desenha o retângulo do botão
        self.screen.blit(self.msg_image, self.msg_image_rect)#desenha a imagem do texto no botão

    def check_chances(self):
        return self.settings.chances > 0
