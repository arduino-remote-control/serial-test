""" Socket UDP Client """
import socket

PORT = 5555
IP = 'localhost'
BC = '192.168.0.255'
SEND = BC

if __name__ == "__main__":
    print('UDP Client')

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    print('Send to {}:{}'.format(SEND, PORT))
    sock.sendto(str.encode("teste"), (SEND, PORT))

    data, addr = sock.recvfrom(1024)
    print("Recv {}: {}".format(addr, data))
