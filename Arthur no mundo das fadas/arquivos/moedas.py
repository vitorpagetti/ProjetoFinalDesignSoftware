import pygame
class Moedas(pygame.sprite.Sprite):#cria as sprites de moeda
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('imagens/moeda.png')
        self.rect = self.image.get_rect()