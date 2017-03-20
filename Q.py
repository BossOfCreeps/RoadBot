import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
p=GPIO.PWM(27,50)
p.start(7.5)
try:
        while True:
                p.ChangeDutyCycle(6.7)
except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()

