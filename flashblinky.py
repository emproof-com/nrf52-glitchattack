import pylink
import sys

from common import init

jlink = None
try:
    jlink = init()
except:
    print('Device is locked.')
    exit(1)
jlink.halt()
jlink.flash_file(sys.argv[1], 0)
print('Blinky flashed.')
