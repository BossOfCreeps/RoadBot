import RPi.GPIO as GPIO
from socket import *
import threading
from time import sleep

host = '10.0.0.14'
port = 8895
addr = (host,port)
sp=10
tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(addr)
tcp_socket.listen(1)

conn, addr = tcp_socket.accept()    
while True:
    side = conn.recv(1024)
    print(side)
    if (side=="F"):
        IN1=40
        IN2=38
        IN3=36
        IN4=32
        IN5=37
        IN6=35
        IN7=33
        IN8=31
        EN0=29
        print "forward"
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
        speed.start(sp)
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
        GPIO.output(IN5, GPIO.LOW)
        GPIO.output(IN6, GPIO.HIGH)
        GPIO.output(IN7, GPIO.LOW)
        GPIO.output(IN8, GPIO.HIGH)
    if (side=="B"):
        IN1=40
        IN2=38
        IN3=36
        IN4=32
        IN5=37
        IN6=35
        IN7=33
        IN8=31
        EN0=29
        print "backward"
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
        speed.start(sp)
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
        GPIO.output(IN5, GPIO.HIGH)
        GPIO.output(IN6, GPIO.LOW)
        GPIO.output(IN7, GPIO.HIGH)
        GPIO.output(IN8, GPIO.LOW)
    if (side=="L"):
        IN1=40
        IN2=38
        IN3=36
        IN4=32
        IN5=37
        IN6=35
        IN7=33
        IN8=31
        EN0=29
        print "left"
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
        speed.start(sp)
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
        GPIO.output(IN5, GPIO.LOW)
        GPIO.output(IN6, GPIO.HIGH)
        GPIO.output(IN7, GPIO.LOW)
        GPIO.output(IN8, GPIO.HIGH)
    if (side=="R"):
        IN1=40
        IN2=38
        IN3=36
        IN4=32
        IN5=37
        IN6=35
        IN7=33
        IN8=31
        EN0=29
        print "right"
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
        speed.start(sp)
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
        GPIO.output(IN5, GPIO.HIGH)
        GPIO.output(IN6, GPIO.LOW)
        GPIO.output(IN7, GPIO.HIGH)
        GPIO.output(IN8, GPIO.LOW)
    if (side=="S"):
        IN1=40
        IN2=38
        IN3=36
        IN4=32
        IN5=37
        IN6=35
        IN7=33
        IN8=31
        EN0=29
        print "stop"
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
        speed.start(sp)
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        GPIO.output(IN5, GPIO.LOW)
        GPIO.output(IN6, GPIO.LOW)
        GPIO.output(IN7, GPIO.LOW)
        GPIO.output(IN8, GPIO.LOW)

