from pygame.locals import *
import pygame
import time


def StartGame():
    pygame.init()

    screen = pygame.display.set_mode((800,600), 0 ,32)

    pygame.display.set_caption('Welcome to Alien Vengence!')

    screen.fill(pygame.Color('white'))

    backgrounds = []
    hero = []
    

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

    while y == 1:
        screen.blit(backgrounds[0], Rect( 0 , 0 , 400, 400))
        pygame.display.update()
        event = pygame.event.poll()
        for x in range(0,len(hero)-1):
            hero[x].set_colorkey(pygame.Color('white'))
            screen.blit(hero[x], (10 + 10 * x ,100))
            
            screen.blit(hero[x], (5 + 12 * x ,50))
            
            screen.blit(hero[x], (180 + 8 * x ,10))
            
            screen.blit(hero[x], (10 + 10 * x ,500))
            
            screen.blit(hero[x], (5 + 11 * x ,300))
            
            screen.blit(hero[x], (381.5,229))
            
            
            pygame.display.update()
            pygame.time.delay(100)
            
            screen.blit(backgrounds[0], Rect( 0 , 0 , 400, 400))
            pygame.display.update()
            event = pygame.event.poll()
            if event.type == KEYDOWN and event.key == K_SPACE:
                exit()
            if event.type == QUIT:
                exit()
            
        if event.type == KEYDOWN and event.key == K_SPACE:
            exit()
        if event.type == QUIT:
            exit()
            
StartGame()
    
    
    
    

