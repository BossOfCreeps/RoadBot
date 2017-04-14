from socket import *

host = '172.16.12.41'
port = 8888
addr = (host,port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(addr)
tcp_socket.listen(1)

while True:
    conn, addr = tcp_socket.accept()
    print('client addr: ', addr)
    
    data = conn.recv(1024)
  
    print(data)
   
    #    conn.close()
    
tcp_socket.close()

