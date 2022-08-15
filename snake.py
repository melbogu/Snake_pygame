import pygame
import sys
from pygame.locals import *
from random import seed
from random import randint
from random import choice

BLACK = (0,0,0)
SALMON = (255,229,204)
DARKRED = (204,0,0)

class block:
    def __init__(self, coorx, coory):
        self.coorx = coorx
        self.coory = coory

def start():
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()

    gameactiv = True
    x = 0
    y = 0
    right = True
    left = False
    up = False
    down = False
    youlost = False
    helloAgain = False
    startbutton = True
    youwon = False
    randomAB = [i for i in range(0,476,25)]
    a = choice(randomAB)
    b = choice(randomAB)
    first = block(0,0)
    snakelist = [first]

    while gameactiv:
        
        if not youlost and not youwon:
            if startbutton:
                screen.fill(SALMON)
                fontObj = pygame.font.SysFont('calibri', 36, bold=True)
                textSurfaceObj = fontObj.render("Are you ready?", True, BLACK)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (250, 250)
                fontObj2 = pygame.font.SysFont('calibri', 30, bold=True)
                textSurfaceObj2 = fontObj2.render("Press Enter to start the game.", True, BLACK)
                textRectObj2 = textSurfaceObj2.get_rect()
                textRectObj2.center = (250, 280)
                screen.blit(textSurfaceObj, textRectObj)
                screen.blit(textSurfaceObj2, textRectObj2)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameactiv = False  
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            startbutton = False
            elif not startbutton:
                if helloAgain:
                    x = 0
                    y = 0
                    a = choice(randomAB)
                    b = choice(randomAB)
                    right = True
                    left = False
                    up = False
                    down = False
                    youlost = False
                    helloAgain = False
                screen.fill(SALMON)                

                for i, _ in enumerate(snakelist):
                    snakey = pygame.Rect(snakelist[i].coorx,snakelist[i].coory,25,25)
                    pygame.draw.rect(screen, BLACK, snakey)
                        

                food = pygame.Rect(a,b,25,25)
                pygame.draw.rect(screen, DARKRED, food)
                pygame.display.flip()
                clock.tick(4)

                alreadySet = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameactiv = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            if not left:
                                x -= 25
                                left = True
                                right = False
                                up = False
                                down = False
                                alreadySet = True
                        elif event.key == pygame.K_RIGHT:
                            if not right:
                                x += 25
                                right = True
                                left = False
                                up = False
                                down = False
                                alreadySet = True
                        elif event.key == pygame.K_UP:
                            if not up:
                                y -= 25
                                right = False
                                left = False
                                up = True
                                down = False
                                alreadySet = True
                        elif event.key == pygame.K_DOWN:
                            if not down:
                                y += 25
                                right = False
                                left = False
                                up = False
                                down = True
                                alreadySet = True

                

                if not alreadySet:
                    if right:
                        x += 25
                    elif left:
                        x -= 25
                    elif up:
                        y -= 25
                    elif down:
                        y += 25
                
                # update all coordinates of all snake blocks
                for i, _ in reversed(list(enumerate(snakelist))):
                    if i!=0:
                        snakelist[i].coorx = snakelist[i-1].coorx
                        snakelist[i].coory = snakelist[i-1].coory
                
                # store new coordinates of the front block of the snake
                snakelist[0].coorx = x
                snakelist[0].coory = y
                                    
                # check if the player lost
                if (right and x >= 476) or (left and x<0) or (up and y<0) or (down and y>=476):
                    youlost = True
                
                for i, _ in enumerate(snakelist):
                    if i != 0:
                        if (snakelist[0].coorx == snakelist[i].coorx) and (snakelist[0].coory == snakelist[i].coory):
                            youlost = True
                
                # check if snake is on food
                if a == x and b == y:
                    a = choice(randomAB)
                    b = choice(randomAB)
                    newblock = block(snakelist[len(snakelist)-1].coorx, snakelist[len(snakelist)-1].coory)
                    snakelist.append(newblock)

                if len(snakelist)==400:
                    youwon = True

                    

        elif youlost:
            helloAgain = False
            screen.fill(SALMON)
            fontObj = pygame.font.SysFont('calibri', 36, bold=True)
            textSurfaceObj = fontObj.render("You have lost!", True, BLACK)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (250, 250)
            fontObj2 = pygame.font.SysFont('calibri', 30, bold=True)
            textSurfaceObj2 = fontObj2.render("Press Enter to play again.", True, BLACK)
            textRectObj2 = textSurfaceObj2.get_rect()
            textRectObj2.center = (250, 280)
            screen.blit(textSurfaceObj, textRectObj)
            screen.blit(textSurfaceObj2, textRectObj2)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameactiv = False  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        helloAgain = True
            if helloAgain:
                youlost = False
                youwon = False

        elif youwon:
            helloAgain = False
            screen.fill(SALMON)
            fontObj = pygame.font.SysFont('calibri', 36, bold=True)
            textSurfaceObj = fontObj.render("You win, congratulations!", True, BLACK)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (250, 250)
            fontObj2 = pygame.font.SysFont('calibri', 30, bold=True)
            textSurfaceObj2 = fontObj2.render("Press Enter to play again.", True, BLACK)
            textRectObj2 = textSurfaceObj2.get_rect()
            textRectObj2.center = (250, 280)
            screen.blit(textSurfaceObj, textRectObj)
            screen.blit(textSurfaceObj2, textRectObj2)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameactiv = False  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        helloAgain = True
            if helloAgain:
                youlost = False
                youwon = False
          

    
if __name__ == '__main__':
    pygame.init()
    start()
    pygame.quit()