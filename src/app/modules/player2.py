import pygame


class Player2:
    def __init__(self, settings):
        self.settings = settings
        self.width = self.settings.player_width
        self.height = self.settings.player_height
        self.position = [settings.screen_width - 50, settings.screen_height // 2 - 50]
        self.speed = settings.player_speed

    def move(self, ball_position):
        if ball_position[1] < self.position[1] + self.height / 2:
            self.position[1] -= self.speed
        elif ball_position[1] > self.position[1] + self.height / 2:
            self.position[1] += self.speed

        # Impede que o jogador saia da tela
        self.position[1] = max(
            0,
            min(
                self.settings.screen_height - self.height,
                self.position[1],
            ),
        )

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            pygame.Rect(self.position[0], self.position[1], self.width, self.height),
        )
