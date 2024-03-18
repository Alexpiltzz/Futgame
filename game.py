import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
GOAL_WIDTH = 100
GOAL_HEIGHT = 200
GOAL_LINE = WIDTH - GOAL_WIDTH

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Configurações do jogador e da bola
PLAYER_SIZE = 50
BALL_SIZE = 20

# Velocidade do jogador e da bola
PLAYER_SPEED = 0.2
BALL_SPEED_X = 0.2
BALL_SPEED_Y = 0.1

# Criando a tela do jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Futebol")


# Função para desenhar o jogador
def draw_player(x, y):
    pygame.draw.rect(screen, RED, (x, y, PLAYER_SIZE, PLAYER_SIZE))


# Função para desenhar a bola
def draw_ball(x, y):
    pygame.draw.circle(screen, BLUE, (x, y), BALL_SIZE)


# Função principal do jogo
def main():
    # Posição inicial do jogador
    player_x = 50
    player_y = HEIGHT // 2 - PLAYER_SIZE // 2

    # Posição inicial da bola
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2

    # Velocidade inicial da bola
    ball_speed_x = BALL_SPEED_X
    ball_speed_y = BALL_SPEED_Y

    while True:
        screen.fill(WHITE)

        # Lidando com eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimento do jogador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            player_y += PLAYER_SPEED

        # Verificando se a bola bateu na parede ou no jogador
        if ball_x <= 0 or ball_x >= WIDTH:
            ball_speed_x *= -1
        if ball_y <= 0 or ball_y >= HEIGHT:
            ball_speed_y *= -1
        if (
            ball_x <= player_x + PLAYER_SIZE
            and ball_y >= player_y
            and ball_y <= player_y + PLAYER_SIZE
        ):
            ball_speed_x *= -1

        # Movimento da bola
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Desenhando os elementos na tela
        draw_player(player_x, player_y)
        draw_ball(ball_x, ball_y)

        # Desenhando o gol
        pygame.draw.rect(
            screen,
            BLACK,
            (GOAL_LINE, (HEIGHT - GOAL_HEIGHT) // 2, GOAL_WIDTH, GOAL_HEIGHT),
            2,
        )

        pygame.display.flip()


if __name__ == "__main__":
    main()
