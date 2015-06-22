import pygame
 
LEFT = 1


running = 1
screen = pygame.display.set_mode((320, 200))
 
while running:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        running = 0
    elif e.type == pygame.MOUSEBUTTONDOWN and e.button == LEFT:
        print ("alo")
    elif e.type == pygame.MOUSEBUTTONUP and e.button == LEFT:
         print ("oi")
 
    screen.fill((0, 0, 0))
    pygame.display.flip()