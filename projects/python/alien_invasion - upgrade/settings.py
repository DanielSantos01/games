class Settings():
    """Classe para armazenar as configurações da invasão alienígena"""
    def __init__(self):
                                             #configurações da tela
        self.screen_width = 1000                                         #largura da tela
        self.screen_height = 600                                         #altura da tela
        self.screen_dimension = (self.screen_width, self.screen_height)  #dimensão da tela (largura X altura)
        self.bg_color = (205, 127, 50)                                   #cor de fundo da tela

                                           #configuraçoes da espaçonave
        self.ship_speed_factor = 1.5                                     #define o fator de velocidade da espaçonave (decimal = precisão)
        self.ship_limit = 3

                                           #configurações dos projéteis
        self.bullet_speed_factor = 3                                     #define o fator de velocidade do projétil
        self.bullet_width = 3                                            #define a largura do projétil
        self.bullet_height = 15                                          #define a altura do projétil
        self.bullet_color = (255, 0, 0)                                 #define a tupla com a cor do projétil
        self.bullets_allowed = 3                                         #define a quantidade permitida de projéteis na tela
                                           #Configurações dos alienígenas
        self.alien_speed_factor = 1                                      #fator de velocidade dos alienígenas
        self.fleet_drop_speed = 10                                       #velocidade de queda dos alienígenas
        self.fleet_direction = 1                                         #direção da frota (1 = direita, -1 = esquerda)

        self.speedup_scale = 1.1                                         #taxa de variação da velocidade
        self.score_scale = 1.5                                           #taxa de variação dos pontos
        self.initialize_dynamic_settings()
        self.flag_direction = 1

    def initialize_dynamic_settings(self):
        """inicializa as configurações que mudam no decorrer do jogo"""
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 7
        self.alien_speed_factor = 1.5
        self.fleet_direction = 2
        self.alien_points = 50

    def increase_speed(self):
        """aumenta as configurações de velocidade"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)





