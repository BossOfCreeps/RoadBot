import cv2
import threading
import time
from DC import setupDC, setupSpeed, forward, backward, left, right
cap = cv2.VideoCapture('http://localhost:8080/?action=stream')


d = 40
R = 245
G = 225
B = 168
a = 0

def server(interval):
    global a
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

t=threading.Thread(target=server, args=(5,))
t.deamon = True
t.start()
setupDC()
setupSpeed(50)
forward()

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
      y = y + 45
    x = x + 45
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
    
  cv2.imshow('Video', frame)
  if cv2.waitKey(1) == 27:
    exit(0)
