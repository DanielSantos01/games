import pygame.sysfont

class Button():
    def __init__(self, screen, message):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #definindo as dimensões e as propriedades do botão
        self.width, self.heigth = 200, 50
        self.button_color = (255, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 24)

        #constrói o objeto rect do botão e o centraliza
        self.rect = pygame.Rect(0, 0, self.width, self.heigth)
        self.rect.center = self.screen_rect.center

        #a mensagem do botão deve ser carregada apenas uma vez
        self.prep_msg(message)

    def prep_msg(self, message):
        self.msg_image = self.font.render(message, True, self.text_color, self.button_color)

        #obtém o rect da imagem criada
        self.msg_image_rect = self.msg_image.get_rect()

        # transforma o centro da msg no centro do botão
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

