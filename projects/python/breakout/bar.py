import pygame
class Bar():

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        #bar dimensions
        self.width = 200
        self.height = 30

        #bar color
        self.color = (255, 255, 255)

        #rect
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.height

        #flags
        self.flag_right = False;
        self.flag_left = False;

    #function who draws bar in the screen
    def draw(self):
        if self.flag_left and self.rect.left >= 0:
            self.rect.left -= 1

        if self.flag_right and self.rect.right <= self.screen_rect.width:
            self.rect.right += 1

        pygame.draw.rect(self.screen, self.color, self.rect)


