from pygame.locals import *
import pygame
from AxeClass import *

class Warrior(pygame.sprite.Sprite):
    def __init__(self, xCoord, yCoord,axe):
        pygame.sprite.Sprite.__init__(self)
        self.x = xCoord
        self.y = yCoord
        self.axe = axe
        self.axeVar = 0
        self.axeVar1 = 0
        self.axeVar2 = 0
        self.axe1 = 1
        self.axe2 = 0
        self.axe3 = 0
        self.count4 = 1
        self.inc = 3
        self.int1 = 0
        self.die = 0
        self.dieCount = 0
        self.right = 2
        self.left = 1
        self.int = 0
        self.times1 = 2
        self.active = False
        self.rect = Rect(xCoord,yCoord,1,1)
        self.count = 1
        self.warrior = []
        self.warrior1 = []
        self.warrior2 = []
        self.warrior.append(pygame.image.load('BAMF1.bmp'))
        self.warrior.append(pygame.image.load('BAMF2.bmp'))
        self.warrior.append(pygame.image.load('BAMF3.bmp'))
        self.warrior.append(pygame.image.load('BAMF4.bmp'))
        for x in range(len(self.warrior)):
            self.warrior1.append(pygame.transform.scale2x(self.warrior[x]))
        for x in range(len(self.warrior1)):
            self.warrior2.append(pygame.transform.flip(self.warrior1[x],True,False))
        self.warriorDie = []
        self.warriorDieL = []
        self.warriorDieR = []
        self.warriorDie.append(pygame.image.load('bugdie1.bmp'))
        self.warriorDie.append(pygame.image.load('bugdie2.bmp'))
        self.warriorDie.append(pygame.image.load('bugdie3.bmp'))
        for x in range(len(self.warriorDie)):
            self.warriorDieL.append(pygame.transform.scale2x(self.warriorDie[x]))
        for x in range(len(self.warriorDieL)):
            self.warriorDieR.append(pygame.transform.flip(self.warriorDieL[x],True,False))
        
    def throw(self,surface):
        if self.left == 1:
            dim = self.warrior1[self.int].get_size()
            dimX = dim[0]
            dimY = dim[1]
            #self.x -= 5
            self.rect = Rect(self.x,self.y,dimX,dimY)
            self.warrior1[self.int].set_colorkey(pygame.Color(1,150,255))
            surface.blit(self.warrior1[self.int],self.rect)
            self.count += 1
            if self.count == 3:
                self.int += 1
                self.count = 0
            self.times1 += 1
        if self.int == 4:
            self.int = 0
            self.left = 2
        if self.left == 2:
            dim = self.warrior1[0].get_size()
            dimX = dim[0]
            dimY = dim[1]
            self.rect = Rect(self.x,self.y,dimX,dimY)
            self.warrior1[0].set_colorkey(pygame.Color(1,150,255))
            surface.blit(self.warrior1[0],self.rect)
        if self.int == 2:
            self.axeVar = 1
        #if self.axeVar == 1:
        if self.axe1 == 1:
            print'1'
            if self.int == 2:
                self.axeVar = 1
            if self.axeVar == 1:
                self.axe[0].throw(surface,self.x)
                self.check = self.axe[0].check()
                self.check1 = self.axe[0].check1()
                if self.check1 ==1 and self.check == 1:
                    self.left = 1
                    self.axe2 = 1
                    self.int = 0
                    self.axe1 = 0
                    self.axeVar2 = 0
                    self.axe3 = 0
                    self.check = 0
                    self.check1 = 0
                    for x in range(len(self.axe)):
                        self.axe[x].setX(self.x)
                if self.check1 == 1:
                    print 'check1'
                    self.left = 1
                    self.axe2 = 1
                    self.int = 0
                    self.axe[1].setX(self.x)
                if self.check == 1:
                    print 'check'
                    self.axe1 = 0
                    self.axeVar = 0
                self.check = 0
                self.check1 = 0
        if self.axe2 == 1:
            print '2'
            if self.int == 2:
                self.axeVar1 = 1
            if self.axeVar1 == 1:
                self.axe[1].throw(surface,self.x)
                self.check = self.axe[1].check()
                self.check1 = self.axe[1].check1()
                if self.check1 ==1 and self.check == 1:
                    self.left = 1
                    self.axe3 = 1
                    self.int = 0
                    self.axe2 = 0
                    self.axeVar2 = 0
                    self.axe1 = 0
                    self.check = 0
                    self.check1 = 0
                    for x in range(len(self.axe)):
                        self.axe[x].setX(self.x)
                if self.check1 == 1:
                    print 'check1'
                    self.left = 1
                    self.axe3 = 1
                    self.int = 0
                    self.axe[2].setX(self.x)
                if self.check == 1:
                    print 'check'
                    self.axe2 = 0
                    self.axeVar1 = 0
                self.check = 0
                self.check1 = 0
        if self.axe3 == 1:
            print '3'
            if self.int == 2:
                self.axeVar2 = 1
            if self.axeVar2 == 1:
                self.axe[2].throw(surface,self.x)
                self.check = self.axe[2].check()
                self.check1 = self.axe[2].check1()
                if self.check1 ==1 and self.check == 1:
                    self.left = 1
                    self.axe1 = 1
                    self.int = 0
                    self.axe3 = 0
                    self.axeVar2 = 0
                    self.axe2 = 0
                    self.check = 0
                    self.check1 = 0
                    for x in range(len(self.axe)):
                        self.axe[x].setX(self.x)
                if self.check1 == 1:
                    print 'check1'
                    self.left = 1
                    self.axe1 = 1
                    self.int = 0
                    self.axe[0].setX(self.x)
                if self.check == 1:
                    print 'check'
                    self.axe3 = 0
                    self.axeVar2 = 0
                self.check = 0
                self.check1 = 0
        if self.die == 1:
            self.dieCount += 1
            if self.dieCount == (2*self.inc)-2:
                self.kill()
                for x in range(len(self.axe)):
                    self.axe[x].setDie()
            where = (self.x,self.y)
            if self.right == 1:
                self.warriorDieR[self.int1].set_colorkey(pygame.Color('white'))
                surface.blit(self.warriorDieR[self.int1],where)
                if self.dieCount == self.count4:
                    self.int1 += 1
                    self.count4 += self.inc
            else:
                self.warriorDieL[self.int1].set_colorkey(pygame.Color('white'))
                surface.blit(self.warriorDieL[self.int1],where)
                if self.dieCount == self.count4:
                    self.int1 += 1
    
    def update(self,surface,enemy,windowWidth,num):
        if self.active == False:
            if self.x <= windowWidth:
                self.active = True
        else:
            self.throw(surface)
            if enemy != None:
                if bool(pygame.sprite.spritecollideany(self, enemy)) == True:
#                if pygame.sprite.collide_rect(self, self.enemy) == True:
                    if self.left == 1:
                        self.right = 0
                    else:
                        self.right = 1
                    self.left = 3
                    self.die = 1
        self.x -= num