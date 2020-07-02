
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

