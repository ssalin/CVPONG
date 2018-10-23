import numpy as np
import cv2
import screeninfo
import math
import ball as b
winname = "neato"
screen_id = 0
screen = screeninfo.get_monitors()[screen_id]
WIDTH = screen.width 
HEIGHT = screen.height

crad = 100 #radius of ball
#put ball in middle of screen
x = WIDTH/2 
y = HEIGHT/2
#open the camera
cap = cv2.VideoCapture(0)
if (cap.isOpened == False):
    print("ERROR OPENING CAMERA") #add more advanced error-behavior later
FWIDTH = int(cap.get(3)) 
FHEIGHT = int(cap.get(4))


def setwin(): #setup window. openCV seems reluctant to do fullscreen borderless.
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    cv2.moveWindow(winname, screen.x-1,screen.y-1)
    cv2.setWindowProperty(winname,
                          cv2.WND_PROP_FULLSCREEN,
                          cv2.WND_PROP_FULLSCREEN)

    
def main():
    ball = b(WIDTH,HEIGHT,crad)
    y = int(math.floor(FHEIGHT/2))#until i add vector movement
    #tester blurb for ball movement functions
    #black image. maybe add overlayed at some point. 2 ambitious 4 now.
    bimg = np.zeros((HEIGHT,WIDTH,3), np.uint8)
    setwin()
    ret, img = cap.read()
    ball.draw(bimg)
    cv2.imshow(winname,bimg) #need to see cam feed to debug hand finding 
    cv2.waitkey(2)
    #clean up
    cap.release()
    cv2.destroyAllWindows()

main()
