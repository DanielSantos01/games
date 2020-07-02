import pygame
class Ball():

    def __init__(self,screen, bar, setting):
        self.settings = setting
        self.bar = bar
        self.screen = screen

        self.radius = 15
        self.center = [bar.rect.centerx, bar.rect.top-self.radius]

        self.rect = pygame.Rect(0, 0, 2*self.radius, 2*self.radius)

        self.up = False
        self.down = False

    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 255), self.center, self.radius)

    def update(self):
        #se o jogo estiver parado, o centro da bola é o centro da barra
        if not self.settings.game_start:
            self.center[0] = self.bar.rect.centerx
        else:
            #se o jogo tiver começado, a bola sobe até o topo
            if (self.center[1] - self.radius) > 0 and not self.down:
                self.up = True
            else:
                #se a bola já tiver chegado ao topo, faz ela descer
                self.up = False
                self.down = True
                if (self.center[1] + self.radius) == self.screen.get_rect().height:
                    self.down = False

        self.move()


    def move(self):
        if self.up:
            self.center[1] -= 1

        if self.down:
            self.center[1] += 1

        self.update_rect()


    def update_rect(self):
        self.rect.centerx = self.center[0]
        self.rect.centery = self.center[1]