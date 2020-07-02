from alien import Alien
from getters_functions import get_number_aliens_x, get_number_rows

def create_fleet(game_settings, screen, ship, aliens):
    """cria uma frota completa de alienígenas"""
    alien = Alien(game_settings, screen)                                       #cria um alienígena apenas para pegar suas dimensões
    number_alien_x = get_number_aliens_x(game_settings, alien.rect.width)      #recebe o número possível de aliens em uma linha
    number_rows = get_number_rows(game_settings, ship.rect.height, alien.rect.height)
    for row_number in range (number_rows):
        for alien_number in range(number_alien_x):                              #percorre de 0 até o núemro calculado de alienígenas
            create_alien(game_settings,screen,aliens, alien_number, row_number) #realiza a criação da frota de aliens

#-----------------------------------------------------------------------------------------------------------------------
def create_alien(game_settings, screen, aliens, alien_number, row_number):
    alien = Alien(game_settings, screen)                                       #cria um novo alien
    alien_width = alien.rect.width                                             #obtém a largura do alien
    alien.x = alien_width + (2 * alien_width * alien_number)                   #define a posição x de cada alien
    alien.rect.x = alien.x                                                     #passa a posição x calculada para o rect do objeto
    if game_settings.flag_direction == 1:
        alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)#define a posição y de cada alien
    else:
        alien.rect.y = (6*alien.rect.height) + (2 * alien.rect.height * row_number)
    aliens.add(alien)                                                          #adiciona o objeto à lista
