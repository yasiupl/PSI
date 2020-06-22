#!/bin/python3

import socket

TCP_IP = '0.0.0.0'
TCP_PORT = 1338
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print("Listening on " + TCP_IP + ":" + str(TCP_PORT))

while True:
	conn, addr = s.accept()
	data = conn.recv(BUFFER_SIZE)
	if data: 
		print("[TCP] Echoing back to " + str(addr))
		conn.send(data)  # echo
	conn.close()