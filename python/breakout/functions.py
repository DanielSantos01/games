import pygame
import sys
from objects import Objects

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

def update_screen(barra, screen, ball, setting, objects, btn):
    screen.fill(setting.bg_color)
    barra.draw()
    ball.update()
    check_colision(barra, ball, objects)
    objects.draw(screen)
    ball.draw()
    if not setting.game_start:
        btn.draw_button()
    pygame.display.flip()

def check_colision(barra, ball, objects):
    if barra.rect.colliderect(ball.rect):
        ball.direction(ball.rect.centerx)
        ball.down = False

    for obj in objects.sprites():
        if ball.rect.colliderect(obj.rect):
            if ball.up:
                ball.go_down()
            else:
                ball.go_up()
            objects.remove(obj)
            break

def dispose_objects(screen, group):
    obj = Objects()
    number = space_available_x(screen, obj)

    for v_number in range(4):
        for h_number in range(number+1):
            create_object(group, h_number, v_number)


def space_available_x(screen, obj):
    available_space = screen.get_rect().width
    objects_number = int(available_space / (obj.rect.width + 5))
    return objects_number


def create_object(group, h_number, v_number):
    obj = Objects()
    obj_width = obj.rect.width
    space_x = (obj_width*h_number)
    obj.rect.x = space_x
    obj.rect.y = 30 + (v_number*obj.rect.height)
    group.add(obj)
