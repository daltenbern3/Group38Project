import pygame,math
from Platforms import *
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self,platforms,bullet,speed=6,jumph=21,WindowHeight=600):
        pygame.sprite.Sprite.__init__(self)
        self.x=200
        self.y=400
        self.rect=pygame.Rect(self.x,self.y,60,80)
        self.interact=(self.x+30,self.y+80)
        self.platforms=platforms
        self.num=0
        self.bullet=bullet
        self.bullets=pygame.sprite.Group()
        self.bx=0
        self.first=1
        self.moving=False
        self.rate=speed
        self.j=jumph
        self.alive=True
        self.firerate=3
        self.standlist=[]
        self.standlist.append(pygame.image.load('HeroStand1.bmp'))
        self.d=1
        self.motion=2
        self.falling=False
        self.jumping=False
        self.shooting=False
        self.imageover=None
        self.over=False
        self.die = 0
        self.dieCount = 0
        self.int1 = 0
        self.action=[self.walk,self.stand,self.walk,self.jump,self.jump,self.jump]
        self.windowHeight=WindowHeight
          
        
        self.standlist= []
        self.standlist.append(pygame.transform.scale2x(pygame.image.load('HeroStand1.bmp')))
        self.standlisti=[]    
        for i in self.standlist:
            self.standlisti.append(pygame.transform.flip(i,True,False))
            
        self.jumplist=[]
        self.jumplist.append(pygame.transform.scale2x(pygame.image.load('HeroJump1.bmp')))
        self.jumplist.append(pygame.transform.scale2x(pygame.image.load('HeroJump2.bmp')))
        self.jumplist.append(pygame.transform.scale2x(pygame.image.load('HeroJump3.bmp')))
        self.jumplist.append(pygame.transform.scale2x(pygame.image.load('HeroJump4.bmp')))
        self.jumplist.append(pygame.transform.scale2x(pygame.image.load('HeroJump5.bmp')))
        self.jumplisti=[]
        for i in self.jumplist:
            self.jumplisti.append(pygame.transform.flip(i,True,False))
        
        self.walklist=[]
        self.walklist.append(pygame.transform.scale2x(pygame.image.load('HeroWalk1.bmp')))
        self.walklist.append(pygame.transform.scale2x(pygame.image.load('HeroWalk2.bmp')))
        self.walklist.append(pygame.transform.scale2x(pygame.image.load('HeroWalk3.bmp')))
        self.walklist.append(pygame.transform.scale2x(pygame.image.load('HeroWalk4.bmp')))
        self.walklist.append(pygame.transform.scale2x(pygame.image.load('HeroWalk5.bmp')))
        self.walklist.append(pygame.transform.scale2x(pygame.image.load('HeroWalk6.bmp')))
        self.walklisti=[]
        for i in self.walklist:
            self.walklisti.append(pygame.transform.flip(i,True,False))

        self.transition=[pygame.transform.scale2x(pygame.image.load('Transition.bmp'))]
        
        self.shootlist=[pygame.transform.scale2x(pygame.image.load('HeroShoot1.bmp'))]
        self.shootlisti=[]
        for i in self.shootlist:
            self.shootlisti.append(pygame.transform.flip(i,True,False))
        self.shooting=False
        self.k1=-1
        self.k2=0
        self.k3=-1
        self.k4=-1
        self.k5=0
        self.k6=7
        self.k7=10
        self.a=0
        
        self.bugDie = []
        self.bugDieL = []
        self.bugDie.append(pygame.image.load('bugdie1.bmp'))
        self.bugDie.append(pygame.image.load('bugdie2.bmp'))
        self.bugDie.append(pygame.image.load('bugdie3.bmp'))
        for x in range(len(self.bugDie)):
            self.bugDieL.append(pygame.transform.scale2x(self.bugDie[x]))
        
    def moves(self,tuple,screen):
        self.rect.width=tuple[2].get_width()
        self.rect.height=tuple[2].get_height()
        
        self.rect.top=(tuple[1]+self.rect.top)
        self.num=tuple[0]
        tuple[2].set_colorkey(Color('white'))
        screen.blit(tuple[2],self.rect)
        
        self.interact=(self.rect.centerx,self.rect.bottom)
        
    def fall(self):
        self.falling=True
        if self.d==1:
            list=self.jumplist
        else:
            list=self.jumplisti 
           
        if self.over==True:
            image=self.imageover
        else:
            image=list[0]
                
        if self.moving==True:
            k5=self.rate
        else:
            k5=0 
        
        return (self.d*k5,self.rate,image)
    
    def stand(self):
        if self.d==1:
            list=self.standlist
        else:
            list=self.standlisti 
        
        if self.jumping==True:
            self.jumping=False
            if self.d==1:
                list=self.jumplist
            else:
                list=self.jumplisti
                
        if self.over==True:
            image=self.imageover
        else:
            image=list[0]
        return (0,0,image)
    
    def walk(self):
        self.moving=True
        if self.d==1:
            list=self.walklist
        else:
            list=self.walklisti
        
        if self.over==True:
            image=self.imageover
        else:
            image=list[self.k2]
            
        walkingvar = (self.d*self.rate,0,image)
         
        self.k2+=1
         
        if self.k2>=len(list):
            self.k2=0
            
        return walkingvar
    
    def shoot(self):
        if self.d==1:
            list=self.shootlist
        else:
            list=self.shootlisti 
        
        if self.moving==True:
            k2=self.rate
            self.k3=0
        else:
            k2=0
                    
        self.imageover=list[0]
        self.k7=0
        self.over=True
            
        walkingvar = (self.d*k2,0,list[0])
        
        self.makeShot()
        
        self.shooting=False
        
        return walkingvar
        
    def jump(self):
        if self.falling==False:
            self.jumping=True
            
        if self.d==1:
            list=self.jumplist
        else:
            list=self.jumplisti 
            
        if self.moving==True:
            k5=self.rate
        else:
            k5=0 
           
        if self.over==True:
            image=self.imageover
        else:
            image=list[0]
            
        if self.k5>=self.j:
            self.k5=0
            walkingvar = (self.d*k5,-self.rate,image)
            self.jumping=False
            self.motion-=3
        else:
            walkingvar = (self.d*k5,-self.rate,image)
            self.k5+=1
            
        return walkingvar
    
    #def makeShot(self):
                
    def makeShot(self):
        if self.bullet[self.bx].check1() == 1:
            if self.bx == 14:
                self.bx = 0
            self.bx += 1
            self.bullet[self.bx].setDir(self.d,self.rect.left+70,self.rect.top+5)
            self.bullets.add(self.bullet[self.bx])
        '''for x in range(len(self.bullet)):
            if self.bullet[x].check() == 1:
                self.bullets.remove(self.bullet[x])'''
        if self.first == 1:
            self.bullet[self.bx].setDir(self.d,self.rect.left+70,self.rect.top+5)
            self.bullets.add(self.bullet[self.bx])
            self.first = 0
            if self.bx == 15:
                self.bx = 0
            
    def makeGroup(self):
        for x in range(len(self.bullet)):
            if self.bullet[x].check() == 1:
                self.bullets.remove(self.bullet[x])
        return self.bullets
    
    def update(self,enemy,events,screen):
        for i in events:
            if self.jumping==True:
                if i.type==KEYDOWN:
                    if i.key==K_RIGHT:
                        self.moving=True
                        self.d=1
                        self.motion+=1
                    elif i.key==K_LEFT:
                        self.moving=True
                        self.d=-1
                        self.motion-=1
                    if i.key==K_SPACE:
                        self.shooting=True
                if i.type==KEYUP:
                    if i.key==K_RIGHT:
                        self.moving=False
                        self.motion+=1
                    elif i.key==K_LEFT:
                        self.moving=False
                        self.motion-=1
            elif i.type==KEYDOWN:
                self.motion=2
                if i.key==K_RIGHT:
                    self.moving=True
                    self.d=1
                    self.motion=3
                elif i.key==K_LEFT:
                    self.moving=True
                    self.d=-1
                    self.motion=1
                if i.key==K_UP:
                    self.motion+=3
                if i.key==K_SPACE:
                    self.shooting=True
            elif i.type==KEYUP:
                if i.key==K_RIGHT:
                    self.moving=False
                    self.motion-=1
                elif i.key==K_LEFT:
                    self.moving=False
                    self.motion+=1
        
        if self.over==True:
            self.k7 += 1
            if self.k7>=11:
                self.over=False
        
        if self.motion>=7 or self.motion<=0:
            self.motion=2
        
        if enemy != None:
                if bool(pygame.sprite.spritecollideany(self, enemy)) == True:
                    self.die = 1
                    self.alive=False
                    
        if self.rect.centery>=self.windowHeight:
            self.die=1 
                    
        if self.alive == True:
            if self.shooting==True:
                self.moves(self.shoot(),screen)
            
            self.a=0
            for i in self.platforms:
                if bool(i.rect.collidepoint(self.interact))==True or self.jumping==True:
                    self.falling=False
                    self.moves(self.action[self.motion-1](),screen)
                    self.a=1
                    break
            if self.a==0 and self.shooting!=True:
                self.moves(self.fall(),screen)
                
        if self.die == 1:
            self.dieCount += 1
            where = (self.rect.left,self.rect.top)
            self.bugDieL[self.int1].set_colorkey(pygame.Color('white'))
            screen.blit(self.bugDieL[self.int1],where)
            self.alive = False
            if self.dieCount == 1:
                self.int1 += 1
            if self.dieCount == (2*3)-2:
                self.kill()
                self.rect = Rect(0,0,0,0)
                self.die = 0
         
        return self.num, self.die
        