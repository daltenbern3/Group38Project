from pygame.locals import *
import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, xCoord, yCoord,enemy):
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
        self.enemy = enemy
        self.right = 2
        self.left = 1
        self.still = 0
        self.int = 0
        self.times1 = 2
        self.active = False
        self.rect = Rect(xCoord,yCoord,1,1)
        self.count = 1
        self.count1 = 0
        self.bullet = []
        self.bullet1 = []
        self.bullet2 = []
        self.bullet.append(pygame.image.load('bullet.bmp'))
        #for x in range(len(self.bullet)):
            #self.bullet1.append(pygame.transform.scale2x(self.bullet[x]))
        self.bullet1 = self.bullet
        for x in range(len(self.bullet1)):
            self.bullet2.append(pygame.transform.flip(self.bullet1[x],True,False))
        self.bulletDie = []
        self.bulletDieL = []
        self.bulletDieR = []
        self.bulletDie.append(pygame.image.load('bugdie1.bmp'))
        self.bulletDie.append(pygame.image.load('bugdie2.bmp'))
        self.bulletDie.append(pygame.image.load('bugdie3.bmp'))
        #for x in range(len(self.bulletDie)):
            #self.bulletDieL.append(pygame.transform.scale2x(self.bulletDie[x]))
        self.bulletDieL = self.bulletDie
        for x in range(len(self.bulletDieL)):
            self.bulletDieR.append(pygame.transform.flip(self.bulletDieL[x],True,False))
        
    def shoot(self,surface,xStill,lftrt):
        self.left = lftrt
        if self.left == 1:
            dim = self.bullet1[0].get_size()
            dimX = dim[0]
            dimY = dim[1]
            self.x += 10
            self.rect = Rect(self.x,self.y + 2 * dimY,dimX,dimY)
            self.bullet1[0].set_colorkey(pygame.Color('white'))
            surface.blit(self.bullet1[0],self.rect)
            self.count += 1
            if self.count == 2:
                self.int += 1
                self.count = 0
            self.times1 += 1
            self.count1 += 1
        if self.left == -1:
            dim = self.bullet2[0].get_size()
            dimX = dim[0]
            dimY = dim[1]
            self.x -= 10
            self.rect = Rect(self.x-85,self.y + 2 * dimY,dimX,dimY)
            self.bullet2[0].set_colorkey(pygame.Color('white'))
            surface.blit(self.bullet2[0],self.rect)
            self.count += 1
            if self.count == 2:
                self.int += 1
                self.count = 0
            self.times1 += 1
            self.count1 += 1
        if self.count1 * 10 == 800:
            self.done = 1
            self.count1 = 0
            self.still = 0
            self.left = 1
            self.x = xStill
        if self.count1 * 10 == 100:
            self.done1 = 1
        if self.die == 1:
            self.dieCount += 1
            if self.dieCount == (2*self.inc)-2:
                self.dieCount = 0
                self.die = 0
                self.x = xStill
                self.left = 1
                self.right = 2
                self.done = 1
                self.done1 = 1
                self.int1 = 0
                self.count1 = 0
                self.rect = Rect(self.x,self.y ,1,1)
                return True
            where = (self.x,self.y)
            if self.right == 1:
                self.bulletDieR[self.int1].set_colorkey(pygame.Color('white'))
                surface.blit(self.bulletDieR[self.int1],where)
                if self.dieCount == self.count4:
                    self.int1 += 1
                    self.count4 += self.inc
            if self.right == 0:
                self.bulletDieL[self.int1].set_colorkey(pygame.Color('white'))
                surface.blit(self.bulletDieL[self.int1],where)
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
        
    def setDir(self,lftrt,xCoord,yCoord):
        self.lftrt = lftrt
        self.x = xCoord
        self.y = yCoord
        self.xStill = xCoord
    
    def update(self,surface,enemy,windowWidth,num):
        if self.active == False:
            if self.x <= windowWidth:
                self.active = True
        else:
            self.shoot(surface,self.xStill,self.lftrt)
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