import cv2 
import threading 
import time 
import socket 
import RPi.GPIO as GPIO 
from time import sleep 
cap = cv2.VideoCapture('http://localhost:8080/?action=stream')

sock = socket.socket()
sock.connect(('10.0.0.19', 9090))
sock.send('hello, world!')

#    data = sock.recv(1024)
#    if (data>""):
#         print data
#sock.close()

IN1=3
IN2=5
IN3=7
IN4=8
IN5=11
IN6=13
IN7=15
IN8=16
EN1=19
EN2=21
EN3=23
EN4=24
speed=60

d = 30
R = 148
G = 59
B = 75
a = 0

def stop ():
    GPIO.output(IN1, GPIO.LOW)  # white back
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)  # while forward
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(IN5, GPIO.LOW)  # black forward
    GPIO.output(IN6, GPIO.LOW)
    GPIO.output(IN7, GPIO.LOW)  # black back
    GPIO.output(IN8, GPIO.LOW)

def forward ():
    GPIO.output(IN1, GPIO.HIGH) # white back
    GPIO.output(IN2, GPIO.LOW)  
    GPIO.output(IN3, GPIO.LOW)  # while forward
    GPIO.output(IN4, GPIO.HIGH)
    GPIO.output(IN5, GPIO.HIGH) # black forward
    GPIO.output(IN6, GPIO.LOW)
    GPIO.output(IN7, GPIO.LOW)  # black back
    GPIO.output(IN8, GPIO.HIGH)

def backward ():
    GPIO.output(IN1, GPIO.LOW)  # white back
    GPIO.output(IN2, GPIO.HIGH) 
    GPIO.output(IN3, GPIO.HIGH) # while forward
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(IN5, GPIO.LOW)  # black forward
    GPIO.output(IN6, GPIO.HIGH)
    GPIO.output(IN7, GPIO.HIGH) # black back
    GPIO.output(IN8, GPIO.LOW)

def left ():
    GPIO.output(IN1, GPIO.LOW)  # white back
    GPIO.output(IN2, GPIO.HIGH) 
    GPIO.output(IN3, GPIO.HIGH) # while forward
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(IN5, GPIO.HIGH) # black forward
    GPIO.output(IN6, GPIO.LOW)
    GPIO.output(IN7, GPIO.LOW)  # black back
    GPIO.output(IN8, GPIO.HIGH)

def right ():
    GPIO.output(IN1, GPIO.HIGH) # white back
    GPIO.output(IN2, GPIO.LOW)  
    GPIO.output(IN3, GPIO.LOW)  # while forward
    GPIO.output(IN4, GPIO.HIGH)
    GPIO.output(IN5, GPIO.LOW)  # black forward
    GPIO.output(IN6, GPIO.HIGH)
    GPIO.output(IN7, GPIO.HIGH) # black back
    GPIO.output(IN8, GPIO.LOW)
    
#def server(interval):
#    global a
    #while True:
    #    if (a == 0):
    #        setupDC()
    #        setupSpeed(50)
    #        a=1
    #    if (a==1):
    #        forward()
    #        a=2
    #    if (a==1):
    #        backward()
    #        a=3
    #    if (a==1):
    #        left()
    #        a=4
    #    if (a==1):
    #        right()
    #        a=1

#t=threading.Thread(target=server, args=(5,))
#t.deamon = True
#t.start()

#setupDC

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
p1=GPIO.PWM(22,100)
p2=GPIO.PWM(26,100)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(IN5, GPIO.OUT)
GPIO.setup(IN6, GPIO.OUT)
GPIO.setup(IN7, GPIO.OUT)
GPIO.setup(IN8, GPIO.OUT)
GPIO.setup(EN1, GPIO.OUT)
GPIO.setup(EN2, GPIO.OUT)
GPIO.setup(EN3, GPIO.OUT)
GPIO.setup(EN4, GPIO.OUT)

speed1=GPIO.PWM(EN1,100)
speed2=GPIO.PWM(EN2,100)
speed3=GPIO.PWM(EN3,100)
speed4=GPIO.PWM(EN4,100)

speed1.start(speed)
speed2.start(speed)
speed3.start(speed)
speed4.start(speed)

while True:
  X = 0
  Y = 0
  C = 0
  ret, frame = cap.read()
  x = 0
  while x < 640:
    y = 0
    while y < 360:
      if (abs(frame[y,x,2]-R)<d) and (abs(frame[y,x,1]-G)<d) and (abs(frame[y,x,0]-B)<d):
        X = X + x
        Y = Y + y
        C = C + 1
      y = y + 35
    x = x + 35
  if (C>0):
    X = X/C
    Y = Y/C
    rig=1
    lef=1
    top=1
    bot=1
    D=d+10
    while ((abs(frame[Y+bot,X,2]-R)<D) and (abs(frame[Y+bot,X,1]-G)<D) and (abs(frame[Y+bot,X,0]-B)<D)and(Y+bot<359)):
      bot = bot + 1
    while ((abs(frame[Y-top,X,2]-R)<D) and (abs(frame[Y-top,X,1]-G)<D) and (abs(frame[Y-top,X,0]-B)<D)and(Y-top>0)):
      top = top + 1
    while ((abs(frame[Y,X+rig,2]-R)<D) and (abs(frame[Y,X+rig,1]-G)<D) and (abs(frame[Y,X+rig,0]-B)<D)and(X+rig<639)):
      rig = rig + 1
    while ((abs(frame[Y,X-lef,2]-R)<D) and (abs(frame[Y,X-lef,1]-G)<D) and (abs(frame[Y,X-lef,0]-B)<D)and(X-lef>0)):
      lef = lef + 1
    X=X+rig-lef
    Y=Y+bot-top
    cv2.circle(frame, (X, Y), 3, (255,255,255), -1)
    #cv2.imshow('Video', frame)
  if (Y>0) and (Y<225):
    forward()
  else:
#   backward()
#    sleep(0.5)
    stop()
    
    print "wait socket"
    sock.send('hello')
    data = sock.recv(1024)
    print data
    if (data == "yes"):
#            backward()
#            sleep(2)
#            stop()
        p1.start(7.5)
        p2.start(7.5)
        p1.ChangeDutyCycle(90/7.2)
        p2.ChangeDutyCycle(135/7.2)
        time.sleep(1)

        p1.ChangeDutyCycle(1/7.2)
        p2.ChangeDutyCycle(120/7.2)
        time.sleep(1)

        p1.ChangeDutyCycle(180/7.2)
        p2.ChangeDutyCycle(45/7.2)
        time.sleep(1)
        p1.stop()
        p2.stop()
        exit()
    if (data=="no"):
        exit()

  print Y
  if cv2.waitKey(1) == 27:
    exit(0)
