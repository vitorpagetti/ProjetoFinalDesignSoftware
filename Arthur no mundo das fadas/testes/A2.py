import pygame

WHITE = (255,255,255)#define a partir de RGB a cor desejada , usamos isso de inicio para plotar na tela plataformas monstros e player
BLACK = (0,0,0)
'''janela height e widht serve para definirmos o tamanho da tela que será inicializada'''
janela_height = 600
janela_widht = 800
 
class Player(pygame.sprite.Sprite):#aqui construimos os comandos e mecanica do player por meio de uma classe

    '''pygame.sprite.Sprite é usado para chamarmos essa classe que vem na biblioteca pygame. Com ela,
    conseguimos definir a classe desejada como sprite e atribuir funçoes ja criadas para ela. Caso essa classe pai
    nao seja chamada , fica impossivel de plotar objetos na tela e atualiza-la para dar sensação de movimento'''
    def __init__(self):
        super().__init__()#inicia na classe player o init de sprite.Sprite
        
        self.image = pygame.image.load('AD.png')#define a imagem inicial da classe player
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
            self.change_y = -10#pula 10 casas para cima
        
    def parar(self):#para horizontalmente e verticalmente
        self.change_x = 0
    def descer(self):#desce
        self.change_y = 4
    def parar_updown(self):
        self.change_y = 0
    def calc_grav(self):

        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        if self.rect.y >= janela_height - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = janela_height - self.rect.height
    def update(self):
        
        self.calc_grav()
        
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, self.level.plataformas, False)
        for block in block_hit_list:
           
           
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
          
                self.rect.left = block.rect.right
        # cima/baixo
        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, self.level.plataformas, False)
        for block in block_hit_list:
 
     
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
        
            self.change_y = 0
        hit = pygame.sprite.spritecollide(self,self.level.monstros,False)
        for monster in hit:
            if self.change_x > 0 and self.change_y == 0:
                self.kill()
            elif self.change_x < 0 and self.change_y == 0:
                self.kill()
        
        hit2 = pygame.sprite.spritecollide(self,self.level.monstros,False)
        for monster in hit2:
            if self.change_y != 0:
                monster.kill()
                self.change_y = -10
        
        if self.change_y < 0:
            if self.change_x > 0:
                self.image = pygame.image.load('JD.png')
            elif self.change_x < 0:
                self.image = pygame.image.load('JE.png')
            
        if self.change_y == 0:
            if self.change_x > 0:
                self.image = pygame.image.load('AD.png')
            if self.change_x < 0:
                self.image = pygame.image.load('AE.png')
        
        if self.change_y == 0 and self.change_x == 0:
            self.image = pygame.image.load('AD.png')
        
        if self.rect.right > janela_widht:
                self.rect.right = janela_widht
        if self.rect.left < 0:
                self.rect.left = 0
        if self.rect.top < 0:
                self.rect.top = 0
        if self.rect.bottom > janela_height:
                self.rect.bottom = janela_height
class Platform(pygame.sprite.Sprite):
    def __init__(self,widht,height):
        super().__init__()
        self.image = pygame.Surface([widht,height])
        self.rect = self.image.get_rect()
        
        self.image.fill(WHITE)

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('back.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        
class Level(): 
    def __init__(self,player):
        self.plataformas = pygame.sprite.Group()
        self.monstros = pygame.sprite.Group()
        self.backgrounds = pygame.sprite.Group()        
        self.player = player
        self.mudar_mundo = 0
        self.level_limit = -1000
    def update(self):
        self.plataformas.update()
        self.monstros.update()
    
    def draw(self,screen):        
        screen.fill(BLACK)
        self.plataformas.draw(screen)    
        self.backgrounds.draw(screen)
        self.monstros.draw(screen)
    def shift_world(self, mudar_x):
        self.mudar_mundo += mudar_x
        for platform in self.plataformas:
            platform.rect.x += mudar_x
 
        for monstro in self.monstros:
            monstro.rect.x += mudar_x
        
        for background in self.backgrounds:
            background.rect.x += mudar_x

class Monstros(pygame.sprite.Sprite):
    def __init__(self,sprite):
        super().__init__()
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()
        
        self.change_y = 0
        self.change_x = 2
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.right < 0:
            self.change_x = 0


                
class Level01(Level):
    def __init__(self,player):
        Level.__init__(self,player)
        
        self.level_limit = -1500
        
        level = [[2500, 200, 0, 500],
                 ]#widht,height , x e y dos blocos
        for platform in level:#usa todas coordenadas indicadas no array acima para criar blocos nesses lugares
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.plataformas.add(block)
        level_m= [['M1.png',200,450],
                 ] #define widht , height , x , y e movimento no eixo inicial do monstro
        
        
        for enemy in level_m:#usa todas coordenadas indicadas no array acima para criar blocos nesses lugares
            monstro = Monstros(enemy[0])
            monstro.rect.x = enemy[1]
            monstro.rect.y = enemy[2]
            monstro.player = self.player
            self.monstros.add(monstro)
        
        back = Background()
        
        self.backgrounds.add(back)

def main():
    """ Main Program """
    pygame.init()
 
    size = [janela_widht, janela_height]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Arthur no mundo das fadas")
    pygame.mixer.music.load('musica.ogg') 
    
    
    pygame.mixer.music.play()
   
    player = Player()
 
   
    level_list = []
    level_list.append( Level01(player) )
 
   
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    player.rect.x = 0
    player.rect.y = 300
    active_sprite_list.add(player)
 
   
    done = False
 
    
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.direita()
                if event.key == pygame.K_a:
                    player.esquerda()
                if event.key == pygame.K_w:
                    player.pular()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.parar()
                if event.key == pygame.K_d:
                    player.parar()
                    

                            
                    
        
        active_sprite_list.update()
        
        current_level.update()
 
        
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)
 
        current_position = player.rect.x + current_level.mudar_mundo
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
        
        
        
        current_level.draw(screen)
        active_sprite_list.draw(screen)
 
        clock.tick(60)
 
 
        pygame.display.flip()
 
    # Possibilita ao usuario fechar a tela do jogo
    pygame.quit()
 
if __name__ == "__main__":
    main()                