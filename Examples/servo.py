import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
p1=GPIO.PWM(22,100)
p2=GPIO.PWM(26,100)
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

