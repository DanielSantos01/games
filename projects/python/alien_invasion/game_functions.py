import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, game_settings, screen, ship, bullets, score):
    """responde a pressionamentos de teclas"""
    if event.key == pygame.K_RIGHT:                                            #verifica se a seta direita foi pressionada
        ship.moving_right = True                                               #habilita a movimentação para a direita
    elif event.key == pygame.K_LEFT:                                           #verifica se a seta para a esquerda foi pressionada
        ship.moving_left = True                                                #habilita a movimentação para a esquerda
    elif event.key == pygame.K_SPACE:                                          #verifica se a tecla espaço foi pressionada
        fire_bullets(game_settings, screen, ship, bullets)                     #chama a função de disparo de projéteis
        ship.shot()
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

#-----------------------------------------------------------------------------------------------------------------------
def check_play_button(score,screen,aliens, bullets, ship, game_settings, stats, play_button, mouse_x, mouse_y):
    """inicia o jogo quando o jogador clicar em play"""
    if play_button.rect.collidepoint(mouse_x, mouse_y)and(not stats.game_active):#verifica se a posição do click se sobrepõe à pos do botão
        stats.reset_stats()                                                    #carrega as novas chances do jogador
        game_settings.initialize_dynamic_settings()                            #dá inicio às velocidades padrões de começo de jogo
        stats.reset_stats()                                                    #reseta os status do jogo
        stats.game_active = True                                               #ativa o jogo
        score.prep_score()
        score.prep_high_score()
        score.prep_level()
        score.prep_ships()
        aliens.empty()
        bullets.empty()                                                        #elimina os projéteis restantes
        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()                                                     #centraliza a nave
        pygame.mouse.set_visible(False)                                        #desabilita o cursor

#-----------------------------------------------------------------------------------------------------------------------
def check_events(game_settings, screen, ship, bullets, stats, play_button, aliens, score):
    """responde a eventos ocorridos nas teclas e no mouse"""
    for event in pygame.event.get():                                           #observa eventos do teclado e do mouse
                                          #SAIR DO JOGO
        if event.type == pygame.QUIT:                                          #se o evento for ocasionado pelo botão de fechar a janela...
            score.save_high_score()
            sys.exit()                                                         #realiza o fechamento da mesma
        elif  event.type == pygame.MOUSEBUTTONDOWN:                            #verifica se houve algum evento de click no mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()                          #devolve uma tupla com as coordenadas x e y do click do mouse
            check_play_button(score,screen,aliens,bullets,ship,game_settings,stats,play_button,mouse_x,mouse_y)

                                     #FUNÇÕES DA ESPAÇONAVE
        elif event.type == pygame.KEYDOWN:                                     #verifica se uma tecla foi pressionada
            check_keydown_events(event,game_settings,screen,ship,bullets,score)#chama a função de tratamento de teclas pressionadas
        elif event.type == pygame.KEYUP:                                       #verifica se uma tecla foi solta
            check_keyup_events(ship, event)                                    #chama a função de tratamento de teclas soltas

#-----------------------------------------------------------------------------------------------------------------------
def update_screen(game_settings, screen, ship, aliens, bullets, stats, play_button, score):
    """Realiza a atualização dos frames"""
    screen.fill(game_settings.bg_color)                                        #redesenha a tela a cada ciclo com uma cor específica
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

    check_bullet_alien_collision(game_settings, screen, ship, aliens, bullets, stats, score) #verifica se o projétil atingiu algum alien

#-----------------------------------------------------------------------------------------------------------------------
def check_bullet_alien_collision(game_settings, screen, ship, aliens, bullets, stats, score):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)       #verifica se houve colisão entre objetos de dois grupos
    if len(aliens) == 0:                                                       #verifica se todos os aliens foram destruídos
        bullets.empty()                                                        #apaga todos os projéteis restantes
        game_settings.increase_speed()                                         #aumenta a velocidade do jogo
        stats.level += 1                                                       #incrementa o nível
        score.prep_level()                                                     #atualiza a renderização do nível
        create_fleet(game_settings, screen, ship, aliens)                      #cria uma nova frota

    if collisions:                                                             #caso o dict collisions não esteja vazio...
        game_settings.flag = True
        for aliens in collisions.values():                                     #percorre os valores do dict
            stats.score += (game_settings.alien_points * len(aliens))          #incrementa os pontos
            score.prep_score()                                                 #atualiza o score
            #aliens[0].shot_down()
        check_high_score(stats, score)                                         #verifica se tem um novo recorde

    # os argumentos True, True em groupcollide dizem que se os dois elementos colidiram, devem ser apagados
    # o retorno do método é um dicionário contendo na chave os objetos bullet e como valor os objetos alien que colidiram
    # para um projétil potente que destruiria mais de 1 alien, poderia ser colocado False, True (ele desapareceria na parte superior da tela)

#-----------------------------------------------------------------------------------------------------------------------
def fire_bullets(game_settings, screen, ship, bullets):                        #cria um novo projétil e o adiciona ao grupo de projéteis
    if len(bullets) < game_settings.bullets_allowed:                           #verifica se o número de projéteis não ultrapassa o permitido
        new_bullet = Bullet(game_settings, screen, ship)                       #cria um novo projétil
        bullets.add(new_bullet)                                                #adiciona o novo projétil ao grupo/lista de projéteis

#-----------------------------------------------------------------------------------------------------------------------
def get_number_aliens_x(game_settings, alien_width):
    available_space_x = game_settings.screen_width - 2 * alien_width           #obtém, através de cálculo, o espaço disponível para aliens
    number_alien_x = int(available_space_x / (2 * alien_width))                #obtém, através de cálculo, quantos aliens cabem no espaço
    return number_alien_x

#-----------------------------------------------------------------------------------------------------------------------
def get_number_rows(game_settings, ship_height, alien_height):
    """determina o número de linhas com alienígenas que cabem na tela"""
    available_space_y = game_settings.screen_height-(3*alien_height)-ship_height
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

#-----------------------------------------------------------------------------------------------------------------------
def create_alien(game_settings, screen, aliens, alien_number, row_number):
    alien = Alien(game_settings, screen)                                       #cria um novo alien
    alien_width = alien.rect.width                                             #obtém a largura do alien
    alien.x = alien_width + (2 * alien_width * alien_number)                   #define a posição x de cada alien
    alien.rect.x = alien.x                                                     #passa a posição x calculada para o rect do objeto
    alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)    #define a posição y de cada alien
    aliens.add(alien)                                                          #adiciona o objeto à lista

#-----------------------------------------------------------------------------------------------------------------------
def create_fleet(game_settings, screen, ship, aliens):
    """cria uma frota completa de alienígenas"""
    alien = Alien(game_settings, screen)                                       #cria um alienígena apenas para pegar suas dimensões
    number_alien_x = get_number_aliens_x(game_settings, alien.rect.width)      #recebe o número possível de aliens em uma linha
    number_rows = get_number_rows(game_settings, ship.rect.height, alien.rect.height)

    for row_number in range (number_rows):
        for alien_number in range(number_alien_x):                              #percorre de 0 até o núemro calculado de alienígenas
            create_alien(game_settings,screen,aliens, alien_number, row_number) #realiza a criação da frota de aliens

#-----------------------------------------------------------------------------------------------------------------------
def update_aliens(game_settings, stats, screen, ship, aliens, bullets, score):
    """verifica se a frota está em uma das bordas e então atualiza sua posição"""
    check_fleet_edges(game_settings, aliens)                                    #verifica se algum objeto tocou a borda
    aliens.update()                                                             #atualiza a posição dos aliens
    if pygame.sprite.spritecollideany(ship, aliens):                            #verifica se houve colisão entre a nave e algum alien
        ship_hit(game_settings, stats, screen, ship, aliens, bullets, score)    #reinicia o jogo pois a nave foi atingida
    check_aliens_bottom(game_settings,stats,screen,ship,aliens,bullets,score)   #vrifica se algum alien atingiu a borda de baixo da tela

                   #o método spritecollideany aceia dois argumentos: um srpite (ship) e um grupo (aliens)

#-----------------------------------------------------------------------------------------------------------------------
def check_fleet_edges(game_settings, aliens):
    """responde apropriadamente se algum alienígena atingiu uma borda"""
    for alien in aliens.sprites():                                              #percorre o grupo de aliens
        if alien.check_edges():                                                 #verifica se algum tocou alguma borda da tela
            change_fleet_direction(game_settings, aliens)                       #muda a direção e reduz a altura da frota
            break                                                               #sai do laço

#-----------------------------------------------------------------------------------------------------------------------
def change_fleet_direction(game_settings, aliens):
    """faz toda a frota descer e mudar sua direção"""
    for alien in aliens.sprites():                                              #percorre o grupo de aliens
        alien.rect.y += game_settings.fleet_drop_speed                          #aumenta a posição y de cada alien, fazendo-os descer
    game_settings.fleet_direction *= -1                                         #muda a direção do movimento

#-----------------------------------------------------------------------------------------------------------------------
def ship_hit(game_settings, stats, screen, ship, aliens, bullets, score):
    """responde se uma espaçonave foi atingida por um alienígena"""
    if stats.ships_left > 0:                                                    #analisa se o jogador ainda tem alguma chance
        stats.ships_left -= 1                                                   #diminui uma chance
        score.prep_ships()                                                      #atualiza na tela  numero de naves
        aliens.empty()                                                          #alimina os aliens restantes na tela
        bullets.empty()                                                         #elimina os projéteis restantes na tela
        create_fleet(game_settings, screen, ship, aliens)                       #cria uma nova frota
        ship.center_ship()                                                      #centraliza a nave
        sleep(0.5)                                                              #espera 0.5s
    else:
        stats.game_active = False                                               #desabilita o jogo
        pygame.mouse.set_visible(True)                                          #habilita o cursor

#-----------------------------------------------------------------------------------------------------------------------
def check_aliens_bottom(game_settings, stats, screen, ship, aliens, bullets, score):
    """verifica se algum alienígena alcançou a parte inferior da tela"""
    screen_rect = screen.get_rect()                                             #obtém a área da tela
    for alien in aliens.sprites():                                              #percorre o grupo de aliens
        if alien.rect.bottom >= screen_rect.bottom:                             #verifica se algum alien atingiu a borda de baixo da tela
            ship_hit(game_settings, stats, screen, ship, aliens, bullets, score)#reinicia o jogo
            break                                                               #sai do laço

#-----------------------------------------------------------------------------------------------------------------------
def check_high_score(stats, score):
    """verifica se há uma nova pontuação máxima"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.prep_high_score()

