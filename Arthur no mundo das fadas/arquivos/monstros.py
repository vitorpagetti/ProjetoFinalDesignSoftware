import pygame
class Monstros(pygame.sprite.Sprite):
    '''como os monstros serão os mesmos nao é necessário colocar as sprites no init'''
    def __init__(self,limite):
        super().__init__()
        self.image = pygame.image.load('imagens/MD.png')
        self.rect = self.image.get_rect()
        self.limitemax = self.rect.x + limite#cria o movimento dos monstros
        self.limitemin = self.rect.x - limite
        self.change_y = 0
        self.change_x = 2
    def update(self):
        
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.right < 0:
            self.change_x = 0
        if self.rect.x == self.limitemax:#movimento do monstro para esquerda
            self.change_x = - 2
        if self.rect.x == self.limitemin:#movimento do monstro para direita
            self.change_x = 2
        if self.change_x > 0:
            if self.rect.x % 1.5 != 0:
                self.image = pygame.image.load('imagens/MD.png')
            if self.rect.x % 1.5 == 0:
                self.image = pygame.image.load('imagens/MD2.png')
        if self.change_x < 0:
            if self.rect.x % 1.5 != 0:
                self.image = pygame.image.load('imagens/ME.png')
            if self.rect.x % 1.5 == 0:
                self.image = pygame.image.load('imagens/ME2.png')