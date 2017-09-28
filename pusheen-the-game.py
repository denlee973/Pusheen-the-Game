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
pusheenL = [pusheen1L,pusheen2L,pusheen3L,pusheen4L]

pusheen1R = pygame.image.load('pusheenWalk-1R.png')
pusheen2R = pygame.image.load('pusheenWalk-2R.png')
pusheen3R = pygame.image.load('pusheenWalk-3R.png')
pusheen4R = pygame.image.load('pusheenWalk-4R.png')
pusheenR = [pusheen1R,pusheen2R,pusheen3R,pusheen4R]

dpusheen1 = pygame.image.load('donutPusheen-1.png')
dpusheen2 = pygame.image.load('donutPusheen-2.png')
dpusheen3 = pygame.image.load('donutPusheen-3.png')
dpusheen4 = pygame.image.load('donutPusheen-4.png')

rat1 = pygame.image.load('rat1.png')
rat2 = pygame.image.load('rat2.png')
rat3 = pygame.image.load('rat3.png')
rat4 = pygame.image.load('rat4.png')
rat5 = pygame.image.load('rat5.png')
ratR = [rat1,rat2,rat3,rat4,rat5]

rat1L = pygame.image.load('rat1L.png')
rat2L = pygame.image.load('rat2L.png')
rat3L = pygame.image.load('rat3L.png')
rat4L = pygame.image.load('rat4L.png')
rat5L = pygame.image.load('rat5L.png')
ratL = [rat1L,rat2L,rat3L,rat4L,rat5L]

table = pygame.image.load('table.png')
tree = pygame.image.load('tree.png')
frame = pygame.image.load('frame.jpg')
cupboard = pygame.image.load('cupboard.png')
donut = pygame.image.load('donut.png')

# Other settings
scrn = 2
ratDir = "L"
ratLoc = [1280,105]
ratNum = 1
ratNow = rat1
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

def background(scrn):
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
        rect(WHITE,755,135,80,120)
        rect(RED,755,200,80,5)

    # Score Screen
    elif scrn == 3:
        congrats = tfont.render("CONGRATULATIONS!",False,WHITE)
        screen.blit(congrats,(300,200))
        screen.blit(dpusheen1,(500,300))

def boundaries():
    if pusheenLoc[0] + 100 > 256 and pusheenLoc[0] < 492 and pusheenLoc[1] + 65 > 540 and pusheenLoc[1] < 545:
        pusheenLoc[1] = 542-65
        return "Table"
    elif pusheenLoc[0] + 100 > 530 and pusheenLoc[0] < 730 and pusheenLoc[1] + 65 > 430 and pusheenLoc[1] < 435:
        pusheenLoc[1] = 430-65
        return "Shelf"
    elif pusheenLoc[0] + 100 > 655 and pusheenLoc[0] < 1055 and pusheenLoc[1] + 65 > 255 and pusheenLoc[1] < 260:
        pusheenLoc[1] = 260-65
        return "Cupboard1"
    elif pusheenLoc[0] + 100 > 655 and pusheenLoc[0] < WIDTH and pusheenLoc[1] + 65 > 120 and pusheenLoc[1] < 125:
        pusheenLoc[1] = 120-65
        return "Cupboard2"

    elif pusheenLoc[1] + 65 > 612:
        if pusheenDir == "R" and pusheenLoc[0] + 100 > 925 and pusheenLoc[0] + 100 < 930:
            pusheenLoc[0] = 925-100
        elif pusheenDir == "L" and pusheenLoc[0] < 995 and pusheenLoc[0] > 990:
            pusheenLoc[0] = 1000
        return "Floor"

    elif pusheenLoc[0] + 100 > 925 and pusheenLoc[0] < 995 and pusheenLoc[1] + 65 < 580 and pusheenLoc[1] +65 > 570:
        pusheenLoc[1] = 570-65
        return "Pot"

    else:
        return "Floor"
        
def animation(num,now,images,incr):
    max = len(images)
    for i in range(max):
        if num > i*incr and num <= (i+1)*incr:
            now = images[i]
            break
    if num <= max*incr:
        num += 1
    else:
        num = 1
    return num,now

def enemy():
    global ratDir
    global ratNum
    global ratNow
    if ratDir == "L":
        ratNum,ratNow = animation(ratNum,ratNow,ratL,10)
        screen.blit(ratNow,(ratLoc[0],ratLoc[1]))
        ratLoc[0] += -2
        if ratLoc[0] < 650 and ratLoc[0] > 640:
            ratDir = "R"
            print "YOOOOOO"

    if ratDir == "R":
        ratNum,ratNow = animation(ratNum,ratNow,ratR,10)
        screen.blit(ratNow,(ratLoc[0],ratLoc[1]))
        ratLoc[0] += 2
        if ratLoc[0] < 1280 and ratLoc[0] > 1270:
            ratDir = "L"
    print ratDir, ratLoc[0]

def shoot():
    x = pusheenLoc[0] 
    y = pusheenLoc[1]

    if pusheenDir == "R":
        rect(WHITE,200,200,500,500)
        print x,y

    else:
        rect(WHITE,x,y,50,5)
    redraw_screen()

def jump(maxH):
    if pusheenLoc[1] >= maxH + 120:
        while pusheenLoc[1] >= maxH:
            pusheenLoc[1] += -2
            if keys[pygame.K_LEFT]:
                    pusheenLoc[0] += -1
            elif keys[pygame.K_RIGHT]:
                    pusheenLoc[0] += 1
            redraw_screen()

def character(scrn):
    if scrn == 2:
        screen.blit(pusheenNow,(pusheenLoc[0],pusheenLoc[1]))

def collect(donutx,donuty):
    global score
    collectNow = False
    if pusheenLoc[0] + 100 > donutx and pusheenLoc[0] < donutx + 20 and pusheenLoc[1] + 65 > donuty and pusheenLoc[1] < donuty + 20:
        collectNow = True
        score += 1

    return collectNow,score

def donutBlit():
    global score
    if collected[0] == False:
        screen.blit(donut,(300,500))
        collected[0],score = collect(300,500)
    if collected[1] == False:
        screen.blit(donut,(670,390)) 
        collected[1],score = collect(670,390)
    if collected[2] == False:
        screen.blit(donut,(1000,600))
        collected[2],score = collect(1000,600)
    if collected[3] == False:
        screen.blit(donut,(790,170))
        collected[3],score = collect(790,170)
    if collected[4] == False:
        screen.blit(donut,(1150,80))
        collected[4],score = collect(1150,80)
    if score >= 5:
        scrn = 3
    else:
        printscore = font.render("Score: "+str(score),False,WHITE)
        screen.blit(printscore,[50,50])
        scrn = 2
    return scrn

# Redraws the screen
def redraw_screen():
    global scrn
    background(scrn)
    character(scrn)
    enemy()
    scrn = donutBlit()
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
        
    
    if scrn == 0 or scrn == 1:
        if keys[pygame.K_RETURN]:
            scrn += 1



    place = boundaries()
    if scrn == 2:
        if keys[pygame.K_RIGHT]:
            if pusheenLoc[0] <= WIDTH-35:
                pusheenLoc[0] += 3
            while keys[pygame.K_RIGHT]:
                pusheenNum,pusheenNow = animation(pusheenNum,pusheenNow,pusheenR,10)
                break
            pusheenDir = "R"
        if keys[pygame.K_LEFT]:
            if pusheenLoc[0] >= 0:
                pusheenLoc[0] += -3
            while keys[pygame.K_LEFT]:
                pusheenNum,pusheenNow = animation(pusheenNum,pusheenNow,pusheenL,10)
                break
            pusheenDir = "L"
    
        if keys[pygame.K_UP]:
            if place == "Floor":
                jump(450)
            elif place == "Table":
                jump(350)
            elif place == "Shelf":
                jump(190)
            elif place == "Cupboard1":
                jump(50)
            elif place == "Cupboard2":
                jump(0)
            elif place == "Pot":
                jump(360)

        if keys[pygame.K_SPACE]:
            print "SHOOT"
            shoot = True
            shoot()
    
        if pusheenLoc[1] < 580:
            pusheenLoc[1] += 3


    #global variables for position values
    redraw_screen()                     # the screen window must be constantly redrawn - animation
    pygame.time.delay(4)                # pause for 2 miliseconds
                                        
pygame.quit()                           # always quit pygame when done!

