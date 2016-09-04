""" Send and recv """
import sys
import threading
import serial
import binascii

ser = serial.Serial('/dev/ttyACM0')
def worker():
    print("Start worker")
    while True:
        value = ser.readline()
        print(value)

def sendBinary(value):
    print("Sending '%s'" % value)
    for i in value.ljust(10, ' '):
        ser.write(binascii.a2b_qp(i))

t = threading.Thread(target=worker)
t.start()

if __name__ == "__main__":
    print("Serial cli")

    for line in sys.stdin:
        cmd = line.splitlines()[0]
        if len(cmd) > 0:
            sendBinary(cmd)
