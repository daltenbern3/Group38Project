import pygame
from Platforms import *
from pygame.locals import *
from pygame import color
from BugClass import *
from Player import *
from BulletClass import *
from DragonClass import *
from WarriorClass import *
from AxeClass import *
from EndScreen import EndGame
from TitleScreen import StartGame

StartGame()
def gameloop():
    pygame.init()
    windowWidth,windowHeight=800,600

    screenRect=pygame.Rect(0,0,windowWidth,windowHeight)
    screen=pygame.display.set_mode((windowWidth,windowHeight),0,32)

    axe = [Axe(3300,225),Axe(3300,225),Axe(3300,225)]
    axe1 = [Axe(3800,325),Axe(3800,325),Axe(3800,325)]
    pygame.mixer.music.load('MarioStarman')
    pygame.mixer.music.play(loops=-1, start=0.0)

    platforms=pygame.sprite.Group()
    enemies=pygame.sprite.Group()

    bgd = pygame.image.load('GameBackground1.bmp')

    lvl1platforms=[Platform(0,500,600),Platform(200,400,200),Platform(400,300,200),Platform(600,400,1800),Platform(800,200,200),Platform(800,100,1400),Platform(1000,300,200),Platform(1600,300,400),Platform(2200,200,600),Platform(2400,500,1000),Platform(2800,400,400),Platform(3200,300,400),Platform(3600,400,600)]
    lvl1enemies=[Bug(950,350),Bug(550,250,2),Bug(2250,350,4),Bug(1350,50,6),Bug(1750,50,9),Bug(2150,50,5),Bug(1150,350,2),Bug(1750,350,7),Bug(1750,350,8),Bug(1550,350,5),Bug(1550,350,8),Bug(1850,250,3),Bug(1950,350,5),Bug(2350,350,7),Bug(2100,350,2),Bug(3050,450,6),Bug(2800,150,6),Dragon(900,220,4),Dragon(1700,220,6),Dragon(1800,220,8),Dragon(2350,320,10),Dragon(2350,220,5),Dragon(2550,20,5),Dragon(3350,320,8),Warrior(3300,225,axe),axe[0],axe[1],axe[2],Warrior(3800,325,axe1),axe1[0],axe1[1],axe1[2]]

    for plat in lvl1platforms:
        platforms.add(plat)  
    for mons in lvl1enemies:
        enemies.add(mons)



    bullet = []
    for x in range(15):
        bullet.append(Bullet(0,0,enemies))
        bullets = pygame.sprite.Group()
        player=Player(platforms,bullet)
    num=0
    die=0
    while True:
        events=pygame.event.get()
        for i in events:
            if i.type==QUIT:
                exit()
        screen.blit(bgd, screenRect)
        platforms.update(screen,screenRect,num)
    
        enemies.update(screen,bullets,screenRect,num)
        num,die=player.update(enemies,events,screen)
        bullets = player.makeGroup()
        bullets.update(screen,enemies,screenRect,num)
        pygame.display.update()
    
        pygame.time.delay(25)
    
        if die == 1:
            EndGame()
            gameloop()


gameloop()


    
if __name__=='__main__':
    pass