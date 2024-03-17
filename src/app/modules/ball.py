class Ball:
    def __init__(self, settings):
        self.settings = settings
        self.reset()

    def move(self):
        self.position[0] += self.settings.ball_speed[0]
        self.position[1] += self.settings.ball_speed[1]

        # Colisão com as bordas superior e inferior
        if (
            self.position[1] <= 0
            or self.position[1]
            >= self.settings.screen_height - self.settings.ball_height
        ):
            self.settings.ball_speed[1] *= -1

    def reset(self):
        self.position = [
            self.settings.screen_width // 2 - self.settings.ball_width // 2,
            self.settings.screen_height // 2 - self.settings.ball_height // 2,
        ]
