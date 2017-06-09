# __init__.py

#----- CONFIG -----------------------------------------------------------------

DEBUG = False
BAUD = 115200

def trace(msg):
    if DEBUG:
        print(str(msg))

def info(msg):
    print(msg)


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

import serial
#TODO: Might want to catch ImportError here and offer friendly advice on how to fix?


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
        raise RuntimeError("No port selected, giving in")
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
s = get_serial()

#TODO: want something other than an exception dump here if it fails
#need the option to show a message and just stop the program,
#or throw an exception (perhaps a configurable option)


#----- GET RAW REPL -----------------------------------------------------------

# wrap a repl around it
trace("creating a raw REPL connection via serial")
repl = repl.REPL(s)

trace("entering raw repl mode")
repl.to_raw()

#print("Trying to send a command")
#repl.send_command("print('hello')")
#print(repl.wait_response())


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
