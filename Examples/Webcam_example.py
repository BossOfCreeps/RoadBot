import cv2

cv2.namedWindow("preview")
#vc2 = cv2.VideoCapture(0)
vc = cv2.CaptureFromFile('10.0.0.14:8080/?action=stream')

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    print frame [0,0]
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")
