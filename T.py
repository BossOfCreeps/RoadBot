import numpy as np
import RPi.GPIO as GPIO
import cv2
from time import sleep

ix,iy,ir,ig,ib = -1,-1, -1, -1, -1
IN1=40
IN2=38
IN3=36
IN4=32
IN5=37
IN6=35
IN7=33
IN8=31
EN0=29

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
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global ir, ig, ib
        cv2.circle(img,(x,y),100,(255,0,0),-1)
        ir, ig, ib = frame[y,x,2],frame[y,x,1],frame[y,x,0]
        print ir, ig, ib, x, y

sleep(3)


sleep(2)
GPIO.cleanup()

#
cv2.namedWindow('frame')
cap = cv2.VideoCapture(0)
img = np.zeros((512,512,3), np.uint8)
#
cv2.setMouseCallback('frame',draw_circle)
go=""
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = box(frame,0,213,340,345,0,0,0)
    frame = box(frame,213,218,340,480,0,0,0)
    frame = box(frame,0,10,0,10,ir, ig, ib)
    #print ix, iy, ir, ig, ib, frame[iy,ix,2], frame[iy,ix,1], frame[iy,ix,0]
    step=20
    maxi=60
    x=340
    while x<480-step:
        x=x+step
        y=0
        while y<213-step:
            y=y+step
            #print x, y
            if (abs(170 - frame[x,y,2])<maxi) and (abs(frame[x,y,1]-170)<maxi) and (abs(frame[x,y,0]-200)<maxi):
                frame = box(frame,y-5,y+5,x-5,x+5,0,0,0)
    f=False
    s=False

    frame = box(frame,20-3,20+3,400-3,400+3,255,0,0)
    frame = box(frame,60-3,60+3,400-3,400+3,255,0,0)
    if (abs(170 - frame[20,400,2])<maxi) and (abs(frame[20,400,1]-170)<maxi) and (abs(frame[20,400,0]-200)<maxi):
        f=True
    if (abs(170 - frame[60,400,2])<maxi) and (abs(frame[60,400,1]-170)<maxi) and (abs(frame[60,400,0]-200)<maxi):
        s=True
    if f and s:
        print "f"
    else:
        print "b"
    if not f and not s and go != "b":
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(40, GPIO.OUT)
        GPIO.setup(38, GPIO.OUT)
        GPIO.setup(36, GPIO.OUT)
        GPIO.setup(32, GPIO.OUT)
        GPIO.setup(31, GPIO.OUT)
        GPIO.setup(37, GPIO.OUT)
        GPIO.setup(35, GPIO.OUT)
        GPIO.setup(33, GPIO.OUT)
        GPIO.setup(29, GPIO.OUT)
        speed=GPIO.PWM(EN0,100)
        speed.start(100)
        GPIO.output(40, GPIO.LOW)
        GPIO.output(38, GPIO.HIGH)
        GPIO.output(36, GPIO.LOW)
        GPIO.output(32, GPIO.HIGH)
        GPIO.output(37, GPIO.LOW)
        GPIO.output(35, GPIO.HIGH)
        GPIO.output(33, GPIO.LOW)
        GPIO.output(31, GPIO.HIGH)
        print go
    if f and s and go != "forward":
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(40, GPIO.OUT)
        GPIO.setup(38, GPIO.OUT)
        GPIO.setup(36, GPIO.OUT)
        GPIO.setup(32, GPIO.OUT)
        GPIO.setup(31, GPIO.OUT)
        GPIO.setup(37, GPIO.OUT)
        GPIO.setup(35, GPIO.OUT)
        GPIO.setup(33, GPIO.OUT)
        GPIO.setup(29, GPIO.OUT)
        speed=GPIO.PWM(EN0,100)
        speed.start(100)
        GPIO.output(40, GPIO.LOW)
        GPIO.output(38, GPIO.LOW)
        GPIO.output(36, GPIO.LOW)
        GPIO.output(32, GPIO.LOW)
        GPIO.output(37, GPIO.LOW)
        GPIO.output(35, GPIO.LOW)
        GPIO.output(33, GPIO.LOW)
        GPIO.output(31, GPIO.LOW)
        print go
    if f and s:
        go= "forward"
    else:
        go ="b"
#
    cv2.imshow('frame', frame)
    k = cv2.waitKey(20) & 0xFF
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
#
cv2.destroyAllWindows()
