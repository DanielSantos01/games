class GameStats():
    """armazena dados estatísticos do jogo"""

    def __init__(self, game_settings):
        self.game_settings = game_settings                                 #obtém as configurações do jogo
        self.reset_stats()                                                 #atualiza as chances do jogador
        self.game_active = False                                           #estado inicial do jogo
        with open('highscore.json') as file:
            self.high_score = int(file.read())

    #-------------------------------------------------------------------------------------------------------------------
    def reset_stats(self):
        """inicializa dados estatísticos que podem mudar durante o jogo"""
        self.ships_left = self.game_settings.ship_limit
        self.score = 0
        self.level = 1