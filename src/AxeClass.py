from pygame.locals import *
import pygame

class Axe(pygame.sprite.Sprite):
    def __init__(self, xCoord, yCoord):
        pygame.sprite.Sprite.__init__(self)
        self.x = xCoord
        self.y = yCoord
        self.xStill = xCoord
        self.count4 = 1
        self.done = 0
        self.done1 = 0
        self.inc = 3
        self.int1 = 0
        self.die = 0
        self.dieCount = 0
        self.poo = 0
        self.right = 2
        self.left = 1
        self.still = 0
        self.int = 0
        self.times1 = 2
        self.active = False
        self.rect = Rect(xCoord,yCoord,1,1)
        self.count = 1
        self.count1 = 0
        self.warrior = pygame.transform.scale2x(pygame.image.load('BAMF1.bmp'))
        self.axe = []
        self.axe1 = []
        self.axe2 = []
        self.axe.append(pygame.image.load('BAMFaxe1.bmp'))
        self.axe.append(pygame.image.load('BAMFaxe2.bmp'))
        self.axe.append(pygame.image.load('BAMFaxe3.bmp'))
        for x in range(len(self.axe)):
            self.axe1.append(pygame.transform.scale2x(self.axe[x]))
        for x in range(len(self.axe1)):
            self.axe2.append(pygame.transform.flip(self.axe1[x],True,False))
        self.axeDie = []
        self.axeDieL = []
        self.axeDieR = []
        self.axeDie.append(pygame.image.load('bugdie1.bmp'))
        self.axeDie.append(pygame.image.load('bugdie2.bmp'))
        self.axeDie.append(pygame.image.load('bugdie3.bmp'))
        for x in range(len(self.axeDie)):
            self.axeDieL.append(pygame.transform.scale2x(self.axeDie[x]))
        for x in range(len(self.axeDieL)):
            self.axeDieR.append(pygame.transform.flip(self.axeDieL[x],True,False))
        
    def throw(self,surface,xStill):
        if self.left == 1:
            dim = self.axe1[self.int].get_size()
            dimX = dim[0]
            dimY = dim[1]
            self.x -= 10
            self.rect = Rect(self.x,self.y + 2 * dimY,dimX,dimY)
            self.axe1[self.int].set_colorkey(pygame.Color(1,150,255))
            surface.blit(self.axe1[self.int],self.rect)
            self.count += 1
            if self.count == 2:
                self.int += 1
                self.count = 0
            self.times1 += 1
            self.count1 += 1
            print self.count1
            if self.count1 == 7:
                self.still = 1
            '''if self.still == 1:
                dim = self.warrior.get_size()
                dimX = dim[0]
                dimY = dim[1]
                self.rect1 = Rect(self.xStill,self.y,dimX,dimY)
                self.warrior.set_colorkey(pygame.Color(1,150,255))
                surface.blit(self.warrior,self.rect1)'''
        if self.int == 2:#was 5
            self.int = 0
        if self.count1 * 10 == 800:
            self.done = 1
            self.count1 = 0
            self.still = 0
            self.left = 1
            self.x = xStill
            self.rect = Rect(0,0,0,0)
            self.poo = 0
        if self.count1 * 10 == 270:
            self.done1 = 1
            self.poo = 1
        if self.die == 1:
            self.dieCount += 1
            if self.dieCount == (2*self.inc)-2:
                self.dieCount = 0
                self.die = 0
                self.x = xStill
                self.left = 1
                self.right = 2
                self.done = 1
#                if self.poo == 1:
                self.done1 = 1
                self.poo = 0
                self.int1 = 0
                self.count1 = 0
                self.rect = Rect(self.x,self.y ,1,1)
                return True
            where = (self.x,self.y)
            if self.right == 1:
                self.axeDieR[self.int1].set_colorkey(pygame.Color('white'))
                surface.blit(self.axeDieR[self.int1],where)
                if self.dieCount == self.count4:
                    self.int1 += 1
                    self.count4 += self.inc
            if self.right == 0:
                self.axeDieL[self.int1].set_colorkey(pygame.Color('white'))
                surface.blit(self.axeDieL[self.int1],where)
                if self.dieCount == self.count4:
                    self.int1 += 1
    def check(self):
        if self.done == 1:
            self.done = 0
            return 1
        else:
            return 0
    
    def check1(self):
        if self.done1 == 1:
            self.done1 = 0
            return 1
        else:
            return 0
        
    def setX(self,x):
        self.x = x
        self.count1 = 0
    
    def setDie(self):
        self.rect = Rect(0,0,0,0)
    
    def update(self,surface,enemy,windowWidth,num):
        if self.active == False:
            if self.x <= windowWidth:
                self.active = True
        else:
            #self.throw(surface)
            if enemy != None:
                if bool(pygame.sprite.spritecollideany(self, enemy)) == True:
                #if pygame.sprite.collide_rect(self, self.enemy) == True:
                    if self.left == 1:
                        self.right = 0
                    else:
                        self.right = 1
                    self.left = 3
                    self.die = 1
        self.x -= num