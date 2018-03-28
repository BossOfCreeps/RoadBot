#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
#sock.bind(('10.0.0.14', 9090))
sock.bind(('192.168.0.100', 9090))
sock.listen(1)
conn, addr = sock.accept()

print 'connected:', addr

while True:
    data = conn.recv(1024)
    #if not data:
    #    break
    #print data
    conn.send("Seva")

conn.close()
