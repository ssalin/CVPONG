import cv2

class ball:

    def __init__(self,x,y,rad,xmax,ymax):
        self.xpos = x
        self.xspeed = 1
        self.xmax = xmax
        
        self.ypos = y
        self.yspeed = 1
        self.ymax = ymax
        
        self.radius = rad
   
    def move(self):
       # while (x-crad) > 0) || ((self.x+self.radius) < 1080):
        self.xpos = self.xpos + self.xspeed
        if (self.ypos + self.radius > self.ymax):
            self.yspeed = self.yspeed * (-1)
        self.ypos = self.ypos + self.yspeed
            
    
    def draw(self,IMG):
        cv2.circle(IMG,
                  (int (self.xpos),
                   int (self.ypos)),
                   int (self.radius),
                   (0,0,255),-1)#could make ball chg color
