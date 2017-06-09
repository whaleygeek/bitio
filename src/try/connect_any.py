# WORK IN PROGRESS - DO NOT USE


# connect_any - connect to any number of microbits

from microbit import microbits # any number, don't auto connect
import time

#TODO: do we want to connect to it as:
#   a gateway microbit with gateway API
#   a REPL microbit with REPL API
#   something else with another API?
# depending on use, drivescan and auto flasher might auto load appropriate hex file for you

microbit = microbits.get_microbit() # get first available microbit
microbit.connect()
print("connected")


while True:
    time.sleep(1)
    print("tick")