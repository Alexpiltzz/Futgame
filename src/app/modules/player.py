import pygame


class Player:
    def __init__(self, settings):
        self.settings = settings
        self.position = [50, self.settings.screen_height // 2 - 50]

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.position[1] -= self.settings.player_speed
        if keys[pygame.K_s]:
            self.position[1] += self.settings.player_speed

        # Impede que o jogador saia da tela
        self.position[1] = max(
            0,
            min(
                self.settings.screen_height - self.settings.player_height,
                self.position[1],
            ),
        )
