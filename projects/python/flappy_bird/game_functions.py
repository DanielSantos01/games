import sys
import pygame
from ground import Ground
from pipe_up import PipeUp
from pipe_down import PipeDown

def check_events(bird, screen, settings, pipe_up_group, pipe_down_group, score):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_events(event, bird, screen, settings, pipe_up_group, pipe_down_group, score)

#-----------------------------------------------------------------------------------------------------------------------
def keydown_events(event, bird, screen, settings, pipe_up_group, pipe_down_group, score):
    if event.key == pygame.K_SPACE and not settings.flag_run_game and settings.flag_run_once:
        start_level(bird, screen, settings, pipe_up_group, pipe_down_group, score)
    elif event.key == pygame.K_SPACE and not settings.flag_run_game:
        settings.flag_run_once = True
    elif event.key == pygame.K_SPACE:
        bird.up()
        bird.wing()

def start_level(bird, screen, settings, pipe_up_group, pipe_down_group, score):
    first_pipes(screen, settings, pipe_up_group, pipe_down_group)
    bird.center_bird()
    bird.up()
    score.reset_score()
    settings.flag_run_game = True
    settings.flag_run_once = False
    settings.flag_point = True
#-----------------------------------------------------------------------------------------------------------------------
def new_ground(ground_group, screen, settings):
        ground_group.empty()
        new_ground = Ground(screen, settings)
        ground_group.add(new_ground)

#-----------------------------------------------------------------------------------------------------------------------
def update_screen(screen, bird, settings, ground_group, button, game_over, pipe_up_group, pipe_down_group, score):
    screen.blit(settings.BACKGROUND, settings.BACKGROUND_ALIGN)
    if settings.flag_run_game:
        execute_game(bird, ground_group, settings, pipe_up_group, pipe_down_group, screen, score)
    else:
        show_pause_screen(bird, ground_group, screen, settings, button, game_over, pipe_up_group, pipe_down_group, score)
    pygame.display.update()

#-----------------------------------------------------------------------------------------------------------------------
def execute_game(bird,ground_group, settings, pipe_up_group, pipe_down_group, screen, score):
    update_groups(bird, ground_group, settings, pipe_up_group, pipe_down_group)
    check_point(bird, score, pipe_down_group, settings)
    check_ground(ground_group, screen, settings)
    check_pipe_out(pipe_up_group, pipe_down_group, screen, settings)
    draw_groups(bird, ground_group, pipe_up_group, pipe_down_group, screen, score)

#-----------------------------------------------------------------------------------------------------------------------
def check_point(bird, score, pipe_down_group, settings):
    center_pipe = pipe_down_group.sprites()[settings.number].rect.x
    if center_pipe < 200 and settings.flag_point:
        bird.point()
        update_score(score)
        settings.flag_point = False

def update_score(score):
    score.update_score()
    pygame.display.flip()

#-----------------------------------------------------------------------------------------------------------------------
def update_groups(bird, ground, settings, pipe_up, pipe_down):
    bird.update()
    ground.update()
    pipe_up.update()
    pipe_down.update()
    if pygame.sprite.spritecollideany(bird, ground) or pygame.sprite.spritecollideany(bird, pipe_up) or \
            pygame.sprite.spritecollideany(bird, pipe_down):
        settings.flag_run_game = False
        settings.flag_restart_level = True
        bird.hit()

#-----------------------------------------------------------------------------------------------------------------------
def draw_groups(bird, ground, pipe_up, pipe_down, screen, score):
    bird.blitme()
    ground.draw(screen)
    pipe_up.draw(screen)
    pipe_down.draw(screen)
    score.show_score()
    pygame.display.flip()

#-----------------------------------------------------------------------------------------------------------------------
def check_ground(ground_group, screen, settings):
    if ground_group.sprites()[0].check_out():
        new_ground(ground_group, screen, settings)

#-----------------------------------------------------------------------------------------------------------------------
def check_pipe_out(pipe_up_group, pipe_down_group, screen, settings):
    check_pipe_up_out(pipe_up_group, screen, settings)
    check_pipe_down_out(pipe_down_group, screen, settings)

#-----------------------------------------------------------------------------------------------------------------------
def check_pipe_up_out(pipe_up_group, screen, settings):
    for pipe in pipe_up_group.sprites():
        if pipe.is_out():
            reuse_pipe_up(pipe, pipe_up_group, screen, settings)
            settings.flag_point = True

#-----------------------------------------------------------------------------------------------------------------------
def check_pipe_down_out(pipe_down_group, screen, settings):
    for pipe in pipe_down_group.sprites():
        if pipe.is_out():
            reuse_pipe_down(pipe, pipe_down_group, screen, settings)

#-----------------------------------------------------------------------------------------------------------------------
def reuse_pipe_up(pipe, pipe_up_group, screen, settings):
    number = pipe.number
    pipe_up_group.remove(pipe)
    new_pipe = PipeUp(screen, settings, number)
    new_pipe.rect.x = (pipe_up_group.sprites()[-1].rect.x) + new_pipe.rect.width * 4
    pipe_up_group.add(new_pipe)

#-----------------------------------------------------------------------------------------------------------------------
def reuse_pipe_down(pipe, pipe_down_group, screen, settings):
    number = pipe.number
    pipe_down_group.remove(pipe)
    new_pipe = PipeDown(screen, settings, number)
    new_pipe.rect.x = (pipe_down_group.sprites()[-1].rect.x) + new_pipe.rect.width * 4
    pipe_down_group.add(new_pipe)

#-----------------------------------------------------------------------------------------------------------------------
def first_pipes(screen, settings, pipe_up_group, pipe_down_group):
    pipe_up_group.empty()
    pipe_down_group.empty()
    for number in range(len(settings.up_height)):
        #pipe_up
        pipe_up = PipeUp(screen, settings, number)
        pipe_up.rect.x = (screen.get_rect().right + 2*pipe_up.rect.width) + number * pipe_up.rect.width * 4
        pipe_up_group.add(pipe_up)
        #pipe_down
        pipe_down = PipeDown(screen, settings, number)
        pipe_down.rect.x = ((screen.get_rect().right + 2*pipe_down.rect.width)) + number * pipe_down.rect.width * 4
        pipe_down_group.add(pipe_down)
    if not settings.flag_run_once:
        settings.flag_restart_level = False
    pygame.display.flip()
#-----------------------------------------------------------------------------------------------------------------------
def show_pause_screen(bird, ground_group, screen, settings, button, game_over, pipe_up, pipe_down, score):
    if settings.flag_run_once:
        button.draw_button()
        bird.pause()
        #bird.blitme()
        ground_group.update()
        check_ground(ground_group, screen, settings)
    else:
        bird.blitme()
        pipe_up.draw(screen)
        pipe_down.draw(screen)
        game_over.draw_button()
        score.show_score()
    ground_group.draw(screen)
    pygame.display.update()