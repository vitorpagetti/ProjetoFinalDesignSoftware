import pygame
WHITE = (255,255,255)
class Platform(pygame.sprite.Sprite):#criação das plataformas
    def __init__(self,widht,height):
        super().__init__()
        self.image = pygame.Surface([widht,height])
        self.rect = self.image.get_rect()
        
        self.image.fill(WHITE)