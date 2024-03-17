import pygame


class Renderer:
    @staticmethod
    def draw_elements(
        screen,
        settings,
        player_position,
        opponent_position,
        ball_position,
        player_score,
        opponent_score,
        game_mode,
    ):

        screen.fill(settings.bg_color)

        # Desenha a barra divisória
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (
                settings.screen_width // 2 - settings.barrier_width // 2,
                0,
                settings.barrier_width,
                settings.screen_height,
            ),
        )

        # Desenha os jogadores e a bola
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (
                player_position[0],
                player_position[1],
                settings.player_width,
                settings.player_height,
            ),
        )
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (
                opponent_position[0],
                opponent_position[1],
                settings.opponent_width,
                settings.opponent_height,
            ),
        )
        pygame.draw.ellipse(
            screen,
            (255, 255, 255),
            (
                ball_position[0],
                ball_position[1],
                settings.ball_width,
                settings.ball_height,
            ),
        )

        # Exibe os pontos dos jogadores
        font = pygame.font.SysFont(None, 36)
        player_score_text = font.render(
            f"Player Score: {player_score}", True, (255, 255, 255)
        )
        opponent_score_text = font.render(
            f"Opponent Score: {opponent_score}", True, (255, 255, 255)
        )
        screen.blit(player_score_text, (20, 20))
        screen.blit(
            opponent_score_text,
            (settings.screen_width - opponent_score_text.get_width() - 20, 20),
        )

        pygame.display.update()
