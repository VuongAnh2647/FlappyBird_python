import flappybird as fb
class Bird():
    def __init__(self):
        self.width = fb.BIRDWIDTH
        self.height = fb.BIRDHEIGHT
        self.x = (fb.WINDOWNWIDTH - self.width)/2
        self.y = (fb.WINDOWNHEIGHT - self.height)/2
        self.speed = 0 #toc do bay
        self.surface = fb.BIRDING

    def draw(self):
        fb.DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y)))

    def update(self, mouseClick):
        self.y += self.speed + 0.5*fb.G #y= vot + 1/2*g*t^2
        self.speed += fb.G #v=vo + g*t
        if mouseClick == True:
            self.speed = fb.SPEEDLY