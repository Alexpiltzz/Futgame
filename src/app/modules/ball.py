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

    def check_collision_with_player(self, player_position, player_width, player_height):
        return (
            player_position[0]
            <= self.position[0] + self.settings.ball_width
            <= player_position[0] + player_width
            and player_position[1]
            <= self.position[1] + self.settings.ball_height
            <= player_position[1] + player_height
        )

    def check_collision_with_opponent(
        self, opponent_position, opponent_width, opponent_height
    ):
        return (
            opponent_position[0]
            <= self.position[0]
            <= opponent_position[0] + opponent_width
            and opponent_position[1]
            <= self.position[1]
            <= opponent_position[1] + opponent_height
        )
