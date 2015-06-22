import pygame
import sys, pygame
from menu import *


WHITE = (255,255,255)
BLACK = (0,0,0)

janela_height = 600
janela_widht = 800
 
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load('AD.png')
        self.rect = self.image.get_rect()
        
        self.change_x = 0
        self.change_y = 0
    def direita(self):#boneco vai para direita
        self.change_x = 4
    def esquerda(self):#boneco vai para esquerda
        self.change_x = -4
    def pular(self):#boneco pula
    
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.plataformas, False)
        self.rect.y -= 2
 

        if len(platform_hit_list) > 0 or self.rect.bottom >= janela_height:
            self.change_y = -10
        
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
                
        if self.rect.right > janela_widht:
                self.rect.right = janela_widht
        if self.rect.left < 0:
                self.rect.left = 0
        if self.rect.top < 0:
                self.rect.top = 0
        if self.rect.bottom > janela_height:
                self.rect.bottom = janela_height
        
        if self.change_y == 0 and self.change_x == 0:
            self.image = pygame.image.load('AD.png')
        if self.change_y != 0:
            if self.change_x > 0:
                if self.rect.y % 1.5 == 0:
                    self.image = pygame.image.load('JD.png')
                if self.rect.y % 1.5 > 0:
                    self.image = pygame.image.load('AD.png')
            if self.change_x < 0:
                if self.rect.y % 1.5 == 0:
                    self.image = pygame.image.load('JE.png')
                if self.rect.y % 1.5 > 0:
                    self.image = pygame.image.load('AE.png')
        
        if self.change_y == 0:
            if self.change_x > 0:
                if self.rect.x % 5 != 0:
                    self.image = pygame.image.load('AD.png')
                if self.rect.x % 5 == 0:
                    self.image = pygame.image.load('JD2.png')
            if self.change_x < 0:
                if self.rect.x % 5 == 0:
                    self.image = pygame.image.load('AE.png')
                if self.rect.x % 5 != 0:
                    self.image = pygame.image.load('JE.png')
                
                


        '''if self.change_y != 0:
            if self.change_x > 0:    
                if self.rect.y % 2 == 0:
                    self.image = pygame.image.load('JD.png')
                if self.rect.y % 2 > 0:
                    self.image = pygame.image.load('AD.png')
            if self.change_x < 0:
                if self.rect.y % 2 == 0:
                    self.image = pygame.image.load('JE.png')
                if self.rect.y % 2 > 0:
                    self.image = pygame.image.load('AE.png')
                    
        if self.change_y == 0 or self.change_x == 0:
            if self.change_x < 0:
                self.image = pygame.image.load('AE.png')
            if self.change_x > 0:
                self.image = pygame.image.load('AD.png')'''
        
            
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
    def __init__(self,sprite,sprite2,limite):
        super().__init__()
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()
        self.limitemax = self.rect.x + limite
        self.limitemin = self.rect.x - limite
        self.change_y = 0
        self.change_x = 2
        self.sprite = sprite
        self.sprite2= sprite2
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.right < 0:
            self.change_x = 0
        if self.rect.x == self.limitemax:
            self.change_x = - 2
        if self.rect.x == self.limitemin:
            self.change_x = 2
        if self.change_x != 0:
            if self.rect.x % 5 != 0:
                self.image = pygame.image.load(self.sprite)
            if self.rect.x % 5 == 0:
                self.image = pygame.image.load(self.sprite2)


                
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
        level_m= [['M1.png','M12.png',200,450,70],
                 ] #define widht , height , x , y e movimento no eixo inicial do monstro
        
        
        for enemy in level_m:#usa todas coordenadas indicadas no array acima para criar blocos nesses lugares
            monstro = Monstros(enemy[0],enemy[1],enemy[4])
            monstro.rect.x = enemy[2]
            monstro.rect.y = enemy[3]
            monstro.player = self.player
            monstro.limitemax = enemy[2] + enemy[4]
            monstro.limitemin = enemy[2] - enemy[4]
            self.monstros.add(monstro)
        back = Background()
        
        self.backgrounds.add(back)
class Limpar():
    def __init__(self,screen,widht,height):
        self.widht = widht
        self.height = height
        empty = pygame.Color(0,0,0,0) #The last 0 indicates 0 alpha, a transparent color
        screen = pygame.Surface((self.widht, self.height))
        screen.fill(empty)


def main():
    """ Main Program """
    pygame.init()
 
    size = [janela_widht, janela_height]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Arthur no mundo das fadas")
    pygame.display.set_icon(pygame.image.load(("fada.png")))
    pygame.mixer.music.load('musica.ogg') 
    
    
    pygame.mixer.music.play()
   
    player = Player()
    limpar = Limpar(screen,janela_widht,janela_height)
   
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
            '''if event.type == pygame.mouse.get_pressed() and event.button == 0:# LMB
                limpar'''
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.direita()
                if event.key == pygame.K_a:
                    player.esquerda()
                if event.key == pygame.K_w:
                    player.pular()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_q:
                    active_sprite_list.update()
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