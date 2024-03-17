import os
from modules.game import PingPongGame


def clear_terminal():
    # Limpa o terminal dependendo do sistema operacional
    os.system("cls" if os.name == "nt" else "clear")


def close_terminal():
    # Fecha o terminal dependendo do sistema operacional
    os.system("exit" if os.name == "nt" else "exit")


if __name__ == "__main__":
    clear_terminal()  # Limpa o terminal antes de iniciar o jogo
    game = PingPongGame()
    game.run_game()
    close_terminal()  # Fecha o terminal após o término do jogo
