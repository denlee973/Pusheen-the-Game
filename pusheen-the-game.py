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
HEIGHT= 680
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Pusheen the Game')

# Colours
GREEN = (0,255,0)
GRASSGREEN = (31,155,70)
RED = (255,0,0)
PINK = (255, 183, 237)
BLUE = (0, 0, 255)
SKYBLUE = (119,169,249)
WHITE = (255,255,255)
BLACK = (0,0,0)

# Fonts
font = pygame.font.SysFont('Comic Sans MS',20,False,False)
tfont = pygame.font.SysFont('Comic Sans MS',60,True,False)

# Images
pusheen1 = pygame.image.load('pusheenWalk-1.png')
pusheen2 = pygame.image.load('pusheenWalk-2.png')
pusheen3 = pygame.image.load('pusheenWalk-3.png')
pusheen4 = pygame.image.load('pusheenWalk-4.png')
table = pygame.image.load('table.png')
tree = pygame.image.load('tree.png')
frame = pygame.image.load('frame.jpg')


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
        pass
    # Score Screen
    elif scrn == 3:
        pass

def donut():
     
    collected,score = collect()
    
    if collected == False:
        scrn.blit(donut,(300,300))

    printscore = font.render("Score: "+str(score),False,WHITE)
    scrn.blit(printscore,[500,450])

# Redraws the screen
def redraw_screen():
    background()
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
        

     

    #global variables for position values
    redraw_screen()                     # the screen window must be constantly redrawn - animation
    pygame.time.delay(2)                # pause for 2 miliseconds
#---------------------------------------#                                        
pygame.quit()                           # always quit pygame when done!

