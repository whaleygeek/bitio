# __init__.py

#----- CONFIG -----------------------------------------------------------------

DEBUG = False
BAUD = 115200

def trace(msg):
    if DEBUG:
        print(str(msg))

def warn(msg):
    print("warning:%s" % str(msg))

def info(msg):
    print(msg)

def fail(msg):
    print("error:%s" % str(msg))
    import sys
    sys.exit(-1)


#----- IMPORTS ----------------------------------------------------------------

try:
    import repl
except ImportError:
    from . import repl

try:
    import portscan
except ImportError:
    from . import portscan

try:
    import api
except ImportError:
    from . import api

import sys, os

SERIAL_PATH = os.path.dirname(__file__) #TODO: or abspath??
trace("Using path:%s" % str(SERIAL_PATH))
if SERIAL_PATH not in sys.path:
    sys.path.append(SERIAL_PATH)

try:
    import serial
except ImportError:
    fail("I can't find pyserial on your system. That's odd, it should be included in this project")


#----- PORTSCAN ---------------------------------------------------------------

# reuse or scan for a new port
trace("will reuse cache or scan for new port")

name = portscan.getName()
if name != None:
    if DEBUG:
        trace("Using port:" + name)
    PORT = name
else:
    name = portscan.find()
    if name == None:
        fail("No port selected, giving in")
    PORT = name


#----- CONNECT TO SERIAL ------------------------------------------------------

# get the serial port
def get_serial():
    s = serial.Serial(PORT)
    s.baudrate = BAUD
    s.parity   = serial.PARITY_NONE
    s.databits = serial.EIGHTBITS
    s.stopbits = serial.STOPBITS_ONE
    s.timeout = 0 # non blocking mode

    s.close()
    s.port = PORT
    s.open()
    return s

info("connecting...")
trace("getting active serial port connection to micro:bit")

while True:
    try:
        s = get_serial()
        break # got a valid connection
    except Exception as e:
        warn("Could not open the serial port that was remembered from last time")
        portscan.forget()
        name = portscan.find()
        if name == None:
            fail("Still can't find a port, giving in")
        PORT = name
        # go round again and try and open serial port


#----- GET RAW REPL -----------------------------------------------------------

# wrap a repl around it
trace("creating a raw REPL connection via serial")
repl = repl.REPL(s)

trace("entering raw repl mode")
repl.to_raw()


#----- CREATE MICROBIT ABSTRACTION --------------------------------------------

trace("creating a MicroBit API class around it")
microbit = api.MicroBit(repl)


#----- TURN THIS MODULE into a microbit instance ------------------------------

# i.e. when people do import microbit
# what they then want is to be able to say microbit.button_a.was_pressed()
# and for it to map directly through to the microbit object above.

# make this module look like a single microbit

me = sys.modules[__name__]
sys.modules[__name__] = microbit

info("Your micro:bit has been detected")
info("Now running your program")


# END
