import RPi.GPIO as GPIO
from time import sleep

IN1=3
IN2=5
IN3=7
IN4=8
IN5=11
IN6=13
IN7=15
IN8=16
EN1=19
EN2=21
EN3=23
EN4=24
speed=50

def setupDC ():
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)
    GPIO.setup(IN5, GPIO.OUT)
    GPIO.setup(IN6, GPIO.OUT)
    GPIO.setup(IN7, GPIO.OUT)
    GPIO.setup(IN8, GPIO.OUT)
    GPIO.setup(EN1, GPIO.OUT)
    GPIO.setup(EN2, GPIO.OUT)
    GPIO.setup(EN3, GPIO.OUT)
    GPIO.setup(EN4, GPIO.OUT)

def setupSpeed (s):
    speed1=GPIO.PWM(EN1,100)
    speed2=GPIO.PWM(EN2,100)
    speed3=GPIO.PWM(EN3,100)
    speed4=GPIO.PWM(EN4,100)
    speed1.start(50)
    speed2.start(50)
    speed3.start(50)
    speed4.start(50)

def forward ():
    GPIO.output(IN1, GPIO.HIGH) # white back
    GPIO.output(IN2, GPIO.LOW)  
    GPIO.output(IN3, GPIO.LOW)  # while forward
    GPIO.output(IN4, GPIO.HIGH)
    GPIO.output(IN5, GPIO.HIGH) # black forward
    GPIO.output(IN6, GPIO.LOW)
    GPIO.output(IN7, GPIO.LOW)  # black back
    GPIO.output(IN8, GPIO.HIGH)

def backward ():
    global IN1
    global IN2
    global IN3
    global IN4
    global IN5
    global IN6
    global IN7
    global IN8
    global EN1
    global EN2
    global EN3
    global EN4
    GPIO.output(IN1, GPIO.LOW)  # white back
    GPIO.output(IN2, GPIO.HIGH) 
    GPIO.output(IN3, GPIO.HIGH) # while forward
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(IN5, GPIO.LOW)  # black forward
    GPIO.output(IN6, GPIO.HIGH)
    GPIO.output(IN7, GPIO.HIGH) # black back
    GPIO.output(IN8, GPIO.LOW)

def left ():
    global IN1
    global IN2
    global IN3
    global IN4
    global IN5
    global IN6
    global IN7
    global IN8
    global EN1
    global EN2
    global EN3
    global EN4
    GPIO.output(IN1, GPIO.LOW)  # white back
    GPIO.output(IN2, GPIO.HIGH) 
    GPIO.output(IN3, GPIO.HIGH) # while forward
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(IN5, GPIO.HIGH) # black forward
    GPIO.output(IN6, GPIO.LOW)
    GPIO.output(IN7, GPIO.LOW)  # black back
    GPIO.output(IN8, GPIO.HIGH)

def right ():
    global IN1
    global IN2
    global IN3
    global IN4
    global IN5
    global IN6
    global IN7
    global IN8
    global EN1
    global EN2
    global EN3
    global EN4
    GPIO.output(IN1, GPIO.HIGH) # white back
    GPIO.output(IN2, GPIO.LOW)  
    GPIO.output(IN3, GPIO.LOW)  # while forward
    GPIO.output(IN4, GPIO.HIGH)
    GPIO.output(IN5, GPIO.LOW)  # black forward
    GPIO.output(IN6, GPIO.HIGH)
    GPIO.output(IN7, GPIO.HIGH) # black back
    GPIO.output(IN8, GPIO.LOW)

setupDC()

speed1=GPIO.PWM(EN1,100)
speed2=GPIO.PWM(EN2,100)
speed3=GPIO.PWM(EN3,100)
speed4=GPIO.PWM(EN4,100)

speed1.start(speed)
speed2.start(speed)
speed3.start(speed)
speed4.start(speed)

while True:
    forward()
