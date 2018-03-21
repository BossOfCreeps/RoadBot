import cv2
import urllib 
import numpy as np
import gc
import threading
import time

def clock(interval):
    while True:
        gc.collect()
        time.sleep(interval)

gc.enable()
t=threading.Thread(target=clock, args=(3,))
t.deamon = True
t.start()

stream=urllib.urlopen('http://10.0.0.14:8080/?action=stream')
bytes=''
while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        cv2.imshow('i',i)
        if cv2.waitKey(1) ==27:
            exit(0)  
