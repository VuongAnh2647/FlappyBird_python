import flappybird as fb
import pygame,sys,os,Bird,Columns,Scores
from pygame.locals import *

def rectCollision(rect1, rect2):
    if(rect1[0] <= rect2[0] + rect2[2] and rect2[0] <= rect1[0] + rect1[2] and rect1[1] <= rect2[1]+rect2[3] and rect2[1] <= rect1[1]+rect1[3]):
        return True
    return False

def isGameOver(bird,columns):
    for i in range(3):
        rectBird = [bird.x, bird.y, bird.width, bird.height]
        rectColumn1 = [ columns.ls[i][0], columns.ls[i][1] - columns.height, columns.width, columns.height]
        rectColumn2 = [ columns.ls[i][0], columns.ls[i][1] + columns.blank, columns.width, columns.height ]
        if rectCollision(rectBird,rectColumn1) == True or rectCollision(rectBird, rectColumn2) == True:
            return True
    if bird.y + bird.height < 0 or bird.y + bird.height > fb.WINDOWNHEIGHT:
        return True
    return False

def gamePlay(bird, columns, score):
    bird.__init__()
    bird.speed = fb.SPEEDLY
    columns.__init__()
    score.__init__()
    while True:
        mouseClick = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouseClick = True
        
        fb.DISPLAYSURF.blit(fb.BACKGROUND, (0,0))

        columns.draw()
        columns.update()

        bird.draw()
        bird.update(mouseClick)

        score.draw()
        score.update(bird, columns)

        if isGameOver(bird, columns) == True:
            return

        pygame.display.update()
        fb.fpsClock.tick(fb.FPS)
def gameStart(bird):
    bird.__init__()

    font1 = pygame.font.SysFont('cosolas', 25)
    commentSuface = font1.render('*Click to start*', True, fb.blue)
    commentSize = commentSuface.get_size()
    
    start_title = fb.text_format("GO!", fb.font, 50, fb.yellow)
    start_title_rect = start_title.get_rect()
    
    while True:
        #draw_menu()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == MOUSEBUTTONDOWN:
                return
        
        fb.DISPLAYSURF.blit(fb.BACKGROUND, (0, 0))
        bird.draw()
        fb.DISPLAYSURF.blit(start_title, (int((fb.WINDOWNWIDTH - start_title_rect[2])/2), 100))
        fb.DISPLAYSURF.blit(commentSuface, (int((fb.WINDOWNWIDTH - commentSize[0])/2), 500))

        pygame.display.update()
        fb.fpsClock.tick(fb.FPS)
        

def gameOver(bird, columns, score):
    #font = pygame.font.SysFont('consolas', 60)
    headingSuface = fb.text_format('GAMEOVER', fb.font, 50, fb.red)
    headingSuface_rect = headingSuface.get_rect()
    
    font1 = pygame.font.SysFont('consolas', 20)
    commentSuface = font1.render('*Press "space" to replay*', True, (255, 0, 0))
    commentSize = commentSuface.get_size()

    font1 = pygame.font.SysFont('consolas', 30)
    scoreSuface = font1.render('Score: ' + str(score.score), True, (0, 0, 0))
    scoreSize = scoreSuface.get_size()
    

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type ==MOUSEBUTTONDOWN :
                    return
        
        fb.DISPLAYSURF.blit(fb.BACKGROUND, (0, 0))
        columns.draw()
        bird.draw()
        fb.DISPLAYSURF.blit(headingSuface, (int((fb.WINDOWNWIDTH - headingSuface_rect[2])/2), 100))
        fb.DISPLAYSURF.blit(commentSuface, (int((fb.WINDOWNWIDTH - commentSize[0])/2), 500))
        fb.DISPLAYSURF.blit(scoreSuface, (int((fb.WINDOWNWIDTH - scoreSize[0])/2), 160))

        pygame.display.update()
        fb.fpsClock.tick(fb.FPS)