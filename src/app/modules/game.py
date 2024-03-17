import pygame
import sys
from config.settings import Settings
from modules.renderer import Renderer
from modules.ball import Ball
from modules.player import Player
from modules.opponent import Opponent


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

        # Inicialização dos objetos
        self.player = Player(self.settings)
        self.opponent = Opponent(self.settings)
        self.ball = Ball(self.settings)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Adicionar funcionalidade de pausar o jogo
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.pause_game()

    def pause_game(self):
        # Pausar o jogo
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False
            pygame.display.update()

    def move_ball(self):
        self.ball.move()

        # Verificar a colisão com o jogador e o oponente
        if self.ball.check_collision_with_player(
            self.player
        ) or self.ball.check_collision_with_opponent(self.opponent):
            self.settings.ball_speed[0] *= -1

        # Verificar se houve gol
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
            self.player.move()
            self.opponent.move(self.ball.position)
            self.move_ball()
            Renderer.draw_elements(
                self.screen,
                self.settings,
                self.player.position,
                self.opponent.position,
                self.ball.position,
                self.player_score,
                self.opponent_score,
            )


if __name__ == "__main__":
    game = PingPongGame()
    game.run_game()
