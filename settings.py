class Settings:
    """Classe para armazenar as configurações do Jogo Invasão Alienígena"""

    def __init__(self):
        """Inicializa as configurações do jogo"""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configurações da nave
        self.ship_limit = 3

        # Configuração de projétil
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Configuração do alienígena
        self.fleet_drop_speed = 10

        # A rapidez com que o jogo acelera
        self.score_scale = 1.5
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializa as configurações que mudam ao longo do jogo"""
        self.ship_speed = 2.0
        self.bullet_speed = 4.0
        self.alien_speed = 1.0

        # fleet_direction de 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1

        # Configurações de pontuação
        self.alien_points = 50

    def increase_speed(self):
        """Aumenta as configurações de velocidade"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
