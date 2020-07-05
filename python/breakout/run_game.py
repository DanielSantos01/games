import pygame
import functions as function
from pygame.sprite import Group
from settings import Settings
from bar import Bar
from ball import Ball
from button import Button

def run():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode(setting.screen_dimension)
    pygame.display.set_caption('BreakOut - Python')
    barra = Bar(screen)
    ball = Ball(screen, barra, setting)
    objs = Group()
    btn = Button(screen, 'press space to start')
    function.dispose_objects(screen, objs)

    while True:
        function.check_events(barra, setting)
        function.update_screen(barra, screen, ball, setting, objs, btn)

run()
