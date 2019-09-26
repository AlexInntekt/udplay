import socket

UDP_IP1 = "192.168.0.64"
UDP_PORT = 5000

message = "hello"      # not the real command string

def send():
    # try:
    #     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #     s.bind(("", UDP_PORT))
    #     msg = message.encode('utf-8')
    #     s.sendto(msg, (UDP_IP1, UDP_PORT))
    # except socket.error as e:
    #     print("Error: ", e)

    # return s

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto(bytes(message, "utf-8"), (UDP_IP1, UDP_PORT))

def receive(sock):
    print("Receiving data: \n")

    while True:
        data, addr = sock.recvfrom(4096)      # buffer size is 4096 bytes
        print ("received message:", data)


# if __name__ == "__main__":    
#     s = SendData()
#     ReceiveData(s)

