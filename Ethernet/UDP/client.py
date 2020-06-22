#!/bin/python3

import socket
import time
import struct

UDP_IP = '10.200.200.1'
UDP_PORT = 1337

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mean = 0
max = 0
min = 100
n = 0
N = 10

print("Measuring TCP roundtrip time to/from {0}".format(str(UDP_IP)))


while n < N:
    start = time.time()
    sock.sendto(struct.pack('!d', start), (UDP_IP, UDP_PORT))
    data, addr = sock.recvfrom(1024)
    end = time.time()
    roundtrip_ms = (end - struct.unpack('!d', data)[0]) * 1000
    print("[UDP {0}/{1}] Roundtrip time: {2:.2f}ms".format(n+1, N, roundtrip_ms))

    mean += roundtrip_ms/N
    if roundtrip_ms > max:
        max = roundtrip_ms
    if roundtrip_ms < min:
        min = roundtrip_ms

    n = n + 1
    time.sleep(1)

print("Min: {0:.2f}, Mean: {1:.2f}, Max: {2:.2f}".format(min,mean,max))