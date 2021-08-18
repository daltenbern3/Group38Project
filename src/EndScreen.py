from pygame.locals import *
import pygame
import time



def EndGame():
    pygame.init()

    screen = pygame.display.set_mode((800,600), 0 ,32)

    pygame.display.set_caption('Game Over!')

    screen.fill(pygame.Color('white'))

    backgrounds = []
    hero = []
    
    pygame.mixer.music.load('TitleMusic2')
    pygame.mixer.music.play(loops=-1, start=0.0)
    

    backgrounds.append(pygame.image.load('DeathScene.bmp'))
    
    hero.append(pygame.image.load('HeroDead1.bmp'))
    hero1 = [pygame.transform.scale2x(hero[0])]
    
    hero1[0].set_colorkey(pygame.Color('white'))


    runnings = 1

    while runnings == 1:
        screen.blit(backgrounds[0], Rect( 0 , 0 , 400, 400))
        
        
        
        screen.blit(hero1[0], (350,335))
            
        pygame.display.update()
        pygame.time.delay(100)
            
        
        event = pygame.event.poll()
        if event.type == KEYDOWN and event.key == K_SPACE:
            pygame.mixer.music.stop()
            break
        if event.type == QUIT:
            exit()
            
        

            

            

    
    
    
    

