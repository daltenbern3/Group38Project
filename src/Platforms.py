import pygame
from pygame import color

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,w):
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.w=w
        self.h=30
        self.image=pygame.transform.scale(pygame.image.load('Platform1.bmp'),(self.w,self.h))
        
        self.rect=pygame.Rect(x,y,w,self.h)
    def draws(self,win,winrect):
        if self.rect.colliderect(winrect)==True or winrect.contains(self.rect)==True:
            win.blit(self.image,self.rect)
            #pygame.draw.rect(win,pygame.Color('green'),self.rect)
    def update(self,win,winrect,rate):
        self.draws(win,winrect)
        self.rect.left-=rate