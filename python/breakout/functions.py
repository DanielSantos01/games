import pygame
import sys
from objects import Objects


def check_events(bar, settings, chances, score):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            score.check_high_score()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown(event, bar, settings, chances, score)

        elif event.type == pygame.KEYUP:
            check_keyup(event, bar)


def check_keydown(event, bar, settings, chances, score):
    if event.key == pygame.K_ESCAPE:
        score.check_high_score()
        sys.exit()

    elif event.key == pygame.K_RIGHT:
        bar.flag_right = True

    elif event.key == pygame.K_LEFT:
        bar.flag_left = True

    elif event.key == pygame.K_SPACE:
        # endgame situation
        if not settings.pre_start and not settings.game_start:
            settings.pre_start = True
            settings.game_over = False
            chances.left = 3
            score.value = 0
            score.level = 1
        # pre_start situation
        elif settings.pre_start:
            settings.pre_start = False
            settings.game_start = True


def check_keyup(event, bar):
    if event.key == pygame.K_RIGHT:
        bar.flag_right = False

    elif event.key == pygame.K_LEFT:
        bar.flag_left = False


def update_screen(bar, screen, ball, settings, object_group, btn_start, btn_game_over, chances, score):
    check_new_level(ball, object_group, score, screen)
    screen.fill(settings.bg_color)

    # draw the bar and update the ball position
    bar.draw()
    ball.update()

    # analyse collision
    check_collision(bar, ball, object_group, score)

    # draw the wall
    draw_wall(object_group)

    # draw the ball
    ball.draw()

    # check and show the chances
    chances.prep_chances(chances.left)
    chances.show()

    score.prep_score()
    score.show()

    check_draw_button(settings, btn_start, btn_game_over)
    pygame.display.flip()


def draw_wall(object_group):
    for obj in object_group:
        obj.blitme()


def check_collision(bar, ball, objects, score):
    if bar.rect.colliderect(ball.rect):
        ball.direction(ball.rect.centerx)
        ball.go_up()

    for obj in objects:
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
    obj = Objects(screen)
    elements_in_x = space_available_x(screen, obj)
    for v_number in range(score.level):
        for h_number in range(elements_in_x + 1):
            create_object(group, h_number, v_number, screen)


def space_available_x(screen, obj):
    available_space = screen.get_rect().width
    horizontal_number = int(available_space / (obj.rect.width + 5))
    return horizontal_number


def create_object(group, h_number, v_number, screen):
    obj = Objects(screen)
    space_x = obj.rect.width*h_number
    space_y = obj.rect.height*v_number
    obj.rect.x = space_x
    obj.rect.y = 30 + space_y
    group.append(obj)


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
