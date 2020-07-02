import pygame
from pygame.sprite import Group
import game_functions as function
from game_over_button import GameOverButton
from scoreboard import Scoreboard
from settings import Settings
from ground import Ground
from button import Button
from bird import Bird

def run_game():
    pygame.init()
    settings = Settings()
    clock = pygame.time.Clock()
    #tela
    screen = pygame.display.set_mode(settings.SCREEN_DIMENSION)
    pygame.display.set_caption('Flappy Bird - Python')
    surface = pygame.image.load('images/bluebird-midflap.png')
    pygame.display.set_icon(surface)
    #objetos
    bird = Bird(settings, screen)
    ground = Ground(screen, settings)
    button = Button(screen, settings)
    game_over = GameOverButton(screen, settings)
    score = Scoreboard(screen)
    #grupos
    ground_group = Group()
    pipe_up_group = Group()
    pipe_down_group = Group()
    #adições
    ground_group.add(ground)

    #-------------------------------------------------------------------------------------------------------------------
    while True:
        clock.tick(30)
        function.check_events(bird, screen, settings, pipe_up_group, pipe_down_group, score)
        function.update_screen(screen, bird, settings, ground_group, button, game_over, pipe_up_group, pipe_down_group, score)

run_game()