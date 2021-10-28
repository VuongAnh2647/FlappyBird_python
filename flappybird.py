import pygame,os, menu, Bird, Columns, Scores
from pygame.locals import *



pygame.init()
os.environ['SDL_VIDEO-CENTERED'] = '1'

WINDOWNWIDTH = 400
WINDOWNHEIGHT=600

def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont,textSize)
    newText = newFont.render(message, 0, textColor)

    return newText

white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

font = (r"C:\Users\ADMIN\Documents\Nam3\BTLpython\SuperMario256.ttf")

BIRDWIDTH = 40
BIRDHEIGHT = 30
G = 0.5
SPEEDLY = -8
BIRDING = pygame.image.load(r"C:\Users\ADMIN\Documents\Nam3\BTLpython\flappybird\img\bird1.png")

COLUMNWIDTH = 60
COLUMNHEIGHT = 500
BLANK = 160
DISTANCE = 200
COLUMNSPEED = 2
COLUMNING = pygame.image.load(r"C:\Users\ADMIN\Documents\Nam3\BTLpython\flappybird\img\column1.png")

MONSTERWIDTH = 50
MONSTERHEIGHT = 54
SPEED = -8
MONSTER = pygame.image.load(r"C:\Users\ADMIN\Documents\Nam3\BTLpython\flappybird\img\frame-1.png")

BACKGROUND = pygame.image.load(r"C:\Users\ADMIN\Documents\Nam3\BTLpython\flappybird\img\background1.png")
Menu_bg = pygame.image.load(r"C:\Users\ADMIN\Documents\Nam3\BTLpython\flappybird\img\background1.png")

FPS=60
fpsClock = pygame.time.Clock()

DISPLAYSURF =  pygame.display.set_mode((WINDOWNWIDTH, WINDOWNHEIGHT))
pygame.display.set_caption('Flappy Bird')

def main():
    bird = Bird.Bird()
    columns = Columns.Columns()
    score = Scores.Scores()
    
    while True:
        menu.main_menu()      
if __name__ == '__main__':
    main()