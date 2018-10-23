import cv2

class ball:

    def __init__(self,x,y,rad):
        self.xpos = x
        self.xspeed = 0
        self.ypos = y
        self.yspeed = 0
        self.radius = rad
   
    def move(ball):
        while (x-crad) > 0:
            drawball()
            ball.x = ball.xpos + ball.xspeed
            ball.y = ball.ypos + ball.yspeed
    
    def drawball(self,IMG):
        cv2.circle(IMG,(self.xpos,self.ypos),self.radius,(0,0,255),-1)
        #update image 
        #setwin()
        #cv2.imshow(winname,img)
        #cv2.waitKey(2)


