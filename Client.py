import cv2
import numpy as np
import socket
import sys
import pickle
import struct

cv2.namedWindow("preview")
cap = cv2.VideoCapture(0)
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('10.0.0.19', 8084))

while True:
    ret,frame = cap.read()
    data = pickle.dumps(frame)
    clientsocket.sendall(struct.pack("L", len(data)) + data)
    cv2.imshow("preview", frame)
    print frame [0,0]
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        cv2.destroyWindow("preview")
        break