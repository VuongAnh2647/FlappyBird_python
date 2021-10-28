import flappybird as fb
import pygame
class Scores():
    def __init__(self):
        self.score = 0
        self.addScore = True

    def draw(self):
         font = pygame.font.SysFont('consolas',40)
         scoreSuface = font.render(str(self.score), True, (0, 0 ,0))
         textSize = scoreSuface.get_size()
         fb.DISPLAYSURF.blit(scoreSuface, (int((fb.WINDOWNWIDTH - textSize[0])/2), 100))

    def update(self, bird, columns ):
        collision = False
        for i in range(3):
            rectColumn = [ columns.ls[i][0] + columns.width, columns.ls[i][1], 1, columns.blank]
            rectBird = [ bird.x, bird.y, bird.width, bird.height ]
            if rectCollision(rectBird, rectColumn) == True:
                collision = True
                break
        if collision == True:
            if self.addScore == True:
                self.score += 1
            self.addScore = False
        else:
            self.addScore = True

def rectCollision(rect1, rect2):
    if(rect1[0] <= rect2[0] + rect2[2] and rect2[0] <= rect1[0] + rect1[2] and rect1[1] <= rect2[1]+rect2[3] and rect2[1] <= rect1[1]+rect1[3]):
        return True
    return False
