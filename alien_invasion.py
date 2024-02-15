import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Classe geral para gerenciar ativos e comportamentos do jogo"""

    def __init__(self):
        """Inicializa o jogo e cria recursos"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.clock = pygame.time.Clock()


    def run_game(self):
        """Inicia o loop principal do jogo"""
        while True:
            # Observa eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redesenha a tela durante cada passagem pelo loop
            self.screen.fill(self.settings.bg_color)

            # Deixa a tela mais recente desenhada visível
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Cria uma instância do jogo e a executa
    ai = AlienInvasion()
    ai.run_game()
