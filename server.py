#!/usr/bin/env python3

#reference https://docs.python.org/3.4/howto/sockets.html

import socket
import os

def simple_chat_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                       #open a socket
    s.bind(("localhost", 0))                                                    #bind the socket to a port
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    fo = open("PORT", "w")                                                      #save the port number to a file for the client to read
    fo.write(str(s.getsockname()[1]))
    fo.close()
    print("Server listening on: localhost on port: ", s.getsockname()[1])
    s.listen(1)                                                                 #listening to connection
    conn, addr = s.accept()                                                     #accept incoming connection
    print("Connected by ", addr)
    print("Waiting for message...")
    mes = conn.recv(1024)                                                       #recv message from client
    if not mes:
        mes = conn.recv(1024)
    mes = mes.decode()
    if mes == "/q":                                                             #quit if recv /q
        conn.close()
        s.close()
        return
    print("Type /q to quit")
    print(mes)
    print("Enter message to send...")
    while True:                                                                 #loop until recv /q or user type /q
        print('>', end='')
        mes = str(input())                                                      #get message to send from user
        if mes == "/q":                                                         #if user type /q quit and send /q to client
            conn.send(b'/q')
            conn.close()
            break
        conn.sendall(mes.encode())                                              #send message to client
        mes = conn.recv(1024)                                                   #recv message from client
        if not mes:
            mes = conn.recv(1024)
        mes = mes.decode()
        if mes == "/q":                                                         #quit if recv /q
            conn.close()
            break
        print(mes)
    s.close()

if __name__ == "__main__":
    simple_chat_server()
