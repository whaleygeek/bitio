import microbit
import time

microbit.radio.on()
print("host radio on")

while True:
    time.sleep(1)
    print("SEND")
    microbit.radio.send("HELLO")
