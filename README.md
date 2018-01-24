# Video-Game
Platform Game
#Samantha Stinson
#May 16, 2016
#Final Exam Project
#Gillagins Adventure Under The Sea

#-----------------------------------------------------------------------------------------------------------------------
#importing commands
#importing random
import random
#importing pygame
import pygame

#-----------------------------------------------------------------------------------------------------------------------
#initalizing pygame
pygame.init()

#-----------------------------------------------------------------------------------------------------------------------
##introduction statement
#print "\n                        Gilligan's Adventure Under The Sea"
#print "\nGilligan is going snorkeling for treasures under the sea."
#name=raw_input("\nEnter your name:")
#print "Press enter to begin the game after you have read the instructions."
#"\n\n3,2,1... Begin!!!"

#-----------------------------------------------------------------------------------------------------------------------
#setting screen
#dimensions
WIDTH = 700
HEIGHT= 500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
#screen caption
pygame.display.set_caption("Gilligan's Adventure Under The Sea")

#-----------------------------------------------------------------------------------------------------------------------
#defining colour values
BLACK = (0,0,0)
WHITE = (181, 181, 181)
BLUE = (81, 144, 232)
WHITE = (255,255,255)
GREY=(110,112,115)
YELLOW=(247,247,96)
DGREY=(84,85,87)
DDGREY=(69,70,71)

#-----------------------------------------------------------------------------------------------------------------------
#global values
GROUND = HEIGHT-10
GRAVITY = 2
RUN_SPEED = 10
JUMP_SPEED = -20
score=0
treasureGroup = pygame.sprite.Group()
ended=False
lives=3
count=0
gameLevel=1
enemyx=[]
enemyy=[]
platformX=[]
platformY=[]

#-----------------------------------------------------------------------------------------------------------------------
#classes
#player class
class Player(pygame.sprite.Sprite):
    #constructor
    def __init__(self, picture=None):
        pygame.sprite.Sprite.__init__(self)
        #coordinates
        self.x = 0
        self.y = 0
        #speed
        self.vx = 0
        self.vy = 0
        #state that allows image to be seen or not seen, so not allowed to be seen untill spawned/created
        self.visible = False
        #default is loading a blank pic
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
        #updating
        self.update()

    #creator of player  
    def spawn(self, x, y):
        #changing the co-ordinates so that they are in the center of the object--player
        self.x = x-self.rect.width//2
        self.y = y-self.rect.height//2
        #co-ordinating the properties to the rectangle shape
        self.rect = pygame.Rect(self.x, self.y, self.rect.width//1.5, self.rect.height//1.5)
        #allows the object--player to be visible
        self.visible = True
        #updating
        self.update()
    
    def setImage(self, newImage):
        self.image = pygame.image.load(newImage)
        self.rect = self.image.get_rect()
    
    #draws the player
    def draw(self, surface):
        #rectangle image on the screen
        surface.blit(self.image, self.rect)

    #new dimensions
    #creates and updates the new dimensions for the image of player  
    def update(self):
        self.rect = pygame.Rect(self.x,self.y,self.rect.width,self.rect.height)

    #makes the player run
    def run(self):
        self.x=self.x+self.vx
        self.update()
        
    #makes the player stop
    def stop(self):
        self.vx=0
    
    #makes player fall
    def fall(self):
        self.y=self.y+self.vy
        self.update()

    #allows to send how much you want to move, steps to move
    #the moving motions after a button is clicked
    ##the motion of the player horizontally
    def nudge(self, horizontal_kick):
        self.vx=horizontal_kick
        
    #lets the player jump
    def jump(self, vertical_kick):
        self.vy=vertical_kick
    
    #always accellerate
    def accellerate(self, gravity):
        self.vy=self.vy + gravity
    
    #have we reached platform
    def settle_on(self, level):
        self.y=level-self.rect.height
        self.vy=0
        self.update()
        
    #if i am on a surface true or false
    def settled_on(self, level):
        return self.y + self.rect.height == level and self.vy == 0
        #returning 2 variables
    
    #values above/below
    def above(self, level):
        return self.y+self.rect.height<=level

    def below(self, level):
        return self.y+self.rect.height>level

    #Check dimensions of the next rectangle, see what we have reached
    def next_rect(self):
        return pygame.Rect(self.x+self.vx, self.y+self.vy, self.rect.width, self.rect.height)
    
    #kills the player when they collide with the enemy
    def kill(self):
        if lives>1:
            self.x=WIDTH/2
            self.y=HEIGHT/2
        if lives==1:
            self.x=800
            self.y=800
        self.update
    
    #boundries
    #keeps the player inside the screen
    def bumpF(self):
        player.x=player.x+10
    
    def bumpB(self):
        player.x=player.x-10
        
#-----------------------------------------------------------------------------------------------------------------------
#platform class
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

#-----------------------------------------------------------------------------------------------------------------------
#treasure class
class Treasure(pygame.sprite.Sprite):
    #constructor
    def __init__(self, picture=None):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.visible = False
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
        self.update()
    
    #spawns the treasure
    def spawn(self, x, y):
        self.x = x-self.rect.width/2
        self.y = y-self.rect.height/2
        self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
        self.visible = True
        self.update()

    #draws the treasure
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    #resets the position of the treasure so they are off screen
    def reset_position(self):
        self.x=800
        self.y=800
    
    #updates the chest
    def update(self):
        self.rect = pygame.Rect(self.x,self.y,self.rect.width,self.rect.height)

#-----------------------------------------------------------------------------------------------------------------------
#chest class
class Chest(pygame.sprite.Sprite):
    #constructor
    def __init__(self, picture=None):
        pygame.sprite.Sprite.__init__(self)
        self.x = 335
        self.y = 475
        self.visible = False
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
        self.update()

    #spawns the chest
    def spawn(self, x, y):
        self.x = x-self.rect.width/2
        self.y = y-self.rect.height/2
        self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
        self.visible = False
        self.update()

    #draws the chest
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    #updates the chest
    def update(self):
        self.rect = pygame.Rect(self.x,self.y,self.rect.width,self.rect.height)
    
#-----------------------------------------------------------------------------------------------------------------------
class Enemy(pygame.sprite.Sprite):
    #constructor
    def __init__(self, picture=None):
        pygame.sprite.Sprite.__init__(self)
        self.x = 35
        self.y = HEIGHT-15
        self.vx=5
        self.visible = False
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
        self.update()
    
    #spawns the enemy
    def spawn(self, x, y):
        self.x = x-self.rect.width/2
        self.y = y-self.rect.height/2
        self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
        self.visible = True
        self.update()
    
    #draws the enemy
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    #updates the enemy  
    def update(self):
        self.rect = pygame.Rect(self.x,self.y,self.rect.width,self.rect.height)
    
    #moves the enemy
    def move(self):
        self.x=self.x+self.vx
    
    #it is the constant movement of the enemy in the area it is pertained to 
    def movement(self):
        if self.x<=WIDTH+10 or self.x>0:
            self.vx=self.vx
        if self.x>WIDTH-25 or self.x<0:
            self.vx=-(self.vx)
    
    #keeps the enemy at rest
    def stop(self):
        self.x=0
    
#----------------------------------------------------------------------------------------------------------------------
#background drawing functions
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

#-----------------------------------------------------------------------------------------------------------------------
#redraw function
#function that redraws all objects
#draw in redraw
def redraw_screen():
    #filling colour of screen 
    screen.fill(BLUE)
    #drawing commands
    #draws the instruction cover
    if count==0:
        title="title.png"
        titleImage= pygame.image.load(title)
        screen.blit(titleImage, (0,0))
    
    if count==1:
        cover="cover.png"
        coverImage= pygame.image.load(cover)
        screen.blit(coverImage, (0,0))
    
    #draws the game
    if count>1:
        #drawing the background image
        background(screen)
        sandfloor(screen)
        greyRect(screen)
    
        #drawing platform images
        for platform in platforms:
            platform.draw(screen)
        
        #drawing the treasure
        treasureGroup.draw(screen)
        
        #drawing the enemy
        for enemy in enemies:
            enemy.draw(screen)
    
        #stamping the image of lives hearts
        NumberOfHearts=["no lives.png","1 lives.png","2 lives.png","3 lives.png"] 
        livesImages= pygame.image.load(NumberOfHearts[lives])
        screen.blit(livesImages, (625,3))
        
        #if 11 diamonds are collected, then draw the treasure chest
        if score>=11:
            chest.draw(screen)
        
        #stamping the text of the title
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Gilligan's Adventure Under The Sea",True,WHITE)
        screen.blit(text, [200, 2])
        
        #stamping the text for the lives
        fontL = pygame.font.SysFont('Calibri', 25, True, False)
        text = fontL.render("Lives:",True,WHITE)
        screen.blit(text, [570,2])
        
        #drawing the player
        player.draw(screen)
        if ended==True:
            pygame.draw.rect(screen, WHITE, (0,0,800,800),0)
    
    #updating the program
    pygame.display.update()
    
#-----------------------------------------------------------------------------------------------------------------------
#main program starts here

def levelOne():
    #x values
    platformX = [12,180,144,75,574,490,604,100,300,204,140,400,544,12,590,336,480,512,602,47]
    #y values
    platformY = [420,320,320,280,60,60,60,50,220,140,140,350,420,200,200,220,350,350,200,420]
    enemyx=[20]
    enemyy=[HEIGHT-23]
    
    return platformX, platformY,enemyx,enemyy

def levelTwo():
    platformX = [10,50,110,160,75,400,480,550,604,495,604,315,540]
    #y values
    platformY = [400,100,100,100,300,225,225,225,225,145,75,355,430]
    enemyx=[20, 50]
    enemyy=[HEIGHT-23,200]
    return platformX,platformY,enemyx,enemyy

#-----------------------------------------------------------------------------------------------------------------------

#player
#creates the player
#movement is the variable that changes the image when the direction of the character changes
movement="main_character.png"
player = Player(movement)
#spawning player
player.spawn(350,475)

#-----------------------------------------------------------------------------------------------------------------------
#the enemy
#creates the enemy
enemies = []

for i in range(0,len(enemyx)):
    enemy = Enemy("crab.png")
    #spawning player
    enemy.spawn(enemyx[i],enemyy[i])
    enemies.append(enemy)

#-----------------------------------------------------------------------------------------------------------------------
#the platform
#horizontal platform lists
platforms = []

for i in range(len(platformX)):
    platform = Platform("newPlatform.png")
    platform.spawn(platformX[i],platformY[i])
    #adding object created, so its in a list of objects
    platforms.append(platform)

##vertical
#platforms_v=[]
#platformY_v=[245,345,60,125,300,400,10]
#platformX_v=[130,530,270,520,480,300,375]

#-----------------------------------------------------------------------------------------------------------------------
#the treasure
#treasure lists
treasures=[]
#x values
tX=[35,45,120,245,600,575,425,670,600,355,215]
#y values
tY=[175,395,255,295,395,330,330,175,35,200,120]

#creates the treasure
for i in range(0,11):
    if i==0:
        treasure = Treasure("blueD.png")
    if i==1:
        treasure = Treasure("purpleD.png")
    if i==2:
        treasure = Treasure("greenD.png")
    if i==3:
        treasure = Treasure("whiteD.png")
    if i==4:
        treasure = Treasure("pinkD.png")
    if i==5:
        treasure = Treasure("blueD.png")
    if i==6:
        treasure = Treasure("purpleD.png")
    if i==7:
        treasure = Treasure("greenD.png")
    if i==8:
        treasure = Treasure("whiteD.png")
    if i==9:
        treasure = Treasure("pinkD.png")
    if i==10:
        treasure = Treasure("blueD.png")
        
    #spawns the treasure
    treasure.spawn(tX[i],tY[i])
    #adding object created, so its in a list of objects
    treasures.append(treasure)
    treasureGroup.add(treasure)
 
#-----------------------------------------------------------------------------------------------------------------------          
#chest
#creates the chest
chest=Chest("finalChest.png")
#spawning chest if 11 diamonds are collected
if score>=11:
    chest.spawn(335,475)
    #sets the image to visable too
    chest.visible == False

#-----------------------------------------------------------------------------------------------------------------------
#the running part of program
level = GROUND  
clock = pygame.time.Clock()
FPS = 30
inPlay = True

#-----------------------------------------------------------------------------------------------------------------------
#keyboard commands
while inPlay:
    clock.tick(FPS)            
    pygame.event.get()
    keys = pygame.key.get_pressed()     
    
    #looks at if the escape key is pressed
    if keys[pygame.K_ESCAPE]:
        inPlay = False
        
    if keys[pygame.K_RETURN]:
        count=count+1
    
    #the up button is pressed
    if keys[pygame.K_UP] and player.settled_on(level)==True: #boolean
        #defines the image of the player based on its movement
        player.setImage("up.png")
        player.jump(JUMP_SPEED)
        #updates the player
        player.update()
        
    #the right button is pressed
    elif keys[pygame.K_RIGHT]:
        #defines the image of the player based on its movement
        player.setImage("right.png")
        player.nudge(RUN_SPEED)
        #updates the player
        player.update()

    #the left button is pressed
    elif keys[pygame.K_LEFT]:
        #defines the image of the player based on its movement
        player.setImage("left.png")
        player.nudge(-RUN_SPEED)
        #updates the player
        player.update()
    
    #nothing is pressed  
    else:
        player.stop()
        #defines the image of the player based on its movement
        player.setImage("main_character.png")
        #updates the player
        player.update()
    
    #if the game hasnt started yet, keep the enemy at rest
    #if count<=1:
        #enemy.stop()
    
    #if the game has started, let the enemy move
    if count>1:
        if gamelevel==0:
            platformX, platformY,enemyx,enemyy=levelOne()
        
        if gamelevel==1:
            platformX, platformY,enemyx,enemyy=levelTwo()    
        
        #starts the movement of the enemy
        enemy.move()
        enemy.movement()
        #updates the movement
        enemy.update()

    #makes the player move
    #horizontal motion
    player.run()
    #vertical motion
    player.accellerate(GRAVITY)
    
    #updates the diamonds
    treasureGroup.update()

    #checks to see if the player is above or has collided with platform
    for platform in platforms:
        if player.above(platform.y) and player.next_rect().colliderect(platform):
            level=platform.y
            player.settle_on(level)
    
    #allows the player to fall
    player.fall()
    
    #checks if the player is on the ground level
    if player.below(GROUND):
        level=GROUND
        #if so, settle
        player.settle_on(level)
    
    #checks to see if the player has collided with the enemy
    if player.next_rect().colliderect(enemy):
        #if its collided, the player is killed
        player.kill()
        #one life is lost
        lives=lives-1
        #lives print statement cost
        print "\n\nYou lost one life! \nlives:",lives
        
    #removes the treasure if the player has hit it
    treasure_hit = pygame.sprite.spritecollide(player, treasureGroup, True)
 
    #checks the collisions of the diamonds
    for treasure in treasure_hit:
        #keeps the score of the diamonds
        score += 1
        #score print statement
        print "\nDiamonds collected:", score, "/11"
        #resets the treasures position once collected
        treasure.reset_position()
    
    #checks to see if the player has collided with the treasure chest and that there is 11 diamonds collected
    if player.next_rect().colliderect(chest) and score>10:
        gameLevel=gameLevel+1
    
    #if there are no lives left, the game ends 
    if lives<1:
        #once inplay is false, the program ends
        inPlay=False
        #print statement
        print "\n\nGame Over!\nSorry", name,", YOU LOST!\n\n"

    #boundries horizontal
    if player.x>=WIDTH-25:
        player.bumpB()
    if player.x<=-5:
        player.bumpF()
    player.update()
    


    #redraws the screen
    redraw_screen()
#-----------------------------------------------------------------------------------------------------------------------
#quits the program
pygame.quit()
