from pygame.locals import *
import pygame

class Bug(pygame.sprite.Sprite):
    def __init__(self, xCoord, yCoord,numTimes=5):
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
        self.bug = []
        self.bug1 = []
        self.bug2 = []
        self.bug.append(pygame.image.load('bug 1L.bmp'))
        self.bug.append(pygame.image.load('bug 2L.bmp'))
        self.bug.append(pygame.image.load('bug 3L.bmp'))
        self.bug.append(pygame.image.load('bug 4L.bmp'))
        self.bug.append(pygame.image.load('bug 5L.bmp'))
        self.bug.append(pygame.image.load('bug 6L.bmp'))
        for x in range(len(self.bug)):
            self.bug1.append(pygame.transform.scale2x(self.bug[x]))
        for x in range(len(self.bug1)):
            self.bug2.append(pygame.transform.flip(self.bug1[x],True,False))
        self.bugDie = []
        self.bugDieL = []
        self.bugDieR = []
        self.bugDie.append(pygame.image.load('bugdie1.bmp'))
        self.bugDie.append(pygame.image.load('bugdie2.bmp'))
        self.bugDie.append(pygame.image.load('bugdie3.bmp'))
        for x in range(len(self.bugDie)):
            self.bugDieL.append(pygame.transform.scale2x(self.bugDie[x]))
        for x in range(len(self.bugDieL)):
            self.bugDieR.append(pygame.transform.flip(self.bugDieL[x],True,False))
        self.numOfFrames = len(self.bug)-1
        
    def Pace(self,surface):
        if self.left == 1:
            dim = self.bug1[self.int].get_size()
            dimX = dim[0]
            dimY = dim[1]
            self.x -= 5
            self.rect = Rect(self.x,self.y,dimX,dimY)
            self.bug1[self.int].set_colorkey(pygame.Color('white'))
            surface.blit(self.bug1[self.int],self.rect)
            self.count += 1
            if self.count == 3:
                self.int += 1
                self.count = 0
            self.times1 += 1
        if self.left == 0:
            dim = self.bug2[self.int].get_size()
            dimX = dim[0]
            dimY = dim[1]
            self.x += 5
            self.rect = Rect(self.x,self.y,dimX,dimY)
            self.bug2[self.int].set_colorkey(pygame.Color('white'))
            surface.blit(self.bug2[self.int],self.rect)
            self.count += 1
            if self.count == 3:
                self.int += 1
                self.count = 0
            self.times1 += 1
        if self.int == self.numOfFrames:#was 5
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
            where = (self.x,self.y)
            if self.right == 1:
                self.bugDieR[self.int1].set_colorkey(pygame.Color('white'))
                surface.blit(self.bugDieR[self.int1],where)
                if self.dieCount == self.count4:
                    self.int1 += 1
                    self.count4 += self.inc
            else:
                self.bugDieL[self.int1].set_colorkey(pygame.Color('white'))
                surface.blit(self.bugDieL[self.int1],where)
                if self.dieCount == self.count4:
                    self.int1 += 1
    
    def update(self,surface,enemy,windowWidth,num):
        if self.active == False:
            if self.x <= windowWidth:
                self.active = True
        else:
            self.Pace(surface)
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