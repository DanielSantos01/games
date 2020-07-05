import pygame.sysfont


class Button:
    def __init__(self, screen, message):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # define the dimensions of the button
        self.width, self.heigth = 200, 50
        self.button_color = (255, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 24)

        # construct the rect of the button and centralize
        self.rect = pygame.Rect(0, 0, self.width, self.heigth)
        self.rect.center = self.screen_rect.center

        self.msg_image = ''
        self.msg_image_rect = 0

        self.prep_msg(message)

    def prep_msg(self, message):
        self.msg_image = self.font.render(message, True, self.text_color, self.button_color)

        # get the rect of the created image
        self.msg_image_rect = self.msg_image.get_rect()

        # transform the image center in the button center
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

