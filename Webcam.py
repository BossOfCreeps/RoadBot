import numpy as np
import RPi.GPIO as GPIO
import cv2
from time import sleep
from socket import *
import threading

stop=False
r1=255
g1=255
b1=255
q1=50

def clock(interval):
    host = '192.168.0.106'
    port = 8888
    addr = (host,port)

    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(addr)
    tcp_socket.listen(1)

    while True:
        conn, addr = tcp_socket.accept()
        data = conn.recv(1024)
        print(data)
    tcp_socket.close()
    if (data=="STOP"):
        global stop
        stop=True

t = threading.Thread(target=clock, args=(15,))
t.daemon = True
t.start()

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

GPIO.setwarnings(False)
GPIO.cleanup()
# cv2.namedWindow('frame')
cap = cv2.VideoCapture(0)
img = np.zeros((512,512,3), np.uint8)
# cv2.setMouseCallback('frame',draw_circle)
go=""

while(True):
    ret, frame = cap.read()

    frame = box(frame,0,213,340,345,0,0,0)
    frame = box(frame,213,218,340,480,0,0,0)
    frame = box(frame,0,10,0,10,ir, ig, ib)
   
    step=20
    maxi=40
    x=340
#    while x<480-step:
#        x=x+step
#        y=0
#        while y<213-step:
#            y=y+step
            
            #if (abs(229 - frame[x,y,2])<maxi) and (abs(frame[x,y,1]-147)<maxi) and (abs(frame[x,y,0]-128)<maxi):
            #    frame = box(frame,y-5,y+5,x-5,x+5,0,0,0)
    f=False
    s=False
    #frame = box(frame,20-3,20+3,400-3,400+3,255,0,0)
    #frame = box(frame,60-3,60+3,400-3,400+3,255,0,0)

    if (abs(r1 - frame[400,20,2])<maxi) and (abs(frame[400,20,1]-g1)<maxi) and (abs(frame[400,20,0]-b1)<maxi):
        f=True
    if (abs(r1 - frame[400,60,2])<maxi) and (abs(frame[400,60,1]-g1)<maxi) and (abs(frame[400,60,0]-b1)<maxi):
        s=True
    
    if f and s and go != "f":
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
    
    if not f and s and go != "r":
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
        GPIO.output(40, GPIO.HIGH)
        GPIO.output(38, GPIO.LOW)
        GPIO.output(36, GPIO.HIGH)
        GPIO.output(32, GPIO.LOW)
        GPIO.output(37, GPIO.LOW)
        GPIO.output(35, GPIO.HIGH)
        GPIO.output(33, GPIO.LOW)
        GPIO.output(31, GPIO.HIGH)
    if f and not s and go != "l":
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
        GPIO.output(37, GPIO.HIGH)
        GPIO.output(35, GPIO.LOW)
        GPIO.output(33, GPIO.HIGH)
        GPIO.output(31, GPIO.LOW)
    if not f and not s and go != "b":
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

    if f and s:
        go="f"
    if f and not s:
        go="l"
    if not f and s:
        go="r"
    if not f and not s:
        go="b"
    print go

    frame = box(frame,20-3,20+3,400-3,400+3,255,0,0)
    frame = box(frame,60-3,60+3,400-3,400+3,255,0,0)
#    cv2.imshow('frame', frame)
    k = cv2.waitKey(20) & 0xFF
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
#cv2.destroyAllWindows()
