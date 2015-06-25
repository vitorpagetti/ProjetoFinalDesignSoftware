import pygame
janela_height = 600
janela_widht = 800
class Player(pygame.sprite.Sprite):#aqui construimos os comandos e mecanica do player por meio de uma classe

    '''pygame.sprite.Sprite é usado para chamarmos essa classe que vem na biblioteca pygame. Com ela,
    conseguimos definir a classe desejada como sprite e atribuir funçoes ja criadas para ela. Caso essa classe pai
    nao seja chamada , fica impossivel de plotar objetos na tela e atualiza-la para dar sensação de movimento'''
    def __init__(self):
        super().__init__()#inicia na classe player o init de sprite.Sprite
        
        self.image = pygame.image.load('imagens/AD.png')#define a imagem inicial da classe player
        self.rect = self.image.get_rect()#transforma a imagem em um retangulo. Com isso, podemos usar funçoes especificas de retangulos
        
        self.change_x = 0#atribui o valor inicial do movimento do personagem no eixo X
        self.change_y = 0#mesma coisa so que para o eixo Y
    def direita(self):#boneco vai para direita
        self.change_x = 4
    def esquerda(self):#boneco vai para esquerda
        self.change_x = -4
    def pular(self):#boneco pula
    
        self.rect.y += 2#caso isso nao seja feito o player nao pula.
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.plataformas, False)#checa colisão entre o player e as plataformas
        self.rect.y -= 2#caso isso nao seja feito o player é teleportado para sua posição inicial na tela
 

        if len(platform_hit_list) > 0 or self.rect.bottom >= janela_height:#se não colidir com nada o player pula
            self.change_y = -12#pula 10 casas para cima
        
    def parar(self):#para horizontalmente e verticalmente
        self.change_x = 0
    def descer(self):#desce / usado no inicio quando nao havia gravidade
        self.change_y = 4
    def calc_grav(self):#gravidade

        if self.change_y == 0:#caso nao haja movimento no eixo Y o player passa a ter um movimento no eixo Y para baixo
            self.change_y = 1
        else:
            self.change_y += .35#o player é derrubado aos poucos
 
        if self.rect.y >= janela_height - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = janela_height - self.rect.height
    def update(self):
        morreu = pygame.mixer.Sound('musicas/fudeu.ogg')
        self.calc_grav()
        
        self.rect.x += self.change_x#atualiza a posiçao do player na tela no eixo x


        block_hit_list = pygame.sprite.spritecollide(self, self.level.plataformas, False)#checa colisao do player com plataformas
        for block in block_hit_list:
            #criação da mecanica entre player e plataforma          
           
            if self.change_x > 0:#se oplayer estiver se movendo para direia e houver colisao ele parará de se mover
                self.rect.right = block.rect.left
            elif self.change_x < 0:
          
                self.rect.left = block.rect.right#para o lado oposto
        # cima/baixo
        self.rect.y += self.change_y#mesma coisa para o eixo Y
        block_hit_list = pygame.sprite.spritecollide(self, self.level.plataformas, False)#mesmo raciocinio mas para o eixo Y
        for block in block_hit_list:
 
     
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
        
            self.change_y = 0
        hit = pygame.sprite.spritecollide(self,self.level.monstros,False)#colisao entre monstro e player
        '''aqui criamos regras para que se o player colida com os monstro de lado ele morre , e se colidir
        de cima para baixo ele mata o monstro'''
        for monster in hit:
            if self.change_x > 0 and self.change_y == 0:
                self.kill()
                pygame.quit()
            elif self.change_x < 0 and self.change_y == 0:
                self.kill()
                pygame.quit()
            if self.change_x == 0 and self.change_y == 0:
                self.kill()
                pygame.quit()
        
        hit2 = pygame.sprite.spritecollide(self,self.level.monstros,False)
        for monster in hit2:
            if self.change_y != 0:
                monster.kill()
                self.change_y = -10
        
        som = pygame.sprite.spritecollide(self,self.level.moedas,True)#moedas desaparecem caso haja colisao
        for barulho in som:
            moeda = pygame.mixer.Sound('musicas/moeda.ogg')#carrega musica moeda
            moeda.play()#roda musica moeda
        
        vitoria = pygame.sprite.spritecollide(self,self.level.asas,True)#colisao entre as reais de arthur e ele
        for barulho in vitoria:
            bvitoria = pygame.mixer.Sound('musicas/vitoria.ogg')
            bvitoria.play()
            pygame.quit()#
                
        '''aqui criamos a mecanica para que o player nao saia da tela , meio que uma "parede" '''               
        if self.rect.left < 0:
                self.rect.left = 0
        if self.rect.bottom > janela_height:
                self.kill()
                morreu.play()
        
        
        '''a partir daqui começamos a usar sprites e condiçoes para que elas variassem para dar sensação de movimento'''
        if self.change_y == 0 and self.change_x == 0:
            self.image = pygame.image.load('imagens/AD.png')
        if self.change_y != 0:
            if self.change_x > 0:
                if self.rect.y % 1.5 == 0:
                    self.image = pygame.image.load('imagens/JD.png')
                if self.rect.y % 1.5 != 0:
                    self.image = pygame.image.load('imagens/AD.png')
            if self.change_x < 0:
                if self.rect.y % 1.5 == 0:
                    self.image = pygame.image.load('imagens/JE.png')
                if self.rect.y % 1.5 != 0:
                    self.image = pygame.image.load('imagens/AE.png')
        
        if self.change_y == 0:
            if self.change_x > 0:
                if self.rect.x % 3 != 0:
                    self.image = pygame.image.load('imagens/AD.png')
                if self.rect.x % 3 == 0:
                    self.image = pygame.image.load('imagens/AD2.png')
            if self.change_x < 0:
                if self.rect.x % 3 == 0:
                    self.image = pygame.image.load('imagens/AE.png')
                if self.rect.x % 3 != 0:
                    self.image = pygame.image.load('imagens/AE2.png')
                    
            
                
            


        '''if self.change_y != 0:
            if self.change_x > 0:    
                if self.rect.y % 2 == 0:
                    self.image = pygame.image.load('imagens/JD.png')
                if self.rect.y % 2 > 0:
                    self.image = pygame.image.load('imagens/AD.png')
            if self.change_x < 0:
                if self.rect.y % 2 == 0:
                    self.image = pygame.image.load('imagens/JE.png')
                if self.rect.y % 2 > 0:
                    self.image = pygame.image.load('imagens/AE.png')
                    
        if self.change_y == 0 or self.change_x == 0:
            if self.change_x < 0:
                self.image = pygame.image.load('imagens/AE.png')
            if self.change_x > 0:
                self.image = pygame.image.load('imagens/AD.png')'''
        