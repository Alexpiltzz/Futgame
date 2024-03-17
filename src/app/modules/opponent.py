class Opponent:
    def __init__(self, settings):
        self.settings = settings
        self.position = [
            self.settings.screen_width - 50,
            self.settings.screen_height // 2 - 50,
        ]

    def move(self, ball_position):
        # Movimento do oponente (IA)
        if (
            self.position[1] + self.settings.opponent_height // 2
            < ball_position[1] + self.settings.ball_height // 2
        ):
            self.position[1] += self.settings.opponent_speed
        elif (
            self.position[1] + self.settings.opponent_height // 2
            > ball_position[1] + self.settings.ball_height // 2
        ):
            self.position[1] -= self.settings.opponent_speed

        # Impede que o oponente saia da tela
        self.position[1] = max(
            0,
            min(
                self.settings.screen_height - self.settings.opponent_height,
                self.position[1],
            ),
        )
