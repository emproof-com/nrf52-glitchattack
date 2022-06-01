import serial
import time
import sys

delay = 11320
glitcher = serial.Serial('/dev/ttyACM0', 115200)
if sys.argv[1] == 'on':
    print('Enabling target power')
    glitcher.write(b'h        ')
    resp = glitcher.read(4)
    print(resp.decode('ascii')[0:2])
else:
    print('Disabling target power')
    glitcher.write(b'l        ')
    resp = glitcher.read(4)
    print(resp.decode('ascii')[0:2])
