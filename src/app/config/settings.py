class Settings:
    def __init__(self):
        # Configurações da tela
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (51, 51, 51)
        self.barrier_width = 5

        # Configurações de jogo
        self.fps = 60
        self.player_speed = 5
        self.opponent_speed = 5
        self.ball_speed = [7, 7]

        # Elementos do jogo
        self.player_width = 10
        self.player_height = 100
        self.opponent_width = 10
        self.opponent_height = 100
        self.ball_width = 30
        self.ball_height = 30
