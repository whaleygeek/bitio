# button.py - demonstrates using a button

import time
import microbit

print("micro:bit connected - press button A to test")

while True:
    time.sleep(0.25)
    if microbit.button_a.was_pressed():
        print("Button A pressed")
        time.sleep(0.5)


# END
