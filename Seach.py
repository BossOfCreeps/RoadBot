import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def box (frame1, x1, x2, y1, y2, b, g, r):
    x=x1
    while x<x2-1:
        x=x+1
        y=y1
        while y<y2-1:
            y=y+1
            if (x<639) and (y<479):
                frame1[y,x]=[r,g,b]
    return frame1
    
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = box(frame,440,640,275,280,0,0,0)
    frame = box(frame,440,445,275,480,0,0,0)

    step=20
    max=40
    x=0
    while x<479-step:
        x=x+step
        y=0
        while y<639-step:
            y=y+step
            if abs(frame[x,y,2]-frame[x,y,1])<max and abs(frame[x,y,0]*2-frame[x,y,1])<max:
                frame = box(frame,x-10,x+10,y-10,y+10,0,0,0)
    
    cv2.imshow('frame',frame)
    #frame[200,200]=[255,255,255]
    print frame[0,0]
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
