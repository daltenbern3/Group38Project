from pygame.locals import *
import pygame
import time


def StartGame():
    pygame.init()

    screen = pygame.display.set_mode((800,600), 0 ,32)

    pygame.display.set_caption('Welcome to Alien Vengeance!')

    screen.fill(pygame.Color('white'))

    backgrounds = []
    hero = []
    
    pygame.mixer.music.load('TitleMusic2')
    pygame.mixer.music.play(loops=-1, start=0.0)
    

    backgrounds.append(pygame.image.load('TitleScreen.bmp'))
    hero.append(pygame.image.load('HeroStand1.bmp'))
    hero.append(pygame.image.load('HeroWalk1.bmp'))
    hero.append(pygame.image.load('HeroWalk2.bmp'))
    hero.append(pygame.image.load('HeroWalk3.bmp'))
    hero.append(pygame.image.load('HeroWalk4.bmp'))
    hero.append(pygame.image.load('HeroWalk5.bmp'))
    hero.append(pygame.image.load('HeroWalk6.bmp'))
    
    
    hero.append(pygame.image.load('HeroWalk1.bmp'))
    hero.append(pygame.image.load('HeroWalk2.bmp'))
    hero.append(pygame.image.load('HeroWalk3.bmp'))
    hero.append(pygame.image.load('HeroWalk4.bmp'))
    hero.append(pygame.image.load('HeroWalk5.bmp'))
    hero.append(pygame.image.load('HeroWalk6.bmp'))
    
    
    hero.append(pygame.image.load('HeroWalk1.bmp'))
    hero.append(pygame.image.load('HeroWalk2.bmp'))
    hero.append(pygame.image.load('HeroWalk3.bmp'))
    hero.append(pygame.image.load('HeroWalk4.bmp'))
    hero.append(pygame.image.load('HeroWalk5.bmp'))
    hero.append(pygame.image.load('HeroWalk6.bmp'))
    
    hero.append(pygame.image.load('HeroJump1.bmp'))
    hero.append(pygame.image.load('HeroJump2.bmp'))
    hero.append(pygame.image.load('HeroJump3.bmp'))
    hero.append(pygame.image.load('HeroJump4.bmp'))
    hero.append(pygame.image.load('HeroJump5.bmp'))
    
    
    hero.append(pygame.image.load('HeroWalk1.bmp'))
    hero.append(pygame.image.load('HeroWalk2.bmp'))
    hero.append(pygame.image.load('HeroWalk3.bmp'))
    hero.append(pygame.image.load('HeroWalk4.bmp'))
    hero.append(pygame.image.load('HeroWalk5.bmp'))
    hero.append(pygame.image.load('HeroWalk6.bmp'))
    
    
    hero.append(pygame.image.load('HeroWalk1.bmp'))
    hero.append(pygame.image.load('HeroWalk2.bmp'))
    hero.append(pygame.image.load('HeroWalk3.bmp'))
    hero.append(pygame.image.load('HeroWalk4.bmp'))
    hero.append(pygame.image.load('HeroWalk5.bmp'))
    hero.append(pygame.image.load('HeroWalk6.bmp'))
    
    
    hero.append(pygame.image.load('HeroJump1.bmp'))
    hero.append(pygame.image.load('HeroJump2.bmp'))
    hero.append(pygame.image.load('HeroJump3.bmp'))
    hero.append(pygame.image.load('HeroJump4.bmp'))
    hero.append(pygame.image.load('HeroJump5.bmp'))
    
    
    hero.append(pygame.image.load('HeroWalk1.bmp'))
    hero.append(pygame.image.load('HeroWalk2.bmp'))
    hero.append(pygame.image.load('HeroWalk3.bmp'))
    hero.append(pygame.image.load('HeroWalk4.bmp'))
    hero.append(pygame.image.load('HeroWalk5.bmp'))
    hero.append(pygame.image.load('HeroWalk6.bmp'))
    
    
    hero.append(pygame.image.load('HeroJump1.bmp'))
    hero.append(pygame.image.load('HeroJump2.bmp'))
    hero.append(pygame.image.load('HeroJump3.bmp'))
    hero.append(pygame.image.load('HeroJump4.bmp'))
    hero.append(pygame.image.load('HeroJump5.bmp'))
    
    
    hero.append(pygame.image.load('HeroWalk1.bmp'))
    hero.append(pygame.image.load('HeroWalk2.bmp'))
    hero.append(pygame.image.load('HeroWalk3.bmp'))
    hero.append(pygame.image.load('HeroWalk4.bmp'))
    hero.append(pygame.image.load('HeroWalk5.bmp'))
    hero.append(pygame.image.load('HeroWalk6.bmp'))
    
    
    hero.append(pygame.image.load('HeroJump1.bmp'))
    hero.append(pygame.image.load('HeroJump2.bmp'))
    hero.append(pygame.image.load('HeroJump3.bmp'))
    hero.append(pygame.image.load('HeroJump4.bmp'))
    hero.append(pygame.image.load('HeroJump5.bmp'))
    
    hero.append(pygame.image.load('HeroWalk1.bmp'))
    hero.append(pygame.image.load('HeroWalk2.bmp'))
    hero.append(pygame.image.load('HeroWalk3.bmp'))
    hero.append(pygame.image.load('HeroWalk4.bmp'))
    hero.append(pygame.image.load('HeroWalk5.bmp'))
    hero.append(pygame.image.load('HeroWalk6.bmp'))
    
    
    hero.append(pygame.image.load('HeroWalk1.bmp'))
    hero.append(pygame.image.load('HeroWalk2.bmp'))
    hero.append(pygame.image.load('HeroWalk3.bmp'))
    hero.append(pygame.image.load('HeroWalk4.bmp'))
    hero.append(pygame.image.load('HeroWalk5.bmp'))
    hero.append(pygame.image.load('HeroWalk6.bmp'))
    
    
    hero.append(pygame.image.load('HeroWalk1.bmp'))
    hero.append(pygame.image.load('HeroWalk2.bmp'))
    hero.append(pygame.image.load('HeroWalk3.bmp'))
    hero.append(pygame.image.load('HeroWalk4.bmp'))
    hero.append(pygame.image.load('HeroWalk5.bmp'))
    hero.append(pygame.image.load('HeroWalk6.bmp'))
    hero.append(pygame.image.load('HeroStand1.bmp'))
    hero.append(pygame.image.load('HeroStand1.bmp'))
    hero.append(pygame.image.load('HeroStand1.bmp'))
    hero.append(pygame.image.load('HeroStand1.bmp'))
    hero.append(pygame.image.load('HeroStand1.bmp'))
    hero.append(pygame.image.load('HeroStand1.bmp'))
    hero.append(pygame.image.load('HeroStand1.bmp'))
    hero.append(pygame.image.load('HeroStand1.bmp'))
    hero.append(pygame.image.load('HeroDead1.bmp'))
    
    
    
    

    


    y = 1

    while True:
        screen.blit(backgrounds[0], Rect( 0 , 0 , 400, 400))
        pygame.display.update()
        event = pygame.event.poll()
        for a in range(0,len(hero)-1):
            hero[a].set_colorkey(pygame.Color('white'))
            screen.blit(hero[a], (10 + 10 * a ,100))
            
            screen.blit(hero[a], (5 + 12 * a ,50))
            
            screen.blit(hero[a], (180 + 8 * a ,10))
            
            screen.blit(hero[a], (10 + 10 * a ,500))
            
            screen.blit(hero[a], (5 + 11 * a ,300))
            
            screen.blit(hero[a], (381.5,229))
            
            
            pygame.display.update()
            pygame.time.delay(100)
            
            screen.blit(backgrounds[0], Rect( 0 , 0 , 400, 400))
            pygame.display.update()
            event = pygame.event.poll()
            if event.type == KEYDOWN and event.key == K_SPACE:
                pygame.mixer.music.stop()
                break
            if event.type == QUIT:
                exit()
            
        if event.type == KEYDOWN and event.key == K_SPACE:
            pygame.mixer.music.stop()
            break
        if event.type == QUIT:
            exit()
            
            

    
    
    
    

