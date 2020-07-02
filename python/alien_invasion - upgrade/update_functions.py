import pygame
from game_functions import ship_hit
from create_functions import create_fleet
from check_functions import check_fleet_edges, check_aliens_bottom
from check_functions import check_aliens_bottom, check_high_score, check_bullet_alien_collision

def update_aliens(game_settings, stats, screen, ship, aliens, bullets, score):
    """verifica se a frota está em uma das bordas e então atualiza sua posição"""
    check_fleet_edges(game_settings, aliens)                                    #verifica se algum objeto tocou a borda
    aliens.update()                                                             #atualiza a posição dos aliens
    if pygame.sprite.spritecollideany(ship, aliens):                            #verifica se houve colisão entre a nave e algum alien
        ship_hit(game_settings, stats, screen, ship, aliens, bullets, score)    #reinicia o jogo pois a nave foi atingida
        create_fleet(game_settings, screen, ship, aliens)
    check_aliens_bottom(game_settings, stats, screen, ship, aliens, bullets, score)    #vrifica se algum alien atingiu a borda de baixo da tela

                   #o método spritecollideany aceia dois argumentos: um srpite (ship) e um grupo (aliens)

#-----------------------------------------------------------------------------------------------------------------------
def update_screen(game_settings, screen, ship, aliens, bullets, stats, play_button, score, background):
    """Realiza a atualização dos frames"""
    background = pygame.transform.scale(background, game_settings.screen_dimension)
    screen.blit(background, (0, 0))
    for bullet in bullets.sprites():                                           #retorna e percorre todos os sprites de bullets
        bullet.draw_bullet()                                                   #desenha na tela o projétil disparado
    ship.blitme()                                                              #desenha a espaçonave no local especificado em sua classe
    aliens.draw(screen)                                                        #desenha o alienígena na tela
    score.prep_score()                                                         #atualiza o valor do score
    score.show_score()                                                         #mostra o valor atualizado na tela
    if not stats.game_active:                                                  #verifica se o jogo não está ativo
        play_button.draw_button()                                              #mostra o botão play
    pygame.display.flip()                                                      #deixa a tela mais recente visível

#-----------------------------------------------------------------------------------------------------------------------
def update_bullets(game_settings, screen, ship, bullets, aliens, stats, score):
    """atualiza a posição dos projéteis e se livra dos projéteis antigos"""
    bullets.update()                                                           #atualiza a posição do projéteis
    for bullet in bullets.copy():                                              #percorre uma cópia da lista em vez da lista em si
        if bullet.rect.bottom <= 0:                                            #verifica se o projétil já está fora da tela
            bullets.remove(bullet)                                             #remove o projetil não visível (poupa processamento)
        elif bullet.rect.bottom >= screen.get_rect().bottom:
            bullets.remove(bullet)

    check_bullet_alien_collision(game_settings, screen, ship, aliens, bullets, stats, score) #verifica se o projétil atingiu algum alien



