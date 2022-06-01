import pylink

# enter the serial number of your J-Link here
sn = None
device = 'NRF52840_XXAA'

def init():
    jlink = pylink.JLink()
    jlink.open(sn)
    jlink.set_tif(pylink.enums.JLinkInterfaces.SWD)
    jlink.connect(device, verbose=True)

    if not jlink.target_connected():
        print("Unable to connect to target")
        exit(1)

    return jlink

def isunlocked():
    jlink = None
    try:
        jlink = init()
    except:
        print('Device is locked.')
        return False
    return True
