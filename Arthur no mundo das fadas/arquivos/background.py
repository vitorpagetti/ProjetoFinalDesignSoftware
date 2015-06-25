import pygame
class Background(pygame.sprite.Sprite):#criação do fundo que é uma sprite sem mecanica
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('imagens/background.jpg')#define a tela do jogo
        self.rect = self.image.get_rect()
        self.rect.x = 0#posiçao x inicial da tela
        self.rect.y = 0#posiçao y inicial da tela
