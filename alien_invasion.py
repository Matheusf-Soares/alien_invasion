import sys

import pygame

class AlienInvasion:
    """Classe geral para gerenciar ativos e comportamentos do jogo"""

    def __init__(self):
        """Inicializa o jogo e cria recursos"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Inicia o loop principal do jogo"""
        while True:
            # Observa eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Deixa a última tela mais visível
            pygame.display.flip()

if __name__ == '__main__':
    # Cria uma instância do jogo e a executa
    ai = AlienInvasion()
    ai.run_game()
