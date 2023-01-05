# echo-server.py

import socket

def convertTuple(tup):
    wholestring = ''.join(str(tup))
    return wholestring

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        data = conn.recv(1024) # number of bytes to receive and process
        address = convertTuple(addr)
        message = str(data,'utf-8')
        if message != "":
            print("Message from " + address + " : " + message)
        if message == "quit":
            print("Message from " + address + " : " + message)
            break
    s.close()
