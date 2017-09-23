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
pusheen1L = pygame.image.load('pusheenWalk-1L.png') #100x65
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
donut = pygame.image.load('donut.png')

# Other settings
scrn = 2
pusheenDir = "R"
pusheenLoc = [0,580]
pusheenNum = 1
pusheenNow = pusheen1R
collected = [False,False,False,False,False]
score = 0

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
        screen.blit(tree,(900,450))
        screen.blit(frame,(580,350))
        rect(WHITE,530,430,200,10)
        screen.blit(cupboard,(645,120))

    # Score Screen
    elif scrn == 3:
        pass

def boundaries():
    if pusheenLoc[0] + 100 > 256 and pusheenLoc[0] < 492 and pusheenLoc[1] +65 > 540 and pusheenLoc[1] < 545:
        pusheenLoc[1] = 542-65
        return "Table"
    if pusheenLoc[0] +100 > 530 and pusheenLoc[0] < 730 and pusheenLoc[1]+65 > 430 and pusheenLoc[1] < 435:
        pusheenLoc[1] = 430-65
        return "Shelf"
    else:
        return "Floor"
        



def jump(maxH):
    if pusheenLoc[1] >= maxH + 120:
        while pusheenLoc[1] >= maxH:
            pusheenLoc[1] += -2
            if keys[pygame.K_LEFT]:
                    pusheenLoc[0] += -1
            elif keys[pygame.K_RIGHT]:
                    pusheenLoc[0] += 1
            redraw_screen()

def character():
    screen.blit(pusheenNow,(pusheenLoc[0],pusheenLoc[1]))

def collect(donutx,donuty):
    global score
    collectNow = False
    if pusheenLoc[0] + 100 > donutx and pusheenLoc[0] < donutx + 20 and pusheenLoc[1] + 65 > donuty and pusheenLoc[1] < donuty + 20:
        collectNow = True
        score += 1

    return collectNow,score

def donutBlit():
    if collected[0] == False:
        screen.blit(donut,(300,500))
        collected[0],score = collect(300,500)
    if collected[1] == False:
        screen.blit(donut,(610,400))
        collected[1],score = collect(610,400)
    if collected[2] == False:
        screen.blit(donut,(900,560))
        collected[2],score = collect(900,560)
    if collected[3] == False:
        screen.blit(donut,(670,160))
        collected[3],score = collect(670,160)
    if collected[4] == False:
        screen.blit(donut,(1150,80))
        collected[4],score = collect(1150,80)


    # printscore = font.render("Score: "+str(score),False,WHITE)
    # screen.blit(printscore,[500,450])

# Redraws the screen
def redraw_screen():
    background()
    character()
    donutBlit()
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



    place = boundaries()

    if keys[pygame.K_RIGHT]:
        if pusheenLoc[0] <= WIDTH-35:
            pusheenLoc[0] += 2
        while keys[pygame.K_RIGHT]:
            if pusheenNum <= 10:
                pusheenNow = pusheen1R
        
            elif pusheenNum > 10 and pusheenNum <= 20:
                pusheenNow = pusheen2R
                
            elif pusheenNum > 20 and pusheenNum <= 30:
                pusheenNow = pusheen3R
                
            elif pusheenNum > 30 and pusheenNum <= 40:
                pusheenNow = pusheen4R
                
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
                pusheenNow = pusheen1L
                
            elif pusheenNum > 10 and pusheenNum <= 20:
                pusheenNow = pusheen2L
                
            elif pusheenNum > 20 and pusheenNum <= 30:
                pusheenNow = pusheen3L
                
            elif pusheenNum > 30 and pusheenNum <= 40:
                pusheenNow = pusheen4L
                 
            if pusheenNum <= 40:
                pusheenNum += 1
            else:
                pusheenNum = 1
            break
        pusheenDir = "L"

    if keys[pygame.K_UP]:
        if place == "Floor":
            jump(450)
        elif place == "Table":
            jump(350)
        elif place == "Shelf":
            jump(200)

    if pusheenLoc[1] < 580:
        pusheenLoc[1] += 3


    #global variables for position values
    redraw_screen()                     # the screen window must be constantly redrawn - animation
    pygame.time.delay(4)                # pause for 2 miliseconds
                                        
pygame.quit()                           # always quit pygame when done!

