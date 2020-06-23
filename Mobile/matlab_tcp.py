#!/bin/python3

import socket

TCP_IP = '0.0.0.0'
TCP_PORT = 5555
BUFFER_SIZE = 2

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print("Listening on " + TCP_IP + ":" + str(TCP_PORT))
conn, addr = s.accept()

while True:
	data = conn.recv(BUFFER_SIZE)
	if data: 
		print("[TCP] Recieved data " + str(data))
		conn.send(data)  # echo
conn.close()