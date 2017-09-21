# Denise Lee
# 20 September 2017
# pusheen-the-game.py
# A1 Project

import pygame, sys
from pygame.locals import *
import random

pygame.init()

# Screen Dimensions
WIDTH = 1280
HEIGHT= 700
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Pusheen the Game')

# Colours
GREEN = (0,255,0)
GRASSGREEN = (31,155,70)
RED = (255,0,0)
PINK = (255, 183, 237)
BLUE = (119,169,249)
SKYBLUE = (206, 225, 255)
WHITE = (255,255,255)
BLACK = (0,0,0)

# Fonts
font = pygame.font.SysFont('Comic Sans MS',20,False,False)
tfont = pygame.font.SysFont('Comic Sans MS',60,True,False)

# Images
pusheen1L = pygame.image.load('pusheenWalk-1L.png')
pusheen2L = pygame.image.load('pusheenWalk-2L.png')
pusheen3L = pygame.image.load('pusheenWalk-3L.png')
pusheen4L = pygame.image.load('pusheenWalk-4L.png')
pusheen1R = pygame.image.load('pusheenWalk-1R.png')
pusheen2R = pygame.image.load('pusheenWalk-2R.png')
pusheen3R = pygame.image.load('pusheenWalk-3R.png')
pusheen4R = pygame.image.load('pusheenWalk-4R.png')

table = pygame.image.load('table.png')
tree = pygame.image.load('tree.png')
frame = pygame.image.load('frame.jpg')
cupboard = pygame.image.load('cupboard.png')

# Other settings
scrn = 2
pusheenDir = "R"
pusheenLoc = [0,580]
pusheenNum = 1
pusheenNow = pusheen1R

def rect(colour,x,y,w,h):
    pygame.draw.rect(screen,colour,(x,y,w,h),0)
# function header
# Blits background for multiple screens

def background():
    screen.fill(SKYBLUE)
    # Title Screen
    if scrn == 0:
        pass
    # Instructions
    elif scrn == 1:
        pass
    # Gameplay
    elif scrn == 2:
        # Walls
        rect(WHITE,0,0,32,680)
        rect(WHITE,1216,0,64,680)
        # Floor
        rect(BLUE,0,620,WIDTH,100)
        # Furniture
        screen.blit(table,(256,540))
        screen.blit(tree,(736,450))
        screen.blit(frame,(620,400))
        screen.blit(cupboard,(700,120))

    # Score Screen
    elif scrn == 3:
        pass

def boundaries():
    if pusheenLoc[0] > 450 and pusheenLoc[0] < 550:
        pass
    if pusheenLoc[1] < 600:
        pusheenLoc[1] += 3

def character():
    screen.blit(pusheenNow,(pusheenLoc[0],pusheenLoc[1]))

def donut():
     
    collected,score = collect()
    
    if collected == False:
        scrn.blit(donut,(300,300))

    printscore = font.render("Score: "+str(score),False,WHITE)
    scrn.blit(printscore,[500,450])

# Redraws the screen
def redraw_screen():
    background()
    character()
    pygame.display.update()


# Main Program

inPlay = True
print "Hit ESC to end the program."
while inPlay:
    # Gets event
    pygame.event.get()
    keys = pygame.key.get_pressed()     
    
    #Quit game
    if keys[pygame.K_ESCAPE]:
        inPlay = False
        
    
    if screen == 0:
        if keys[pygame.K_RETURN]:
            screen = 1
            pusheenLoc = [0,580]


    if keys[pygame.K_RIGHT]:
        if pusheenLoc[0] <= WIDTH-35:
            pusheenLoc[0] += 2
        while keys[pygame.K_RIGHT]:
            if pusheenNum <= 10:
                pusheenNow = pusheen2R
        
            elif pusheenNum > 10 and pusheenNum <= 20:
                pusheenNow = pusheen3R
                
            elif pusheenNum > 20 and pusheenNum <= 30:
                pusheenNow = pusheen4R
                
            elif pusheenNum > 30 and pusheenNum <= 40:
                pusheenNow = pusheen1R
                
            if pusheenNum <= 40:
                pusheenNum += 1
            else:
                pusheenNum = 1
            break
        pusheenDir = "R"
    if keys[pygame.K_LEFT]:
        if pusheenLoc[0] >= 0:
            pusheenLoc[0] += -2
        while keys[pygame.K_LEFT]:
            if pusheenNum <= 10:
                pusheenNow = pusheen2L
                
            elif pusheenNum > 10 and pusheenNum <= 20:
                pusheenNow = pusheen3L
                
            elif pusheenNum > 20 and pusheenNum <= 30:
                pusheenNow = pusheen4L
                
            elif pusheenNum > 30 and pusheenNum <= 40:
                pusheenNow = pusheen1L
                
            if pusheenNum <= 40:
                pusheenNum += 1
            else:
                pusheenNum = 1
            break
        pusheenDir = "L"
    if keys[pygame.K_UP]:
        if pusheenLoc[1] >= 550:
            if keys[pygame.K_LEFT]:
                while pusheenLoc[1] >= 400:
                    pusheenLoc[1] += -2
                    pusheenLoc[0] += -1
                    redraw_screen()
            elif keys[pygame.K_RIGHT]:
                while pusheenLoc[1] >= 400:
                    pusheenLoc[1] += -2
                    pusheenLoc[0] += 1
                    redraw_screen()
            else:
                while pusheenLoc[1] >= 400:
                    pusheenLoc[1] += -2
                    redraw_screen()



    #global variables for position values
    redraw_screen()                     # the screen window must be constantly redrawn - animation
    pygame.time.delay(4)                # pause for 2 miliseconds
#---------------------------------------#                                        
pygame.quit()                           # always quit pygame when done!

