import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
p=GPIO.PWM(13,50)
p.start(7.5)
try:
        while True:
                p.ChangeDutyCycle(2.5)
                time.sleep(1)
                p.ChangeDutyCycle(3)
                time.sleep(1)
                p.ChangeDutyCycle(3.5)
                time.sleep(1)
                p.ChangeDutyCycle(4)
                time.sleep(1)
                p.ChangeDutyCycle(4.5)
                time.sleep(1)
                p.ChangeDutyCycle(5)
                time.sleep(1)
                p.ChangeDutyCycle(5.5)
                time.sleep(1)
                p.ChangeDutyCycle(6)
                time.sleep(1)
except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
