import pygame.sysfont

class Chances():
    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        self.width, self.height = 100, 30
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 24)

        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.left = 3
        self.prep_chances(self.left)

    def prep_chances(self, number):
        message = str(number) + ' chances left'
        self.msg_image = self.font.render(message, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()

    def show(self):
        self.screen.fill(self.button_color, self.rect)#desenha o retângulo do botão
        self.screen.blit(self.msg_image, self.msg_image_rect)#desenha a imagem do texto no botão

    def check_chances(self):
        return self.left > 0
