""" Socket UDP Server """
import socket
import main

PORT = 5555
IP = '192.168.0.9'

if __name__ == "__main__":
    print('UDP Server listen on {}'.format(PORT))

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    sock.bind(('', PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        data = data.decode('utf-8')
        print("Recv {}: {}".format(addr, data))
        if data[0] == 'c':
            main.sendBinary(data)
        elif data[0] == 'a':
            sock.sendto(str.encode("Teste Arduino"), addr)
