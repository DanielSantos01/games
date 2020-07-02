import pygame
import sys
from create_functions import create_fleet
from game_functions import change_fleet_direction, ship_hit
from extern_events import check_play_button, check_keydown_events, check_keyup_events

def check_events(game_settings, screen, ship, bullets, stats, play_button, aliens, score):
    """responde a eventos ocorridos nas teclas e no mouse"""
    for event in pygame.event.get():                                           #observa eventos do teclado e do mouse
                                          #SAIR DO JOGO
        if event.type == pygame.QUIT:                                          #se o evento for ocasionado pelo botão de fechar a janela...
            score.save_high_score()
            sys.exit()                                                         #realiza o fechamento da mesma
        elif  event.type == pygame.MOUSEBUTTONDOWN:                            #verifica se houve algum evento de click no mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()                          #devolve uma tupla com as coordenadas x e y do click do mouse
            check_play_button(score, aliens, screen, bullets,ship,game_settings,stats,play_button,mouse_x,mouse_y) #chama a função para verificar se o botão play foi clicado

                                     #FUNÇÕES DA ESPAÇONAVE
        elif event.type == pygame.KEYDOWN:                                     #verifica se uma tecla foi pressionada
            check_keydown_events(event,game_settings,screen,ship,bullets,score)#chama a função de tratamento de teclas pressionadas
        elif event.type == pygame.KEYUP:                                       #verifica se uma tecla foi solta
            check_keyup_events(ship, event)                                    #chama a função de tratamento de teclas soltas

#-----------------------------------------------------------------------------------------------------------------------
def check_aliens_bottom(game_settings, stats, screen, ship, aliens, bullets, score):
    """verifica se algum alienígena alcançou a parte inferior da tela"""
    screen_rect = screen.get_rect()                                             #obtém a área da tela
    for alien in aliens.sprites():                                              #percorre o grupo de aliens
        if alien.rect.bottom >= screen_rect.bottom:                             #verifica se algum alien atingiu a borda de baixo da tela
            ship_hit(game_settings, stats, screen, ship, aliens, bullets, score)#reinicia o jogo
            create_fleet(game_settings, screen, ship, aliens)
            break                                                               #sai do laço
        elif alien.rect.top <= screen_rect.top:
            ship_hit(game_settings, stats, screen, ship, aliens, bullets, score)
            create_fleet(game_settings, screen, ship, aliens)
            break

#-----------------------------------------------------------------------------------------------------------------------
def check_high_score(stats, score):
    """verifica se há uma nova pontuação máxima"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.prep_high_score()

#-----------------------------------------------------------------------------------------------------------------------
def check_bullet_alien_collision(game_settings, screen, ship, aliens, bullets, stats, score):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)       #verifica se houve colisão entre objetos de dois grupos
    if len(aliens) == 0:                                                       #verifica se todos os aliens foram destruídos
        bullets.empty()                                                        #apaga todos os projéteis restantes
        game_settings.increase_speed()                                         #aumenta a velocidade do jogo
        stats.level += 1                                                       #incrementa o nível
        score.prep_level()                                                     #atualiza a renderização do nível
        create_fleet(game_settings, screen, ship, aliens)                      #cria uma nova frota
        ship.center_ship()

    if collisions:                                                             #caso o dict collisions não esteja vazio...
        for aliens in collisions.values():                                     #percorre os valores do dict
            stats.score += (game_settings.alien_points * len(aliens))          #incrementa os pontos
            score.prep_score()                                                 #atualiza o score
        check_high_score(stats, score)                                         #verifica se tem um novo recorde

    # os argumentos True, True em groupcollide dizem que se os dois elementos colidiram, devem ser apagados
    # o retorno do método é um dicionário contendo na chave os objetos bullet e como valor os objetos alien que colidiram
    # para um projétil potente que destruiria mais de 1 alien, poderia ser colocado False, True (ele desapareceria na parte superior da tela)

#-----------------------------------------------------------------------------------------------------------------------
def check_fleet_edges(game_settings, aliens):
    """responde apropriadamente se algum alienígena atingiu uma borda"""
    for alien in aliens.sprites():                                              #percorre o grupo de aliens
        if alien.check_edges():                                                 #verifica se algum tocou alguma borda da tela
            change_fleet_direction(game_settings, aliens)                       #muda a direção e reduz a altura da frota
            break                                                               #sai do laço


