import RPi.GPIO as GPIO
from time import sleep

def forward():
    IN1=40
    IN2=38
    IN3=36
    IN4=32
    IN5=37
    IN6=35
    IN7=33
    IN8=31
    EN0=29
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(IN5, GPIO.HIGH)
    GPIO.output(IN6, GPIO.LOW)
    GPIO.output(IN7, GPIO.HIGH)
    GPIO.output(IN8, GPIO.LOW)
    print 'forward'
    sleep(1)
def backward():
    IN1=40
    IN2=38
    IN3=36
    IN4=32
    IN5=37
    IN6=35
    IN7=33
    IN8=31
    EN0=29    
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    GPIO.output(IN5, GPIO.LOW)
    GPIO.output(IN6, GPIO.HIGH)
    GPIO.output(IN7, GPIO.LOW)
    GPIO.output(IN8, GPIO.HIGH)
    print 'backward'
    sleep(1)    
def stop():
    IN1=40
    IN2=38
    IN3=36
    IN4=32
    IN5=37
    IN6=35
    IN7=33
    IN8=31
    EN0=29
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(IN5, GPIO.LOW)
    GPIO.output(IN6, GPIO.LOW)
    GPIO.output(IN7, GPIO.LOW)
    GPIO.output(IN8, GPIO.LOW)
    sleep(1)
    print "stop"
def init():
    IN1=40
    IN2=38
    IN3=36
    IN4=32
    IN5=37
    IN6=35
    IN7=33
    IN8=31
    EN0=29
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)
    GPIO.setup(IN5, GPIO.OUT)
    GPIO.setup(IN6, GPIO.OUT)
    GPIO.setup(IN7, GPIO.OUT)
    GPIO.setup(IN8, GPIO.OUT)
    GPIO.setup(EN0, GPIO.OUT)
    speed=GPIO.PWM(EN0,100)
    speed.start(75)

init()
forward()
stop()
