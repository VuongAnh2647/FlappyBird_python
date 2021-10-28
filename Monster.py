import flappybird as fb
class Monsters():
    def __init__(self):
        self.width = fb.MONSTERWIDTH
        self.height = fb.MONSTERHEIGHT
        self.x = (fb.WINDOWNWIDTH - self.width)/2
        self.y = (fb.WINDOWNHEIGHT - self.height)/2
        self.speed = 0 #toc do bay
        self.surface = fb.MONSTER

    def draw(self):
        fb.DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y)))
    