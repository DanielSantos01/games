import pygame
import sys
from objects import Objects

def check_events(barra, settings, chances, score):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            score.check_high_score()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown(event, barra, settings, chances, score)

        elif event.type == pygame.KEYUP:
            check_keyup(event, barra)

def check_keydown(event, barra, settings, chances, score):
    if event.key == pygame.K_ESCAPE:
        score.check_high_score()
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
            score.value = 0
            score.level = 1
        #situação de espera pelo click do jogador
        elif settings.pre_start:
            settings.pre_start = False
            settings.game_start = True

def check_keyup(event, barra):
    if event.key == pygame.K_RIGHT:
        barra.flag_right = False

    elif event.key == pygame.K_LEFT:
        barra.flag_left = False

def update_screen(barra, screen, ball, settings, object_group, btn_start, btn_game_over, chances, score):
    #preenche a tela
    screen.fill(settings.bg_color)

    #desenha a barra e atualiza a posição da bola
    barra.draw()
    ball.update()

    #analisa se ocorreu alguma colisão
    check_colision(barra, ball, object_group, score)
    check_new_level(ball, object_group, score, screen)

    #desenha o 'muro'
    object_group.draw(screen)

    #desenha a bola
    ball.draw()

    #checha sempre quantas chances restam para deixar atualizado
    chances.prep_chances(chances.left)
    chances.show()

    score.prep_score()
    score.show()

    check_draw_button(settings, btn_start, btn_game_over)

    pygame.display.flip()

def check_colision(barra, ball, objects, score):
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
            score.update()
            score.check_high_score()
            break

def dispose_objects(screen, group, score):
    object = Objects()
    elements_in_x = space_available_x(screen, object)
    for v_number in range(score.level):
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
    #print('{},{}: {},{}'.format(h_number, v_number, object.rect.x, object.rect.y))
    group.add(object)

def check_new_level(ball, object_group, score, screen):
    if len(object_group) == 0:
        new_level(ball, score, object_group, screen)

def new_level(ball, score, object_group, screen):
    score.level += 1
    ball.center_bar()
    ball.reset('new level')
    dispose_objects(screen, object_group, score)

def check_draw_button(settings, btn_start, btn_game_over):
    if settings.game_over:
        btn_game_over.draw_button()
    if settings.pre_start:
        btn_start.draw_button()
