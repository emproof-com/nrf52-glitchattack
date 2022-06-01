import pylink
import serial
import time

from common import init, isunlocked

def dump():
    jlink = None
    try:
        jlink = init()
    except:
        print('Device is locked.')
        return False
    bs = bytes(jlink.memory_read(0x0, 0x300))
    with open('dump.bin', 'wb') as f:
        f.write(bs)
    print('Written dump to dump.bin')


glitcher = serial.Serial('/dev/ttyACM0', 115200)
while True:
    for delay in range(14800, 14820, 2):
        for width in range(10,30,1):
            print('Disabling target power')
            glitcher.write(b'l        ')
            resp = glitcher.read(4)
            print(resp.decode('ascii')[0:2])
            time.sleep(0.1)
            print('write {} delay'.format(delay))
            glitcher.write('d{:08}'.format(delay).encode('ascii'))
            resp = glitcher.read(4)
            print(resp.decode('ascii')[0:2])
            print('write {} width'.format(width))
            glitcher.write('w{:08}'.format(width).encode('ascii'))
            resp = glitcher.read(4)
            print(resp.decode('ascii')[0:2])
            time.sleep(0.1)
            print('glitch')
            glitcher.write(b'g        ')
            resp = glitcher.read(4)
            print(resp.decode('ascii')[0:2])
            time.sleep(0.1)
            if isunlocked():
                print('Success :)')
                dump()
                exit(0)
# glitcher.write(b'h        ')
print('Disabling target power')
glitcher.write(b'l        ')
resp = glitcher.read(4)
print(resp.decode('ascii')[0:2])
exit(1)
