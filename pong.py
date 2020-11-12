import pygame
import sys
from random import randint

#Configs.
pygame.init()
pygame.display.set_caption('El increible juego Pong')

#Variables.
tamaño = w , h  = 800 , 600
pantalla = pygame.display.set_mode(tamaño)
negro = (0,0,0)

#Clases.
class jugadores(pygame.sprite.Sprite):
    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load('sprites/Paletas.png')
        self.rect = self.sprite.get_rect()
        self.rect.centerx =  x
        self.rect.centery = h/2
        self.posY = (h/2 - 20)
        self.speed = 15

class pelota(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.sprite = pygame.image.load('sprites/Pelota.png')
            self.rect = self.sprite.get_rect()    
            self.rect.centery = h/2
            self.rect.centerx = w/2
            self.speed = [0.5,-0.5]

        def mover(self,time,player1,player2):
            
            self.rect.centerx += self.speed[0] * time
            self.rect.centery += self.speed[1] * time
            
            if self.rect.centerx <= 0 or self.rect.centerx >= w:
                self.rect.centerx = w/2
                self.rect.centery = h/2
                
            if self.rect.centery <= 0 or self.rect.centery >= h:
                self.speed[1] = -self.speed[1]
                self.rect.centery += self.speed[1] * time
            
            if pygame.sprite.collide_rect(self,player1) or pygame.sprite.collide_rect(self,player2):
                self.speed[1]= -self.speed[1]
                self.rect.centerx += self.speed[1] * time   
            
#Funciones.
def main():
	#Crear los objetos.
    player = jugadores(790)
    player2 = jugadores(20)
    bola = pelota()
    clock = pygame.time.Clock()

    while True:
        pantalla.fill(negro)  

        time = clock.tick(60)

        #Verificador de eventos😴.
        for event in pygame.event.get():
            #Cerrar el juego 😃.
            if event.type == pygame.QUIT:    
                pygame.quit()
                sys.exit()
            
            #Movimiento de los jugadores.    
                   
        teclado = pygame.key.get_pressed()
        
        if teclado[pygame.K_UP]:
            player2.posY -= player2.speed
        elif teclado[pygame.K_DOWN]:
            player2.posY += player2.speed
        elif teclado[pygame.K_w]:
            player.posY -= player.speed
        elif teclado[pygame.K_s]:
            player.posY += player.speed
      
      
        
        bola.mover(time,player,player2)
        #dibus
        pantalla.blit(player.sprite,(10,(player.posY)))
        pantalla.blit(player2.sprite, (780,player2.posY))
        pantalla.blit(bola.sprite,(bola.rect.centerx,bola.rect.centery))
        
           
        pygame.display.flip()
main()