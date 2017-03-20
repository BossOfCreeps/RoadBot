import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
p=GPIO.PWM(11,75)
p.start(7.5)
try:
        while True:
                p.ChangeDutyCycle(7.5)
                print "Left"
                time.sleep(1)
                p.ChangeDutyCycle(12.5)
                print "Center"
                time.sleep(1)
                p.ChangeDutyCycle(2.5)
                print "Right"
                time.sleep(1)
except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
