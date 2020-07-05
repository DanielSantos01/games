import pygame


class Bar:
    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings

        # bar dimensions
        self.width = 200
        self.height = 30

        # bar color
        self.color = (255, 255, 255)

        # rect
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.height

        # flags
        self.flag_right = False
        self.flag_left = False

    def draw(self):
        if self.flag_left and self.rect.left >= 0 and not self.settings.game_over:
            self.rect.left -= 1

        if self.flag_right and self.rect.right <= self.screen_rect.width and not self.settings.game_over:
            self.rect.right += 1

        pygame.draw.rect(self.screen, self.color, self.rect)
