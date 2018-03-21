import cv2
import time

cap = cv2.VideoCapture("http://10.0.0.14:8080/?action=stream")

while(cap.isOpened()):
    ret, img = cap.read()
    current_time_in_milliseconds = "%.5f" % time.time()
    filename="{}.jpg".format(current_time_in_milliseconds)
    cv2.imwrite(filename, img)