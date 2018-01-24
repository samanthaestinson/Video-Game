
import pygame, sys
from pygame.locals import *

pygame.init()

#Set Screen Dimensions
WIDTH = 700
HEIGHT= 500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Template')

#Define Colour Values
#constants, values that dont change are in capitals
GREEN = (16,179,19)
RED = (255,0,0)
BLUE = (150, 216, 242)
WHITE = (255,255,255)
red= (194,37,58)
brown=(110,68,2)
black=(5,5,5)
grey=(159,160,161)
BROWN=(89,58,3)
g=(196,196,196)
GREYW=(37,38,38)
BLACK = (0,0,0)
WHITE = (255, 255, 255)
BLUE = (81, 144, 232)
WHITE = (255,255,255)
GREY=(110,112,115)
YELLOW=(247,247,96)
DGREY=(84,85,87)
DDGREY=(69,70,71)

yb=[]
xb=[]

class Platform(pygame.sprite.Sprite):
    #constructor
    def __init__(self, picture=None):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.visible = False
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
        self.update()
    
    #spawns the platforms
    def spawn(self, x, y):
        self.x = x-self.rect.width/8
        self.y = y-self.rect.height/2
        self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
        self.visible = True
        self.update()

    #draws the platforms
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
    #updates the platforms
    def update(self):
        self.rect = pygame.Rect(self.x,self.y,self.rect.width,self.rect.height)




#define variables for general here
#create functions here


def background(screen):
    #cave walls
    pygame.draw.rect(screen, GREY, (0,0,800,20),0)
    pygame.draw.rect(screen, GREY, (0,0,20,440),0)
    pygame.draw.rect(screen, GREY, (680,0,20,500),0)
    pygame.draw.polygon(screen, GREY, [[20,20], [20,30], [30,20]], 0)
    pygame.draw.polygon(screen, GREY, [[680,20], [680,30], [670,20]], 0)
    
    pygame.draw.rect(screen, DGREY, (0,0,800,15),0)
    pygame.draw.rect(screen, DGREY, (0,0,15,440),0)
    pygame.draw.rect(screen, DGREY, (685,0,15,500),0)
    pygame.draw.polygon(screen, DGREY, [[15,15], [15,25], [25,15]], 0)
    pygame.draw.polygon(screen, DGREY, [[675,15], [685,25], [700,0]], 0)    
    
    pygame.draw.rect(screen, DDGREY, (0,0,800,10),0)
    pygame.draw.rect(screen, DDGREY, (0,0,10,440),0)
    pygame.draw.rect(screen, DDGREY, (690,0,10,500),0)
    pygame.draw.polygon(screen, DDGREY, [[10,10], [10,20], [20,10]], 0)
    pygame.draw.polygon(screen, DDGREY, [[680,10], [690,10], [690,20]], 0)
    
def sandfloor(screen):
    xc=0
    for i in range(0,6):
        pygame.draw.circle(screen, YELLOW, (xc,980),500,0)
        xc=xc+150
        
def greyRect(screen):
    for i in range(len(platformX)):
        yb.append(platformY[i]+2)
        xb.append(platformX[i])
        pygame.draw.rect(screen, GREY, (xb[i],yb[i], 87 , 10),0)


#function that redraws the screen
def redraw_screen():
    #filling colour of screen 
    screen.fill(BLUE)
    
    #drawing commands
    #call functions here

    background(screen)
    sandfloor(screen)
    greyRect(screen)
    
    #updating

    
    for platform in platforms:
        platform.draw(screen)


    pygame.display.update()

#the platform
#horizontal platform lists
platforms = []
#x values
platformX = [10,50,110,160,75,400,480,550,604,495,604,315,540]
#y values
platformY = [400,100,100,100,300,225,225,225,225,145,75,355,430]
#spawing the platform 
for i in range(len(platformX)):
    platform = Platform("newPlatform.png")
    platform.spawn(platformX[i],platformY[i])
    #adding object created, so its in a list of objects
    platforms.append(platform)



inPlay = True
print "Hit ESC to end the program."

while inPlay:
    #deals with any keyboard options once program is run
    #looks for the event (action of using keyboard)
    pygame.event.get()
    #generates a True/False list for the status of all keys
    keys = pygame.key.get_pressed()     
    
    #looks for escape to be pressed
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    
    #keyboard commands
    
    #animation commands



    
    redraw_screen()                    
    pygame.time.delay(2)                # pause for 2 miliseconds
#---------------------------------------#                                        
pygame.quit()                           # always quit pygame when done!
