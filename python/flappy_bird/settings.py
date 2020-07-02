import pygame
class Settings():
    def __init__(self):
        #screen
        self.SCREEN_HEIGHT = 680
        self.SCREEN_WIDTH = 400
        self.SCREEN_DIMENSION = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        #background
        self.BACKGROUND = pygame.image.load('images/background-day.png')
        self.BACKGROUND = pygame.transform.scale(self.BACKGROUND, self.SCREEN_DIMENSION)
        self.BACKGROUND_ALIGN = (0, 0)
        #ground
        self.ground_width = 2 * self.SCREEN_WIDTH
        self.ground_height = 100
        #bird position
        self.const_up = 10
        self.fall = 10
        self.gravity = 1
        #pause
        self.dimension = (200, 340)
        #pipes height
        self.up_height = [150, 100, 50, 300, 350, 180, 400, 50, 80, 420]
        self.down_height = [300, 350, 400, 150, 100, 270, 50, 400, 370, 30]
        #control flags
        self.flag_run_game = False
        self.flag_run_once = True
        self.flag_restart_level = False
        self.flag_point = True
        self.number = 0
