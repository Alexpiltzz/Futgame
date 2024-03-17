import pygame
import sys
from config.settings import Settings
from modules.renderer import Renderer
from modules.ball import Ball
from modules.player import Player
from modules.player2 import Player2
from modules.opponent import Opponent


class Menu:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()

        # Inicialização dos objetos
        self.player = Player(self.settings)
        self.player2 = Player2(self.settings)  # Adicionando um jogador 2
        self.opponent = Opponent(self.settings)
        self.ball = Ball(self.settings)

    def draw_menu(self):
        while True:
            self.screen.fill((0, 0, 0))
            title = self.font.render("Ping Pong Challenge", True, (255, 255, 255))
            title_rect = title.get_rect(center=(self.settings.screen_width // 2, 100))
            self.screen.blit(title, title_rect)

            one_player = self.font.render("1v1 - Press '1'", True, (255, 255, 255))
            one_player_rect = one_player.get_rect(
                center=(self.settings.screen_width // 2, 300)
            )
            self.screen.blit(one_player, one_player_rect)

            against_computer = self.font.render(
                "Against Computer - Press '2'", True, (255, 255, 255)
            )
            against_computer_rect = against_computer.get_rect(
                center=(self.settings.screen_width // 2, 400)
            )
            self.screen.blit(against_computer, against_computer_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        return "1v1"
                    elif event.key == pygame.K_2:
                        return "against_computer"
            self.clock.tick(30)


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
        self.player = Player(self.settings)
        self.player2 = None
        self.opponent = Player2(self.settings)
        self.ball = Ball(self.settings)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def move_ball(self):
        self.ball.move()

        # Colisão com as raquetes (jogador e oponente)
        if (
            self.ball.check_collision_with_player(
                self.player.position,
                self.settings.player_width,
                self.settings.player_height,
            )
            or (
                self.player2
                and self.ball.check_collision_with_player(
                    self.player2.position,
                    self.settings.player_width,
                    self.settings.player_height,
                )
            )
            or self.ball.check_collision_with_opponent(
                self.opponent.position,
                self.settings.opponent_width,
                self.settings.opponent_height,
            )
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
        menu = Menu(self.screen, self.settings)
        game_mode = menu.draw_menu()

        if game_mode == "1v1":
            self.player2 = Player2(self.settings)

        clock = pygame.time.Clock()

        while True:
            clock.tick(self.settings.fps)
            self.handle_events()
            self.player.move()
            if self.player2:
                self.player2.move()
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
                game_mode,  # Adicione o modo de jogo aqui
            )


if __name__ == "__main__":
    game = PingPongGame()
    game.run_game()
