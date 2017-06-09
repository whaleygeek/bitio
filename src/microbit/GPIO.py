# microbit/GPIO.py  08/06/2017  D.J.Whale
#
# A simple GPIO abstraction that works just like RPi.GPIO
# and could form part of anyio.GPIO too.

#TODO: how does this get access to the discovered/connected micro:bit?
#If we are also using the microbit abstraction, we really want to share the same repl
#interface so that we can do buttons and display as well as GPIO abstraction simultaneously

BOARD = 1
BCM = 2
MICROBIT = 3
IN = 4
OUT = 5
HIGH = True
LOW = False

#TODO: Decide which pins to surface on the micro:bit
#TODO: If try to use display pins, have to turn display off
pins = (0,1,2,3,4,5,6,7,8,9) #TODO decide which pins to surface
modes = {}

def setwarnings(flag):
    pass # nothing to do

def setmode(mode):
    pass # Nothing to do, board type is ignored

def setup(pin, mode):
    if pin not in pins:
        raise ValueError("Unsupported pin:%s" % str(pin))
    modes[pin] = mode

def input(pin):
    if not pin in modes or modes[pin] != IN:
        raise RuntimeError("Pin not configured as an input:%s" % str(pin))
    #TODO read hardware for pin to get value
    return False #TODO: return repl_bool("print(pin%s.digital_read())")

def output(pin, value):
    if not pin in modes or modes[pin] != OUT:
        raise RuntimeError("Pin not configured as an output:%s" % str(pin))
    #TODO: write to change state
    #TODO: repl("pin%s.digital_write(%s)")

def cleanup():
    pass
    #TODO: close the micro:bit port down??

# END
