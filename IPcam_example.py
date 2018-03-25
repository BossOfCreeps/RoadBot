import cv2
cap = cv2.VideoCapture('http://localhost:8080/?action=stream')

d = 30
R = 200
G = 90
B = 80

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
      y = y + 40
    x = x + 40
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
