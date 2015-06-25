import asas,background,level,level01,moedas,monstros,pygame,player,platform

def main():
    """ programa principal"""
    pygame.init()#inicia o pygame
 
    size = [player.janela_widht, player.janela_height]#define o tamanho da telA
    screen = pygame.display.set_mode(size)#CRIA A TELA
 
    pygame.display.set_caption("Arthur no mundo das fadas")#titulo da janela
    pygame.display.set_icon(pygame.image.load(("imagens/fada.png")))#desenho do icone
    
   
    jogador = player.Player()#cria o player
 
   
    level_list = []#lista dos levels
    level_list.append( level01.Level01(jogador) )
 
   
    current_level_no = 0#level inicial
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()#cria o grupo do player
    player.level = current_level
 
    player.rect.x = 0#posiçao inicial do player na tela
    player.rect.y = 300#posiçao inicial do player na tela
    active_sprite_list.add(player)
 
   
    done = False
 
    
    clock = pygame.time.Clock()#relogio que auxilia no tempo do jogo
 
    # -------- looping do jogo -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
            '''teclas de movimentação dos personagens'''    
            if event.type == pygame.KEYDOWN:#ao apertar o botao
                if event.key == pygame.K_d:
                    jogador.direita()
                if event.key == pygame.K_a:
                    jogador.esquerda()
                if event.key == pygame.K_w:
                    jogador.pular()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_q:
                    active_sprite_list.update()
            if event.type == pygame.KEYUP:#ao soltar o botao
                if event.key == pygame.K_a:
                    jogador.parar()
                if event.key == pygame.K_d:
                    jogador.parar()
                    
                            
        active_sprite_list.update()#atualiza o grupo
        
        current_level.update()
 
        
        if player.rect.right >= 500:#a partir dessa coordenada o mundo começa a ser "puxado" para tras
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)
 
        current_position = player.rect.x + current_level.mudar_mundo
        if current_position < current_level.level_limit:#checa se o player ja chegou no fim do level
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
                
        '''aqui desenhamos tudo na tela'''        
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        
        clock.tick(60)#60 fps de atualizaçao
 
 
        pygame.display.flip()#atualiza tudo na tela
 
    # Possibilita ao usuario fechar a tela do jogo
    pygame.quit()
 

if __name__ == "__main__":
    main()                
