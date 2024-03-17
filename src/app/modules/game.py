import pygame
import sys
from config.settings import Settings
from modules.renderer import Renderer
from modules.ball import Ball


class PingPongGame:
    def __init__(self):
        # Inicialização do Pygame
        pygame.init()

        # Configurações do jogo
        self.settings = Settings()

        # Configuração da tela do jogo
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Ping Pong Challenge")

        # Variáveis do jogo
        self.player_score = 0
        self.opponent_score = 0

        # Posições iniciais
        self.player_position = [50, self.settings.screen_height // 2 - 50]
        self.opponent_position = [
            self.settings.screen_width - 50,
            self.settings.screen_height // 2 - 50,
        ]
        self.ball = Ball(self.settings)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def move_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player_position[1] -= self.settings.player_speed
        if keys[pygame.K_s]:
            self.player_position[1] += self.settings.player_speed

        # Impede que o jogador saia da tela
        self.player_position[1] = max(
            0,
            min(
                self.settings.screen_height - self.settings.player_height,
                self.player_position[1],
            ),
        )

    def move_opponent(self):
        # Movimento do oponente (IA)
        if (
            self.opponent_position[1] + self.settings.opponent_height // 2
            < self.ball.position[1] + self.settings.ball_height // 2
        ):
            self.opponent_position[1] += self.settings.opponent_speed
        elif (
            self.opponent_position[1] + self.settings.opponent_height // 2
            > self.ball.position[1] + self.settings.ball_height // 2
        ):
            self.opponent_position[1] -= self.settings.opponent_speed

        # Impede que o oponente saia da tela
        self.opponent_position[1] = max(
            0,
            min(
                self.settings.screen_height - self.settings.opponent_height,
                self.opponent_position[1],
            ),
        )

    def move_ball(self):
        self.ball.move()

        # Colisão com as raquetes (jogador e oponente)
        if (
            self.player_position[0]
            <= self.ball.position[0] + self.settings.ball_width
            <= self.player_position[0] + self.settings.player_width
            and self.player_position[1]
            <= self.ball.position[1] + self.settings.ball_height
            <= self.player_position[1] + self.settings.player_height
        ) or (
            self.opponent_position[0]
            <= self.ball.position[0]
            <= self.opponent_position[0] + self.settings.opponent_width
            and self.opponent_position[1]
            <= self.ball.position[1]
            <= self.opponent_position[1] + self.settings.opponent_height
        ):
            self.settings.ball_speed[0] *= -1

        # Verifica se a bola marcou gol
        if self.ball.position[0] <= 0:
            self.opponent_score += 1
            self.reset_ball()
        elif (
            self.ball.position[0]
            >= self.settings.screen_width - self.settings.ball_width
        ):
            self.player_score += 1
            self.reset_ball()

    def reset_ball(self):
        self.ball.reset()

    def run_game(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(self.settings.fps)
            self.handle_events()
            self.move_player()
            self.move_opponent()
            self.move_ball()
            Renderer.draw_elements(
                self.screen,
                self.settings,
                self.player_position,
                self.opponent_position,
                self.ball.position,
                self.player_score,
                self.opponent_score,
            )
