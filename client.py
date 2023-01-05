# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message=input('Message: ')
        if message=='quit':
            s.sendall(bytes(message,'utf-8'))
            s.close()
            break
        s.sendall(bytes(message,'utf-8'))
