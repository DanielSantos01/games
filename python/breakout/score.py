import pygame.sysfont

class Score():
    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        self.width, self.height = 200, 30
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 24)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen.get_rect().width - 160

        self.level = 1
        self.value = 0
        with open('score/high_score.txt', 'r') as high:
            self.high_score = int(high.readline())

    def prep_score(self):
        message = 'level: {}     score: {}       high: {}'.format(self.level, self.value, self.high_score)
        self.msg_image = self.font.render(message, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = self.rect.centerx

    def show(self):
        self.screen.fill(self.button_color, self.rect)#desenha o retângulo do botão
        self.screen.blit(self.msg_image, self.msg_image_rect)#desenha a imagem do texto no botão

    def update(self):
        self.value += self.level*10

    def check_high_score(self):
        if self.value > self.high_score:
            self.high_score = self.value
            with open('score/high_score.txt', 'w') as high:
                high.write(str(self.high_score))