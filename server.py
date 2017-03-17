from socket import *

host = '10.0.0.14'
port = 7772
addr = (host,port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(addr)
tcp_socket.listen(1)

while True:
    
#    question = input('Do you want to quit? y\\n: ')
#    if question == 'y': break
    
    print('wait connection...')
    
    conn, addr = tcp_socket.accept()
    print('client addr: ', addr)
    
    data = conn.recv(1024)
   
    print(data)
    conn.send(b'Hello from server!')
    conn.close()
    
tcp_socket.close()
