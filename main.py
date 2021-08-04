#!/usr/bin/env python3
import selectors
import socket
import types


messages = []
message_history = []


class ServerConnection:
    ip = ''
    port = ''

    def __init__(self):
        pass



def connect(host,port):
    s = socket.socket()
    server = (host,port)
    s.connect(server)
    while True:
        str = input("S: ")
        s.send(str.encode())
        if(str.lower == "exit"):
            break
        #print("N: ", s.recv(1024).decode())




def main():
    new_connection = ServerConnection()
    print("Please enter the required information to connect to the chat server.\nExample: Server IP: 127.0.0.1 and Server Port: 443")
    new_connection.ip = input("Server IP: ")
    new_connection.port = int(input("Server Port: "))
    connect(host=new_connection.ip, port=new_connection.port)

if __name__ == '__main__':
    main()


