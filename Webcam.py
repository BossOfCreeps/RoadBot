import numpy as np
import RPi.GPIO as GPIO
import cv2
from time import sleep
from dc import forward, backward, stop,init

ix,iy,ir,ig,ib = -1,-1, -1, -1, -1

def box (frame1, x1, x2, y1, y2, r, g, b):
    x=x1
    while x<x2-1:
        x=x+1
        y=y1
        while y<y2-1:
            y=y+1
            if (x<639) and (y<479):
                frame1[y,x]=[b,g,r]
    return frame1

def draw_circle(event,x,y,flags,param):
    global ix,iy,ir,ig,ib 
    if event == cv2.EVENT_LBUTTONDBLCLK:
        forward()
        stop()
        cv2.circle(img,(x,y),100,(255,0,0),-1)
        ix,iy,ir,ig,ib = x,y,frame[iy,ix,2],frame[iy,ix,1],frame[iy,ix,0]

init()
forward()
stop()
GPIO.setwarnings(False)
cv2.namedWindow('frame')
cap = cv2.VideoCapture(0)
img = np.zeros((512,512,3), np.uint8)
cv2.setMouseCallback('frame',draw_circle)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = box(frame,440,640,275,280,0,0,0)
    frame = box(frame,440,445,275,480,0,0,0)
    frame = box(frame,0,10,0,10,ir, ig, ib)
    #print ix, iy, ir, ig, ib, frame[iy,ix,2], frame[iy,ix,1], frame[iy,ix,0]
    step=20
    maxi=50
    x=0
    while x<480-step:
        x=x+step
        y=0
        while y<640-step:
            y=y+step
            #print x, y
            if (abs(frame[x,y,2]-ir)<maxi) and (abs(frame[x,y,1]-ig)<maxi) and (abs(frame[x,y,0]-ib)<maxi):
                frame = box(frame,y-5,y+5,x-5,x+5,0,0,0)
    
    cv2.imshow('frame', frame)
    k = cv2.waitKey(20) & 0xFF
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
