from time import sleep
import pygame
from create_functions import create_fleet
from bullet import Bullet

#-----------------------------------------------------------------------------------------------------------------------
def change_fleet_direction(game_settings, aliens):
    """faz toda a frota descer e mudar sua direção"""
    for alien in aliens.sprites():                                              #percorre o grupo de aliens
        if game_settings.flag_direction == 1:
            alien.rect.y += game_settings.fleet_drop_speed                      #aumenta a posição y de cada alien, fazendo-os descer
        else:
            alien.rect.y -= game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1                                         #muda a direção do movimento

#-----------------------------------------------------------------------------------------------------------------------
def ship_hit(game_settings, stats, screen, ship, aliens, bullets, score):
    """responde se uma espaçonave foi atingida por um alienígena"""
    if stats.ships_left > 0:                                                    #analisa se o jogador ainda tem alguma chance
        new_chance(game_settings, stats, screen, ship, aliens, bullets, score)  #espera 0.5s
    else:
        stats.game_active = False                                               #desabilita o jogo
        pygame.mouse.set_visible(True)                                          #habilita o cursor

#-----------------------------------------------------------------------------------------------------------------------
def fire_bullets(game_settings, screen, ship, bullets):                        #cria um novo projétil e o adiciona ao grupo de projéteis
    if len(bullets) < game_settings.bullets_allowed:                           #verifica se o número de projéteis não ultrapassa o permitido
        new_bullet = Bullet(game_settings, screen, ship)                       #cria um novo projétil
        bullets.add(new_bullet)

#-----------------------------------------------------------------------------------------------------------------------
def rotate_image(ship):
    angle = 180;
    rotated_image = pygame.transform.rotate(ship.image, angle)
    ship.image = rotated_image
    ship.blitme()
    pygame.display.flip()

#-----------------------------------------------------------------------------------------------------------------------
def new_chance(game_settings, stats, screen, ship, aliens, bullets, score):
    stats.ships_left -= 1
    score.ships.empty()
    aliens.empty()
    bullets.empty()
    score.prep_ships()
    create_fleet(game_settings, screen, ship, aliens)
    ship.center_ship()
    reset_flags(ship)
    sleep(0.5)

def reset_flags(ship):
    ship.moving_left = False
    ship.moving_right = False
    ship.moving_up = False
    ship.moving_donwn = False
