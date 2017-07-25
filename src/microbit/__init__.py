# __init__.py

import sys

#----- CONFIG -----------------------------------------------------------------

##DEVICE_NAME = "whaleygeek's awesome microbit"
DEVICE_NAME = "micro:bit"
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

# Allow user to set debug flag on command line
if 'debug' in sys.argv:
    DEBUG = True

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

SERIAL_PATH = os.path.dirname(os.path.abspath(__file__))
trace("Using path:%s" % str(SERIAL_PATH))
if SERIAL_PATH not in sys.path:
    sys.path.insert(0, SERIAL_PATH)

try:
    import serial
except ImportError as e:
    info("Can't find pyserial on your system")
    if DEBUG:
        trace(str(e))
        import traceback
        ex_type, ex, tb = sys.exc_info()
        traceback.print_tb(tb)
        trace(sys.path)

    fail("That's odd, it should be included in this project")

if hasattr(serial, "BITIO"):
    trace("Yay, I loaded the BITIO packaged pyserial")
else:
    warn("I got the system installed pyserial, that was unexpected")

#----- PORTSCAN ---------------------------------------------------------------

# reuse or scan for a new port
trace("will reuse cache or scan for new port")

name = portscan.getName(DEVICE_NAME)
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
trace("getting active serial port connection to %s" % DEVICE_NAME)

while True:
    try:
        s = get_serial()
        break # got a valid connection
    except Exception as e:
        warn("Could not open the serial port that was remembered from last time")
        portscan.forget()
        name = portscan.find(DEVICE_NAME)
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

info("Your %s has been detected" % DEVICE_NAME)
info("Now running your program")


# END
