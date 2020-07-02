import pygame
from pygame.sprite import Group
import game_functions as function
from scoreboard import Scoreboard
from game_stats import GameStats
from settings import Settings
from button import Button
from ship import Ship

#-----------------------------------------------------------------------------------------------------------------------
def run_game():
    pygame.init()                                                                 #inicializa as funções do pygame
    game_settings = Settings()                                                    #instancia um objeto contendo as configurações do jogo
    screen = pygame.display.set_mode(game_settings.screen_dimension)              #cria a tela do jogo (param. Tupla larg X alt)
    ship = Ship(screen, game_settings)                                            #cria a espaçonave
    bullets = Group()                                                             #cria um grupo no qual serão armazenados todos os projéteis
    aliens = Group()                                                              #cria um grupo de aliens
    function.create_fleet(game_settings, screen, ship, aliens)                    #cria uma frota de alienígenas
    pygame.display.set_caption('alien invasion')                                  #define o título da janela
    stats = GameStats(game_settings)                                              #criando um objeto contendo os status do jogo
    score = Scoreboard(game_settings, screen, stats)                              #cria um objeto score
    play = Button(screen, 'play')                                                 #criando o botão play

    while True:                                                                   #inicia o laço principal do jogo
        function.check_events(game_settings,screen,ship,bullets,stats,play,aliens,score)
        if stats.game_active:
            ship.update()
            function.update_bullets(game_settings,screen,ship,bullets,aliens,stats,score)
            function.update_aliens(game_settings,stats,screen,ship,aliens,bullets, score)
        function.update_screen(game_settings,screen,ship,aliens,bullets,stats,play,score)

#-----------------------------------------------------------------------------------------------------------------------
run_game()                                                                        #chamada da função
