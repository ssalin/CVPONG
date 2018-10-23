import cv2

class ball:

    def __init__(self,x,y,rad):
        self.xpos = x
        self.xspeed = 1
        self.ypos = y
        self.yspeed = 0
        self.radius = rad
   
    def move(self):
       # while (x-crad) > 0) || ((self.x+self.radius) < 1080):
        self.xpos = self.xpos + self.xspeed
        self.ypos = self.ypos + self.yspeed
    
    def draw(self,IMG):
        cv2.circle(IMG,
                  (int (self.xpos),
                   int (self.ypos)),
                   int (self.radius),
                   (0,0,255),-1)
        #update image 
        #setwin()
        #cv2.imshow(winname,img)
        #cv2.waitKey(2)


