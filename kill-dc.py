import RPi.GPIO as GPIO
from time import sleep

IN1=40
IN2=38
IN3=36
IN4=32

IN5=37
IN6=35
IN7=33
IN8=31
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(IN5, GPIO.OUT)
GPIO.setup(IN6, GPIO.OUT)
GPIO.setup(IN7, GPIO.OUT)
GPIO.setup(IN8, GPIO.OUT)
GPIO.cleanup()
