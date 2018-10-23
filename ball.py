import cv2

class ball:

    def __init__(self):
        self.xpos = 0
        self.xspeed = 0
        self.ypos = 0
        self.yspeed = 0
   
    def move(ball):
        while (x-crad) > 0:
            drawball()
            ball.x = ball.xpos + ball.xspeed
            ball.y = ball.ypos + ball.yspeed
    
    def drawball():
        global x
        #read from camera
        ret, img = cap.read()
        #draw black image
        #img = np.zeros((HEIGHT,WIDTH,3), np.uint8)
        #draw circle
        cv2.circle(img,(x,(y)),crad,(0,0,255),-1)
        #update image 
        setwin()
        cv2.imshow(winname,img)
        cv2.waitKey(2)


