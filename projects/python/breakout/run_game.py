import pygame
import functions as function
from settings import Settings
from bar import Bar

def run():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode(setting.screen_dimension)
    pygame.display.set_caption('BreakOut - Python')
    barra = Bar(screen)
        
    while True:
        function.check_events(barra)
        function.update_screen(barra, screen, setting)



run()
