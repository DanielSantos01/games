import pygame

class Ball():
    def __init__(self, screen, bar, settings, chances):
        self.settings = settings
        self.bar = bar
        self.screen = screen
        self.chances = chances

        #cor branca
        self.color = (255, 255, 255)

        #especificações da bolinha
        self.radius = 15
        self.center = [self.bar.rect.centerx, self.bar.rect.top - self.radius]

        #forma o retângulo para a bolinha (necessário para detectar colisôes com a barra)
        self.rect = pygame.Rect(0, 0, 2*self.radius, 2*self.radius)

        self.deflection = 0

        #flags de movimentação
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)

    def update(self):
        if not self.settings.game_start:
            self.follow_bar()
        else:
            self.set_flags()
            self.move()

    def set_flags(self):
        #movimento vertical
        if (self.center[1] - self.radius) > 0 and not self.down:
            self.go_up()
        else:
            self.go_down()
            if (self.center[1] + self.radius) >= self.screen.get_rect().height:
                self.fail()
                self.bar.rect.centerx = self.screen.get_rect().centerx

        #movimento horizontal
        if self.right or self.left:
            if (self.center[0] - self.radius) > 0 and not self.right:
                self.go_left()
            else:
                self.go_right()
                if (self.center[0] + self.radius) >= self.screen.get_rect().width:
                    self.go_left()

    def go_up(self):
        self.up = True
        self.down = False

    def go_down(self):
        self.up = False
        self.down = True

    def go_left(self):
        self.right = False
        self.left = True

    def go_right(self):
        self.left = False
        self.right = True

    def fail(self):
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.chances.left -= 1
        self.what_to_do()

    def what_to_do(self):
        if self.chances.check_chances():
            self.settings.pre_start = True
            self.settings.game_start = False
        else:
            self.settings.pre_start = False
            self.settings.game_start = False
            self.settings.game_over = True

    def follow_bar(self):
        self.center[0] = self.bar.rect.centerx
        self.center[1] = self.bar.rect.top - self.radius

    def move(self):
        if self.up:
            self.center[1] -= 1

        if self.down:
            self.center[1] += 1

        if self.left:
            self.center[0] -= self.deflection

        if self.right:
            self.center[0] += self.deflection

        self.update_rect()

    def update_rect(self):
        self.rect.centerx = self.center[0]
        self.rect.centery = self.center[1]

    def direction(self, centerx):
        #direita
        if centerx > self.bar.rect.centerx + 25 and centerx <= self.bar.rect.centerx + 40:
            self.deflection = 0.1
            self.right = True
            self.left = False

        elif centerx > self.bar.rect.centerx + 40 and centerx <= self.bar.rect.centerx + 60:
            self.deflection = 0.2
            self.right = True
            self.left = False

        elif centerx > self.bar.rect.centerx + 60 and centerx <= self.bar.rect.centerx + 85:
            self.deflection = 0.3
            self.right = True
            self.left = False

        elif centerx > self.bar.rect.centerx + 85:
            self.deflection = 0.5
            self.right = True
            self.left = False

        #esquerda
        elif centerx < self.bar.rect.centerx - 25 and centerx >= self.bar.rect.centerx - 40:
            self.deflection = 0.1
            self.right = False
            self.left = True

        elif centerx < self.bar.rect.centerx - 40 and centerx >= self.bar.rect.centerx - 60:
            self.deflection = 0.2
            self.right = False
            self.left = True

        elif centerx < self.bar.rect.centerx - 60 and centerx >= self.bar.rect.centerx - 85:
            self.deflection = 0.3
            self.right = False
            self.left = True

        elif centerx < self.bar.rect.centerx - 85:
            self.deflection = 0.5
            self.right = False
            self.left = True