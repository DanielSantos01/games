import pygame
from pygame.sprite import Group
import create_functions as create
from check_functions import check_events
from scoreboard import Scoreboard
from game_stats import GameStats
import update_functions as update
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
    create.create_fleet(game_settings, screen, ship, aliens)                    #cria uma frota de alienígenas
    pygame.display.set_caption('alien invasion')                                  #define o título da janela
    stats = GameStats(game_settings)                                              #criando um objeto contendo os status do jogo
    score = Scoreboard(game_settings, screen, stats)                              #cria um objeto score
    play = Button(game_settings, screen, 'play')                                  #criando o botão play
    background = pygame.image.load('imagens/black_theme/background.png')

    while True:                                                                   #inicia o laço principal do jogo
        check_events(game_settings,screen,ship,bullets,stats,play,aliens,score)#verifica as ocorrencias de eventos no teclado e no mouse
        if stats.game_active:                                                     #verifica se o jogo está ativo (com naves restantes)
            ship.update()                                                         #atualiza o posicionamento do objeto (imagem)
            update.update_bullets(game_settings,screen, ship,bullets,aliens, stats, score)#realiza a atualização da posição dos projéteis
            update.update_aliens(game_settings,stats,screen,ship,aliens,bullets,score)#realiza a atualização da posição dos aliens
        update.update_screen(game_settings,screen,ship,aliens,bullets,stats,play,score, background)#realiza a atualização da tela

#-----------------------------------------------------------------------------------------------------------------------
run_game()                                                                        #chamada da função
