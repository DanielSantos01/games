import pygame
import functions as function
from settings import Settings
from bar import Bar
from ball import Ball
from button import Button
from chances import Chances
from score import Score


def run():
    pygame.init()

    # load the game settings
    settings = Settings()

    # create the screen and add a title
    screen = pygame.display.set_mode(settings.screen_dimension)
    pygame.display.set_caption('BreakOut - Python')

    # create the game elements
    bar = Bar(screen, settings)
    chances = Chances(screen, settings)
    score = Score(screen, settings)
    ball = Ball(screen, bar, settings, chances, score)
    btn_start = Button(screen, 'press space to start')
    btn_game_over = Button(screen, 'Game Over')

    object_group = []
    function.dispose_objects(screen, object_group, score)

    while True:
        function.check_events(bar, settings, chances, score)
        function.update_screen(bar, screen, ball, settings, object_group, btn_start, btn_game_over, chances, score)


run()
