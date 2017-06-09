# WORK IN PROGRESS - DO NOT USE

# connect1_custom - connect using a user supplied custom API wrapper
# this might also imply force loading or checking for a specific .hex loaded on micro:bit

import microbit
import time

# if we want to connect with some other API:
#
# host side will verify on connection that the correct thing has loaded
# classname will offer the API it wants to
# it might also use the drivescan to find the drive and flash the correct file first

class MyAPI():
    pass

microbit.use_API(MyAPI)

# specifying the serial port
microbit.connect() # use portscan.cache or portscan workflow


# what if we want to force a specific port name rather than use auto detected default?

print("connected")

while True:
    microbit.my_api_method()
    time.sleep(1)
    print("tick")

# END
