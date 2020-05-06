import pygame.sysfont
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """uma classe para mostrar a pontuação"""
    def __init__(self, game_settings, screen, stats):
        """inicializa os atributos de pontuação"""
        self.game_settings = game_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.stats = stats

        #configurações da fonte para a exibição da pontuação
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 28)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    #-------------------------------------------------------------------------------------------------------------------
    def prep_score(self):
        """transforma a pontuação em uma imagem renderizada"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "score: {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, None)

        #exibe a pontuaçã no canto superior esquerdo da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20

    #-------------------------------------------------------------------------------------------------------------------
    def prep_high_score(self):
        """transforma a pontuação máxima em uma imagem renderizada"""
        high_score = int(round(self.stats.high_score, -1))#arredonda para o inteiro multiplo de 10 mais proximo
        high_score_str = "high score: {:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, None)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = self.score_rect.top

    #-------------------------------------------------------------------------------------------------------------------
    def prep_level(self):
        """transforma o nível em uma imagem renderizada"""
        self.level_image = self.font.render(('level: {}'.format(self.stats.level)), True, self.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx
        self.level_rect.top = self.score_rect.top

    #-------------------------------------------------------------------------------------------------------------------
    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen, self.game_settings)
            ship.rect.x = 10 + int((ship_number * ship.rect.width / 2))
            ship.rect.y = self.score_rect.top + 30
            ship.image = pygame.transform.scale(ship.image, (30, 30))
            self.ships.add(ship)

    #-------------------------------------------------------------------------------------------------------------------
    def show_score(self):
        """desenha a pontuação na tela"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    #-------------------------------------------------------------------------------------------------------------------
    def save_high_score(self):
        with open('game_data/highscore.json', 'w') as file:
            file.write(str(self.stats.high_score))