import socket

from p import receive

UDP_IP1 = "192.168.0.64"
UDP_PORT = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
s.bind(("", UDP_PORT))

receive(s)
