import pygame

class Scoreboard():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.score = [pygame.image.load('images/0.png'),
                      pygame.image.load('images/1.png'),
                      pygame.image.load('images/2.png'),
                      pygame.image.load('images/3.png'),
                      pygame.image.load('images/4.png'),
                      pygame.image.load('images/5.png'),
                      pygame.image.load('images/6.png'),
                      pygame.image.load('images/7.png'),
                      pygame.image.load('images/8.png'),
                      pygame.image.load('images/9.png'),]

        self.score_rect = self.score[0].get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.centery = 50
        self.center_second_number = self.score_rect.centerx + 23
        self.first_number = 0
        self.second_number = 0
        self.third_number = 0
        self.flag_one_number = True
        self.flag_two_numbers = False
        self.flag_three_numbers = False

    #-------------------------------------------------------------------------------------------------------------------
    def show_score(self):
        if self.flag_one_number:
            self.screen.blit(self.score[self.first_number], self.score_rect)
        elif self.flag_two_numbers:
            self.screen.blit(self.score[self.second_number], self.score_rect)
            self.score_rect.centerx = self.center_second_number
            self.screen.blit(self.score[self.first_number], self.score_rect)
            self.score_rect.centerx = self.screen_rect.centerx

    #-------------------------------------------------------------------------------------------------------------------
    def update_score(self):
        self.first_number += 1
        if self.first_number > 9:
            self.first_number = 0
            self.second_number += 1
            self.flag_two_numbers = True
            self.flag_one_number = False
        if self.second_number >= 9 and self.first_number >= 9:
            self.second_number += 1
            self.flag_one_number = False

    #-------------------------------------------------------------------------------------------------------------------
    def reset_score(self):
        self.first_number = 0
        self.second_number = 0
        self.third_number = 0
        self.flag_one_number = True
        self.flag_two_numbers = False
        self.flag_three_numbers = False