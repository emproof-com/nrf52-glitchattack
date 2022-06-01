import pylink
import time

from common import sn, device

def unlock():
    jlink = pylink.JLink()
    jlink.open(sn)
    jlink.set_tif(pylink.enums.JLinkInterfaces.SWD)
    # for unlocking we need to talk directly to the access/debug ports
    jlink.coresight_configure()
    jlink.coresight_write(1, 0x50000000, False)
    jlink.coresight_write(2, 0x01000000, False)
    jlink.coresight_write(1, 0x00000001, True)
    ret = jlink.coresight_read(2, True)
    if ret != 1:
        print('Unable to start unlock.')
        exit(1)
    i = 0
    while True:
        if i > 100:
            print('Unlock timed out.')
            exit(1)
        ret = jlink.coresight_read(3, True)
        if ret == 1:
            break
        i += 1
        time.sleep(0.01)
    jlink.connect(device, verbose=True)

    if not jlink.target_connected():
        print("Unable to connect to target")
        exit(1)

    return jlink

jlink = unlock()
print('Device unlocked, firmware is erased')
