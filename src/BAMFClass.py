import pygame
from pygame.locals import *

class BAMF(pygame.sprite.Sprite):
    def __init__(self,xCoord,yCoord):
        pygame.sprite.Sprite.__init__(self)
        self.x = xCoord
        self.y = yCoord
        self.int = 0
        self.int1 = 0
        self.manVar = 1
        self.axeVar = 0
        self.first = 1
        self.count = 0
        self.count1 = 0
        self.count2 = 0
        self.xCord = self.x
        self.bamf = []
        self.bamf.append(pygame.image.load('BAMF1.bmp'))
        self.bamf.append(pygame.image.load('BAMF2.bmp'))
        self.bamf.append(pygame.image.load('BAMF3.bmp'))
        self.bamf.append(pygame.image.load('BAMF4.bmp'))
        self.bamf.append(pygame.image.load('BAMF1.bmp'))
        self.bamfAxe = []
        self.bamfAxe.append(pygame.image.load('BAMFaxe1.bmp'))
        self.bamfAxe.append(pygame.image.load('BAMFaxe2.bmp'))
        self.bamfAxe.append(pygame.image.load('BAMFaxe3.bmp'))
    
    def throw(self,surface):
        if self.manVar == 1:
            dim = self.bamf[self.int].get_size()
            dimX = dim[0]
            dimY = dim[1]
            rect = Rect(self.x,self.y,dimX,dimY)
            self.bamf[self.int].set_colorkey(pygame.Color(1,150,255))
            surface.blit(self.bamf[self.int],rect)
            self.count1 += 1
            if self.count1 == 2:
                self.int += 1
                self.count1 = 0
            if self.int == 2:
                self.axeVar = 1
            if self.int == 4 and self.count1 == 0:
                self.manVar = 0
                self.int = 0
        if self.axeVar == 1:
            dim = self.bamfAxe[self.int1].get_size()
            dimX = dim[0]
            dimY = dim[1]
            if self.first == 1:
                self.xCord = self.x
                self.first = 0
            self.xCord -= 5
            rect = Rect(self.xCord,self.y + 2*dimY,dimX,dimY)
            self.bamfAxe[self.int1].set_colorkey(pygame.Color(1,150,255))
            surface.blit(self.bamfAxe[self.int1],rect)
            self.count2 += 1
            if self.count2 == 2:
                self.int1 += 1
                self.count2 = 0
            self.count += 1
            if self.count >= 7:
                dim1 = self.bamf[4].get_size()
                dim1X = dim1[0]
                dim1Y = dim1[1]
                rect = Rect(self.x,self.y,dim1X,dim1Y)
                self.bamf[4].set_colorkey(pygame.Color(1,150,255))
                surface.blit(self.bamf[4],rect)
            if self.int1 == 3:
                self.int1 = 0
            if self.count == 40:
                self.manVar = 1
                self.axeVar = 0
                self.first = 1
                self.count = 0


'''pygame.init()

screen = pygame.display.set_mode((400,400),0,32)
pygame.display.set_caption('BAMF!!')
screen.fill(pygame.Color('red'))
bamf = BAMF(200,200)
while True:
    event = pygame.event.poll()
    bamf.throw(screen)
    pygame.time.delay(30)
    pygame.display.update()
    screen.fill(pygame.Color('red'))
    if event.type == QUIT:
        exit()'''
        