import sys
import pygame
from game_functions import fire_bullets, rotate_image, reset_flags, new_chance

def check_keydown_events(event, game_settings, screen, ship, bullets, score):
    """responde a pressionamentos de teclas"""
    if event.key == pygame.K_RIGHT:                                            #verifica se a seta direita foi pressionada
        ship.moving_right = True                                               #habilita a movimentação para a direita
    elif event.key == pygame.K_LEFT:                                           #verifica se a seta para a esquerda foi pressionada
        ship.moving_left = True                                                #habilita a movimentação para a esquerda
    elif event.key == pygame.K_SPACE:                                          #verifica se a tecla espaço foi pressionada
        fire_bullets(game_settings, screen, ship, bullets)                     #chama a função de disparo de projéteis
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_r:
        rotate_image(ship)
        game_settings.flag_direction *= -1
    elif event.key == pygame.K_q:                                              #verifica se a tecla q foi pressionada
        score.save_high_score()
        sys.exit()                                                             #fecha o jogo

#-----------------------------------------------------------------------------------------------------------------------
def check_keyup_events(ship, event):
    """responde a solturas de teclas"""
    if event.key == pygame.K_RIGHT:                                            #verifica se a seta para a direita foi solta
        ship.moving_right = False                                              #desabilita a movimentação para a direita
    elif event.key == pygame.K_LEFT:                                           #verifica se a seta para a esquerda foi solta
        ship.moving_left = False                                               #desabilita a movimentação para a esquerda
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

#-----------------------------------------------------------------------------------------------------------------------
def check_play_button(score, aliens, screen, bullets, ship, game_settings, stats, play_button, mouse_x, mouse_y):
    """inicia o jogo quando o jogador clicar em play"""
    if play_button.rect.collidepoint(mouse_x, mouse_y)and(not stats.game_active):#verifica se a posição do click se sobrepõe à pos do botão
        game_settings.initialize_dynamic_settings()                            #dá inicio às velocidades padrões de começo de jogo
        stats.reset_stats()                                                    #reseta os status do jogo
        stats.game_active = True                                               #ativa o jogo
        score.prep_score()
        score.prep_high_score()
        score.prep_level()
        score.prep_ships()
        bullets.empty()                                                        #elimina os projéteis restantes
        ship.center_ship()                                                     #centraliza a nave
        new_chance(game_settings, stats, screen, ship, aliens, bullets, score)
        reset_flags(ship)
        pygame.mouse.set_visible(False)                                        #desabilita o cursor
