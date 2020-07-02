import pygame
import sys

def check_events(barra, settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown(event, barra, settings)

        elif event.type == pygame.KEYUP:
            check_keyup(event, barra)


def check_keydown(event, barra, settings):
    if event.key == pygame.K_ESCAPE:
        sys.exit()

    elif event.key == pygame.K_RIGHT:
        barra.flag_right = True

    elif event.key == pygame.K_LEFT:
        barra.flag_left = True

    elif event.key == pygame.K_SPACE:
        settings.game_start = True


def check_keyup(event, barra):
    if event.key == pygame.K_RIGHT:
        barra.flag_right = False

    elif event.key == pygame.K_LEFT:
        barra.flag_left = False


def update_screen(barra, screen, ball, setting):
    screen.fill(setting.bg_color)
    barra.draw()
    ball.update()
    ball.draw()
    check_colision(barra, ball)
    pygame.display.flip()


def check_colision(barra, ball):
    if barra.rect.colliderect(ball.rect):
        ball.direction(ball.rect.centerx)
        ball.down = False
