import pygame


class Objects:
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/obj.png')
        self.rect = self.image.get_rect()
        # self.rect = pygame.Rect(0, 0, 90, 30)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # pygame.draw.rect(self.screen, (255, 255, 255), self.rect)
