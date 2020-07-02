import pygame
class Ball():

    def __init__(self,screen, bar):
        self.screen = screen
        self.radius = 15
        self.center = (bar.rect.centerx, bar.rect.top-self.radius)

    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 255), self.center, self.radius)