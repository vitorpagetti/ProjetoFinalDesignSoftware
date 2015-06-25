import pygame
class Asas_de_fada(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('imagens/fada.png')
        self.rect = self.image.get_rect()