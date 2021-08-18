import pygame
from pygame.locals import *
from DragonClass import *
from BugClass import *
from WarriorClass import *
from AxeClass import *


pygame.init()

screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption('Dragon!!')
screen.fill(pygame.Color('blue'))
axe = Axe(600,400,None,4)
drag = Warrior(600,400,None,4,axe)
drag1 = Dragon(300,400,axe,2)
dragons = pygame.sprite.Group(drag,drag1,axe)
while(True):
    event = pygame.event.poll()
    dragons.update(screen,800,0)
    pygame.time.delay(30)
    pygame.display.update()
    screen.fill(pygame.Color('blue'))
    if event.type == QUIT:
        exit()