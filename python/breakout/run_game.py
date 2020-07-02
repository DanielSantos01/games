import pygame
import functions as function
from settings import Settings
from bar import Bar
from ball import Ball

def run():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode(setting.screen_dimension)
    pygame.display.set_caption('BreakOut - Python')
    barra = Bar(screen)
    ball = Ball(screen, barra, setting)
        
    while True:
        function.check_events(barra, setting)
        function.update_screen(barra, screen, ball, setting)



run()
