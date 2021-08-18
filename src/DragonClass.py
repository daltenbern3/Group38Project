from pygame.locals import *
import pygame

class Dragon(pygame.sprite.Sprite):
    def __init__(self, xCoord, yCoord,numTimes=6):
        pygame.sprite.Sprite.__init__(self)
        self.x = xCoord
        self.y = yCoord
        self.count4 = 1
        self.inc = 3
        self.int1 = 0
        self.die = 0
        self.dieCount = 0
        self.right = 2
        self.left = 1
        self.int = 0
        self.times = numTimes
        self.times1 = 2
        self.active = False
        self.rect = Rect(xCoord,yCoord,1,1)
        self.count = 1
        self.dragon = []
        self.dragon1 = []
        self.dragon2 = []
        self.dragon.append(pygame.image.load('Dragon1.bmp'))
        self.dragon.append(pygame.image.load('Dragon2.bmp'))
        self.dragon.append(pygame.image.load('Dragon3.bmp'))
        self.dragon.append(pygame.image.load('Dragon4.bmp'))
        self.dragon.append(pygame.image.load('Dragon5.bmp'))
        for x in range(len(self.dragon)):
            self.dragon1.append(pygame.transform.scale2x(self.dragon[x]))
        for x in range(len(self.dragon1)):
            self.dragon2.append(pygame.transform.flip(self.dragon1[x],True,False))
        self.dragonDie = []
        self.dragonDieL = []
        self.dragonDieR = []
        self.dragonDie.append(pygame.image.load('dragondie1.bmp'))
        self.dragonDie.append(pygame.image.load('dragondie2.bmp'))
        self.dragonDie.append(pygame.image.load('dragondie3.bmp'))
        for x in range(len(self.dragonDie)):
            self.dragonDieL.append(pygame.transform.scale2x(self.dragonDie[x]))
        for x in range(len(self.dragonDieL)):
            self.dragonDieR.append(pygame.transform.flip(self.dragonDieL[x],True,False))
        
    def fly(self,surface):
        if self.left == 1:
            dim = self.dragon1[self.int].get_size()
            dimX = dim[0]
            dimY = dim[1]
            self.x -= 5
            self.rect = Rect(self.x,self.y,dimX,dimY)
            self.dragon1[self.int].set_colorkey(pygame.Color('white'))
            surface.blit(self.dragon1[self.int],self.rect)
            self.count += 1
            if self.count == 3:
                self.int += 1
                self.count = 0
            self.times1 += 1
        if self.left == 0:
            dim = self.dragon2[self.int].get_size()
            dimX = dim[0]
            dimY = dim[1]
            self.x += 5
            self.rect = Rect(self.x,self.y,dimX,dimY)
            self.dragon2[self.int].set_colorkey(pygame.Color('white'))
            surface.blit(self.dragon2[self.int],self.rect)
            self.count += 1
            if self.count == 3:
                self.int += 1
                self.count = 0
            self.times1 += 1
        if self.int == 5:#was 5
            if self.times1 == ((self.times * 15)+1):
                if self.left == 1:
                    self.left = 0
                    self.times1 = 1
                elif self.left == 0:
                    self.left = 1
                    self.times1 = 1
            self.int = 0
        if self.die == 1:
            self.dieCount += 1
            if self.dieCount == (2*self.inc)-2:
                self.kill()
                self.rect = Rect(0,0,0,0)
            where = (self.x,self.y)
            if self.right == 1:
                self.dragonDieR[self.int1].set_colorkey(pygame.Color('white'))
                surface.blit(self.dragonDieR[self.int1],where)
                if self.dieCount == self.count4:
                    self.int1 += 1
                    self.count4 += self.inc
            else:
                self.dragonDieL[self.int1].set_colorkey(pygame.Color('white'))
                surface.blit(self.dragonDieL[self.int1],where)
                if self.dieCount == self.count4:
                    self.int1 += 1
    
    def update(self,surface,enemy,windowWidth,num):
        if self.active == False:
            if self.x <= windowWidth:
                self.active = True
        else:
            self.fly(surface)
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