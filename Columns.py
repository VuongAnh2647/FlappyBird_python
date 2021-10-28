import random
import flappybird as fb
class Columns():
    def __init__(self):
        self.width = fb.COLUMNWIDTH
        self.height = fb.COLUMNHEIGHT
        self.blank = fb.BLANK
        self.distance = fb.DISTANCE
        self.speed = fb.COLUMNSPEED
        self.surface = fb.COLUMNING
        self.ls = []
        for i in range(3) :
            x = fb.WINDOWNWIDTH + i*self.distance
            y = random.randrange(60, fb.WINDOWNHEIGHT - self.blank -60, 20)
            self.ls.append([x, y])

    def update(self):
        for i in range(3):
            self.ls[i][0] -= self.speed

        if self.ls[0][0] < -self.width:
            self.ls.pop(0)
            x = self.ls[1][0] + self.distance
            y = random.randrange(60, fb.WINDOWNHEIGHT - self.blank - 60, 10)
            self.ls.append([x,y])

    def draw(self):
        for i in range(3):
           # self.ls[i][0] -= self.speed #tao chuyen dong cho cot
            fb.DISPLAYSURF.blit(self.surface, (self.ls[i][0], self.ls[i][1] - self.height))
            fb.DISPLAYSURF.blit(self.surface, (self.ls[i][0], self.ls[i][1] + self.blank))
