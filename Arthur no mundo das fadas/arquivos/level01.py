import level,platform,monstros,background,pygame,asas
class Level01(level.Level):
    def __init__(self,player):
        level.Level.__init__(self,player)
        
        self.level_limit = -4600#tamanho do level1
        musica = pygame.mixer.Sound('musicas/musica.ogg')
        musica.play()
        LEVEL = [[618, 100, 0, 500],
                 [900,100,890,500],
[222,74,1087,293],
[74,74,1540,330],
[74,74,1811,219],
[74,74,2070,219],
[5000,100,2325,500],
[74,74,2600,180],
[74,74,3186,180],
[74,74,2895,104],



                 ]#widht,height , x e y dos blocos e ele é criado na tela
        for plataforma in LEVEL:#usa todas coordenadas indicadas no array acima para criar blocos nesses lugares
            block = platform.Platforma(plataforma[0], plataforma[1])
            block.rect.x = plataforma[2]
            block.rect.y = plataforma[3]
            block.player = self.player
            self.plataformas.add(block)
        level_m= [[200,450,70],

                 ] #define widht , height , x , y e movimento no eixo inicial do monstro.  É criado na tela
        
        
        for enemy in level_m:#usa todas coordenadas indicadas no array acima para criar monstros nesses lugares
            monstro = monstros.Monstros(enemy[2])
            monstro.rect.x = enemy[0]
            monstro.rect.y = enemy[1]
            monstro.player = self.player
            monstro.limitemax = enemy[0] + enemy[2]
            monstro.limitemin = enemy[0] - enemy[2]
            self.monstros.add(monstro)
        back = background.Background()      
        self.backgrounds.add(back)#adiciona o background no level
        
        
        moedas = [[200,400]]#x e y das moedas na tela 
        for moeda in moedas:#cria as moedas do jogo
            coin = moedas.Moedas()
            coin.rect.x = moeda[0]
            coin.rect.y = moeda[1]
            self.moedas.add(coin)  
        Asas = asas.Asas_de_fada()
        Asas.rect.x = 3500
        Asas.rect.y = 300
        self.asas.add(Asas)