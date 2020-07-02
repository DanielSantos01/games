import pygame, sys

def check_events(barra):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown(event, barra)

        elif event.type == pygame.KEYUP:
            check_keyup(event, barra)


def check_keydown(event, barra):
    if event.key == pygame.K_RIGHT:
        barra.flag_right = True

    elif event.key == pygame.K_LEFT:
        barra.flag_left = True


def check_keyup(event, barra):
    if event.key == pygame.K_RIGHT:
        barra.flag_right = False

    elif event.key == pygame.K_LEFT:
        barra.flag_left = False


def update_screen(barra, screen, setting):
    screen.fill(setting.bg_color)
    barra.draw()
    pygame.display.flip()
