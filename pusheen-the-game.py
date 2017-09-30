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
font = pygame.font.SysFont('Comic Sans MS',30,False,False)
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
nomnom = [dpusheen1,dpusheen2,dpusheen3,dpusheen4]

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
scrn = 0
ratDir = "L"
ratLoc = [1150,95]
ratNum = 1
ratNow = rat1
pusheenDir = "R"
pusheenLoc = [0,580]
pusheenNum = 1
pusheenNow = pusheen1R
collected = [False,False,False,False,False]
score = 0
issalive = True
fired = False
laserLoc = [999,999]
laserDir = ""
dnum = 1
dnow = dpusheen1

# rect()
# @param: colour:tuple, x:int, y:int, w:int, h:int
# @return: none
def rect(colour,x,y,w,h):
    pygame.draw.rect(screen,colour,(x,y,w,h),0)

# animation()
# @param: num:int, now:image, images:image[], incr:int
# @return: num:int, now:image
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

# background()
# @param: scrn:int
# @return: none
def background(scrn):
    global issalive
    global dnum
    global dnow
    screen.fill(SKYBLUE)
    # Title Screen
    enter = font.render("Press enter to continue.",False,WHITE)
    if scrn == 0:
        title = tfont.render("PUSHEEN THE GAME",False,WHITE)
        screen.blit(title,(325,200))
        screen.blit(pusheen1L,(600,350))
        screen.blit(enter,(520,500))
    # Instructions
    elif scrn == 1:
        instruct = tfont.render("INSTRUCTIONS",False,WHITE)
        arrow = font.render("Use the arrow keys to move Pusheen.",False,WHITE)
        space = font.render("Press the space bar to shoot lasers.",False,WHITE)
        goal = font.render("Collect all the donuts.",False,WHITE)
        touch = font.render("Don't touch the rat! Kill it with your lasers.",False,WHITE)
        screen.blit(instruct,(400,100))
        screen.blit(arrow,(100,600))
        screen.blit(pusheen1R,(300,500))
        rect(WHITE,800,550,50,5)
        screen.blit(space,(700,600))
        screen.blit(rat1,(700,300))
        screen.blit(goal,(200,200))
        screen.blit(touch,(600,200))
        screen.blit(donut,(300,300))
        screen.blit(enter,(520,400))
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
        if issalive == True:
             issalive = enemy(laserLoc)

    # Score Screen
    elif scrn == 3:
        congrats = tfont.render("CONGRATULATIONS!",False,WHITE)
        screen.blit(congrats,(300,200))
        dnum,dnow = animation(dnum,dnow,nomnom,15)
        screen.blit(dnow,(500,300))
    elif scrn == 4:
        loser = tfont.render("YOU DIED!",False,WHITE)
        screen.blit(loser,(500,300))

# boundaries()
# @param: issalive:bool
# @return: str
def boundaries(issalive):
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
        if issalive == True and pusheenLoc[0] + 100 > ratLoc[0] and pusheenLoc[0] < ratLoc[0] + 100:
            return "DEAD"
        else:
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
        
# enemy()
# @param: laserLoc:int[]
# @return: bool
def enemy(laserLoc):
    global ratDir
    global ratNum
    global ratNow
    if ratDir == "L":
        ratNum,ratNow = animation(ratNum,ratNow,ratL,10)
        screen.blit(ratNow,(ratLoc[0],ratLoc[1]))
        ratLoc[0] += -2
        if ratLoc[0] < 650 and ratLoc[0] > 640:
            ratDir = "R"

    if ratDir == "R":
        ratNum,ratNow = animation(ratNum,ratNow,ratR,10)
        screen.blit(ratNow,(ratLoc[0],ratLoc[1]))
        ratLoc[0] += 2
        if ratLoc[0] < 1150 and ratLoc[0] > 1140:
            ratDir = "L"
    if laserLoc[1] > ratLoc[1] - 150 and laserLoc[1] < ratLoc[1] + 150:
        print laserLoc[0] + 50 >= ratLoc[0], laserLoc[0] <= ratLoc[0] + 100
        if laserLoc[0] + 50 >= ratLoc[0] and laserLoc[0] <= ratLoc[0] + 100:
            print "HI"
            return False
        elif laserLoc[0] >= ratLoc[0] + 100 and laserLoc[0] + 50 <= ratLoc[0]:
            print "EHEH"
            return False
        else:
            return True
    else:
        return True

# shoot()
# @param: x:int, y:int, scrn:int, fired:bool
# @return: x:int
def shoot(x,y,scrn,fired):
    if fired:
        if laserDir == "R":
            rect(WHITE,x,y,50,5)
            x += 2
        else:
            rect(WHITE,x,y,50,5)
            x += -2
        if x > WIDTH or x < 0:
            fired = False
    return x

# jump()
# @param: maxH:int
# @return: none
def jump(maxH):
    if pusheenLoc[1] >= maxH + 120:
        while pusheenLoc[1] >= maxH:
            pusheenLoc[1] += -3
            if keys[pygame.K_LEFT]:
                    pusheenLoc[0] += -1
            elif keys[pygame.K_RIGHT]:
                    pusheenLoc[0] += 1
            pygame.time.delay(2)
            redraw_screen()
    if maxH == 0:
        while pusheenLoc[1] >= 0:
            pusheenLoc[1] += -3
            if keys[pygame.K_LEFT]:
                    pusheenLoc[0] += -1
            elif keys[pygame.K_RIGHT]:
                    pusheenLoc[0] += 1
            pygame.time.delay(2)
            redraw_screen()

# character()
# @param: scrn:int
# @return: none
def character(scrn):
    if scrn == 2:
        screen.blit(pusheenNow,(pusheenLoc[0],pusheenLoc[1]))

# collect()
# @param: donutx:int, donuty:int
# @return: collectNow:bool, score:int
def collect(donutx,donuty):
    global score
    collectNow = False
    if pusheenLoc[0] + 100 > donutx and pusheenLoc[0] < donutx + 20 and pusheenLoc[1] + 65 > donuty and pusheenLoc[1] < donuty + 20:
        collectNow = True
        score += 1

    return collectNow,score

# donutBlit()
# @param: scrn:int
# @return: scrn:int
def donutBlit(scrn):
    global score
    if scrn == 2:
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
            screen.blit(printscore,(50,50))
    return scrn

# redraw_screen()
# @param: none
# @return: none
def redraw_screen():
    global fired
    global scrn
    background(scrn)
    character(scrn)
    scrn = donutBlit(scrn)
    laserLoc[0] = shoot(laserLoc[0],laserLoc[1],scrn,fired)
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
    place = boundaries(issalive)

    if scrn == 0:
        if keys[pygame.K_RETURN]:
            scrn = 1
            pygame.time.delay(300)
    elif scrn == 1:
        if keys[pygame.K_RETURN]:
            scrn = 2

    elif scrn == 2:
        if place == "DEAD":
            scrn = 4
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
            laserLoc = [pusheenLoc[0],pusheenLoc[1]+50] 
            laserDir = pusheenDir
            fired = True
        
        if pusheenLoc[1] < 580:
            pusheenLoc[1] += 3

    #global variables for position values
    redraw_screen()                     # the screen window must be constantly redrawn - animation
    pygame.time.delay(4)                # pause for 2 miliseconds
                                        
pygame.quit()                           # always quit pygame when done!
