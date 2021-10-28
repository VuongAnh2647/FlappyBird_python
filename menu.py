import pygame,os
from pygame.locals import *
import flappybird as fb
import game, Bird, Columns, Scores
def main_menu():

    menu = True
    selected = 'Start'
    bird = Bird.Bird()
    columns = Columns.Columns()
    score = Scores.Scores()
    font1 = pygame.font.SysFont('cosolas', 25)
    commentSuface = font1.render('*Press Enter to choose button*', True, fb.blue)
    commentSize = commentSuface.get_size()

    while menu:
        #mouseclick = False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected = 'Start'
                if event.key==pygame.K_DOWN:
                    selected = "Quit"
                if event.key==pygame.K_RETURN:
                    if selected == 'Start':
                        game.gameStart(bird)
                        game.gamePlay(bird,columns,score)
                        game.gameOver(bird,columns,score)
                    if selected == 'Quit':
                        pygame.quit()
                        quit()
        fb.DISPLAYSURF.blit(fb.Menu_bg,(0,0))
        title = fb.text_format("FLappy Bird", fb.font, 50, fb.yellow)
        if selected == 'Start':
            text_start = fb.text_format("START", fb.font, 35, fb.blue)
        else:
            text_start = fb.text_format("START", fb.font, 35, fb.black)
        if selected == "Quit":
            text_quit = fb.text_format("QUIT", fb.font, 35, fb.red)
        else:
            text_quit = fb.text_format("QUIT", fb.font, 35, fb.black)

        title_rect = title.get_rect()
        start_rect =text_start.get_rect()
        quit_rect = text_quit.get_rect()

        fb.DISPLAYSURF.blit(title, (fb.WINDOWNWIDTH/2 - (title_rect[2]/2), 80))
        fb.DISPLAYSURF.blit(text_start, (fb.WINDOWNWIDTH/2 - (start_rect[2]/2), 300))
        fb.DISPLAYSURF.blit(text_quit, (fb.WINDOWNWIDTH/2 - (quit_rect[2]/2), 360))
        fb.DISPLAYSURF.blit(commentSuface, (int((fb.WINDOWNWIDTH - commentSize[0])/2), 500))
        pygame.display.update()
        fb.fpsClock.tick(fb.FPS)
        pygame.display.set_caption("Flappy Bird")

