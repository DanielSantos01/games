import pygame

class Ball():
    def __init__(self,screen, bar, setting):
        self.settings = setting
        self.bar = bar
        self.screen = screen

        #especificações da bolinha
        self.radius = 15
        self.center = [self.bar.rect.centerx, self.bar.rect.top - self.radius]

        #forma o retângulo para a bolinha (necessário para detectar colisôes com a barra)
        self.rect = pygame.Rect(0, 0, 2*self.radius, 2*self.radius)

        #flags de movimentação
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.first = True


    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 255), self.center, self.radius)


    def update(self):
        #se o jogo estiver parado, o centro da bola é o centro da barra
        if not self.settings.game_start:
            self.follow_bar()
        else:
            #quando o jogo começar, realiza a manutenção das flags de movimento (para cima e para baixo)
            self.set_flags()

        self.move()


    def set_flags(self):
        if (self.center[1] - self.radius) > 0 and not self.down:
            self.up = True
        else:
            self.up = False
            self.down = True
            if (self.center[1] + self.radius) == self.screen.get_rect().height:
                self.down = False
                self.first = True
                self.right = False
                self.left = False
                self.settings.game_start = False

        if not self.first:
            if (self.center[0] - self.radius) > 0 and not self.right:
                self.left = True

            else:
                self.left = False
                self.right = True
                if (self.center[0] + self.radius) >= self.screen.get_rect().width:
                    self.right = False


    def follow_bar(self):
        self.center[0] = self.bar.rect.centerx
        self.center[1] = self.bar.rect.top - self.radius


    def move(self):
        if self.up:
            self.center[1] -= 1

        if self.down:
            self.center[1] += 1

        if self.left:
            self.center[0] -= 0.7

        if self.right:
            self.center[0] += 0.7

        self.update_rect()


    def update_rect(self):
        self.rect.centerx = self.center[0]
        self.rect.centery = self.center[1]


    def direction(self, centerx):
         if self.first:
             self.first = False
         else:
            if centerx > self.bar.rect.centerx:
                self.right = True
                self.left = False
            else:
                self.right = False
                self.left = True
