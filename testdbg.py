import pylink

from common import init

jlink = None
try:
    jlink = init()
except:
    print('Device is locked.')
    exit()
print('Device is unlocked.')
