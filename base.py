import numpy as np
import cv2
import screeninfo
import math
import ball as b
winname = "neato"
screen_id = 0
screen = screeninfo.get_monitors()[screen_id]
WIDTH = 1920#screen.width 
HEIGHT = 1080#screen.height

crad = 50 #radius of ball
#put ball in middle of screen
x = WIDTH/2 
y = HEIGHT/2
#open the camera
cap = cv2.VideoCapture(0)
if (cap.isOpened == False):
    print("ERROR OPENING CAMERA") #add more advanced error-behavior later
FWIDTH = int(cap.get(3)) #see openCV documentation for cap.get(#) info 
FHEIGHT = int(cap.get(4))


def setwin(): #setup window. openCV seems reluctant to do fullscreen borderless.
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    cv2.moveWindow(winname, screen.x-1,screen.y-1)
   # cv2.setWindowProperty(winname,
   #                       cv2.WND_PROP_FULLSCREEN,
   #                       cv2.WND_PROP_FULLSCREEN)

    
def main():
    ball = b.ball(x,y,crad,WIDTH,HEIGHT)
    # y = int(math.floor(FHEIGHT/2))#until i add vector movement
    #tester blurb for ball movement functions
    #black image. maybe add overlayed at some point. 2 ambitious 4 now.
    setwin()
    #ret, fimg = cap.read()
    bimg = np.zeros((HEIGHT,WIDTH,3), np.uint8)

    while ((ball.xpos + crad) < WIDTH):
        ball.draw(bimg)
        ball.move()
        cv2.imshow(winname,bimg) #need to see cam feed to debug hand finding
        
        bimg = np.zeros((HEIGHT,WIDTH,3), np.uint8)#so the ball doesnt leave a trail
        cv2.waitKey(2)#so ball moves at a reasonable speed

    cv2.waitKey(0)#wait for keypress. for debug. will get removed at some point.
    #clean up
    cap.release()
    cv2.destroyAllWindows()

main()
