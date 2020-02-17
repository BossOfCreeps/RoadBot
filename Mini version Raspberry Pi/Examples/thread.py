import threading
import time

def clock(interval):
    while True:
        print("Time is %s" %time.ctime())
        time.sleep(interval)

t=threading.Thread(target=clock, args=(3,))
t.deamon = True
t.start()