import pygame
from pygame.sprite import Group
import functions as function
from settings import Settings
from bar import Bar
from ball import Ball
from button import Button
from chances import Chances
from score import Score

def run():
    #inicia o pygame
    pygame.init()

    #carrega as configurações
    settings = Settings()

    #cria a tela de exibição e adiciona uma legenda
    screen = pygame.display.set_mode(settings.screen_dimension)
    pygame.display.set_caption('BreakOut - Python')

    #cria os elementos do game
    barra = Bar(screen, settings)
    chances = Chances(screen, settings)
    score = Score(screen, settings)
    ball = Ball(screen, barra, settings, chances, score)
    btn_start = Button(screen, 'press space to start')
    btn_game_over = Button(screen, 'Game Over')

    #cria o grupo que compôe o 'muro'
    object_group = Group()
    function.dispose_objects(screen, object_group, score)

    while True:
        function.check_events(barra, settings, chances, score)
        function.update_screen(barra, screen, ball, settings, object_group, btn_start, btn_game_over, chances, score)

run()
