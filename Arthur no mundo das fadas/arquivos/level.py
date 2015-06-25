import pygame
class Level(): #criação de uma classe pai "level" para podermos criar outros levels em seuigda
    def __init__(self,player):
        self.plataformas = pygame.sprite.Group()#cria grupos em que as sprites sao adicionadas
        self.monstros = pygame.sprite.Group()
        self.backgrounds = pygame.sprite.Group()
        self.moedas = pygame.sprite.Group()    
        self.morreu = pygame.sprite.Group()
        self.asas = pygame.sprite.Group()
        self.player = player
        self.mudar_mundo = 0#define o mundo inicial
        self.level_limit = -1000#define o tamanho do level
    def update(self):#atualiza as sprites na tela
        self.plataformas.update()
        self.monstros.update()
    
    def draw(self,screen):#desenha todas as sprites na tela
        screen.fill(BLACK)
        self.plataformas.draw(screen)    
        self.backgrounds.draw(screen)
        self.monstros.draw(screen)
        self.moedas.draw(screen)
        self.morreu.draw(screen)
        self.asas.draw(screen)
    def shift_world(self, mudar_x):
        '''nosso jogo ao inves de o personagem se mover por todo o cenario a partir de um momento o cenario se move
        contra ele dando a impressao de movimento do persongem'''
        self.mudar_mundo += mudar_x#define a velocidade em que a tela se mexe 
        for platform in self.plataformas:
            platform.rect.x += mudar_x
 
        for monstro in self.monstros:
            monstro.rect.x += mudar_x
        
        for background in self.backgrounds:
            background.rect.x += mudar_x