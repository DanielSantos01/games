import pygame


class Ball:
    def __init__(self, screen, bar, settings, chances, score):
        self.settings = settings
        self.bar = bar
        self.screen = screen
        self.chances = chances
        self.score = score

        # white color
        self.color = (255, 255, 255)

        # ball specify
        self.radius = 15
        self.center = [self.bar.rect.centerx, self.bar.rect.top - self.radius]

        # create a rectangle to the ball (necessary to detect collisions)
        self.rect = pygame.Rect(0, 0, 2*self.radius, 2*self.radius)

        self.deflection = 0

        # movement flags
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
        # vertical movement
        if (self.center[1] - self.radius) > 0 and not self.down:
            self.go_up()
        else:
            self.go_down()
            if (self.center[1] + self.radius) >= self.screen.get_rect().height:
                self.reset('fail')
                self.center_bar()

        # horizontal movement
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

    def reset(self, inform):
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        if inform == 'fail':
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

    def center_bar(self):
        self.bar.rect.centerx = self.screen.get_rect().centerx

    def follow_bar(self):
        self.center[0] = self.bar.rect.centerx
        self.center[1] = self.bar.rect.top - self.radius

    def move(self):
        if self.up:
            self.center[1] -= self.score.level

        if self.down:
            self.center[1] += self.score.level

        if self.left:
            self.center[0] -= self.deflection

        if self.right:
            self.center[0] += self.deflection

        self.update_rect()

    def update_rect(self):
        self.rect.centerx = self.center[0]
        self.rect.centery = self.center[1]

    def direction(self, centerx):
        # right
        if self.bar.rect.centerx + 25 < centerx <= self.bar.rect.centerx + 40:
            self.deflection = 0.1
            self.right = True
            self.left = False

        elif self.bar.rect.centerx + 40 < centerx <= self.bar.rect.centerx + 60:
            self.deflection = 0.2
            self.right = True
            self.left = False

        elif self.bar.rect.centerx + 60 < centerx <= self.bar.rect.centerx + 85:
            self.deflection = 0.3
            self.right = True
            self.left = False

        elif centerx > self.bar.rect.centerx + 85:
            self.deflection = 0.5
            self.right = True
            self.left = False

        # left
        elif self.bar.rect.centerx - 25 > centerx >= self.bar.rect.centerx - 40:
            self.deflection = 0.1
            self.right = False
            self.left = True

        elif self.bar.rect.centerx - 40 > centerx >= self.bar.rect.centerx - 60:
            self.deflection = 0.2
            self.right = False
            self.left = True

        elif self.bar.rect.centerx - 60 > centerx >= self.bar.rect.centerx - 85:
            self.deflection = 0.3
            self.right = False
            self.left = True

        elif centerx < self.bar.rect.centerx - 85:
            self.deflection = 0.5
            self.right = False
            self.left = True
