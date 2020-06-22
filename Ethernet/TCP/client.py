#!/bin/python3

import socket
import time
import struct

TCP_IP = '10.200.200.1'
TCP_PORT = 1338
BUFFER_SIZE = 1024

mean = 0
max = 0
min = 100
n = 0
N = 10

print("Measuring TCP roundtrip time to/from {0}".format(str(TCP_IP)))

while n < N:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	start = time.time()
	s.send(struct.pack('!d', start))
	data = s.recv(BUFFER_SIZE)
	end = time.time()
	s.close()
	roundtrip_ms = (end - struct.unpack('!d', data)[0]) * 1000
	print("[TCP {0}/{1}] Roundtrip time: {2:.2f}ms".format(n+1, N, roundtrip_ms))
	

	mean += roundtrip_ms/N
	if roundtrip_ms > max:
		max = roundtrip_ms
	if roundtrip_ms < min:
		min = roundtrip_ms

	n = n + 1
	time.sleep(1)

print("Min: {0:.2f}, Mean: {1:.2f}, Max: {2:.2f}".format(min,mean,max))