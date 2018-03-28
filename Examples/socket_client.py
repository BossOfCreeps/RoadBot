#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('192.168.0.113', 9090))
#sock.send('hello, world!')

a = True

while a:
    data = sock.recv(1024)
    if (data>""):
         print data

sock.close()

print data
