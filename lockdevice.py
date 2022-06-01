import pylink

from common import init

jlink = init()
jlink.memory_write32(0x10001208, [0xFFFFFF00])
print('Device is locked.')
jlink.reset()
