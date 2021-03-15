#!/usr/bin/env python3

#reference https://docs.python.org/3.4/howto/sockets.html

import socket
import os


def simple_chat_client():
    fo = open("PORT", "r")                                                      #read port number from file
    port = int(fo.readline())
    fo.close()
    if os.path.isfile("PORT"):
        os.remove("PORT")
    else:
        print("Server not running!")
    s = socket.socket()                                                         #open a socket
    s.connect(("localhost", port))                                              #connect to server
    print("Connected to: localhost on port: ", port)
    print("Type /q to quit")
    print("Enter message to send...")
    while True:
        print('>', end='')
        mes = str(input())                                                      #get user input
        if mes == "/q":                                                         #send '/q' and quit if user type /q
            s.send(b'/q')
            break
        s.sendall(mes.encode())                                                 #send message to server
        mes = s.recv(1024)                                                      #recv message from server
        if not mes:
            mes = s.recv(1024)
        mes = mes.decode()
        if mes == "/q":                                                         #quit if recv /q
            break
        print(mes)
    s.close()                                                                   #close socket

if __name__ == "__main__":
    simple_chat_client()
