import pygame

class Ship:
    """Classe para cuidar da espaçonave"""

    def __init__(self, ai_game):
        """Inicializa a espaçonave e define sua posição inicial"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Sobe a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Começa cada espaçonave nova no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # Flag de movimento -> Começa com uma nave que não está se movendo
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualiza a posição da nave com base na flag de movimento"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Desenha a espaçonave em sua localização atual"""
        self.screen.blit(self.image, self.rect)
