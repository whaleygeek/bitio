# WORK IN PROGRESS - DO NOT USE


import microbit
import time

# is this how we want it to work?
# This seems really messy
# although we do want a way to pass a custom class in the future too
microbit.use_API(microbit.GATEWAY)
microbit.connect()

# or like this
# I think this is closer to what we want, but not quite right
from microbit import gateway_microbit

gateway_microbit.connect()

# what if we want to force a specific port name rather than use auto detected default?

print("connected")

while True:
    msg = microbit.read_next_message()
    if msg is not None:
        print("got message:%s" % str(msg))
    microbit.send_message("hello")
    time.sleep(0.5)

# END
