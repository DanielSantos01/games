import pygame
import sys
from objects import Objects

def check_events(barra, settings, chances):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown(event, barra, settings, chances)

        elif event.type == pygame.KEYUP:
            check_keyup(event, barra)

def check_keydown(event, barra, settings, chances):
    if event.key == pygame.K_ESCAPE:
        sys.exit()

    elif event.key == pygame.K_RIGHT:
        barra.flag_right = True

    elif event.key == pygame.K_LEFT:
        barra.flag_left = True

    elif event.key == pygame.K_SPACE:
        #situação de fim de jogo
        if not settings.pre_start and not settings.game_start:
            settings.pre_start = True
            settings.game_over = False
            chances.left = 3
        #situação de espera pelo click do jogador
        elif settings.pre_start:
            settings.pre_start = False
            settings.game_start = True

def check_keyup(event, barra):
    if event.key == pygame.K_RIGHT:
        barra.flag_right = False

    elif event.key == pygame.K_LEFT:
        barra.flag_left = False

def update_screen(barra, screen, ball, settings, object_group, btn_start, btn_game_over, chances):
    #preenche a tela
    screen.fill(settings.bg_color)

    #desenha a barra e atualiza a posição da bola
    barra.draw()
    ball.update()

    #analisa se ocorreu alguma colisão
    check_colision(barra, ball, object_group)

    #desenha o 'muro'
    object_group.draw(screen)

    #desenha a bola
    ball.draw()

    #checha sempre quantas chances restam para deixar atualizado
    chances.prep_chances(chances.left)
    chances.show()

    check_draw_button(settings, btn_start, btn_game_over)

    pygame.display.flip()

def check_colision(barra, ball, objects):
    if barra.rect.colliderect(ball.rect):
        ball.direction(ball.rect.centerx)
        ball.go_up()

    for obj in objects.sprites():
        if ball.rect.colliderect(obj.rect):
            if ball.up:
                ball.go_down()
            else:
                ball.go_up()
            objects.remove(obj)
            break

def dispose_objects(screen, group):
    object = Objects()
    elements_in_x = space_available_x(screen, object)
    for v_number in range(4):
        for h_number in range(elements_in_x + 1):
            create_object(group, h_number, v_number)

def space_available_x(screen, object):
    available_space = screen.get_rect().width
    horizontal_number = int(available_space / (object.rect.width + 5))
    return horizontal_number

def create_object(group, h_number, v_number):
    object = Objects()
    space_x = object.rect.width*h_number
    space_y = object.rect.height*v_number
    object.rect.x = space_x
    object.rect.y = 30 + space_y
    group.add(object)

def check_draw_button(settings, btn_start, btn_game_over):
    if settings.game_over:
        btn_game_over.draw_button()
    if settings.pre_start:
        btn_start.draw_button()
